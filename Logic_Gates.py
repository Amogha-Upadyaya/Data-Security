# Aim: Take a Logic Gates Expression as user input. Display the result obtain upon performing the logic gate operations in the expression inputted.
# Logic Gates: AND (&), OR(|), NOT(~), XOR(^)
# Constraint: Do not implement/use pre-defined symbols or functions to derive the result.

# Take a Logic Gates Expression as Input
logic_gates_expression = input("Enter a Logic Gates Expression: ")
# Split the Expression into a list of individual Logic Gates
logic_gates_expression_list = logic_gates_expression.split()
# Take the first Logic Gate as the output
output = logic_gates_expression_list[0]
# Iterate through the remaining Logic Gates
for i in range(1, len(logic_gates_expression_list)):
    # If the Logic Gate is NOT
    if logic_gates_expression_list[i] == "~":
        # Take the next Logic Gate as the output
        output = "~" + output
    # If the Logic Gate is AND
    elif logic_gates_expression_list[i] == "&":
        # Take the next Logic Gate as the output
        output = "&" + output
    # If the Logic Gate is OR
    elif logic_gates_expression_list[i] == "|":
        # Take the next Logic Gate as the output
        output = "|" + output
    # If the Logic Gate is XOR
    elif logic_gates_expression_list[i] == "^":
        # Take the next Logic Gate as the output
        output = "^" + output
# Print the result
print("The result of the Logic Gates Expression is: ", output)
