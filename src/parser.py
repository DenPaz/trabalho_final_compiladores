import ply.yacc as yacc

from src.lexer import tokens  # noqa: F401
from src.semantics import st, types_compatible

precedence = (
    ("right", "EQUALS"),
    ("left", "EQEQ", "NE", "LT", "LE", "GT", "GE"),
    ("left", "PLUS", "MINUS"),
    ("left", "TIMES", "DIVIDE"),
)

start = "program"


def p_program(p):
    """program : declaration_list"""
    p[0] = "ProgramOK"


def p_declaration_list(p):
    """declaration_list : declaration_list declaration
    | empty"""
    pass


def p_declaration(p):
    """declaration : var_declaration
    | func_declaration"""
    pass


def p_var_declaration(p):
    """var_declaration : TYPE var_list SEMICOLON"""
    var_type = p[1]
    variables = p[2]
    # Usa a função do módulo semantics
    for var_name in variables:
        st.add(var_name, var_type, p.lineno(1))


def p_var_list(p):
    """var_list : var_init
    | var_list COMMA var_init"""
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]


def p_var_init(p):
    """var_init : ID
    | ID EQUALS expression"""
    p[0] = p[1]


def p_func_declaration(p):
    """func_declaration : TYPE MAIN LPAREN params RPAREN block
    | TYPE ID LPAREN params RPAREN block"""
    pass


def p_params(p):
    """params : TYPE ID
    | empty"""
    pass


def p_block(p):
    """block : LBRACES statement_list RBRACES"""
    pass


def p_statement_list(p):
    """statement_list : statement_list statement
    | empty"""
    pass


def p_statement(p):
    """statement : expression_statement
    | var_declaration
    | if_statement
    | while_statement
    | for_statement
    | return_statement
    | block"""
    pass


def p_expression_statement(p):
    """expression_statement : expression SEMICOLON
    | SEMICOLON"""
    pass


def p_return_statement(p):
    """return_statement : RETURN expression SEMICOLON"""
    pass


def p_if_statement(p):
    """if_statement : IF LPAREN expression RPAREN statement
    | IF LPAREN expression RPAREN statement ELSE statement"""
    pass


def p_while_statement(p):
    """while_statement : WHILE LPAREN expression RPAREN statement"""
    pass


def p_for_statement(p):
    """for_statement : FOR LPAREN for_init SEMICOLON expression_part SEMICOLON expression_part RPAREN statement"""
    pass


def p_for_init(p):
    """for_init : var_declaration_no_semi
    | expression
    | empty"""
    pass


def p_var_declaration_no_semi(p):
    """var_declaration_no_semi : TYPE var_list"""
    var_type = p[1]
    variables = p[2]
    for var_name in variables:
        st.add(var_name, var_type, p.lineno(1))


def p_expression_part(p):
    """expression_part : expression
    | empty"""
    pass


def p_expression_assign(p):
    """expression : ID EQUALS expression"""
    lhs_name = p[1]
    if st.check(lhs_name, p.lineno(1)):
        lhs_type = st.symbols[lhs_name]
        rhs_type = p[3][0] if p[3] is not None else None

        if rhs_type is not None and not types_compatible(lhs_type, rhs_type):
            print(
                f"ERRO SEMÂNTICO (linha {p.lineno(1)}): "
                f"atribuição incompatível: '{lhs_name}' é '{lhs_type}' "
                f"e expressão é '{rhs_type}'."
            )
    p[0] = (st.symbols.get(lhs_name, None),)


def p_expression_binop(p):
    """expression : expression PLUS expression
    | expression MINUS expression
    | expression TIMES expression
    | expression DIVIDE expression
    | expression LT expression
    | expression LE expression
    | expression GT expression
    | expression GE expression
    | expression EQEQ expression
    | expression NE expression"""
    left_type = p[1][0] if p[1] is not None else None
    right_type = p[3][0] if p[3] is not None else None
    op = p.slice[2].type

    result_type = None

    if left_type is not None and right_type is not None:
        if op in ("PLUS", "MINUS", "TIMES", "DIVIDE"):
            numeric = {"int", "float", "double"}
            if left_type in numeric and right_type in numeric:
                if "double" in (left_type, right_type):
                    result_type = "double"
                elif "float" in (left_type, right_type):
                    result_type = "float"
                else:
                    result_type = "int"
            else:
                print(
                    f"ERRO SEMÂNTICO (linha {p.lineno(2)}): "
                    f"operação aritmética entre tipos incompatíveis "
                    f"'{left_type}' e '{right_type}'."
                )

        elif op in ("LT", "LE", "GT", "GE", "EQEQ", "NE"):
            if (
                left_type == right_type
                or types_compatible(left_type, right_type)
                or types_compatible(right_type, left_type)
            ):
                result_type = "int"
            else:
                print(
                    f"ERRO SEMÂNTICO (linha {p.lineno(2)}): "
                    f"comparação entre tipos incompatíveis "
                    f"'{left_type}' e '{right_type}'."
                )

    p[0] = (result_type,)


def p_expression_group(p):
    """expression : LPAREN expression RPAREN"""
    p[0] = p[2]


def p_expression_id(p):
    """expression : ID"""
    # Checagem semântica
    if st.check(p[1], p.lineno(1)):
        var_type = st.symbols[p[1]]
        p[0] = (var_type,)
    else:
        p[0] = (None,)


def p_expression_literals(p):
    """expression : INTEGER
    | FLOAT
    | STRING
    | CHAR"""
    tok_type = p.slice[1].type
    if tok_type == "INTEGER":
        p[0] = ("int",)
    elif tok_type == "FLOAT":
        p[0] = ("float",)
    elif tok_type == "STRING":
        p[0] = ("string",)
    elif tok_type == "CHAR":
        p[0] = ("char",)


def p_empty(p):
    """empty :"""
    pass


def p_error(p):
    if p:
        print(f"Erro de sintaxe em '{p.value}' na linha {p.lineno}")
    else:
        print("Erro de sintaxe: Fim inesperado do arquivo")


parser = yacc.yacc()
