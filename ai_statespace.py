from collections import deque

def build_graph():
    graph = {}
    num_nodes = int(input("Enter the number of nodes: "))
    
    print("Enter the nodes:")
    for _ in range(num_nodes):
        node = input().strip()
        graph[node] = []

    num_edges = int(input("Enter the number of edges: "))
    
    print("Enter each edge as a pair of nodes (e.g., A B):")
    for _ in range(num_edges):
        u, v = input().strip().split()
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)  
    
    return graph

def bfs(graph, start):
    visited = set() 
    queue = deque([start]) 

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex, end=' ')
            visited.add(vertex)
            queue.extend(neighbor for neighbor in graph[vertex] if neighbor not in visited)

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()  

    visited.add(start)
    print(start, end=' ')
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

def main():
    graph = build_graph()
    
    print("\nGraph built:")
    for node, neighbors in graph.items():
        print(f"{node}: {', '.join(neighbors)}")
    
    start_node = input("\nEnter the starting node for BFS and DFS: ").strip()

    if start_node not in graph:
        print(f"Node {start_node} does not exist in the graph.")
        return

    print("\nBFS traversal starting from node '{}':".format(start_node))
    bfs(graph, start_node)

    print("\nDFS traversal starting from node '{}':".format(start_node))
    dfs(graph, start_node)

if __name__ == "__main__":
    main()