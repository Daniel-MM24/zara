import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from zara_asm_gen import ZaraASMGenerator

def test_asm_generation():
    # Simulated TAC input from previous weeks
    optimized_tac = [
        "t1 = a + 5",
        "if_not t1 goto L1",
        "d = ALLOC Drone",
        "L1:",
        "x = t1"
    ]
    
    print("--- Source TAC ---")
    for line in optimized_tac: print(f"  {line}")
    
    gen = ZaraASMGenerator(optimized_tac)
    gen.generate()
    
    print("\n--- Generated Z-ASM (Machine-like Code) ---")
    gen.log_asm()

if __name__ == "__main__":
    test_asm_generation()