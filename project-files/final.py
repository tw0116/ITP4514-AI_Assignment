from pprint import PrettyPrinter, pprint

sample_dataset = {
    'tsuen wan/twl': [['tai wo hau/twl', 2.0]],
    'tai wo hau/twl': [['tsuen wan/twl', 2.0], ['kwai hing/twl', 2.0]],
    'kwai hing/twl': [['tai wo hau/twl', 2.0], ['kwai fong/twl', 2.0]],
    'kwai fong/twl': [['kwai hing/twl', 2.0], ['lai king/twl', 2.0]],
    'lai king/twl': [['kwai fong/twl', 2.0], ['mei foo/twl', 2.0], ['lai king/tcl', 0]],# <interchange>
    'mei foo/twl': [['lai king/twl', 2.0], ['lai chi kok/twl', 2.0]],
    'lai chi kok/twl': [['mei foo/twl', 2.0], ['cheung sha wan/twl', 2.0]],
    'cheung sha wan/twl': [['lai chi kok/twl', 2.0], ['sham shui po/twl', 2.0]],
    'sham shui po/twl': [['cheung sha wan/twl', 2.0], ['prince edward/twl', 2.0]],
    'prince edward/twl': [['sham shui po/twl', 2.0], ['mong kok/twl', 2.0], ['prince edward/ktl', 0]],# <interchange>
    'mong kok/twl': [['prince edward/twl', 2.0], ['yau ma tei/twl', 2.0], ['mong kok/ktl', 0]],# <interchange>
    'yau ma tei/twl': [['mong kok/twl', 2.0], ['jordan/twl', 2.0], ['yau ma tei/ktl', 0]],# <interchange>
    'jordan/twl': [['yau ma tei/twl', 2.0], ['tsim sha tsui/twl', 2.0]],
    'tsim sha tsui/twl': [['jordan/twl', 2.0], ['admiralty/twl', 2.0]],
    'admiralty/twl': [['tsim sha tsui/twl', 2.0], ['central/twl', 2.0], ['admiralty/il', 0]],# <interchange>
    'central/twl': [['admiralty/twl', 2.0], ['central/il', 0]],# <interchange>

    'tung chung/tcl': [['sunny bay/tcl', 3.3]],
    'sunny bay/tcl': [['tung chung/tcl', 3.3], ['tsing yi/tcl', 3.3]],
    'tsing yi/tcl': [['sunny bay/tcl', 3.3], ['lai king/tcl', 3.3]],
    'lai king/tcl': [['tsing yi/tcl', 3.3], ['nam cheong/tcl', 3.3], ['lai king/twl', 0]],# <interchange>
    'nam cheong/tcl': [['lai king/tcl', 3.3], ['olympic/tcl', 3.3]],
    'olympic/tcl': [['nam cheong/tcl', 3.3], ['kowloon/tcl', 3.3]],
    'kowloon/tcl': [['olympic/tcl', 3.3], ['hong kong/tcl', 3.3]],
    'hong kong/tcl': [['kowloon/tcl', 3.3], ['central/il', 0]],# <interchange>

    'whampoa/ktl': [['ho man tin/ktl', 4.2]],
    'ho man tin/ktl': [['whampoa/ktl', 4.2], ['yau ma tei/ktl', 2.0]],
    'yau ma tei/ktl': [['ho man tin/ktl', 2.0], ['mong kok/ktl', 2.0], ['yau ma tei/twl', 0]],# <interchange>
    'mong kok/ktl': [['yau ma tei/ktl', 2.0], ['prince edward/ktl', 2.0], ['mong kok/twl', 0]],# <interchange>
    'prince edward/ktl': [['mong kok/ktl', 2.0], ['shek kip mei/ktl', 2.0], ['prince edward/twl', 0]],# <interchange>
    'shek kip mei/ktl': [['prince edward/ktl', 2.0], ['kowloon tong/ktl', 2.0]],
    'kowloon tong/ktl': [['shek kip mei/ktl', 2.0], ['lok fu/ktl', 2.0]],
    'lok fu/ktl': [['kowloon tong/ktl', 2.0], ['wong tai sin/ktl', 2.0]],
    'wong tai sin/ktl': [['lok fu/ktl', 2.0], ['diamond hill/ktl', 2.0]],
    'diamond hill/ktl': [['wong tai sin/ktl', 2.0], ['choi hung/ktl', 2.0]],
    'choi hung/ktl': [['diamond hill/ktl', 2.0], ['kowloon bay/ktl', 2.0]],
    'kowloon bay/ktl': [['choi hung/ktl', 2.0], ['ngau tau kok/ktl', 2.0]],
    'ngau tau kok/ktl': [['kowloon bay/ktl', 2.0], ['kwun tong/ktl', 2.0]],
    'kwun tong/ktl': [['ngau tau kok/ktl', 2.0], ['lam tin/ktl', 2.0]],
    'lam tin/ktl': [['kwun tong/ktl', 2.0], ['yau tong/ktl', 2.0]],
    'yau tong/ktl': [['lam tin/ktl', 2.0], ['tiu keng leng/ktl', 2.0], ['yau tong/tkol', 0]],# <interchange>
    'tiu keng leng/ktl': [['yau tong/ktl', 2.0], ['tiu keng leng/tkol', 0]]# <interchange>

    # 'kennedy town/il': [[],],
    # 'hku/il': [[],],
    # 'sai ying pun/il': [[],],
    # 'sheung wan/il': [[],],
    # 'central/il': [[],],# <interchange>
    # 'admiralty/il': [[],],# <interchange>
    # 'wan chai/il': [[],],
    # 'causeway bay/il': [[],],
    # 'tin hau/il': [[],],
    # 'fortress hill/il': [[],],
    # 'north point/il': [[],],# <interchange>
    # 'quarry bay/il': [[],],# <interchange>
    # 'tai koo/il': [[],],
    # 'sai wan ho/il': [[],],
    # 'shau kei wan/il': [[],],
    # 'heng fa chuen/il': [[],],
    # 'chai wan/il': [[],],

    # 'po lam/tkol': [[],],
    # 'hang hau/tkol': [[],],
    # 'lohas park/tkol': [[],],
    # 'tseung kwan o/tkol': [[],],
    # 'tiu keng leng/tkol': [[],],# <interchange>
    # 'yau tong/tkol': [[],],# <interchange>
    # 'quarry bay/tkol': [[],],# <interchange>
    # 'north point/tkol': [[],]# <interchange>
}

