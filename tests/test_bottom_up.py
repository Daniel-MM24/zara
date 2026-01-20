from lexer import tokenize
from bottom_up_parser import ShiftReduceParser

def test_bottom_up():
    print("--- Testing Bottom-Up Parser ---")
    
    # Test 1: Simple Assignment
    zara_code = "x = 10;"
    print(f"\nParsing: {zara_code}")
    ShiftReduceParser(tokenize(zara_code)).parse()

    # Test 2: Multi-statement code
    zara_code_2 = "integer x = 10; x = 5;"
    print(f"\nParsing: {zara_code_2}")
    ShiftReduceParser(tokenize(zara_code_2)).parse()

if __name__ == "__main__":
    test_bottom_up()