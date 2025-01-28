import re

# Helper functions for CNF conversion

def replace_biconditional(statement):
    """Replace biconditional 'if and only if' by '(P → Q) and (Q → P)'."""
    if 'if and only if' in statement:
        parts = statement.split('if and only if')
        left = parts[0].strip()
        right = parts[1].strip()
        return f"((not P or Q) and (not Q or P))"
    return statement

def replace_implication(statement):
    """Replace implication 'if P then Q' with 'not P or Q'."""
    match = re.search(r'if (.+?) then (.+)', statement)
    if match:
        left = match.group(1).strip()
        right = match.group(2).strip()
        return f"(not P or Q)"
    return statement

def move_negation(statement):
    """Move negation inward using De Morgan's laws."""
    if 'not ' in statement:
        statement = statement.replace('and', '∧').replace('or', '∨')
    return statement

def distribute_or(statement):
    """Distribute OR over AND in logical expressions to convert to CNF."""
    if 'or' in statement:
        parts = statement.split(' or ')
        if len(parts) > 1 and ' and ' in parts[0]:
            left_parts = parts[0].split(' and ')
            return f"({left_parts[0]} or {parts[1]}) and ({left_parts[1]} or {parts[1]})"
        elif len(parts) > 1 and ' and ' in parts[1]:
            right_parts = parts[1].split(' and ')
            return f"({parts[0]} or {right_parts[0]}) and ({parts[0]} or {right_parts[1]})"
    return statement

def to_cnf(statement):
    """Convert logical expression to CNF step by step."""
    statement = replace_biconditional(statement)
    statement = replace_implication(statement)
    statement = move_negation(statement)
    statement = distribute_or(statement)
    return statement

def assign_placeholders(statement):
    """Assign placeholders like P, Q, R to parts of the sentence."""
    parts = re.split(r'\bif\b|\bthen\b|\bif and only if\b|\band\b|\bor\b', statement)
    parts = [part.strip() for part in parts if part.strip()]  # Clean up and remove empty parts

    placeholders = {}
    for i, part in enumerate(parts):
        placeholders[chr(80 + i)] = part  # Assign P, Q, R, etc.

    # Replace actual parts in the statement with placeholders
    for placeholder, text in placeholders.items():
        statement = statement.replace(text, placeholder)
    
    return statement, placeholders

def display_placeholders(placeholders):
    """Display which part of the sentence corresponds to which placeholder."""
    print("\nMapping of parts to placeholders:")
    for placeholder, text in placeholders.items():
        print(f"{placeholder}: {text}")

def get_user_input():
    """Take full sentence input from the user."""
    print("Enter a logical expression in text form (e.g., 'If it is raining then it is wet outside').")
    return input("Enter the logical expression: ")

# Main function
def main():
    user_input = get_user_input()
    
    # Step 1: Assign placeholders to parts of the statement
    statement_with_placeholders, placeholders = assign_placeholders(user_input)
    
    # Step 2: Convert to CNF using placeholders
    cnf_statement = to_cnf(statement_with_placeholders)
    
    # Step 3: Display the mapping and the CNF form
    display_placeholders(placeholders)
    print("\nThe statement in Conjunctive Normal Form (CNF) is:")
    print(cnf_statement)

# Example execution
if __name__ == "__main__":
    main()
