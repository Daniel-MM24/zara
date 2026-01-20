Zara Compiler: A Modular End-to-End Compiler

The Zara Compiler is a fully functional, modular compiler designed to translate the high-level Zara programming language into low-level assembly code (Z-ASM). This project demonstrates the complete pipeline of compiler construction, from raw text processing to machine code generation and optimization.
 Features

    Panic Mode Error Recovery: The parser can detect syntax errors, skip to the next statement, and continue compiling to find multiple errors in one pass.

    Intermediate Representation (TAC): Generates Three-Address Code, a platform-independent middle-level language.

    Object-Oriented Support: Handles class hierarchies, inheritance, and method name-mangling.

    Optimization: Implements constant folding and dead code elimination to improve execution speed.

    Targeted Assembly: Produces Z-ASM instructions ready for a virtual machine or register-based architecture.

🏗 Architecture

The compiler is built in six distinct stages, ensuring a separation of concerns and easy maintainability:
1. Lexical Analysis (lexer.py)

Scans the source code and breaks it down into meaningful tokens (Keywords, Identifiers, Operators).
2. Syntax Analysis (parser_lite.py)

Validates the token stream against the Zara context-free grammar. It uses a recursive-descent approach and features robust error recovery.
3. Semantic Analysis (semantic_analyzer.py)

Checks for "logic" errors, such as type mismatches (e.g., adding a string to an integer) and scope rules (using undeclared variables).
4. Intermediate Code Generation (zara_tac_engine.py)

Translates high-level constructs like if-else and do-while loops into a flat, 3-address format (x=y op z).
5. Code Optimization (zara_optimizer.py)

Refines the TAC by performing Constant Folding (calculating math at compile-time) and Dead Code Elimination.
6. Code Generation (zara_asm_gen.py)

Maps the optimized TAC to specific Z-ASM instructions, allocating registers (R1, R2, etc.) and managing memory labels.
🛠 Installation & Usage
Prerequisites

    Python 3.x

Running the Compiler

To compile a Zara program and see the output of all stages, run the master orchestrator:
Bash

python3 main_compiler.py

Running Tests

Individual components can be tested using the provided test scripts:
Bash

python3 test_parser.py
python3 test_asm_gen.py

📝 Example Transformation

Zara Source:
Code snippet

integer x = 10 + 5;
if (x) {
    print(x);
}

Generated Z-ASM:
Code snippet

LOAD R1, 15        ; Optimized from 10 + 5
STORE x, R1
CMP R1, 0
JZ L1              ; Jump to L1 if x is 0
PARAM R1
CALL print, 1
L1:

 Key Learning Outcomes

    Implementing LL(1) parsing techniques.

    Designing Symbol Tables for nested scopes.

    Translating control flow into conditional jumps and labels.

    The importance of Intermediate Representations for porting compilers to different hardware.

 License

This project is open-source and available under the MIT License.