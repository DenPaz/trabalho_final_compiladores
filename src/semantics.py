class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def add(self, name, type, lineno):
        if name in self.symbols:
            print(f"ERRO SEMÂNTICO (linha {lineno}): Variável '{name}' já declarada.")
            return False
        self.symbols[name] = type
        return True

    def check(self, name, lineno):
        if name not in self.symbols:
            print(f"ERRO SEMÂNTICO (linha {lineno}): Variável '{name}' não declarada.")
            return False
        return True

    def clear(self):
        self.symbols = {}


def types_compatible(dest, src):
    if dest == src:
        return True
    if dest in ("float", "double") and src == "int":
        return True
    return False


st = SymbolTable()
