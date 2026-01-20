class ZaraParser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.errors = [] # To store found errors

    def current_token(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else (None, None)

    def match(self, kind, value=None):
        k, v = self.current_token()
        if k == kind and (value is None or v == value):
            self.pos += 1
            return v
        return None

    def expect(self, kind, value=None):
        res = self.match(kind, value)
        if not res:
            k, v = self.current_token()
            msg = f"Expected {kind} '{value if value else ''}', found {k} '{v}'"
            raise SyntaxError(msg)
        return res

    # --- Error Recovery Logic ---

    def synchronize(self):
        """Panic Mode: Skip tokens until the start of the next statement."""
        print(">>> Recovering...")
        while self.pos < len(self.tokens):
            kind, value = self.current_token()
            # Stop if we hit a semicolon (end of current statement)
            if value == ';':
                self.pos += 1 
                return
            # Stop if we hit a keyword that starts a NEW block/statement
            if value in ['if', 'do', 'while', 'integer', 'float', 'string', '{']:
                return
            self.pos += 1

    # --- Grammar Rules ---

    def parse_statement(self):
        """Dispatches to specific rules; wrapped for error recovery."""
        try:
            kind, value = self.current_token()
            if value in ['integer', 'float', 'string', 'stack', 'array']:
                self.parse_declaration()
            elif value == 'if':
                self.parse_if()
            elif value == 'do':
                self.parse_dowhile()
            elif value == '{':
                self.parse_block()
            elif kind == 'IDENTIFIER':
                self.parse_assignment()
            elif kind == 'EOF':
                return
            else:
                raise SyntaxError(f"Unexpected token '{value}'")
        except SyntaxError as e:
            self.errors.append(str(e))
            print(f"❌ SYNTAX ERROR: {e}")
            self.synchronize()

    def parse_declaration(self):
        v_type = self.expect('KEYWORD')
        v_name = self.expect('IDENTIFIER')
        if self.match('OPERATOR', '='):
            self.parse_expression()
        self.expect('DELIMITER', ';')
        print(f"Parsed Declaration: {v_type} {v_name}")

    def parse_if(self):
        self.expect('KEYWORD', 'if')
        self.expect('DELIMITER', '(')
        self.parse_expression()
        self.expect('DELIMITER', ')')
        self.parse_block()
        if self.match('KEYWORD', 'else'):
            self.parse_block()
        print("Parsed If-Else structure")

    def parse_dowhile(self):
        self.expect('KEYWORD', 'do')
        self.parse_block()
        self.expect('KEYWORD', 'while')
        self.expect('DELIMITER', '(')
        self.parse_expression()
        self.expect('DELIMITER', ')')
        self.expect('DELIMITER', ';')
        print("Parsed Do-While loop")

    def parse_block(self):
        self.expect('DELIMITER', '{')
        while self.current_token()[1] != '}' and self.pos < len(self.tokens):
            self.parse_statement()
        self.expect('DELIMITER', '}')

    def parse_assignment(self):
        name = self.expect('IDENTIFIER')
        self.expect('OPERATOR', '=')
        self.parse_expression()
        self.expect('DELIMITER', ';')
        print(f"Parsed Assignment to {name}")

    def parse_expression(self):
        """Refined: Consumes full expressions like '10 + 5' or 'x - 1'"""
        # 1. Consume the first part (ID or Number)
        kind, value = self.current_token()
        if kind not in ['IDENTIFIER', 'INTEGER', 'FLOAT', 'STRING']:
            raise SyntaxError(f"Invalid expression at '{value}'")
        self.pos += 1
        
        # 2. Check if there is an operator following it (the 'lookahead')
        kind, value = self.current_token()
        if kind == 'OPERATOR' and value in ['+', '-', '*', '/']:
            self.pos += 1 # Consume '+' or '-'
            # 3. Recursively parse the right side
            self.parse_expression() 
        
        return value

    def parse_program(self):
        print("--- Starting Parse ---")
        while self.pos < len(self.tokens):
            self.parse_statement()
        if not self.errors:
            print("--- Parsing Complete: Success ---")
        else:
            print(f"--- Finished with {len(self.errors)} errors ---")