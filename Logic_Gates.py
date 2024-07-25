# Aim: Take a Logic Gates Expression as user input. Based on the logica gates provided as input, perform the logic gate operations and display the result.
# Logic Gates: AND (&), OR(|), NOT(~), XOR(^)
# Constraint: Do not implement/use pre-defined symbols or functions to derive the result.

# Define the logic gate functions

def AND(a, b):
    """Returns the result of the AND gate."""
    return 1 if a == 1 and b == 1 else 0

def NOT(a):
    """Returns the result of the NOT gate."""
    return 0 if a == 1 else 1

def OR(a, b):
    """Returns the result of the OR gate."""
    return 1 if a == 1 or b == 1 else 0

def XOR(a, b):
    """Returns the result of the XOR gate."""
    return 1 if a != b else 0

# Function to evaluate the expression
def evaluate_expression(expression):
    i = 0
    length = len(expression)
    result = None
    
    while i < length:
        token = expression[i]
        
        if token == '~':
            i += 1
            operand = int(expression[i])
            result = NOT(operand)
        elif token in ('&', '|', '^'):
            operator = token
            i += 1
            operand = int(expression[i])
            if operator == '&':
                result = AND(result, operand)
            elif operator == '|':
                result = OR(result, operand)
            elif operator == '^':
                result = XOR(result, operand)
        else:
            if result is None:
                result = int(token)
            else:
                result = int(token)
        i += 1
    
    return result

# Take a Logic Gates Expression as Input
logic_gates_expression = input("Enter a Logic Gates Expression (e.g., 1 & 0 | 1 ^ ~0): ")

# Split the Expression into a list of tokens (operands and operators)
tokens = logic_gates_expression.split()

# Evaluate the expression and print the result
result = evaluate_expression(tokens)
print("The result of the Logic Gates Expression is:", result)
