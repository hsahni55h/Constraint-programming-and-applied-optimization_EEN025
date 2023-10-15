import gurobipy as gp
from gurobipy import GRB

File_name = "ft10.txt"  # rename the required file name


# function to PreProcess the data from file
def FileProcessing(filename):
    # Define variables to store the data
    instance_name = ""
    n = 0  # Number of jobs
    m = 0  # Number of machines
    job_sequence = []
    machine_processing_times = {}
    dict_list = []
    JOB_Data = {}

    # Open the file for reading
    with open(filename, "r") as file:
        lines = file.readlines()

    # Process each line in the file
    for line in lines:
        line = line.strip()  # Remove leading/trailing whitespace and newline characters

        # Check if the line contains the instance name
        if line.startswith("instance"):
            instance_name = line.split()[-1]
        # Check if the line contains the problem size
        elif line.count(" ") == 1:
            n, m = map(int, line.split())
        # Check if the line contains job/machine data
        elif line.startswith(('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10')):
            data = list(map(int, line.split()))
            if len(data) == m * 2:
                job_sequence.append(data)

    for sublist in job_sequence:
        my_dict = {}
        for i in range(0, len(sublist), 2):
            key = sublist[i]
            value = sublist[i + 1]
            my_dict[key] = value
        dict_list.append(my_dict)

    for d in range(n):
        JOB_Data[d + 1] = dict_list[d]

    Total_time = sum(inner_value for inner_dict in JOB_Data.values() for inner_value in inner_dict.values())
    return {
        "instance_name": instance_name,
        "n": n,
        "m": m,
        "JOB_Data": JOB_Data,
        "Total_time": Total_time
    }

# Function to create data structure
def data(job_data):
    process_t = []
    for inner_dict in job_data.values():
        inner_list = []
        for k, v in inner_dict.items():
            inner_list.append(k)
            inner_list.append(v)
        process_t.append(inner_list)
    return process_t


ProcessInfo = FileProcessing(File_name)

# Required information
num_jobs = ProcessInfo["n"]
num_machines = ProcessInfo["m"]
JOB_Data = ProcessInfo["JOB_Data"]
Total_time = ProcessInfo["Total_time"]

# Print the data preprocessing results
print("Instance Name: ", ProcessInfo["instance_name"])
print("No of Jobs: ", ProcessInfo["n"])
print("No of Machines: ", ProcessInfo["m"])
print("Jobs Process: ", ProcessInfo["JOB_Data"], "Data Structure: {Job no : {Machine no: Processing Time}}")
print("Total Process Time: ", ProcessInfo["Total_time"], "mins")

# Required Job data
processing_times = data(JOB_Data)

model = gp.Model()

# Variables
start_times = {}
makespan = model.addVar(name='makespan')

for j in range(num_jobs):
    for i in range(num_machines):
        start_times[(j, i)] = model.addVar(vtype=GRB.CONTINUOUS, lb=0.0, name=f'start_{j}_{i}')

# Constraints

for j in range(num_jobs):
    for i in range(num_machines - 1):
        model.addConstr(start_times[(j, i)] + processing_times[i][j] <= start_times[(j, i + 1)])
        # print("test1", processing_times[i][j])

for i in range(num_machines):
    for j in range(num_jobs - 1):
        model.addConstr(start_times[(j, i)] + processing_times[i][j] <= start_times[(j + 1, i)])
#
for j in range(num_jobs):
    model.addConstr(start_times[(j, num_machines - 1)] + processing_times[num_machines - 1][j] <= makespan)
    # print("test2", processing_times[num_machines - 1][j])

# Objective
model.setObjective(makespan, GRB.MINIMIZE)

model.optimize()

if model.status == GRB.OPTIMAL:
    print("Optimal Schedule:")
    optimal_makespan = makespan.X
    print("Gurobi Optimal Makespan:", optimal_makespan)
    print("Gurobi Start Times:")
    [print("Job %d starts on machine %d at Start Time %d " % (j + 1, i + 1, start_times[(j, i)].x)) for j in
     range(num_jobs) for i in range(num_machines)]

else:
    print("Gurobi: No solution found.")
