graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

def shortest_path(graph, start, goal):
    try:
        return next(dfs_paths(graph, start, goal))
    except StopIteration:
        return "Target Not Found"

print("path from source to target node:")
print(list(shortest_path(graph, 'A', 'F')))

