import re

# Define token patterns using (Name, Regular Expression)
# Order matters: keywords must come before identifiers
TOKEN_PATTERNS = [
    ('KEYWORD',    r'\b(if|else|then|do|while|for|to|returns|integer|float|string|array|stack)\b'),
    ('FLOAT',      r'\d+\.\d+'),
    ('INTEGER',    r'\d+'),
    ('STRING',     r'"[^"]*"'),
    ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*'),
    ('OPERATOR',   r'==|!=|<=|>=|[+\-*/><=]'),
    ('DELIMITER',  r'[();,{}]'),
    ('SKIP',       r'[ \t\n]+'),  # Whitespace
    ('MISMATCH',   r'.'),         # Any other character
]

def tokenize(code):
    tokens = []
    # Combine patterns into one master regex
    master_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_PATTERNS)
    
    for match in re.finditer(master_regex, code):
        kind = match.lastgroup
        value = match.group()
        
        if kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            print(f"Lexical Error: Unexpected character '{value}'")
        else:
            tokens.append((kind, value))
    return tokens

# Quick test within the module
if __name__ == "__main__":
    sample_zara = 'if (x > 10.5) { integer y = 20; }'
    for t in tokenize(sample_zara):
        print(t)