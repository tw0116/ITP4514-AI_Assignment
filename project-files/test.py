# A function to find the line of the "station_start" and "station_end"
# Check whether the "station_start" and the "station_end" at the same line.

    # if "station_start" and "station_end" are at the same line
        # alther heuristic function of the lines

    # if "station_start" and "station_end" are not at the same line
        # alther heuristic function of the lines

import json
from pprint import PrettyPrinter, pprint
from queue import Empty

graph = {
    'A': [['B', 2.0]],
    'B': [['A', 2.0], ['C', 2.0], ['F', 2.0], ['G', 3.0]],
    'C': [['B', 2.0], ['H', 2.0]],
    'D': [['E', 2.0], ['H', 2.0]],
    'E': [['D', 2.0], ['I', 2.0]],
    'F': [['B', 2.0]],
    'G': [['B', 3.0], ['J', 2.0]],
    'H': [['C', 2.0], ['D', 2.0], ['K', 2.0]],
    'I': [['E', 2.0], ['L', 2.0]],
    'J': [['G', 2.0], ['P', 5.0]],
    'K': [['H', 2.0], ['P', 3.0]],
    'L': [['I', 2.0], ['M', 2.0], ['R', 2.0]],
    'M': [['L', 2.0]],
    'N': [['O', 2.0]],
    'O': [['N', 2.0], ['P', 3.0]],
    'P': [['J', 5.0], ['K', 3.0], ['O', 3.0], ['Q', 2.0]],
    'Q': [['P', 2.0], ['R', 2.0]],
    'R': [['Q', 2.0], ['S', 2.0]],
    'S': [['R', 2.0]]
}

graph2 = {
    "line1" : {
        'A_L1': [['B_L1', 0]],
        'B_L1': [['A_L1', 0], ['C_L1', 0], ['B_L2', 0]],
        'C_L1': [['B_L1', 0], ['H_L1', 0]],
        'H_L1': [['C_L1', 0], ['K_L1', 0], ['H_L3', 0]],
        'K_L1': [['H_L1', 0], ['P_L1', 0], ['K_L3', 0]],
        'P_L1': [['K_L1', 0], ['P_L5', 0]]
    },
    
    "line2" : {
        'F_L2': [['B_L1', 0]],
        'B_L2': [['F_L2', 0], ['G_L2', 0], ['B_L1', 0]],
        'G_L2': [['B_L1', 0], ['J_L2', 0]],
        'J_L2': [['G_L2', 0], ['P_L2', 0]],
        'P_L2': [['J_L2', 0], ['P_L5', 0]]
    },

    "line3" : {
        'K_L3': [['H_L3', 0], ['K_L1', 0]],
        'H_L3': [['K_L3', 0], ['D_L3', 0], ['H_L1', 0]],
        'D_L3': [['H_L3', 0], ['E_L3', 0]],
        'E_L3': [['D_L3', 0], ['I_L3', 0]],
        'I_L3': [['E_L3', 0], ['L_L3', 0]],
        'L_L3': [['I_L3', 0], ['L_L4', 0]]
    },

    "line4" : {
        'R_L4': [['L_L4', 0], ['R_L5', 0]],
        'L_L4': [['R_L4', 0], ['M_L4', 0], ['L_L4', 0]],
        'M_L4': [['L_L4', 0]]
    },

    "line5" : {
        'N_L5': [['O_L5', 0]],
        'O_L5': [['N_L5', 0], ['P_L5', 0]],
        'P_L5': [['O_L5', 0], ['Q_L5', 0], ['P_L1', 0], ['P_L2', 0]],
        'Q_L5': [['P_L5', 0], ['R_L5', 0]],
        'R_L5': [['Q_L5', 0], ['S_L5', 0], ['R_L4', 0]],
        'S_L5': [['R_L5', 0]]
    }
}

# for node in graph:
#     for i in graph[node]:
#         print(i[0])
#     print("====")

# start = str(input("Enter Start: "))
# end = str(input("Enter End: "))

def load_graph(file_name):
    with open(file_name) as f:
        data = json.load(f)
        return data

def find_path(graph, start, end, path=[]):

    path = path + [start]

    if start == end:
        return path

    if start not in graph.keys():
        return None
        
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath:
                return newpath
    return None


