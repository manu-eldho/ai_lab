from collections import deque

def water_jug_problem_bfs():
    capacity1 = int(input("cap 1:"))
    capacity2 = int(input("cap 2: "))
    target = int(input('target: '))
    print(f"cap 1:{capacity1},cap 2:{capacity2}")
    initial_state = (0, 0)
    
    queue = deque([(initial_state, [])])  
    visited = set() 
    visited.add(initial_state)
    
    while queue:
        (x, y), path = queue.popleft()
        if x == target:
            output = []
            output.append("Steps to measure exactly 2 liters in Jug A:")
            for i, (a, b) in enumerate(path + [(x, y)]):
                output.append(f"Step {i+1}: Jug A = {a} liters, Jug B = {b} liters")
            return "\n".join(output)
        
        next_states = [
            ((capacity1, y), "Fill Jug A"),                    
            ((x, capacity2), "Fill Jug B"),                    
            ((0, y), "Empty Jug A"),                                
            ((x, 0), "Empty Jug B"),                                
            ((max(x - (capacity2 - y), 0), min(y + x, capacity2)), "Pour A to B"),
            ((min(x + y, capacity1), max(y - (capacity1 - x), 0)), "Pour B to A")
        ]
        
        for (new_a, new_b), _ in next_states:
            new_state = (new_a, new_b)
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [(x, y)]))  # Append new state and updated path

    return "No solution found to measure exactly 2 liters in Jug A."

print(water_jug_problem_bfs())