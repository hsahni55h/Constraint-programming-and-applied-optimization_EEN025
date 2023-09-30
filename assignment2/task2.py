from read_job_scheduling_data import *
from shop_floor_layout import *


def task2():
    speed = 5.0                   # (in m/s) This is given data
    
    # Specify the file name (without full path) in the same directory as the script
    file_path = 'ft06.txt'        # TODO: change the file name as per requirement.

    # Read job scheduling data from the specified file
    n, m, times, machines = read_job_scheduling_data(file_path)

    # For all the jobs in the list find shortest path between machines
    machine_pairs_list = []
    distances_list = []
    paths_list = []
    time_required_list = []
    for machine_sequence in machines:
        machine_pairs = [(machine_sequence[i], machine_sequence[i+1]) for i in range(0, len(machine_sequence) - 1)]
        distances = []
        paths = []
        for start, end in machine_pairs:
            dist, path = shop_floor.astar(machine_node[start], machine_node[end])
            distances.append(dist)
            paths.append([node.name for node in path])
        distances_list.append(distances)
        time_required_list.append([d/speed for d in distances])
        paths_list.append(paths)
        machine_pairs_list.append(machine_pairs)
    
    # print the data to stdout
    for i in range(len(distances_list)):
        print("---------- ----------")
        print("machine_pairs_list[{}] = {}".format(i, machine_pairs_list[i]))
        print("time_required_list[{}] = {}".format(i, time_required_list[i]))
        print("paths_list[{}] = {}".format(i, paths_list[i]))
        print("distances_list[{}] = {}".format(i, distances_list[i]))
    print("---------- ----------")
    print(">>>> NOTE: in above output, machine number indexing starts from 0. <<<<")

# Entry point of the script
if __name__ == "__main__":
    task2()

