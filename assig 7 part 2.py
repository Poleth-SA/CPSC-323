class PredictiveParser:
    def __init__(self, parsing_table):
        self.parsing_table = parsing_table

    def parse(self, input_string):
        stack = ['$', 'S']  # Initialize stack with $ and start symbol S
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
                    for symbol in reversed(production):  # Push symbols in reverse order
                        stack.append(symbol)
            else:
                print("Rejected")
                return

            print("Stack:", stack)

# Constructed predictive parsing table based on the augmented grammar
parsing_table = {
    'S': {'a': 'aW'},
    'W': {'=': '=E'},
    'E': {'a': 'TE\'', '(': 'TE\''},
    'E\'': {'+': '+TE\'', '-': '-TE\'', ')': 'λ', '$': 'λ'},
    'T': {'a': 'FT\'', '(': 'FT\''},
    'T\'': {'*': '*FT\'', '/': '/FT\'', '+': 'λ', '-': 'λ', ')': 'λ', '$': 'λ'},
    'F': {'a': 'a', '(': '(E)'}
}

# Initialize predictive parser with constructed parsing table
parser = PredictiveParser(parsing_table)

# Test cases
test_cases = ["a=(a+a)*a$", "a=a*(a-a)$", "a=(a+a)a$"]

# Parse each test case
for i, test_case in enumerate(test_cases, 1):
    print(f"\nParsing (ii): {test_case}")
    parser.parse(test_case)
