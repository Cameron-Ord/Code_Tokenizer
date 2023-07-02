import re

# Define token types using regular expressions

token_patterns = [
    
    ('NUMBER', r'\d+'),
    
    ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*'),
    
    ('OPERATOR', r'\+|-|\*|/|=|<|>'),
    
    ('PUNCTUATION', r'[(),;:.]'),
    
    ('STRING', r'`[^`]*`|\'[^\']*\'|\"[^\"]*\"'),
    
    ('WHITESPACE', r'\s+')
    
]


# Tokenize the input source code

def tokenize(code):
    tokens=[]
    position = 0
    
    while position < len(code):
        match = None
        
        for token_type, pattern in token_patterns:
            regex = re.compile(pattern)
            match = regex.match(code, position)
            
            if match:
                token_value = match.group(0)
                tokens.append((token_type, token_value))
                position = match.end(0)
                break
            
        if not match:
            raise Exception(f"Invalid token at position {position}")
        
    return tokens


def tokenize_user_input():
    user_input = input('enter code to tokenize: ')
    tokens = tokenize(user_input)
    
    numbers = []
    identifiers = []
    operators = []
    punctuation = []
    strings = []

    for token_type, token_value in tokens:
        if token_type == 'NUMBER':
            numbers.append((token_type, token_value))
        elif token_type == 'IDENTIFIER':
            identifiers.append((token_type, token_value))
        elif token_type == 'OPERATOR':
            operators.append((token_type, token_value))
        elif token_type == 'PUNCTUATION':
            punctuation.append((token_type, token_value))
        elif token_type == 'STRING':
            strings.append((token_type, token_value))

    # Print or process the token lists if needed
    print("Numbers:", numbers)
    print("Identifiers:", identifiers)
    print("Operators:", operators)
    print("Punctuation:", punctuation)
    print("Strings:", strings)
        
tokenize_user_input()