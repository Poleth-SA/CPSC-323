class PredictiveParser:
    def __init__(self, parsing_table):
        self.parsing_table = parsing_table

    def parse(self, input_string):
        stack = ['$', 'E']  # Initialize stack with $ and start symbol E
        input_string += '$'  # Append $ to the end of the input string
        input_index = 0  # Pointer to track the current input symbol

        while len(stack) > 0:
            top_symbol = stack[-1]
            current_input_symbol = input_string[input_index]

            if top_symbol == current_input_symbol == '$':  # Parsing completed
                print("Accepted")
                return

            if top_symbol == current_input_symbol:  # Match terminal symbol
                stack.pop()  # Pop from stack
                input_index += 1  # Move to next input symbol
            elif top_symbol in self.parsing_table and current_input_symbol in self.parsing_table[top_symbol]:
                # Replace non-terminal symbol with production rule from parsing table
                production = self.parsing_table[top_symbol][current_input_symbol]
                stack.pop()  # Pop non-terminal from stack
                if production != 'λ':  # If production is not lambda, push symbols onto stack
                    for symbol in production[::-1]:  # Push symbols in reverse order
                        stack.append(symbol)
            else:
                print("Rejected")
                return

            print("Stack:", stack)

# Predictive parsing table
parsing_table = {
    'E': {'i': 'TQ', '(': 'TQ'},
    'Q': {'+': '+TQ', '-': '-TQ', ')': 'λ', '$': 'λ'},
    'T': {'i': 'FR', '(': 'FR'},
    'R': {'*': '*FR', '/': '/FR', '+': 'λ', '-': 'λ', ')': 'λ', '$': 'λ'},
    'F': {'i': 'i', '(': '(E)'}
}

# Initialize predictive parser with parsing table
parser = PredictiveParser(parsing_table)

# Test cases
test_cases = ["(i+i)*i$", "i*(i-i)$", "i(i+i)$"]

# Parse each test case
for test_case in test_cases:
    print("\nParsing:", test_case)
    parser.parse(test_case)
