class ShiftReduceParser:
    def __init__(self, tokens):
        self.tokens = tokens + [('EOF', '$')]  # Append end-of-file
        self.stack = []
        self.pos = 0

        # Define Reduction Rules: (Pattern on Stack) -> (Reduced Non-Terminal)
        self.rules = [
            (['KEYWORD', 'IDENTIFIER', 'OPERATOR', 'INTEGER', 'DELIMITER'], 'STMT'), # Declaration
            (['IDENTIFIER', 'OPERATOR', 'INTEGER', 'DELIMITER'], 'STMT'),            # Assignment
            (['KEYWORD', 'DELIMITER', 'STMT', 'KEYWORD', 'DELIMITER', 'IDENTIFIER', 'DELIMITER', 'DELIMITER'], 'STMT'), # Do-While
            (['STMT', 'STMT'], 'STMT_LIST'),
            (['DELIMITER', 'STMT_LIST', 'DELIMITER'], 'BLOCK')
        ]

    def shift(self):
        kind, value = self.tokens[self.pos]
        self.stack.append(kind)
        self.pos += 1
        print(f"Shift: {value:<10} | Stack: {self.stack}")

    def reduce(self):
        for pattern, result in self.rules:
            # Check if the end of the stack matches a rule pattern
            if self.stack[-len(pattern):] == pattern:
                for _ in range(len(pattern)):
                    self.stack.pop()
                self.stack.append(result)
                print(f"Reduce: {' '.join(pattern)} -> {result}")
                return True # Reduced successfully
        return False

    def parse(self):
        print(f"{'ACTION':<15} | {'STACK CONTENT'}")
        print("-" * 40)
        
        while self.pos < len(self.tokens):
            # Resolve Conflict: If we can reduce, we try to reduce before shifting
            # This is a basic "Reduce-Preferred" strategy
            if not self.reduce():
                if self.tokens[self.pos][0] == 'EOF':
                    break
                self.shift()
        
        # Final check for acceptance
        if 'STMT' in self.stack or 'STMT_LIST' in self.stack:
            print("\n✅ Parsing Successful: Program reduced to root.")
        else:
            print("\n❌ Parsing Failed: Stack contains unresolved symbols.")

# Example Usage
if __name__ == "__main__":
    from lexer import tokenize
    code = "integer x = 10; x = 5;"
    parser = ShiftReduceParser(tokenize(code))
    parser.parse()