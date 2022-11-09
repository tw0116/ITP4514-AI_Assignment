sample_dataset = {
    "tsuen wan/twl": [["tai wo hau/twl", 2.0]],
    "tai wo hau/twl": [["tsuen wan/twl", 2.0], ["kwai hing/twl", 2.0]],
    "kwai hing/twl": [["tai wo hau/twl", 2.0], ["kwai fong/twl", 2.0]],
    "kwai fong/twl": [["kwai hing/twl", 2.0], ["lai king/twl", 2.0]],
    "lai king/twl": [["kwai fong/twl", 2.0], ["mei foo/twl", 2.0], ["lai king/tcl", 0]], # Interchange
    "mei foo/twl": [["lai king/twl", 2.0], ["lai chi kok/twl", 2.0]],
    "lai chi kok/twl": [["mei foo/twl", 2.0], ["cheung sha wan/twl", 2.0]],
    "cheung sha wan/twl": [["lai chi kok/twl", 2.0], ["sham shui po/twl", 2.0]],
    "sham shui po/twl": [["cheung sha wan/twl", 2.0], ["prince edward/twl", 2.0]],
    "prince edward/twl": [["sham shui po/twl", 2.0], ["mong kok/twl", 2.0], ["prince edward/ktl", 0]], # Interchange
    "mong kok/twl": [["prince edward/twl", 2.0], ["yau ma tei/twl", 2.0], ["mong kok/ktl", 0]], # Interchange
    "yau ma tei/twl": [["mong kok/twl", 2.0], ["jordan/twl", 2.0], ["yau ma tei/ktl", 0]], # Interchange
    "jordan/twl": [["yau ma tei/twl", 2.0], ["tsim sha tsui/twl", 2.0]],
    "tsim sha tsui/twl": [["jordan/twl", 2.0], ["admiralty/twl", 2.0]],
    "admiralty/twl": [["tsim sha tsui/twl", 2.0], ["central/twl", 2.0], ["admiralty/il", 0]], # Interchange
    "central/twl": [["admiralty/twl", 2.0], ["central/il", 0]], # Interchange

    "tung chung/tcl": [["sunny bay/tcl", 3.3]],
    "sunny bay/tcl": [["tung chung/tcl", 3.3], ["tsing yi/tcl", 3.3]],
    "tsing yi/tcl": [["sunny bay/tcl", 3.3], ["lai king/tcl", 3.3]],
    "lai king/tcl": [["tsing yi/tcl", 3.3], ["nam cheong/tcl", 3.3], ["lai king/twl", 0]], # Interchange
    "nam cheong/tcl": [["lai king/tcl", 3.3], ["olympic/tcl", 3.3]],
    "olympic/tcl": [["nam cheong/tcl", 3.3], ["kowloon/tcl", 3.3]],
    "kowloon/tcl": [["olympic/tcl", 3.3], ["hong kong/tcl", 3.3]],
    "hong kong/tcl": [["kowloon/tcl", 3.3], ["central/il", 0]], # Interchange

    "whampoa/ktl": [["ho man tin/ktl", 4.2]],
    "ho man tin/ktl": [["whampoa/ktl", 4.2], ["yau ma tei/ktl", 2.0]],
    "yau ma tei/ktl": [["ho man tin/ktl", 2.0], ["mong kok/ktl", 2.0], ["yau ma tei/twl", 0]],
    "mong kok/ktl": [["yau ma tei/ktl", 2.0], ["prince edward/ktl", 2.0], ["mong kok/twl", 0]],
    "prince edward/ktl": [["mong kok/ktl", 2.0], ["shek kip mei/ktl", 2.0], ["prince edward/twl", 0]], # Interchange
    "shek kip mei/ktl": [["prince edward/ktl", 2.0], ["kowloon tong/ktl", 2.0]],
    "kowloon tong/ktl": [["shek kip mei/ktl", 2.0], ["lok fu/ktl", 2.0]],
    "lok fu/ktl": [["kowloon tong/ktl", 2.0], ["wong tai sin/ktl", 2.0]],
    "wong tai sin/ktl": [["lok fu/ktl", 2.0], ["diamond hill/ktl", 2.0]],
    "diamond hill/ktl": [["wong tai sin/ktl", 2.0], ["choi hung/ktl", 2.0]],
    "choi hung/ktl": [["diamond hill/ktl", 2.0], ["kowloon bay/ktl", 2.0]],
    "kowloon bay/ktl": [["choi hung/ktl", 2.0], ["ngau tau kok/ktl", 2.0]],
    "ngau tau kok/ktl": [["kowloon bay/ktl", 2.0], ["kwun tong/ktl", 2.0]],
    "kwun tong/ktl": [["ngau tau kok/ktl", 2.0], ["lam tin/ktl", 2.0]],
    "lam tin/ktl": [["kwun tong/ktl", 2.0], ["yau tong/ktl", 2.0]],
    "yau tong/ktl": [["lam tin/ktl", 2.0], ["tiu keng leng/ktl", 2.0], ["yau tong/tkol", 0]], # Interchange
    "tiu keng leng/ktl": [["yau tong/ktl", 2.0], ["tiu keng leng/tkol", 0]], # Interchange

    "kennedy town/il": [["hku/il", 1.9]],
    "hku/il": [["kennedy town/il", 1.9], ["sai ying pun/il", 1.9]],
    "sai ying pun/il": [["hku/il", 1.9], ["sheung wan/il", 1.9]],
    "sheung wan/il": [["sai ying pun/il", 1.9], ["central/il", 1.9]],
    "central/il": [["sheung wan/il", 1.9], ["admiralty/il", 1.9], ["central/twl", 0]], # Interchange
    "admiralty/il": [["central/il", 1.9], ["wan chai/il", 1.9], ["admiralty/twl", 0]], # Interchange
    "wan chai/il": [["admiralty/il", 1.9], ["causeway bay/il", 1.9]],
    "causeway bay/il": [["wan chai/il", 1.9], ["tin hau/il", 1.9]],
    "tin hau/il": [["causeway bay/il", 1.9], ["fortress hill/il", 1.9]],
    "fortress hill/il": [["tin hau/il", 1.9], ["north point/il", 1.9]],
    "north point/il": [["fortress hill/il", 1.9], ["quarry bay/il", 1.9], ["north point/tkol", 0]], # Interchange
    "quarry bay/il": [["north point/il", 1.9], ["tai koo/il", 1.9], ["quarry bay/tkol", 0]], # Interchange
    "tai koo/il": [["quarry bay/il", 1.9], ["sai wan ho/il", 1.9]],
    "sai wan ho/il": [["tai koo/il", 1.9], ["shau kei wan/il", 1.9]],
    "shau kei wan/il": [["sai wan ho/il", 1.9], ["heng fa chuen/il", 1.9]],
    "heng fa chuen/il": [["shau kei wan/il", 1.9], ["chai wan/il", 1.9]],
    "chai wan/il": [["heng fa chuen/il", 1.9]],

    "po lam/tkol": [["hang hau/tkol", 4.2]],
    "hang hau/tkol": [["po lam/tkol", 4.2], ["tseung kwan o/tkol", 4.2]],
    "lohas park/tkol": [["tseung kwan o/tkol", 4.2]],
    "tseung kwan o/tkol": [["hang hau/tkol", 4.2], ["tiu keng leng/tkol", 4.2], ["lohas park/tkol", 4.2]],
    "tiu keng leng/tkol": [["tseung kwan o/tkol", 4.2], ["yau tong/tkol", 4.2], ["tiu keng leng/ktl", 0]], # Interchange
    "yau tong/tkol": [["tiu keng leng/tkol", 4.2], ["quarry bay/tkol", 4.2], ["yau tong/ktl", 0]], # Interchange
    "quarry bay/tkol": [["yau tong/tkol", 4.2], ["north point/tkol", 4.2], ["quarry bay/il", 0]], # Interchange
    "north point/tkol": [["quarry bay/tkol", 4.2], ["north point/il", 0]] # Interchange
}

