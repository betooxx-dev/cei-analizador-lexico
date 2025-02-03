"""Implementación del analizador léxico"""
import re
from tokens import TOKENS

class LexicalAnalyzer:
    def __init__(self):
        self.tokens = TOKENS

    def analyze(self, source_code):
        tokens = []
        position = 0
        line = 1
        column = 1
        
        while position < len(source_code):
            match = None
            
            for token_type, pattern in self.tokens:
                regex = re.compile(pattern, re.UNICODE)
                match = regex.match(source_code, position)
                
                if match:
                    lexeme = match.group(0)
                    if token_type != "ESPACIO":
                        tokens.append((token_type, lexeme, line, column))
                    
                    if '\n' in lexeme:
                        line += lexeme.count('\n')
                        column = len(lexeme) - lexeme.rindex('\n') if '\n' in lexeme else column + len(lexeme)
                    else:
                        column += len(lexeme)
                    
                    position = match.end()
                    break
            
            if not match:
                char_error = source_code[position]
                raise ValueError(f"Error léxico: carácter no reconocido '{char_error}' en línea {line}, columna {column}")
        
        return tokens