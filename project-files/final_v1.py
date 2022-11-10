import json
from pprint import PrettyPrinter, pprint
from itertools import zip_longest

sample_dataset = {
    "tsuen wan/twl": [["tai wo hau/twl", 2.0]],
    "tai wo hau/twl": [["tsuen wan/twl", 2.0], ["kwai hing/twl", 2.0]],
    "kwai hing/twl": [["tai wo hau/twl", 2.0], ["kwai fong/twl", 2.0]],
    "kwai fong/twl": [["kwai hing/twl", 2.0], ["lai king/twl", 2.0]],
    "lai king/twl": [["kwai fong/twl", 2.0], ["mei foo/twl", 2.0], ["lai king/tcl", 0]],
    "mei foo/twl": [["lai king/twl", 2.0], ["lai chi kok/twl", 2.0]],
    "lai chi kok/twl": [["mei foo/twl", 2.0], ["cheung sha wan/twl", 2.0]],
    "cheung sha wan/twl": [["lai chi kok/twl", 2.0], ["sham shui po/twl", 2.0]],
    "sham shui po/twl": [["cheung sha wan/twl", 2.0], ["prince edward/twl", 2.0]],
    "prince edward/twl": [["sham shui po/twl", 2.0], ["mong kok/twl", 2.0], ["prince edward/ktl", 0]],
    "mong kok/twl": [["prince edward/twl", 2.0], ["yau ma tei/twl", 2.0], ["mong kok/ktl", 0]],
    "yau ma tei/twl": [["mong kok/twl", 2.0], ["jordan/twl", 2.0], ["yau ma tei/ktl", 0]],
    "jordan/twl": [["yau ma tei/twl", 2.0], ["tsim sha tsui/twl", 2.0]],
    "tsim sha tsui/twl": [["jordan/twl", 2.0], ["admiralty/twl", 2.0]],
    "admiralty/twl": [["tsim sha tsui/twl", 2.0], ["central/twl", 2.0], ["admiralty/il", 0]],
    "central/twl": [["admiralty/twl", 2.0], ["central/il", 0]],

    "tung chung/tcl": [["sunny bay/tcl", 3.3]],
    "sunny bay/tcl": [["tung chung/tcl", 3.3], ["tsing yi/tcl", 3.3]],
    "tsing yi/tcl": [["sunny bay/tcl", 3.3], ["lai king/tcl", 3.3]],
    "lai king/tcl": [["tsing yi/tcl", 3.3], ["nam cheong/tcl", 3.3], ["lai king/twl", 0]],
    "nam cheong/tcl": [["lai king/tcl", 3.3], ["olympic/tcl", 3.3]],
    "olympic/tcl": [["nam cheong/tcl", 3.3], ["kowloon/tcl", 3.3]],
    "kowloon/tcl": [["olympic/tcl", 3.3], ["hong kong/tcl", 3.3]],
    "hong kong/tcl": [["kowloon/tcl", 3.3], ["central/il", 0]], 

    "whampoa/ktl": [["ho man tin/ktl", 4.2]],
    "ho man tin/ktl": [["whampoa/ktl", 4.2], ["yau ma tei/ktl", 2.0]],
    "yau ma tei/ktl": [["ho man tin/ktl", 2.0], ["mong kok/ktl", 2.0], ["yau ma tei/twl", 0]],
    "mong kok/ktl": [["yau ma tei/ktl", 2.0], ["prince edward/ktl", 2.0], ["mong kok/twl", 0]],
    "prince edward/ktl": [["mong kok/ktl", 2.0], ["shek kip mei/ktl", 2.0], ["prince edward/twl", 0]],
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
    "yau tong/ktl": [["lam tin/ktl", 2.0], ["tiu keng leng/ktl", 2.0], ["yau tong/tkol", 0]], 
    "tiu keng leng/ktl": [["yau tong/ktl", 2.0], ["tiu keng leng/tkol", 0]], 

    "kennedy town/il": [["hku/il", 1.9]],
    "hku/il": [["kennedy town/il", 1.9], ["sai ying pun/il", 1.9]],
    "sai ying pun/il": [["hku/il", 1.9], ["sheung wan/il", 1.9]],
    "sheung wan/il": [["sai ying pun/il", 1.9], ["central/il", 1.9]],
    "central/il": [["sheung wan/il", 1.9], ["admiralty/il", 1.9], ["central/twl", 0]],
    "admiralty/il": [["central/il", 1.9], ["wan chai/il", 1.9], ["admiralty/twl", 0]],
    "wan chai/il": [["admiralty/il", 1.9], ["causeway bay/il", 1.9]],
    "causeway bay/il": [["wan chai/il", 1.9], ["tin hau/il", 1.9]],
    "tin hau/il": [["causeway bay/il", 1.9], ["fortress hill/il", 1.9]],
    "fortress hill/il": [["tin hau/il", 1.9], ["north point/il", 1.9]],
    "north point/il": [["fortress hill/il", 1.9], ["quarry bay/il", 1.9], ["north point/tkol", 0]],
    "quarry bay/il": [["north point/il", 1.9], ["tai koo/il", 1.9], ["quarry bay/tkol", 0]],
    "tai koo/il": [["quarry bay/il", 1.9], ["sai wan ho/il", 1.9]],
    "sai wan ho/il": [["tai koo/il", 1.9], ["shau kei wan/il", 1.9]],
    "shau kei wan/il": [["sai wan ho/il", 1.9], ["heng fa chuen/il", 1.9]],
    "heng fa chuen/il": [["shau kei wan/il", 1.9], ["chai wan/il", 1.9]],
    "chai wan/il": [["heng fa chuen/il", 1.9]],

    "po lam/tkol": [["hang hau/tkol", 4.2]],
    "hang hau/tkol": [["po lam/tkol", 4.2], ["tseung kwan o/tkol", 4.2]],
    "lohas park/tkol": [["tseung kwan o/tkol", 4.2]],
    "tseung kwan o/tkol": [["hang hau/tkol", 4.2], ["tiu keng leng/tkol", 4.2], ["lohas park/tkol", 4.2]],
    "tiu keng leng/tkol": [["tseung kwan o/tkol", 4.2], ["yau tong/tkol", 4.2], ["tiu keng leng/ktl", 0]],
    "yau tong/tkol": [["tiu keng leng/tkol", 4.2], ["quarry bay/tkol", 4.2], ["yau tong/ktl", 0]],
    "quarry bay/tkol": [["yau tong/tkol", 4.2], ["north point/tkol", 4.2], ["quarry bay/il", 0]],
    "north point/tkol": [["quarry bay/tkol", 4.2], ["north point/il", 0]]
}

