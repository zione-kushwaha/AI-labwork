# WAP to represent the following graphs using a dictionary.

def print_graph(graph):
    for node in graph:
        print(node, '->', graph[node])


graph = {
    'A': ['B', 'C'],
    'B': [ 'D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': ['H'],
    'F': [],
    'G': [],
    'H': []
}

print_graph(graph)