import re

# Define token types using regular expressions

token_patterns = [
    
    ('NUMBER', r'\d+'),
    
    ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*'),
    
    ('OPERATOR', r'\+|-|\*|/|=|<|>'),
    
    ('PUNCTUATION', r'[(),;:]'),
    
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
    
    position = 0
    
    while True:
        
        tokens_len = []
            
        for token_type, token_value in tokens:
            if(token_type == 'NUMBER'):
                numbers.append((token_type, token_value))
                
                tokens_len.append(0)
            
            elif(token_type == 'IDENTIFIER'):
                identifiers.append((token_type,token_value))
                
                tokens_len.append(0)
            elif(token_type == 'OPERATORS'):
                operators.append((token_type, token_value))
                
                tokens_len.append(0)
            elif(token_type == 'PUNCTUATION'):
                punctuation.append((token_type, token_value))
                
                tokens_len.append(0)
            elif(token_type == 'STRINGS'):
                strings.append((token_type, token_value))
           
                tokens_len.append(0)
                
        position = len(tokens_len)   
        
        if(position == len(tokens_len)):
            break 

        
                        
            
        
        
tokenize_user_input()