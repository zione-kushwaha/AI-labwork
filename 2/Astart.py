from queue import PriorityQueue

graph = {
    'biratnagar': {'ithari': 22, 'rangeli': 25, 'biratchowk': 30},
    'ithari': {'dharan': 20, 'biratchowk': 11},
    'dharan': {},
    'rangeli': {'khanepokhari': 25, 'urlabari': 40},
    'biratchowk': {'khanepokhari': 10},
    'khanepokhari': {'urlabari': 12},
    'urlabari': {"damak": 6},
    'damak': {},
}

h = {
    'biratnagar': 46,
    'ithari': 39,
    'dharan': 41,
    'rangeli': 28,
    'biratchowk': 29,
    'khanepokhari': 17,
    'urlabari': 6,
    'damak': 0,
}

def astar(G, h, start, goal):
    pq = PriorityQueue()
    prev = {}
    visited = set()
    # ENQUEUE THE STARTING STATE INTO THE QUEUE 
    pq.put((0 + h[start], start))
    prev[start] = None
    while not pq.empty():
        outstateFscore, outstate = pq.get()
        visited.add(outstate)
        if outstate == goal:
            return True, prev, outstateFscore
        for chimeki in G[outstate]:
            if chimeki not in visited and chimeki not in prev:
                pq.put((outstateFscore - h[outstate] + G[outstate][chimeki] + h[chimeki], chimeki))
                prev[chimeki] = outstate
    return False, prev, outstateFscore

def reconstruct_path(previous, goal):
    path = []
    while goal is not None:
        path.append(goal)
        goal = previous[goal]
    path.reverse()
    return " -> ".join(path)

start = 'biratnagar'
goal = 'damak'
goalFound, previous, _ = astar(graph, h, start, goal)
if goalFound and goal in previous:
    print(reconstruct_path(previous, goal))
else:
    print(f"No path found")