# print(getLine(sample_dataset, 'lai chi kok'))

def getLine(graph, station):
    for node in graph:
        if station == node.split('/', 1)[0]:
            return node.split('/', 1)[1]

def getRoutes():
    return []


costs = dict()
routes = dict()

for station in sample_dataset:
    costs[station] = 999999
    routes[station] = ''

visited = set()
unvisited = set()

def getOptimalRoutes(graph, costs, visited, unvisited, curr_station):

    if curr_station in unvisited:
        unvisited.remove(curr_station)
    visited.add(curr_station)
    print(curr_station)

    for node in graph.items():
        station = node[0]
        adj_nodes = node[1]

        for adj_node in adj_nodes:
            adj_station = adj_node[0]
            cost = adj_node[1]

            print(station, adj_station, cost)

            if (station == curr_station and costs[station] + cost < costs[adj_station]):
                unvisited.add(adj_station)
                costs[adj_station] = costs[station] + cost
                routes[adj_station] = routes[station] + '->' + adj_station
    print()
    print()
    
    costs[curr_station] = 999999
    optimal = min(costs, key = costs.get)

    if optimal not in visited:
        getOptimalRoutes(graph, costs, visited, unvisited, optimal)

start = 'kwai fong'
goal = 'admiralty'

def getNodeByStation(station):
    for node in sample_dataset:
        if station == node.split('/')[0]:
            return node

start_node = getNodeByStation(start)
goal_node = getNodeByStation(goal)

unvisited.add(start_node)
routes[start_node] = start_node
costs[start_node] = 0

getOptimalRoutes(sample_dataset, costs, visited, unvisited, start_node)
print("Path with least cost is: ", routes[goal_node])

# no need to split node
pprint(costs)
pprint(routes)
pprint(visited)
pprint(unvisited)