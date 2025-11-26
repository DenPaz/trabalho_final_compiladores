from src.lexer import lexer
from src.parser import parser
from src.semantics import st

codigo_teste_sucesso = r"""
int main() {
    int a, b, resultado;
    a = 4;
    b = 6;
    if (a >= 10) {
        resultado = a - b;
    } else {
        resultado = a + b;
    }
}
"""

codigo_teste_erro = r"""
int main() {
    int x;
    x = 10;
    y = 20; // Erro aqui
}
"""


def rodar_teste(nome, codigo):
    print(f"\n>>> {nome} <<<")
    st.clear()
    result = parser.parse(codigo, lexer=lexer)
    if result:
        print(f"Status Sintático: {result}")
    else:
        print("Status Sintático: Falha")
    print("Estado Final da Tabela de Símbolos:", st.symbols)


if __name__ == "__main__":
    rodar_teste("TESTE 1:", codigo_teste_sucesso)
    rodar_teste("TESTE 2:", codigo_teste_erro)
