def is_safe(graph, node, color, colors_given, names):
    for neighbor in graph[node]:
        if colors_given[neighbor] == color:
            return False
    return True

def graph_coloring(graph, colors, colors_given, node, names):
    if node == len(graph):
        return True    
    current_name = names[node]
    print(f"\nProcessing node: {current_name}")
    available_colors = [color for color in colors if color not in [colors_given[neighbor] for neighbor in graph[node]]]
    print(f"Available colors for {current_name}: {available_colors}")    
    for color in colors:
        if is_safe(graph, node, color, colors_given, names):
            colors_given[node] = color
            print(f"{current_name} is assigned color {color}")
            if graph_coloring(graph, colors, colors_given, node + 1, names):
                return True
            # Backtracking
            print(f"Backtracking from node {current_name}")
            colors_given[node] = None 
    
    return False

def main():
    n = int(input("Enter the number of nodes: "))
    m = int(input("Enter the number of edges: "))
    names = []
    for i in range(n):
        name = input(f"Enter the name of node {i + 1}: ")
        names.append(name)
    graph = {i: [] for i in range(n)}    
    print("\nEnter the edges pairwise by node names:")
    for _ in range(m):
        u_name, v_name = input().split()
        u = names.index(u_name)
        v = names.index(v_name)
        graph[u].append(v)
        graph[v].append(u)    
    colors = input("\nEnter the available colors (separated by spaces): ").split()
    colors_given = [None] * n    
    if graph_coloring(graph, colors, colors_given, 0, names):
        print("\nNode and corresponding colors are:")
        for i in range(n):
            print(f"Node {names[i]} ---> {colors_given[i]}")
    else:
        print("No solution exists")

main()