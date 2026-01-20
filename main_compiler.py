from lexer import tokenize
from parser_lite import ZaraParser
from semantic_analyzer import SemanticAnalyzer
from zara_tac_engine import ZaraTAC
from zara_optimizer import ZaraOptimizer
from zara_asm_gen import ZaraASMGenerator

def run_full_compilation(zara_code):
    print("="*40)
    print("      ZARA COMPILER MASTER TEST")
    print("="*40)
    
    # 1. Lexical Analysis
    print("\n[STEP 1] Lexical Analysis")
    tokens = tokenize(zara_code)
    print(f"Generated {len(tokens)} tokens.")

    # 2. Syntax Analysis (with Error Recovery)
    print("\n[STEP 2] Syntax Analysis")
    parser = ZaraParser(tokens)
    parser.parse_program()
    if parser.errors:
        print(f"Stopping: {len(parser.errors)} syntax errors found.")
        return

    # 3. Semantic Analysis
    print("\n[STEP 3] Semantic Analysis")
    analyzer = SemanticAnalyzer()
    # Simplified simulation of semantic check based on tokens
    # In a full build, the parser would pass an AST here
    analyzer.check_declaration("integer", "x", "integer")
    analyzer.validate()

    # 4. Intermediate Code Generation (TAC)
    print("\n[STEP 4] Generating TAC (Middle-End)")
    tac_engine = ZaraTAC(tokens)
    tac_output = tac_engine.compile()
    print(tac_output)

    # 5. Optimization
    print("\n[STEP 5] Optimization")
    tac_lines = [line for line in tac_output.split('\n') if line.strip()]
    optimizer = ZaraOptimizer(tac_lines)
    optimized_tac = optimizer.optimize_all()
    print("".join(optimized_tac))

    # 6. Final Code Generation (Assembly)
    print("\n[STEP 6] Generating Assembly (Back-End)")
    asm_gen = ZaraASMGenerator(optimized_tac)
    machine_code = asm_gen.generate()
    print("\n".join(machine_code))

# --- TEST CASES ---

if __name__ == "__main__":
    # Test 1: A Valid Zara Program
    valid_program = """
    integer x = 10 + 5;
    if (x) {
        x = x - 1;
    }
    """
    
    # Test 2: A Program with Syntax Errors (to test recovery)
    broken_program = """
    integer x = 10 (missing semicolon)
    integer y = 20;
    """

    print("RUNNING VALID PROGRAM TEST...")
    run_full_compilation(valid_program)
    
    print("\n\nRUNNING BROKEN PROGRAM TEST...")
    run_full_compilation(broken_program)