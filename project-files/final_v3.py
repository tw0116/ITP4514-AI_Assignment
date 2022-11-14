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
    "central/twl": [["admiralty/twl", 2.0], ["hong kong/tcl", 0], ["central/il", 0]], # Interchange

    "tung chung/tcl": [["sunny bay/tcl", 3.3]],
    "sunny bay/tcl": [["tung chung/tcl", 3.3], ["tsing yi/tcl", 3.3]],
    "tsing yi/tcl": [["sunny bay/tcl", 3.3], ["lai king/tcl", 3.3]],
    "lai king/tcl": [["tsing yi/tcl", 3.3], ["nam cheong/tcl", 3.3], ["lai king/twl", 0]], # Interchange
    "nam cheong/tcl": [["lai king/tcl", 3.3], ["olympic/tcl", 3.3]],
    "olympic/tcl": [["nam cheong/tcl", 3.3], ["kowloon/tcl", 3.3]],
    "kowloon/tcl": [["olympic/tcl", 3.3], ["hong kong/tcl", 3.3]],
    "hong kong/tcl": [["kowloon/tcl", 3.3], ["central/twl", 0], ["central/il", 0]], # Interchange

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
    "central/il": [["sheung wan/il", 1.9], ["admiralty/il", 1.9], ["hong kong/tcl", 0], ["central/twl", 0]], # Interchange
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

visited_line = set()
curr_line = set()

lines_heuristic = dict()
for line in lines:
    lines_heuristic[line] = 0

print(lines_heuristic)











visited_station = set()
curr_station = set()

stations_heuristic = dict()
for station in sample_dataset:
    stations_heuristic[station] = 0
    
for station, heuristic in stations_heuristic.items():
    print({station : heuristic})




# root_line = 'twl'
# visited_line.add(root_line)
# curr_line.add(root_line)

# root_station = 'mei foo/twl'
# visited_station.add(root_station)
# curr_station.add(root_station)

def defHeuristic(dataset, heuristic_set, visited, curr_level, levelNum, heuristic):
    
    levelNum = levelNum + 1

    next_level = set()
    for node in curr_level:
        for adj_node in dataset[node]:
            if adj_node[0] not in visited:
                visited.add(adj_node[0])
                next_level.add(adj_node[0])
                heuristic_set[adj_node[0]] = heuristic_set[adj_node[0]] + levelNum * heuristic

    if len(visited) < len(dataset):
        defHeuristic(dataset, heuristic_set, visited, next_level, levelNum, heuristic)

# defHeuristic(lines, lines_heuristic, visited_line, curr_line, 0, 5)
# defHeuristic(sample_dataset, stations_heuristic, visited_station, curr_station, 0, 1)

# print()
# print(lines_heuristic)
# for station, heuristic in stations_heuristic.items():
#     print({station : heuristic})





def setHeuristic(dataset):
    for station in dataset.items():
        adj_stations = station[1]
        for adj_station in adj_stations:
            line = adj_station[0].split('/')[1]
            adj_station.append(lines_heuristic[line] * stations_heuristic[adj_station[0]])

# setHeuristic(sample_dataset)

# print()
# for station, adj_nodes in sample_dataset.items():
#     print({station: adj_nodes})




def getLine(graph, station):
    for node in graph:
        if station == node.split('/', 1)[0]:
            return node.split('/', 1)[1]

def getNodeByStation(graph, station):
    for node in graph:
        if station == node.split('/')[0]:
            return node




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



start = 'mei foo'
goal = 'central'

start_line = getLine(sample_dataset, start)
goal_line = getLine(sample_dataset, goal)

if start_line == goal_line:
    root_line = start_line
    visited_line.add(root_line)
    curr_line.add(root_line)

if start_line != goal_line:
    root_line = goal_line
    visited_line.add(root_line)
    curr_line.add(root_line)

defHeuristic(lines, lines_heuristic, visited_line, curr_line, 0, 5)

root_station = getNodeByStation(sample_dataset, goal)
visited_station.add(root_station)
curr_station.add(root_station)

defHeuristic(sample_dataset, stations_heuristic, visited_station, curr_station, 0, 1)

print()
print(lines_heuristic)
for station, heuristic in stations_heuristic.items():
    print({station : heuristic})

setHeuristic(sample_dataset)

print()
for station, adj_nodes in sample_dataset.items():
    print({station: adj_nodes})

start_node = getNodeByStation(sample_dataset, start)
goal_node = getNodeByStation(sample_dataset, goal)

# start_node = 'tiu keng leng/tkol'
# goal_node = 'kowloon/tcl'

# start_node = 'kowloon/tcl'
# goal_node = 'tiu keng leng/tkol'

# start_node = 'mei foo/twl'
# goal_node = 'central/il'





unvisited.add(start_node)
routes[start_node] = {'Route': start_node.split('/')[0].title(), 'Line': [start_node.split('/')[1].upper()], 'Transfer Station': []}
costs[start_node] = 0

getOptimalRoutes(sample_dataset, costs, weights, visited, unvisited, start_node)
print("Result:", routes[goal_node])