lines = {
    'twl': [['tcl', 0], ['ktl', 0], ['il', 0]],
    'tcl': [['twl', 0], ['il', 0]],
    'ktl': [['twl', 0], ['tkol', 0]],
    'tkol': [['ktl', 0], ['il', 0]],
    'il': [['twl', 0], ['tcl', 0], ['tkol', 0]],
}

visited = set()
level = set()

root_line = 'il'
visited.add(root_line)
level.add(root_line)

lines_heuristic = dict()
for line in lines:
    lines_heuristic[line] = 0

def defHeuristic(visited, curr_level, levelNum):
    
    levelNum = levelNum + 1

    next_level = set()
    for line in curr_level:
        for adj_line in lines[line]:    
            if adj_line[0] not in visited:
                visited.add(adj_line[0])
                next_level.add(adj_line[0])
                lines_heuristic[adj_line[0]] = lines_heuristic[adj_line[0]] + levelNum * 5

    if len(visited) < len(lines):
        defHeuristic(visited, next_level, levelNum)

def setHeuristic(graph):
    for station in graph.items():
        adj_stations = station[1]

        for adj_station in adj_stations:
            line = adj_station[0].split('/')[1]
            adj_station.append(lines_heuristic[line])

def clearHeuristic(graph):
    for item in graph:
        print({item: graph[item]})

    for station in graph.items():
        adj_stations = station[1]

        for adj_station in adj_stations:
            adj_station.pop()

