import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lexer import tokenize
from parser_lite import ZaraParser

def test_syntax(title, code):
    print(f"\nTEST: {title}")
    try:
        tokens = tokenize(code)
        parser = ZaraParser(tokens)
        parser.parse_program()
    except SyntaxError as e:
        print(f"SYNTAX ERROR: {e}")

# 1. Valid Program
valid_zara = """
integer x = 10;
do {
    x = 5;
} while (x);
"""

# 2. Invalid Program (Missing semicolon)
invalid_zara = """
integer y = 20
"""

if __name__ == "__main__":
    test_syntax("Valid Code", valid_zara)
    test_syntax("Missing Semicolon", invalid_zara)