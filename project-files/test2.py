graph = [
    ['A','B',1,3],
    ['A','C',2,4],
    ['A','H',7,0],
    ['B','D',4,2],
    ['B','E',6,6],
    ['C','F',3,3],
    ['C','G',2,1],
    ['D','E',7,6],
    ['D','H',5,0],
    ['F','H',1,0],
    ['G','H',2,0]
]

temp = []
temp1 = []

for i in graph:
    temp.append(i[0])
    temp1.append(i[1])

nodes = set(temp).union(set(temp1))


def A_star(graph, costs, unvisited, visited, cur_node):

    if cur_node in unvisited:
        unvisited.remove(cur_node)
    visited.add(cur_node)

    for i in graph:
        # print(i[0], i[1], i[2] , cur_node)

        if (i[0] == cur_node and costs[i[0]] + i[2] + i[3] < costs[i[1]]):
            print(i[0], cur_node, i[1], i[2] )
            unvisited.add(i[1])
            costs[i[1]] = costs[i[0]] + i[2] + i[3]
            path[i[1]] = path[i[0]] + ' -> ' + i[1]
    print()
            
    costs[cur_node] = 999999
    small = min(costs, key = costs.get)

    print(visited)
    print(unvisited)
    print(small, costs[small])

    if small not in visited:
        A_star(graph, costs, unvisited, visited, small)


costs = dict()
path = dict()

for i in nodes:
    costs[i] = 999999
    path[i] = ' '

unvisited = set()
visited = set()

# start_node = input("Enter the Start Node: ")
# goal_node = input("Enter the Goal Node: ")
start_node = 'A'
goal_node = 'H'


unvisited.add(start_node)
path[start_node] = start_node
costs[start_node] = 0 

A_star(graph, costs, unvisited, visited, start_node)
print("Path with least cost is: ", path[goal_node])

print()
print(path)
print(costs)
print(unvisited)
print(visited)