def all_paths(graph, curr_node, end_node, path=[]):

    path = path + [curr_node]

    if curr_node == end_node:
        return [path]

    if curr_node not in graph.keys():
        return []
        
    paths = []
    for i in graph[curr_node]:
        if i[0] not in path:
            newpaths = all_paths(graph, i[0], end_node, path)

            for newpath in newpaths:
                paths.append(newpath)

    paths.sort(key=len)
    return paths


def shortest_path(graph, curr_node, end_node, path):

    path = path + [curr_node]
    print("Current path: " + str(path))
    

    # Check whether the "start" and "end" are the same
    # if it is, return none
    if curr_node == end_node:
        print("***End reached***\n")
        return path

    # Check whether "start" is in the graph
    # if it is not, return none
    if curr_node not in graph.keys(): 
        return None

    # Declare the shortest path to none
    shortest = None
    
    # Loop the graph w/ the key of the "start"
    for i in graph[curr_node]:

        if i[0] not in path: # <-- check if the adjacent node is already in the path
            print("\t-> " + i[0])
            new_path = shortest_path(graph, i[0], end_node, path)
            print("\tNew path: " + str(new_path))

            if new_path:
                print(not shortest or len(new_path) < len(shortest))

                if not shortest or len(new_path) < len(shortest):
                    shortest = new_path
                    print("Shortest: " + str(shortest))

    print("Return: " + str(shortest))
    return shortest

# print(shortest_path(graph, 'F', 'Q', path=[]))

def routes(graph, curr, end, cost, path=[]):

    path = path + [curr]
    print("Current path: " + str(path) + "\nCurrent cost: " + str(cost))

    if curr == end:    
        print("***End reached***\n")
        fpath = str(path).replace('[', '').replace(']', '').replace("'", '').replace(', ', ' -> ')
        goal_path = dict()
        goal_path.update({fpath: cost})
        return goal_path

    if curr not in graph.keys():
        return []
        
    paths = dict()
    for adj_node in graph[curr]:
        print("\t--- (" + str(adj_node[1]) + " mins) --> " + adj_node[0])
        if adj_node[0] not in path:
            
            newpaths = routes(graph, adj_node[0], end, cost + adj_node[1], path)
            print("\tCurrent path: " + str(path))
            print("\tNew path: " + str(newpaths))

            for k, v in newpaths.items():
                print("append():" + k + ": " + str(v))
                paths.update({k: v for k, v in sorted(newpaths.items(), key = lambda item: item[1])})
                
    print("Return: " + str(paths))
    return paths

for k, v in routes(graph, 'F', 'Q', 0, path=[]).items():
    print(str(v) + "\t" + k)





# for line in graph2:
#     print(line)
#     for node in graph2[line].items():
#         print("\t" + node[0])
#         for adj_node in node[1]:
#             print("\t\t" + adj_node[0])
#     print("====")

# for line in graph2:
#     for node in graph2[line].items():
#         if node[0] == 'F_L2':
#             for adj_node in node[1]:
#                 print(adj_node[0])
        

def routes2(graph, curr, end, cost, path=[]):

    print()

    path = path + [curr]

    if curr == end:    
        fpath = str(path).replace('[', '').replace(']', '').replace("'", '').replace(', ', ' -> ')
        goal_path = dict()
        goal_path.update({fpath: cost})
        return goal_path
    
    # if curr not in graph.keys():
    #     return []
        
    paths = dict()
    for line in graph2:
        for node in graph2[line].items():
            if node[0] == curr:
                for adj_node in node[1]:

                    if adj_node[0] not in path:
                        newpaths = routes2(graph, adj_node[0], end, cost + adj_node[1], path)

                        for k, v in newpaths.items():
                            paths.update({k: v for k, v in sorted(newpaths.items(), key = lambda item: item[1])})
    return paths

for k, v in routes2(graph2, 'F_L2', 'P_L1', 0, path=[]).items():
    print(str(v) + "\t" + k)

print("~15.0 min(s)\t(A)--<line1>--(B)")
print("~18.2 min(s)\t(A)--<line1>--(B)--<line2>--(C)")

node = "A-L1"
station, line = node.split('-', 1)

print(station)
print(line)