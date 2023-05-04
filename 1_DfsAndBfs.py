def dfs(node, g_node):
    if (g_node in visited):
        return 
    if(node in visited):
        return
    else:
        visited.append(node)
        temp_node=graph[node]
        if(len(temp_node)==0):
            print(node)
            return
        else:
            for i in range(len(temp_node)):
                dfs(temp_node[i], g_node)
            print(node)
            return


def bfs(visited1, graph, node, goal): 
  visited1.append(node)
  queue.append(node)
  while queue:          
    m = queue.pop(0) 
    print (m, end = " ") 
    if(m == goal):
        break;
    for neighbour in graph[m]:
      if neighbour not in visited1:
        visited1.append(neighbour)
        queue.append(neighbour)


graph={
    'A':['B','C'],
    'B':['D','A'],
    'C':[],
    'D':['E','F'],
    'E':['G'],
    'F':[],
    'G':['H'],
    'H':[]
}

node_len=len(graph)
s_node = input("Enter the start node: ")
g_node = input("Enter the end node: ")
visited=[]
print("Following is the path for source to destination using Depth-First Search approach")
dfs(s_node, g_node)



visited1 = []
queue = []
print("\n\nFollowing is the path for source to destination using Breadth-First Search approach")
bfs(visited1, graph, s_node, g_node)    