# --Testing--          
# print(lines_heuristic)
 
# defHeuristic(visited, level, levelNum=0)
# print(lines_heuristic)

# setHeuristic(sample_dataset)
# for item in sample_dataset:
#     print({item: sample_dataset[item]})

# print()

# for line in lines:
#     lines_heuristic[line] = 0

# clearHeuristic(sample_dataset)
# for item in sample_dataset:
#     print({item: sample_dataset[item]})




def getLine(graph, station):
    for node in graph:
        if station == node.split('/', 1)[0]:
            return node.split('/', 1)[1]

def getNodeByStation(graph, station):
    for node in graph:
        if station == node.split('/')[0]:
            return node

# Dijkstra’s Shortest Path Algorithm
routes = dict()
costs = dict()
weights = dict()

for station in sample_dataset:
    routes[station] = {}
    costs[station] = 999999
    weights[station] = 0
    
visited = set()
unvisited = set()

def getOptimalRoutes(graph, costs, weights, visited, unvisited, curr_station):

    if curr_station in unvisited:
        unvisited.remove(curr_station)
    visited.add(curr_station)

    for node in graph.items():
        station = node[0]
        adj_nodes = node[1]

        for adj_node in adj_nodes:
            adj_station = adj_node[0]
            cost = adj_node[1]
            heuristic = adj_node[2]

            if (station == curr_station and adj_station not in visited and costs[station] + cost + heuristic < costs[adj_station]):

                unvisited.add(adj_station)

                costs[adj_station] = costs[station] + cost + heuristic
                weights[adj_station] = weights[station] + cost
                 
                if curr_station.split('/')[1] != adj_station.split('/')[1]:
                    routes[station]['Line'] = routes[station]['Line'] + [adj_station.split('/')[1].upper()]
                else: routes[station]['Line']

                if curr_station.split('/')[1] != adj_station.split('/')[1]:
                    routes[station]['Transfer Station'] = routes[station]['Transfer Station'] + [adj_station.split('/')[0].title()]
                else: routes[station]['Transfer Station']

                routes[adj_station] = {
                    'Route': (
                        routes[station]['Route'] + ' -> ' + adj_station.split('/')[0].title()
                        if curr_station.split('/')[0] != adj_station.split('/')[0] 
                        else routes[station]['Route']
                    ),
                    'Line': routes[station]['Line'],
                    'Transfer Station': routes[station]['Transfer Station'],
                    'Weight': round(weights[adj_station])
                }
    
    costs[curr_station] = 999999
    optimal = min(costs, key = costs.get)

    if optimal not in visited:
        getOptimalRoutes(graph, costs, weights, visited, unvisited, optimal)


start = 'tiu keng leng'
goal = 'kowloon'

# --Newly added--
start_line = getLine(sample_dataset, start)
goal_line = getLine(sample_dataset, goal)

if start_line == goal_line:
    root_line = start_line
    visited.add(root_line)
    level.add(root_line)

if start_line != goal_line:
    root_line = goal_line
    visited.add(root_line)
    level.add(root_line)

    defHeuristic(visited, level, levelNum=0)
    setHeuristic(sample_dataset)


# print()
# print(lines_heuristic)
 
defHeuristic(visited, level, levelNum=0)
# print(lines_heuristic)

setHeuristic(sample_dataset)
# for item in sample_dataset:
#     print({item: sample_dataset[item]})


print()
start_node = getNodeByStation(sample_dataset, start)
goal_node = getNodeByStation(sample_dataset, goal)

unvisited.add(start_node)
routes[start_node] = {'Route': start_node.split('/')[0].title(), 'Line': [start_node.split('/')[1].upper()], 'Transfer Station': []}
costs[start_node] = 0

getOptimalRoutes(sample_dataset, costs, weights, visited, unvisited, start_node)
print("Result:", routes[goal_node])

clearHeuristic(sample_dataset)

print()
for line in lines:
    lines_heuristic[line] = 0

