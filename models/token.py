class Token:
    def __init__(self, token: str, lexema: str, fila: int, col: int) -> None:
        self.token: str = token
        self.lexema: str = lexema
        self.fila: int = fila
        self.col: int = col