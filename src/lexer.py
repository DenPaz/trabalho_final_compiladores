import ply.lex as lex

reserved = {
    "if": "IF",
    "else": "ELSE",
    "for": "FOR",
    "while": "WHILE",
    "return": "RETURN",
    "int": "TYPE",
    "float": "TYPE",
    "double": "TYPE",
    "char": "TYPE",
    "void": "TYPE",
    "main": "MAIN",
}
tokens = [
    "EQUALS",
    "PLUS",
    "MINUS",
    "TIMES",
    "DIVIDE",
    "LPAREN",
    "RPAREN",
    "LBRACES",
    "RBRACES",
    "LT",
    "LE",
    "GT",
    "GE",
    "NE",
    "EQEQ",
    "COMMA",
    "SEMICOLON",
    "INTEGER",
    "FLOAT",
    "STRING",
    "CHAR",
    "ID",
] + list(set(reserved.values()))
t_ignore = " \t\r"


def t_COMMENT(t):
    r"(//[^\n]*|/\*([^*]|\*+[^*/])*\*+/)"
    pass


def t_PREPROCESSOR(t):
    r"\#[^\n]*"
    pass


t_EQUALS = r"="
t_PLUS = r"\+"
t_MINUS = r"-"
t_TIMES = r"\*"
t_DIVIDE = r"/"
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_LBRACES = r"\{"
t_RBRACES = r"\}"
t_LE = r"<="
t_GE = r">="
t_NE = r"!="
t_EQEQ = r"=="
t_LT = r"<"
t_GT = r">"
t_COMMA = r","
t_SEMICOLON = r";"


def t_FLOAT(t):
    r"((\d*\.\d+)([eE][\+\-]?\d+)?|([1-9]\d*[eE][\+\-]?\d+))"
    t.value = float(t.value)
    return t


def t_INTEGER(t):
    r"\d+"
    t.value = int(t.value)
    return t


def t_STRING(t):
    r"\".*?\""
    return t


def t_CHAR(t):
    r"'([^\\'\n]|\\[abfnrtv0'\"\\])'"
    return t


def t_ID(t):
    r"[A-Za-z_][A-Za-z0-9_]*"
    t.type = reserved.get(t.value, "ID")
    return t


def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)


def t_error(t):
    print(f"Caractere ilegal '{t.value[0]}' na linha {t.lexer.lineno}")
    t.lexer.skip(1)


lexer = lex.lex()
