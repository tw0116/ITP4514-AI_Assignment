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


def A_star(graph, costs, open, closed, cur_node):

    if cur_node in open:
        open.remove(cur_node)
    closed.add(cur_node)

    # Find 
    for i in graph:
        if (i[0] == cur_node and costs[i[0]] + i[2] + i[3] < costs[i[1]]):
            open.add(i[1])
            costs[i[1]] = costs[i[0]] + i[2] + i[3] # Update path's cost to the connected node
            path[i[1]] = path[i[0]] + ' -> ' + i[1] # Update path of the connected node
    costs[cur_node] = 999999 
    print(costs)

    small = min(costs, key = costs.get) # Find the key in dict():costs with the minimum value

    if small not in closed:
        A_star(graph, costs, open, closed, small)

# =======================================================================================================================
#   dict(): costs   - Store all the node(s) that has not been searched
#   dict(): path    - Store all the node(s) that has been searched
# =======================================================================================================================
costs = dict()
path = dict()

for i in nodes:
    costs[i] = 999999   # dict():costs - Set the keys as the nodes and all values to 999999
    path[i] = ' '       # dict():path - Set the keys as the nodes and all values to ' '

# =======================================================================================================================
#   set(): open     - Store all the node(s) that has not been searched
#   set(): closed   - Store all the node(s) that has been searched
# =======================================================================================================================
open = set()
closed = set()



start_node = input("Enter the Start Node: ")
open.add(start_node)

path[start_node] = start_node   # Set the value with the key "start_node" to "start_node" since the path begin with the "start_node", example: {A: A} 
costs[start_node] = 0           # Set the value with the key "start_node" to 0, example: {A: 0}  

A_star(graph, costs, open, closed, start_node)

goal_node = input("Enter the Goal Node: ")

print("Path with least cost is: ", path[goal_node])

print(path)
print(costs)
print(open)
print(closed)