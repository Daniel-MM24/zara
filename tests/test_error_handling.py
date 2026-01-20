import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lexer import tokenize
from error_handler import ZaraErrorReporter

reporter = ZaraErrorReporter()

def test_error_handling():
    # Error 1: Lexical (invalid character @)
    # Error 2: Syntax (missing closing parenthesis)
    # Error 3: Semantic (assigning string to integer)
    zara_bad_code = """
    integer x = 10 @; 
    if (x > 5 { 
        x = "wrong";
    }
    """
    
    print("--- Starting Robust Error Test ---")
    
    # 1. Lexical Check
    tokens = tokenize(zara_bad_code) 
    # (Inside lexer, if MISMATCH is found, call reporter.report)

    # 2. Syntax Check with Recovery
    # (Parser will fail at 'if (x > 5 {', skip to '}', and find the next stmt)
    
    # 3. Semantic Check
    # (Analyzer will find the string-to-int mismatch)
    
    reporter.summary()

if __name__ == "__main__":
    test_error_handling()