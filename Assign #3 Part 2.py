class CFGParser:
    def __init__(self):
        self.current_index = 0
        self.input_string = ""
    
    def parse(self, input_string):
        self.input_string = input_string + "$"  # $ represents end of input
        self.current_index = 0
        if self.S():
            if self.input_string[self.current_index] == "$":
                return True
        return False
    
    def S(self):
        if self.current_index < len(self.input_string) and self.input_string[self.current_index] == 'a':
            self.current_index += 1
            return self.S()
        elif self.current_index < len(self.input_string) and self.input_string[self.current_index] == 'b':
            self.current_index += 1
            if self.B():
                return True
        elif self.current_index < len(self.input_string) and self.input_string[self.current_index] == 'c':
            self.current_index += 1
            if self.C():
                return True
        return False
    
    def B(self):
        if self.current_index < len(self.input_string) and self.input_string[self.current_index] == 'b':
            self.current_index += 1
            return self.B()
        elif self.current_index < len(self.input_string) and self.input_string[self.current_index] == 'a':
            self.current_index += 1
            if self.C():
                return True
        elif self.current_index < len(self.input_string) and (self.input_string[self.current_index] == '$' or self.input_string[self.current_index] == '\n'):
            return True
        return False
    
    def C(self):
        if self.current_index < len(self.input_string) and self.input_string[self.current_index] == 'a':
            self.current_index += 1
            return self.S()
        elif self.current_index < len(self.input_string) and (self.input_string[self.current_index] == '$' or self.input_string[self.current_index] == '\n'):
            return True
        return False

# Main function to test the parser
def main():
    parser = CFGParser()
    while True:
        test_string = input("Enter a test string (type 'q' to quit): ")
        if test_string.lower() == 'q':
            break
        if parser.parse(test_string):
            print(f"String '{test_string}' is accepted by the grammar.")
        else:
            print(f"String '{test_string}' is rejected by the grammar.")

if __name__ == "__main__":
    main()
