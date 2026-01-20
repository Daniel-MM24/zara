class SymbolTable:
    def __init__(self):
        # A list of dictionaries. The first is always global.
        self.scopes = [{}] 

    def enter_scope(self):
        self.scopes.append({})
        print(">>> Entered new scope")

    def exit_scope(self):
        if len(self.scopes) > 1:
            self.scopes.pop()
            print("<<< Exited scope")

    def add(self, name, data_type, kind="var"):
        # Check if already in the CURRENT scope
        if name in self.scopes[-1]:
            print(f"Error: {name} already declared in this scope.")
            return False
        self.scopes[-1][name] = {"type": data_type, "kind": kind}
        print(f"Added: {name} ({data_type})")
        return True

    def lookup(self, name):
        # Search from current scope upwards to global
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]
        print(f"Error: {name} not found.")
        return None

    def log(self):
        print("\n--- CURRENT SYMBOL TABLE LOG ---")
        for i, scope in enumerate(self.scopes):
            level = "Global" if i == 0 else f"Local {i}"
            print(f"{level}: {scope}")
        print("--------------------------------\n")