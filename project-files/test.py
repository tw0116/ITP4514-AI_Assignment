# A function to find the line of the "station_start" and "station_end"
# Check whether the "station_start" and the "station_end" at the same line.

    # if "station_start" and "station_end" are at the same line
        # alther heuristic function of the lines

    # if "station_start" and "station_end" are not at the same line
        # alther heuristic function of the lines

import json

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

print(graph['A'][0][0])

for i in graph['B']:
    for j in i[0]:
        print(j)

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


def all_paths(graph, start, end, path=[]):

    path = path + [start]

    if start == end:
        return [path]

    if start not in graph.keys():
        return []
        
    paths = []
    for i in graph[start]:
        for node in i[0]:
            if node not in path:
                newpaths = all_paths(graph, node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
    paths.sort(key=len)
    return paths


def shortest_path(graph, start, end, path):

    path = path + [start]

    # Check whether the "start" and "end" are the same
    # if it is, return none
    if start == end:
        return path

    # Check whether "start" is in the path
    # if it is, return none
    if start not in graph.keys(): 
        return None

    # Declare the shortest path to none
    shortest = None
    
    # Loop the graph w/ the same key of the "start"
    for i in graph[start]:
        for node in i[0]:
            if node not in path:
                new_path = shortest_path(graph, node, end, path)

                if new_path:
                    if not shortest or len(new_path) < len(shortest):
                        shortest = new_path
    return shortest

path = []
print(shortest_path(graph, 'F', 'Q', path))