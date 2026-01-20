import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lexer import tokenize
from ir_generator import ZaraIRGenerator

def test_ir_generation():
    zara_code = """
    x = 10 + 5;
    do {
        count = count + 1;
    } while (count);
    """
    
    print("--- Zara Source Code ---")
    print(zara_code)
    
    tokens = tokenize(zara_code)
    gen = ZaraIRGenerator(tokens)
    intermediate_code = gen.generate()
    
    print("\n--- Generated Intermediate Representation (3AC) ---")
    print(intermediate_code)

if __name__ == "__main__":
    test_ir_generation()