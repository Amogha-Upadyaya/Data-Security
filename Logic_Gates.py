# Define the logic gate functions

def Logic_AND(a, b):
    """Returns the result of the AND gate."""
    return 1 if a == 1 and b == 1 else 0

def Logic_NOT(a):
    """Returns the result of the NOT gate."""
    return 0 if a == 1 else 1

def Logic_OR(a, b):
    """Returns the result of the OR gate."""
    return 1 if a == 1 or b == 1 else 0

def Logic_XOR(a, b):
    """Returns the result of the XOR gate."""
    return 1 if a != b else 0

# Function to evaluate the expression
def evaluate_expression(tokens):
    result = None
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token == '~':
            i += 1
            operand = int(tokens[i])
            operand = Logic_NOT(operand)
            if result is None:
                result = operand
            else:
                # Use previous operator to combine with result
                if prev_operator == '&':
                    result = Logic_AND(result, operand)
                elif prev_operator == '|':
                    result = Logic_OR(result, operand)
                elif prev_operator == '^':
                    result = Logic_XOR(result, operand)
        elif token in ('&', '|', '^'):
            prev_operator = token
        else:
            operand = int(token)
            if result is None:
                result = operand
            else:
                # Use previous operator to combine with result
                if prev_operator == '&':
                    result = Logic_AND(result, operand)
                elif prev_operator == '|':
                    result = Logic_OR(result, operand)
                elif prev_operator == '^':
                    result = Logic_XOR(result, operand)
        i += 1
    
    return result

# Take a Logic Gates Expression as Input
logic_gates_expression = input("Enter a Logic Gates Expression (e.g., 1 & 0 | 1 ^ ~0): ")

# Split the Expression into a list of tokens (operands and operators)
tokens = logic_gates_expression.split()

# Evaluate the expression and print the result
result = evaluate_expression(tokens)
print("The result of the Logic Gates Expression is:", result)
