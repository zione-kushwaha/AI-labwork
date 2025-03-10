# WAP to represent the following graphs using a dictionary with costs.

def print_graph(graph):
    for node in graph:
        for adjacent in graph[node]:
            print(f"{node} -> {adjacent} (cost: {graph[node][adjacent]})")

def dfs(graph, start, goal, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(f'{start} -> ', end='')
    if start == goal:
        return True
    for next_node in graph[start]:
        if next_node not in visited:
            if dfs(graph, next_node, goal, visited):
                return True
    return False

graph = {
    'biratnagar': {'ithari': 22, 'rangeli': 25, 'biratchowk': 30},
    'ithari': {'dharan': 20, 'biratchowk': 11},
    'dharan': {},
    'rangeli': {'khanepokhari': 25, 'ulabari': 40},
    'biratchowk': {'khanepokhari': 10},
    'khanepokhari': {'urlabari': 12},
    'urlabari': {"damak": 6},
    'damak': {},
}

print_graph(graph)
print("\nDFS Traversal:")
start_node = 'biratnagar'
goal_node = 'damak'
if dfs(graph, start_node, goal_node):
    print(f"Path found from {start_node} to {goal_node}")
else:
    print(f"No path found from {start_node} to {goal_node}")