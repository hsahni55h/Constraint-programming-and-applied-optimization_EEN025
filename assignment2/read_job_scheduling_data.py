# Function to read job scheduling data from a text file
def read_job_scheduling_data(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

        # Extract n and m values from the first line
        n, m = map(int, lines[0].split())

        # Initialize lists for times and machines
        times = []
        machines = []

        # Read the remaining lines and extract times and machines data
        for line in lines[1:]:
            data = list(map(int, line.split()))
            machine_process_pairs = [(data[i], data[i + 1]) for i in range(0, len(data), 2)]
            machines.append([pair[0] for pair in machine_process_pairs])
            times.append([pair[1] for pair in machine_process_pairs])

        return n, m, times, machines

# Entry point of the script
if __name__ == "__main__":
    # Specify the file name (without full path) in the same directory as the script
    file_name = 'ft06.txt'

    # Construct the full file path by combining the current directory and the file name
    file_path = file_name

    # Read job scheduling data from the specified file
    n, m, times, machines = read_job_scheduling_data(file_path)

    # print the data to stdout
    print("n = {}".format(n))       # jobs (row count)
    print("m = {}".format(n))       # machines (column count)
    print("machines = {}".format(machines))
    print("times = {}".format(times))
