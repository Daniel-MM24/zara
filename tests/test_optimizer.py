import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from zara_optimizer import ZaraOptimizer

def test_optimization():
    # Zara Source:
    # integer x = 10 + 20;  <-- Constant Folding
    # integer y = 50;       <-- Dead Code (if y is never used)
    # print(x);

    unoptimized_tac = [
        "x = 10 + 20\n",
        "y = 50\n",
        "param x\n",
        "call print, 1\n"
    ]

    print("--- Original TAC ---")
    print("".join(unoptimized_tac))

    optimizer = ZaraOptimizer(unoptimized_tac)
    optimized_tac = optimizer.optimize_all()

    print("--- Optimized TAC ---")
    print("".join(optimized_tac))

if __name__ == "__main__":
    test_optimization()