# Analisador Sintático e Semântico (Subset de C)

Este projeto é uma implementação parcial de um compilador, focada nas fases de:

- Análise léxica (já implementada previamente)
- Análise sintática
- Análise semântica

O código reconhece um subconjunto simples de C, com suporte a:

- Declaração de variáveis
- Atribuições
- Operações aritméticas simples
- Estruturas condicionais (`if` / `if-else`, inclusive aninhadas)
- Laços de repetição (`while` e `for`)
- Função `main` como ponto de entrada

A análise semântica inclui pelo menos três ações:

1. Verificação de **redeclaração de variáveis**
2. Verificação de **uso de variável não declarada**
3. Verificação de **compatibilidade de tipos em atribuições** e em expressões aritméticas/relacionais

---

## Estrutura do Projeto

```text
.
├── main.py
└── src
    ├── lexer.py      # Analisador léxico (PLY)
    ├── parser.py     # Analisador sintático + ações semânticas
    └── semantics.py  # Tabela de símbolos e utilitários de tipos
```

## Pré-requisitos

- [Python](https://www.python.org/downloads/) (versão 3.10 ou superior)
- [uv](https://pypi.org/project/uv/)
- [PLY](https://www.dabeaz.com/ply/)

## Como executar

1. Clone o repositório:

   ```bash
   git clone https://github.com/DenPaz/trabalho_final_compiladores.git
   cd trabalho_final_compiladores
   ```

2. Instale as dependências:

   ```bash
   uv sync
   ```

3. Execute o analisador chamando o `main.py`:
   ```bash
   uv run main.py
   ```
