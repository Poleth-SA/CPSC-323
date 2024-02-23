#-------------------------------------------------------------------------------------------------------------
#//                   Group names: Jessica Sandres and Poleth Salmeron Acosta
#//                  Assignment     : CPSC 323, No.11
#//                  Due date         : 02/01/2024 
#// Purpose: this program reads an expression in postfix form, evaluates the expression
#// and displays its value
#//-----------------------------------------------------------------------------------------------------------------

class Stack:
    # Initialize an empty list to store stack items
    def __init__(self):
        self.items = []

    # Check if the stack is empty
    def is_empty(self):
        return self.items == []

    # Add an item to the top of the stack
    def push(self, item):
        self.items.append(item)

    # Remove and return the item from the top of the stack
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    # Return the item at the top of the stack without removing it
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

# Evaluate a postfix expression given values for variables
def evaluate_postfix(expression, values):
    stack = Stack()  # Create a stack to store operands
    for char in expression:
        if char.isalpha():  # If the character is a letter
            stack.push(values[char])  # Push the corresponding value onto the stack
        elif char in "+-*/":  # If the character is an operator
            operand2 = stack.pop()  # Pop the top operand from the stack
            operand1 = stack.pop()  # Pop the second top operand from the stack
            result = evaluate(char, operand1, operand2)  # Evaluate the expression
            stack.push(result)  # Push the result back onto the stack
    return stack.pop()  # Return the final result

# Evaluate an arithmetic expression given an operator and two operands
def evaluate(operator, operand1, operand2):
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        return operand1 / operand2

# Main function to get user input and perform evaluations
def main():
    values_str = input("Enter the values of a, b, c and d: ")
    values = {letter: int(value) for letter, value in zip('abcd', values_str.split())}
    
    while True:
        expression = input("Enter a postfix expression with $ at the end: ")
        if expression.endswith('$'):  # Ensure the expression ends with a dollar sign
            result = evaluate_postfix(expression[:-1], values)  # Evaluate the expression
            print("Value =", result)  # Print the result
        else:
            print("Invalid postfix expression format.")  # Notify user of invalid expression format
        continue_input = input("CONTINUE(y/n)? ").strip().lower()  # Ask user if they want to continue
        if continue_input != 'y':
            break

# Entry point of the script
if __name__ == "__main__":
    main()
