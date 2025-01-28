import heapq

def best_first_search(graph, heuristic, start, goal):
    open_list = []
    heapq.heappush(open_list, (heuristic[start], start))
    closed_list = set()
    came_from = {}

    while open_list:
        _, current_node = heapq.heappop(open_list)
        
        if current_node == goal:
            return reconstruct_path(came_from, current_node)

        closed_list.add(current_node)

        for neighbor, cost in graph[current_node].items():
            if neighbor in closed_list:
                continue
            heapq.heappush(open_list, (heuristic[neighbor], neighbor))
            came_from[neighbor] = current_node
    
    return None

def a_star_search(graph, heuristic, start, goal):
    open_list = []
    heapq.heappush(open_list, (heuristic[start], start))
    g_score = {start: 0}
    came_from = {}

    while open_list:
        _, current_node = heapq.heappop(open_list)

        if current_node == goal:
            return reconstruct_path(came_from, current_node)
        
        for neighbor, cost in graph[current_node].items():
            tentative_g_score = g_score[current_node] + cost
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current_node
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic[neighbor]
                heapq.heappush(open_list, (f_score, neighbor))
    
    return None

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path

def input_graph():
    graph = {}
    n = int(input("Enter the number of nodes: "))
    print("Enter each node and its neighbors with cost (e.g., A B 2):")
    for _ in range(n):
        node = input("Node: ")
        graph[node] = {}
        m = int(input(f"Enter the number of neighbors for {node}: "))
        for _ in range(m):
            neighbor, cost = input(f"Neighbor and cost for {node}: ").split()
            graph[node][neighbor] = int(cost)
    return graph

def input_heuristic(nodes):
    heuristic = {}
    print("Enter the heuristic values for each node:")
    for node in nodes:
        heuristic[node] = int(input(f"Heuristic for {node}: "))
    return heuristic

if __name__ == "__main__":
    graph = input_graph()
    nodes = graph.keys()
    heuristic = input_heuristic(nodes)
    
    start = input("Enter the initial state: ")
    goal = input("Enter the goal state: ")

    print("\nBest-First Search:")
    path = best_first_search(graph, heuristic, start, goal)
    if path:
        print("Path found:", " -> ".join(path))
    else:
        print("No path found.")
    
    print("\nA* Search:")
    path = a_star_search(graph, heuristic, start, goal)
    if path:
        print("Path found:", " -> ".join(path))
    else:
        print("No path found.")
