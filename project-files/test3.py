import json
from pprint import PrettyPrinter, pprint
from queue import Empty

graph_v1 = {
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

graph_v2 = {
    'A-line1': [['B-line1/line2', 2.0]],
    'B-line1/line2': [['A-line1', 2.0], ['C-line1', 2.0], ['F-line2', 2.0], ['G-line2', 3.0]],
    'C-line1': [['B-line1/line2', 2.0], ['H-line1/line3', 2.0]],
    'D-line3': [['E-line3', 2.0], ['H-line1/line3', 2.0]],
    'E-line3': [['D-line3', 2.0], ['I-line3', 2.0]],
    'F-line2': [['B-line1/line2', 2.0]],
    'G-line2': [['B-line1/line2', 3.0], ['J-line2', 2.0]],
    'H-line1/line3': [['C-line1', 2.0], ['D-line3', 2.0], ['K-line1/line3', 2.0]],
    'I-line3': [['E-line3', 2.0], ['L-line3/line4', 2.0]],
    'J-line2': [['G-line2', 2.0], ['P-line1/line2/line5', 5.0]],
    'K-line1/line3': [['H-line1/line3', 2.0], ['P-line1/line2/line5', 3.0]],
    'L-line3/line4': [['I-line3', 2.0], ['M-line4', 2.0], ['R-line4/line5', 2.0]],
    'M-line4': [['L-line3/line4', 2.0]],
    'N-line5': [['O-line5', 2.0]],
    'O-line5': [['N-line5', 2.0], ['P-line1/line2/line5', 3.0]],
    'P-line1/line2/line5': [['J-line2', 5.0], ['K-line1/line3', 3.0], ['O-line5', 3.0], ['Q-line5', 2.0]],
    'Q-line5': [['P-line1/line2/line5', 2.0], ['R-line4/line5', 2.0]],
    'R-line4/line5': [['Q-line5', 2.0], ['S-line5', 2.0]],
    'S-line5': [['R-line4/line5', 2.0]]
}


    

def routes_v1(graph, curr, end, cost, path=[]):

    path = path + [curr]
    # print("Current path: " + str(path) + "\nCurrent cost: " + str(cost))

    if curr == end:    
        # print("***End reached***\n")
        fpath = str(path).replace('[', '').replace(']', '').replace("'", '').replace(', ', ' -> ')
        goal_path = dict()
        goal_path.update({fpath: cost})
        return goal_path

    if curr not in graph.keys():
        return []
        
    paths = dict()
    for adj_node in graph[curr]:
        # print("\t--- (" + str(adj_node[1]) + " mins) --> " + adj_node[0])
        if adj_node[0] not in path:
            
            newpaths = routes_v1(graph, adj_node[0], end, cost + adj_node[1], path)
            # print("\tCurrent path: " + str(path))
            # print("\tNew path: " + str(newpaths))

            for k, v in newpaths.items():
                # print("append():" + k + ": " + str(v))
                paths.update({k: v for k, v in sorted(newpaths.items(), key = lambda item: item[1])})
                
    # print("Return: " + str(paths))
    return paths

pprint(routes_v1(graph_v1, 'F', 'Q', 0, path=[]))

# for k, v in routes(graph, 'F', 'Q', 0, path=[]).items():
#     print(str(v) + "\t" + k)

def routes_v2(graph, curr, end, cost, path=[], line=[]):

    for node in graph:
        if curr == node.split('-')[0]:
            curr_node = node
            station, _lines = node.split('-', 1)
            lines = _lines.split('/')
    
    path = path + [station]
    line = line + [lines]

    if station == end:
        return [path], cost, line

    routes = []
    for adj_node in graph[curr_node]:
        
        adj_station = adj_node[0].split('-')[0]
        
        if adj_station not in path:

            new_routes = routes_v2(graph, adj_station, end, cost+adj_node[1], path, line)

            for route in new_routes:
                routes.append(route)
    return routes

print(routes_v2(graph_v2, 'A', 'P', 0, path=[]))

# node = 'a-line1/line2/line3'
# station, lines = node.split('-', 1)
# line = lines.split('/')

# print(station)
# print(line)

