import re

class ZaraOptimizer:
    def __init__(self, tac_lines):
        self.tac = tac_lines

    def constant_folding(self):
        """Pass 1: Pre-calculate math like 'x = 2 + 3' into 'x = 5'"""
        optimized = []
        for line in self.tac:
            # Pattern: var = num op num
            match = re.match(r"(\w+) = (\d+) ([\+\-\*\/]) (\d+)", line)
            if match:
                var, n1, op, n2 = match.groups()
                result = eval(f"{n1}{op}{n2}")
                optimized.append(f"{var} = {result}\n")
            else:
                optimized.append(line)
        return optimized

    def dead_code_elimination(self):
        """Pass 2: Remove variables that are assigned but never used"""
        used_vars = set()
        # Find all variables used on the RIGHT side of assignments or in conditions
        for line in self.tac:
            parts = line.split('=')
            if len(parts) > 1:
                used_vars.update(re.findall(r"\b[a-zA-Z_]\w*\b", parts[1]))
            if "if" in line or "goto" in line:
                used_vars.update(re.findall(r"\b[a-zA-Z_]\w*\b", line))

        optimized = []
        for line in self.tac:
            match = re.match(r"(\w+) =", line)
            if match:
                var = match.group(1)
                if var in used_vars or var.startswith('t'): # Keep temps for now
                    optimized.append(line)
            else:
                optimized.append(line)
        return optimized

    def loop_invariant_motion(self):
        """Pass 3: Move code that doesn't change inside a loop to the outside"""
        # Simplification: Identify code between a label and a jump
        # If an assignment doesn't depend on loop variables, it's 'invariant'
        print("Note: Loop Invariant Motion requires a Control Flow Graph (CFG).")
        return self.tac # Returning original for this basic project version

    def optimize_all(self):
        code = self.constant_folding()
        code = self.dead_code_elimination()
        return code
    
   