import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lexer import tokenize

def test_compiler_front_end():
    zara_code = """
    integer count = 0;
    float price = 19.99;
    string name = "Zara";
    stack data;
    
    do {
        count = count + 1;
    } while (count < 10);
    """
    
    print(f"{'TYPE':<12} | {'VALUE':<10}")
    print("-" * 25)
    
    tokens = tokenize(zara_code)
    for kind, value in tokens:
        print(f"{kind:<12} | {value:<10}")

    # Simple verification
    expected_keywords = ['integer', 'float', 'string', 'stack', 'do', 'while']
    found_keywords = [val for kind, val in tokens if kind == 'KEYWORD']
    
    print("\nVerification:")
    print(f"Total tokens found: {len(tokens)}")
    print(f"Keywords detected: {all(k in found_keywords for k in expected_keywords)}")

if __name__ == "__main__":
    test_compiler_front_end()