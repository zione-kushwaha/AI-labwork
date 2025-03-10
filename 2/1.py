# WAP to represent the following graphs using a dictionary with costs.

G = {
    'biratnagar': {'ithari': 22, 'rangeli': 25, 'biratchowk': 30},
    'ithari': {'dharan': 20, 'biratchowk': 11, 'biratnagar': 22},
    'dharan': {'ithari': 20},
    'rangeli': {'khanepokhari': 25, 'urlabari': 40, 'biratnagar': 25},
    'biratchowk': {'khanepokhari': 10},
    'khanepokhari': {'urlabari': 12},
    'urlabari': {"damak": 6},
    'damak': {},
}

def DFS(G, start, goal):
    stack = list()
    prev = dict()
    visited = set()
    # pushing the starting state into stack
    stack.append(start)
    # initializing the prev state of starting state
    prev[start] = " "
    # repeat until the stack is not empty
    while stack:
        poppedState = stack.pop()
        visited.add(poppedState)
        if poppedState == goal:
            return True, prev
        for chimeki in G[poppedState]:
            if chimeki not in stack and chimeki not in visited:
                stack.append(chimeki)
                prev[chimeki] = poppedState
    return False, prev

def reconstruct_path(G, previous, goal):
    path = goal
    while previous[goal] != " ":
        path = previous[goal] + " -> " + path
        goal = previous[goal]
    return path

start = 'dharan'
goal = 'damak'
goalFound, previous = DFS(G, start, goal)
if goalFound:
    print(reconstruct_path(G, previous, goal))
else:
    print("No path found ")