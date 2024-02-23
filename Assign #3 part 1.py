import re

# List of reserved words
reserved = ["while", "for", "switch", "do", "return"]

# Function to check if a token is a number
def is_number(token):
    return token.isdigit()

# Function to check if a token is an identifier
def is_identifier(token):
    return re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', token) is not None

# Function to check if a token is a reserved word
def is_reserved_word(token):
    return token.lower() in reserved

# Function to determine the type of each token and print the result
def determine_token_type(tokens):
    print("{:<15} {:<10} {:<15} {:<15}".format("Token", "Number", "Identifier", "Reserved Word"))
    for token in tokens:
        is_num = "yes" if is_number(token) else "no"
        is_id = "yes" if is_identifier(token) else "no"
        is_reserved = "yes" if is_reserved_word(token) else "no"
        print("{:<15} {:<10} {:<15} {:<15}".format(token, is_num, is_id, is_reserved))

# Main function
def main():
    tokens = ["K-mart", "23andMe", "456", "Tax", "2018", "While", "switch", "do_it", "_Fall_20", "_Jan_19"]
    determine_token_type(tokens)

if __name__ == "__main__":
    main()
