import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lexer import tokenize
from zara_tac_engine import ZaraTAC

def test_compiler_output():
    zara_code = """
    x = a + b;
    if (x) {
        print(x);
    } else {
        reset(0);
    }
    """
    
    print("--- Zara Source ---")
    print(zara_code)
    
    tokens = tokenize(zara_code)
    compiler = ZaraTAC(tokens)
    tac_output = compiler.compile()
    
    print("\n--- Generated TAC ---")
    print(tac_output)

if __name__ == "__main__":
    test_compiler_output()