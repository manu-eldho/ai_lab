def minimax(node, tree, is_maximizing):
    if isinstance(tree[node], int):
        print(f"Leaf Node {node} with value {tree[node]}")
        return tree[node], [node]
    
    print(f"Exploring Node {node}")

    if is_maximizing:
        best_value = float('-inf')
        best_path = []
        for child in tree[node]:
            value, path = minimax(child, tree, False)
            if value > best_value:
                best_value = value
                best_path = [node] + path
    else:
        best_value = float('inf')
        best_path = []
        for child in tree[node]:
            value, path = minimax(child, tree, True)
            if value < best_value:
                best_value = value
                best_path = [node] + path

    print(f"Node {node} has value {best_value}")
    return best_value, best_path

def alpha_beta_pruning(node, tree, alpha, beta, is_maximizing):
    if isinstance(tree[node], int):
        print(f"Leaf Node {node} with value {tree[node]}")
        return tree[node], [node]
    
    print(f"Exploring Node {node} with Alpha={alpha} and Beta={beta}")

    if is_maximizing:
        best_value = float('-inf')
        best_path = []
        for child in tree[node]:
            value, path = alpha_beta_pruning(child, tree, alpha, beta, False)
            if value > best_value:
                best_value = value
                best_path = [node] + path
            alpha = max(alpha, best_value)
            print(f"Node {node} updates Alpha={alpha}")
            if beta <= alpha:
                print(f"Pruning occurs at Node {node} as Beta={beta} <= Alpha={alpha}")
                break
    else:
        best_value = float('inf')
        best_path = []
        for child in tree[node]:
            value, path = alpha_beta_pruning(child, tree, alpha, beta, True)
            if value < best_value:
                best_value = value
                best_path = [node] + path
            beta = min(beta, best_value)
            print(f"Node {node} updates Beta={beta}")
            if beta <= alpha:
                print(f"Pruning occurs at Node {node} as Beta={beta} <= Alpha={alpha}")
                break

    print(f"Node {node} has value {best_value}")
    return best_value, best_path

# Input tree creation from the user
def create_tree():
    tree = {}
    n = int(input("Enter the number of non-leaf nodes: "))
    for _ in range(n):
        node = input("Enter the name of the non-leaf node: ")
        children = input(f"Enter the children of {node} separated by space: ").split()
        tree[node] = children
    
    m = int(input("Enter the number of leaf nodes: "))
    for _ in range(m):
        leaf = input("Enter the name of the leaf node: ")
        value = int(input(f"Enter the value of leaf node {leaf}: "))
        tree[leaf] = value
    
    return tree

# Main Function
if __name__ == "__main__":
    tree = create_tree()
    root = input("Enter the root node: ")

    print("\nRunning Minimax Algorithm")
    optimal_value_minimax, optimal_path_minimax = minimax(root, tree, True)
    print(f"Minimax Optimal Value: {optimal_value_minimax}")
    print(f"Minimax Path: {' -> '.join(optimal_path_minimax)}")

    print("\nRunning Alpha-Beta Pruning Algorithm")
    optimal_value_alpha_beta, optimal_path_alpha_beta = alpha_beta_pruning(root, tree, float('-inf'), float('inf'), True)
    print(f"Alpha-Beta Pruning Optimal Value: {optimal_value_alpha_beta}")
    print(f"Alpha-Beta Pruning Path: {' -> '.join(optimal_path_alpha_beta)}")
