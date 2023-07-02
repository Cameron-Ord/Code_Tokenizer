# Parser class
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token_index = 0

    def parse(self):
        return self.expression()

    def expression(self):
        return self.term()

    def term(self):
        return self.factor()

    def factor(self):
        
        parsed_tokens = []

        while self.current_token_index < len(self.tokens):
            token = self.current_token()

            if token[0] == 'NUMBER':
                self.consume_token()
                print(token)
                parsed_tokens.append(token[1])
            elif token[0] == 'IDENTIFIER':
                self.consume_token()
                print(token)
                parsed_tokens.append(token[1])
            elif token[0] == 'OPERATOR':
                self.consume_token()
                print(token)
                parsed_tokens.append(token[1])
            elif token[0] == 'PUNCTUATION':
                self.consume_token()
                print(token)
                parsed_tokens.append(token[1])
            elif token[0] == 'STRING':
                self.consume_token()
                print(token)
                parsed_tokens.append(token[1])
            elif token[0] == 'WHITESPACE':
                self.consume_token()
                print(token)
                parsed_tokens.append(token[1])
            else:
                raise Exception('Invalid syntax')

        return parsed_tokens


    def current_token(self):
        return self.tokens[self.current_token_index]

    def consume_token(self):
        self.current_token_index += 1



def parse_inputs(tokens):

        parser = Parser(tokens)
        result = parser.parse()
        return result