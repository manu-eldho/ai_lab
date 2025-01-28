def minimax(depth, nodeIndex, maximizingPlayer, values, names, alpha, beta, path, use_pruning):
    # Check if we have reached the leaf node
    if depth == 0 or nodeIndex >= len(values):
        return values[nodeIndex], path
    
    if maximizingPlayer:
        best = float('-inf')
        best_path = None
        for i in range(2):  # Two children in a binary tree
            val, temp_path = minimax(depth - 1, nodeIndex * 2 + i, False, values, names, alpha, beta, path + [names[nodeIndex * 2 + i + 1]], use_pruning)
            if val > best:
                best = val
                best_path = temp_path
            if use_pruning:
                alpha = max(alpha, best)
                if beta <= alpha:
                    break
        return best, best_path
    else:
        best = float('inf')
        best_path = None
        for i in range(2):  # Two children in a binary tree
            val, temp_path = minimax(depth - 1, nodeIndex * 2 + i, True, values, names, alpha, beta, path + [names[nodeIndex * 2 + i + 1]], use_pruning)
            if val < best:
                best = val
                best_path = temp_path
            if use_pruning:
                beta = min(beta, best)
                if beta <= alpha:
                    break
        return best, best_path

def main():
    print("Enter the depth of the game tree:")
    depth = int(input().strip())

    leaf_nodes = 2 ** depth
    total_nodes = 2 ** (depth + 1) - 1

    print(f"Enter the {leaf_nodes} leaf node values (space-separated):")
    values = list(map(int, input().strip().split()))

    if len(values) != leaf_nodes:
        print(f"Error: You must enter exactly {leaf_nodes} leaf node values.")
        return

    print(f"Enter the names of all {total_nodes} nodes (space-separated):")
    names = input().strip().split()

    if len(names) != total_nodes:
        print(f"Error: You must enter exactly {total_nodes} node names.")
        return

    # Run Minimax Algorithm without Alpha-Beta Pruning
    print("\nRunning Minimax Algorithm...")
    best_value_no_pruning, best_path_no_pruning = minimax(depth, 0, True, values, names, float('-inf'), float('inf'), [names[0]], use_pruning=False)
    
    # Run Minimax Algorithm with Alpha-Beta Pruning
    print("\nRunning Minimax Algorithm with Alpha-Beta Pruning...")
    best_value_pruning, best_path_pruning = minimax(depth, 0, True, values, names, float('-inf'), float('inf'), [names[0]], use_pruning=True)

    # Display results
    print(f"\nMinimax without Alpha-Beta Pruning:")
    print(f"The optimal value is: {best_value_no_pruning}")
    print(f"The path to the optimal value is: {' -> '.join(best_path_no_pruning)}")

    print(f"\nMinimax with Alpha-Beta Pruning:")
    print(f"The optimal value is: {best_value_pruning}")
    print(f"The path to the optimal value is: {' -> '.join(best_path_pruning)}")

if __name__ == "__main__":
    main()
