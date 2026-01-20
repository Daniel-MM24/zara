class ZaraASMGenerator:
    def __init__(self, tac_lines):
        self.tac = tac_lines
        self.asm = []
        # Simple register allocator: maps TAC temps to machine registers
        self.reg_map = {} 
        self.next_reg = 1

    def get_reg(self, var):
        if var not in self.reg_map:
            self.reg_map[var] = f"R{self.next_reg}"
            self.next_reg += 1
        return self.reg_map[var]

    def generate(self):
        self.asm.append("; --- Z-ASM START ---")
        for line in self.tac:
            line = line.strip()
            if not line or line.endswith(':'): # Handle Labels
                self.asm.append(line)
                continue

            # Arithmetic: t1 = a + b
            if "=" in line and any(op in line for op in "+-*/"):
                parts = line.split() # ['t1', '=', 'a', '+', 'b']
                dest, src1, op, src2 = self.get_reg(parts[0]), parts[2], parts[3], parts[4]
                
                op_map = {"+": "ADD", "-": "SUB", "*": "MUL", "/": "DIV"}
                self.asm.append(f"LOAD {dest}, {src1}")
                self.asm.append(f"{op_map[op]} {dest}, {src2}")

            # Assignment: x = t1
            elif "=" in line:
                dest, src = line.split(" = ")
                self.asm.append(f"STORE {dest}, {self.get_reg(src)}")

            # Control Flow: if_not t1 goto L1
            elif "if_not" in line:
                parts = line.split()
                self.asm.append(f"CMP {self.get_reg(parts[1])}, 0")
                self.asm.append(f"JZ {parts[4]}") # Jump if Zero

            # Object Creation: x = ALLOC Drone
            elif "ALLOC" in line:
                dest, _, class_name = line.split()
                self.asm.append(f"MALLOC {class_name}_SIZE")
                self.asm.append(f"STORE {dest}, R_ALLOC") # R_ALLOC is return reg

        self.asm.append("; --- Z-ASM END ---")
        return self.asm

    def log_asm(self):
        print("\n".join(self.asm))