graph = {
    'A/line1': [['B/line1', 2.0]],
    'B/line1': [['A/line1', 2.0], ['C/line1', 2.0], ['B/line3', 0]],
    'C/line1': [['B/line1', 2.0], ['H/line1', 2.0]],
    'H/line1': [['C/line1', 2.0], ['K/line1', 2.0],['H/line2', 0]],
    'K/line1': [['H/line1', 2.0], ['P/line1', 3.0],['K/line2', 0]],
    'P/line1': [['K/line1', 3.0], ['P/line3', 0], ['P/line5', 0]],

    'K/line2': [['H/line2', 3.3], ['K/line1', 0]],
    'H/line2': [['K/line2', 3.3], ['D/line2', 3.3], ['H/line1', 0]],
    'D/line2': [['H/line2', 3.3], ['E/line2', 3.3]],
    'E/line2': [['D/line2', 3.3], ['I/line2', 3.3]],
    'I/line2': [['E/line2', 3.3], ['L/line2', 3.3]],
    'L/line2': [['I/line2', 3.3], ['L/line4', 0]],

    'F/line3': [['B/line3', 2.0]],
    'B/line3': [['F/line3', 2.0], ['G/line3', 3.0], ['B/line1', 0]],
    'G/line3': [['B/line3', 3.0], ['J/line3', 2.0]],
    'J/line3': [['G/line3', 2.0], ['P/line3', 5.0]],
    'P/line3': [['J/line3', 5.0], ['P/line1', 0], ['P/line5', 0]],

    'R/line4': [['L/line4', 2.0], ['R/line5', 0]],
    'L/line4': [['R/line4', 2.0], ['M/line4', 2.0],['L/line2', 0]],
    'M/line4': [['L/line4', 2.0]],

    'N/line5': [['O/line5', 2.0]],
    'O/line5': [['N/line5', 2.0], ['P/line5', 2.0]],
    'P/line5': [['O/line5', 2.0], ['Q/line5', 2.0], ['P/line1', 0], ['P/line3', 0]],
    'Q/line5': [['P/line5', 2.0], ['R/line5', 2.0]],
    'R/line5': [['Q/line5', 2.0], ['S/line5', 2.0], ['R/line4', 0]],
    'S/line5': [['R/line5', 2.0]]
}



# print(getLine(sample_dataset, 'lai chi kok'))

# Utilities
def load_graph(file_name):
    with open(file_name) as f:
        data = json.load(f)
        return data

