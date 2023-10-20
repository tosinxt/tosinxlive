import ply.lex as lex

tokens = (
    'IDENTIFIER',
    'NUMBER',
    'PLUS',
    'MINUS',
    'MULTI',
    'DIVIDE',
    'EQUALS',
)
    
t_ignore = '\t'

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_PLUS(t):
    r'\+'
    return t

def t_MINUS(t):
    r'-'
    return t

def t_MULTI(t):
    r'\*'
    return t

def t_EQUALS(t):
    r'='
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    

def t_error(t):
    print("illegal character '%s'" %t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()


data = "x = 10 - 5 * 2"
lexer.input(data)

for token in lexer:
    print(token)