class ZaraOOPCompiler:
    def __init__(self, oop_table):
        self.table = oop_table
        self.tac = []

    def compile_method_call(self, obj_name, obj_class, method_name, args):
        # 1. Resolve which class the method belongs to (Inheritance check)
        resolved_class = self.table.resolve_method(obj_class, method_name)
        
        if not resolved_class:
            print(f"Semantic Error: {method_name} not found in {obj_class}")
            return

        # 2. Generate TAC: Pass 'this' as the first parameter
        self.tac.append(f"param {obj_name}  # Pass 'this'")
        for arg in args:
            self.tac.append(f"param {arg}")
        
        # 3. Name Mangled Call
        mangled_name = f"{resolved_class}_{method_name}"
        self.tac.append(f"call {mangled_name}, {len(args) + 1}")

    def compile_constructor(self, obj_name, class_name):
        self.tac.append(f"{obj_name} = ALLOC {class_name}")
        self.tac.append(f"call {class_name}_init, 1")

    def log_ir(self):
        print("\n--- Generated OO Intermediate Code ---")
        for line in self.tac: print(line)