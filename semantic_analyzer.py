from symbol_table import SymbolTable

class SemanticAnalyzer:
    def __init__(self):
        self.st = SymbolTable()
        self.errors = []

    def report(self, message):
        self.errors.append(f"Semantic Error: {message}")

    def check_declaration(self, var_type, var_name, value_type=None):
        # Rule: Scope check (Already declared?)
        if not self.st.add(var_name, var_type):
            self.report(f"Variable '{var_name}' is already defined.")
        
        # Rule: Type Consistency
        if value_type and var_type != value_type:
            self.report(f"Type Mismatch: Cannot assign {value_type} to {var_type} '{var_name}'.")

    def check_assignment(self, var_name, value_type):
        symbol = self.st.lookup(var_name)
        if not symbol:
            self.report(f"Variable '{var_name}' used before declaration.")
        elif symbol['type'] != value_type:
            self.report(f"Type Mismatch: '{var_name}' is {symbol['type']}, cannot assign {value_type}.")

    def check_collection_usage(self, var_name, action):
        """Checks consistency for stack and array."""
        symbol = self.st.lookup(var_name)
        if not symbol:
            self.report(f"Collection '{var_name}' not found.")
            return

        # Rule: Stack actions vs Array actions
        if symbol['type'] == 'stack' and action not in ['push', 'pop']:
            self.report(f"Invalid action '{action}' for stack '{var_name}'.")
        if symbol['type'] == 'array' and action not in ['index', 'length']:
            self.report(f"Invalid action '{action}' for array '{var_name}'.")

    def validate(self):
        if not self.errors:
            print("✅ Semantic Analysis Passed: Code is type-safe and consistent.")
        else:
            for err in self.errors:
                print(f"❌ {err}")

# Example Simulation
if __name__ == "__main__":
    analyzer = SemanticAnalyzer()
    
    print("--- Running Semantic Analysis ---")
    # integer x = 10; (Correct)
    analyzer.check_declaration("integer", "x", "integer")
    
    # float y = "hello"; (Incorrect: Type Mismatch)
    analyzer.check_declaration("float", "y", "string")
    
    # stack s; s.index(1); (Incorrect: stack doesn't support indexing)
    analyzer.check_declaration("stack", "s")
    analyzer.check_collection_usage("s", "index")
    
    # z = 10; (Incorrect: Undeclared)
    analyzer.check_assignment("z", "integer")
    
    analyzer.validate()