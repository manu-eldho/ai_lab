def clean_room(room):
    if room == '1':
        return '0'
    else:
        return room

goal_state = {'A': '0', 'B': '0'}

# Prompt user for the starting location of the vacuum
print("Enter the starting position of the vacuum (A/B): ")
location = input().upper().strip()

print("Enter the initial state of room A (0 for clean, 1 for dirty): ")
initial_A = input().strip()

print("Enter the initial state of room B (0 for clean, 1 for dirty): ")
initial_B = input().strip()

room_states = {'A': initial_A, 'B': initial_B}

if initial_A not in ['0', '1'] or initial_B not in ['0', '1']:
    print("Invalid input. Please enter either 0 or 1 for room states.")
    exit()

rounds = 0
print("Initial State: ", room_states)
print("Desired Goal State:", goal_state)

while True:
    rounds += 1
    if location == 'A':
        room_states['A'] = clean_room(room_states['A'])
        print("Room A was cleaned.")
        print("Move right")
        location = 'B'
    elif location == 'B':
        room_states['B'] = clean_room(room_states['B'])
        print("Room B was cleaned.")
        print("Move left")
        location = 'A'
    else:
        print("Invalid starting position.")
        break
    
    print("Current State:", room_states)
    
    # Check if the goal state is achieved
    if room_states == goal_state:
        break

print("\nGoal state has been reached.")
print("Total cleaning rounds completed:", rounds)
