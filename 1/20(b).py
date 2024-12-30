# WAP to represent the following graphs using a dictionary with costs.

def print_graph(graph):
    for node in graph:
        for adjacent in graph[node]:
            print(f"{node} -> {adjacent} (cost: {graph[node][adjacent]})")

graph = {
    'biratnagar': {'ithari': 22, 'rangeli': 25, 'dharan': 20},
    'ithari': {'Dharan': 20, 'biratchowk': 11},
    'dharan': {},
    'rangeli': {'khanepokhari': 25, 'ulabari': 40},
    'biratchowk': {'khanepokhari': 10},
    'khanepokhari': {'urlabari': 12},
    'urlabari': {"damak": 6},
    'damak': {},
    
}

print_graph(graph)