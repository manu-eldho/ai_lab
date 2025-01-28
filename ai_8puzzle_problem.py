import heapq

def manhattan_distance(state, goal):
    distance = 0
    for i in range(1, 9):
        x1, y1 = divmod(state.index(i), 3)
        x2, y2 = divmod(goal.index(i), 3)
        distance += abs(x1 - x2) + abs(y1 - y2)
    return distance

def best_first_search(initial, goal):
    open_list = []
    heapq.heappush(open_list, (manhattan_distance(initial, goal), initial))
    closed_list = set()
    came_from = {}

    while open_list:

        _, current_state = heapq.heappop(open_list)
        closed_list.add(tuple(current_state))
        
        if current_state == goal:
            return reconstruct_path(came_from, current_state)
        
        zero_index = current_state.index(0)
        x, y = divmod(zero_index, 3)
        
        neighbors = []
        if x > 0:  # Move blank up
            neighbors.append(zero_index - 3)
        if x < 2:  # Move blank down
            neighbors.append(zero_index + 3)
        if y > 0:  # Move blank left
            neighbors.append(zero_index - 1)
        if y < 2:  # Move blank right
            neighbors.append(zero_index + 1)
        
        for neighbor in neighbors:
            new_state = current_state[:]
            new_state[zero_index], new_state[neighbor] = new_state[neighbor], new_state[zero_index]
            if tuple(new_state) in closed_list:
                continue
            
            heapq.heappush(open_list, (manhattan_distance(new_state, goal), new_state))
            came_from[tuple(new_state)] = current_state
    
    return None

def reconstruct_path(came_from, current):
    path = [current]
    while tuple(current) in came_from:
        current = came_from[tuple(current)]
        path.append(current)
    path.reverse()
    return path

def print_puzzle(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()

def input_puzzle(prompt):
    puzzle = []
    print(prompt)
    for i in range(3):
        row = input(f"Enter row {i+1} (3 numbers separated by spaces, use 0 for the blank): ")
        puzzle.extend([int(num) for num in row.split()])
    return puzzle

if __name__ == "__main__":
    initial = input_puzzle("Enter the initial state:")
    goal = input_puzzle("Enter the goal state:")

    print("\nInitial State:")
    print_puzzle(initial)

    print("Goal State:")
    print_puzzle(goal)

    print("\nBest-First Search:")
    path = best_first_search(initial, goal)
    
    if path:
        print(f"Path to goal found in {len(path)-1} steps:")
        for state in path:
            print_puzzle(state)
    else:
        print("No path found.")
