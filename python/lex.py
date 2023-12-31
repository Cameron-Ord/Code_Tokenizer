import re, parse

# Define token types using regular expressions

token_patterns = [
    
    ('NUMBER', r'\d+'),
    
    ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*'),
    
    ('OPERATOR', r'\+|-|\*|/|=|<|>|\$|\?|!'),
    
    ('PUNCTUATION', r'[(){},;:.\[\]]'),
    
    ('STRING', r'`[^`]*`|\'[^\']*\'|\"[^\"]*\"'),
    
    ('WHITESPACE', r'\s+')
    
]

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
    
    result = parse.parse_inputs(tokens)
    print("Parsed result:", result)
    
tokenize_user_input()