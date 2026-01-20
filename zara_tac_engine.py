class ZaraTAC:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.temp_count = 0
        self.label_count = 0

    def get_temp(self):
        self.temp_count += 1
        return f"t{self.temp_count}"

    def get_label(self):
        self.label_count += 1
        return f"L{self.label_count}"

    def peek(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else (None, None)

    def consume(self, expected_val=None):
        kind, val = self.peek()
        if expected_val and val != expected_val:
            return None
        self.pos += 1
        return val

    # --- TAC Rules ---

    def gen_expression(self):
        """Translates math to TAC. Returns (result_var, code)"""
        left = self.consume() # Simple ID or Literal
        if self.peek()[1] in ['+', '-', '*', '/']:
            op = self.consume()
            right = self.consume()
            temp = self.get_temp()
            return temp, f"{temp} = {left} {op} {right}\n"
        return left, ""

    def gen_method_call(self):
        """Translates method calls: func(arg1, arg2)"""
        func_name = self.consume()
        self.consume("(")
        arg, arg_code = self.gen_expression()
        self.consume(")")
        self.consume(";")
        # TAC for method calls typically uses 'param' and 'call'
        return f"{arg_code}param {arg}\ncall {func_name}, 1\n"

    def gen_if_else(self):
        """Translates If-Else to TAC using labels and gotos"""
        self.consume("if")
        self.consume("(")
        cond, cond_code = self.gen_expression()
        self.consume(")")
        
        label_else = self.get_label()
        label_end = self.get_label()
        
        tac = f"{cond_code}if_not {cond} goto {label_else}\n"
        self.consume("{")
        tac += self.gen_statement() # Body of IF
        self.consume("}")
        tac += f"goto {label_end}\n"
        
        tac += f"{label_else}:\n"
        if self.consume("else"):
            self.consume("{")
            tac += self.gen_statement() # Body of ELSE
            self.consume("}")
        tac += f"{label_end}:\n"
        return tac

    def gen_statement(self):
        _, val = self.peek()
        if val == "if": return self.gen_if_else()
        if self.pos + 1 < len(self.tokens) and self.tokens[self.pos+1][1] == "(":
            return self.gen_method_call()
        # Fallback to assignment
        var_name = self.consume()
        self.consume("=")
        res, code = self.gen_expression()
        self.consume(";")
        return f"{code}{var_name} = {res}\n"

    def compile(self):
        full_tac = ""
        while self.pos < len(self.tokens):
            full_tac += self.gen_statement()
        return full_tac