class ErrorEntry:
    def __init__(self, linea: int, col: int, char: str) -> None:
        self.linea: int = linea
        self.col: int = col
        self.char: str = char