class ZaraIRGenerator:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.temp_count = 0
        self.label_count = 0

    def new_temp(self):
        self.temp_count += 1
        return f"t{self.temp_count}"

    def new_label(self):
        self.label_count += 1
        return f"L{self.label_count}"

    def current_token(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else (None, None)

    def match(self, kind, value=None):
        k, v = self.current_token()
        if k == kind and (value is None or v == value):
            self.pos += 1
            return v
        return None

    # --- Translation Rules (Synthesized Attributes) ---

    def translate_expression(self):
        """Rule: E -> term { + term } - Returns temporary variable name and IR"""
        # For simplicity, handles: id + id or literal
        kind, val = self.current_token()
        self.pos += 1
        
        if self.match('OPERATOR', '+'):
            right_val = self.match('INTEGER') or self.match('IDENTIFIER')
            temp = self.new_temp()
            return temp, f"{temp} = {val} + {right_val}\n"
        
        return val, "" # No operation needed

    def translate_assignment(self):
        """Rule: S -> id = E; - Returns generated IR string"""
        var_name = self.match('IDENTIFIER')
        self.match('OPERATOR', '=')
        expr_result, expr_ir = self.translate_expression()
        self.match('DELIMITER', ';')
        
        return f"{expr_ir}{var_name} = {expr_result}\n"

    def translate_do_while(self):
        """Rule: S -> do { S } while ( E ); - Returns generated IR string"""
        start_label = self.new_label()
        self.match('KEYWORD', 'do')
        self.match('DELIMITER', '{')
        body_ir = self.translate_assignment() # Simplified: one statement body
        self.match('DELIMITER', '}')
        
        self.match('KEYWORD', 'while')
        self.match('DELIMITER', '(')
        cond_var, cond_ir = self.translate_expression()
        self.match('DELIMITER', ')')
        self.match('DELIMITER', ';')

        ir = f"{start_label}:\n"
        ir += f"{body_ir}"
        ir += f"{cond_ir}"
        ir += f"if {cond_var} goto {start_label}\n"
        return ir

    def generate(self):
        full_ir = ""
        while self.pos < len(self.tokens):
            kind, val = self.current_token()
            if val == 'do':
                full_ir += self.translate_do_while()
            elif kind == 'IDENTIFIER':
                full_ir += self.translate_assignment()
            else: self.pos += 1
        return full_ir