def getLine(graph, station):
    for node in graph:
        if station == node.split('/', 1)[0]:
            return node.split('/', 1)[1]

def getNodeByStation(graph, station):
    for node in graph:
        if station == node.split('/')[0]:
            return node

def formatRoute(route):
    return str(route).replace('[', '').replace(']', '').replace("'", '').replace(', ', ' -> ')

def removeDuplicates(list):
    newList = []
    for value in list:
        if value not in newList:
            newList.append(value)
    return newList




# Depth First Search
# def getRoutes(graph, curr, end, weight, route=[], line=[], interchange=[]):

#     if route and route[-1].split('/')[0] == curr.split('/')[0]:
#         interchange = interchange + [curr.split('/')[0]]
#         line = line + [curr.split('/')[1]]
#     elif not route:
#         line = [curr.split('/')[1]]
    
#     route = route + [curr]     

#     if curr == end:
#         fRoute = []
#         for station in route:
#             fRoute.append(station.split('/')[0])
#         result = dict()
#         result.update({'Route': fRoute, 'Line': line, 'Interchange': interchange, 'Weight': weight})
#         return [result]

#     routes = []
#     for adj_node in graph[curr]:

#         adj_station, cost = adj_node[0] , adj_node[1]

#         if adj_station not in route:
#             newRoutes = getRoutes(graph, adj_station, end, weight+cost, route, line, interchange)

#             for newRoute in newRoutes:
#                 routes.append(newRoute)
#     return routes

# start_node = getNodeByStation(graph, 'F')
# goal_node = getNodeByStation(graph, 'Q')

# for result in getRoutes(graph, start_node, goal_node, 0, route=[], line=[], interchange=[]): 
#     for route, line in result.items():
#         print(route, line)
#     print()




# Dijkstra’s Shortest Path Algorithm
costs = dict()
routes = dict()

for station in sample_dataset:
    costs[station] = 999999
    routes[station] = {}

visited = set()
unvisited = set()

def getOptimalRoutes(graph, costs, visited, unvisited, curr_station):

    if curr_station in unvisited:
        unvisited.remove(curr_station)
    visited.add(curr_station)

    for node in graph.items():
        station = node[0]
        adj_nodes = node[1]

        for adj_node in adj_nodes:
            adj_station = adj_node[0]
            cost = adj_node[1]

            if (station == curr_station and adj_station not in visited and costs[station] + cost < costs[adj_station]):

                unvisited.add(adj_station)

                costs[adj_station] = costs[station] + cost
                 
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
                    'Weight': round(costs[adj_station])
                }
    
    costs[curr_station] = 999999
    optimal = min(costs, key = costs.get)

    if optimal not in visited:
        getOptimalRoutes(graph, costs, visited, unvisited, optimal)

# start = 'tiu keng leng'
# goal = 'kowloon'

start = 'kowloon'
goal = 'tiu keng leng'

start_node = getNodeByStation(sample_dataset, start)
goal_node = getNodeByStation(sample_dataset, goal)

unvisited.add(start_node)
routes[start_node] = {'Route': start_node.split('/')[0].title(), 'Line': [start_node.split('/')[1].upper()], 'Transfer Station': []}
costs[start_node] = 0

getOptimalRoutes(sample_dataset, costs, visited, unvisited, start_node)
print("Result:", routes[goal_node])

for result in routes[goal_node].items():
    if result[0] == 'Route':
        route = result[1]
        # print(result[1])

    if result[0] == 'Line':
        line = result[1]
        # print(result[1])

    if result[0] == 'Transfer Station':
        transfer_station = result[1]
        # print(result[1])

    if result[0] == 'Weight':
        weight = result[1]
        # print(result[1])


# Format Sample
# my_list = ['a-1', 'b-2', 'c-3', 'd']
# result_3 = [item.split('-') for item in my_list]
# result_3_flat = [item for l in result_3 for item in l]
# print(result_3)
# print(result_3_flat)

# Final Output
# interchange = [[x for x in t if x is not None] for t in zip_longest(line, transfer_station)]
# solution = '(' + str(start.title()) + ')'
# for l in interchange: 
#     if len(l) == 1:
#         solution = solution + '--' + l[0] + '--'
#     else:
#         solution = solution + '--' + l[0] + '--' + '(' + l[1] + ')'
# solution = solution + '(' + str(goal.title()) + ')'

# print('~' + str(weight) + ' min(s)\t' + str(len(transfer_station)) + ' Interchange\t' + str(len(route.split(' -> ')))  + ' Stops')
# print(solution)