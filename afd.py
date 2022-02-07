from curses.ascii import isalpha
from typing import List, Tuple
from models.error_entry import ErrorEntry
from models.token import Token


#Definimos las palabras reservadas y simbolos del lenguaje 
meses = [
                        'ENERO', 'FEBRERO', 'MARZO', 'ABRIL', 'MAYO',
                        'JUNIO', 'JULIO', 'AGOSTO', 'SEPTIEMBRE', 'OCTUBRE',
                        'NOVIEMBRE', 'DICIEMBRE'
                ]
numbers =['1','2','3','4','5','6','7','8','9','0']

# recibe un string, retorna lista de tokens y errores
def automata(input: str) -> Tuple[Tuple[Token], Tuple[ErrorEntry]]:

    tokens: List[Token] = []  # Lista tokens
    errores: List[ErrorEntry] = []  # Lista errores
    estado: int = 0  # Estado inicial
    lexema: str = ''  # lexema actual
    index: int = 0  # indice
    row: int = 1  # fila

    while index < len(input):
        char = input[index]

        # Estado inicial
        if estado == 0:
            #Lista de transiciones

            if isalpha(char):
                estado = 1
                index += 1
                lexema += char

            elif char is ":":
                estado = 1
                index += 1
                lexema += char

            elif char in numbers:
                estado = 3
                index += 1
                col += 1
                lexema += char

            elif char == '"':
                estado = 4
                index += 1
                col += 1
                lexema += char

            elif char == '@':
                estado = 5
                index += 1
                col += 1
                lexema += char

            elif char == "<":
                estado = 6
                index += 1
                col += 1
                lexema += char
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
            
            # Caracteres ignorados
            
            if char is "\n":
                row += 1
                col = 0
                index += 1

            elif char is "\t":
                col += 1
                index += 1
            

        elif estado == 1:
            if isalpha(char):
                estado = 1
                index += 1
                lexema += char
            elif char == ":":
                estado = 2
                tokens.append(Token('Mes', lexema, row, col))
                lexema = ''
                lexema += char
                tokens.append(Token('Simbolo', lexema, row, col))
                lexema = ''
                index+= 1

        elif estado == 2:
            if char in numbers:
                estado = 3
                index += 1
                lexema += char
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1

        elif estado == 3:
            if char in numbers:
                estado = 3
                lexema += char
                index += 1
            elif char is "=":
                estado = 4
                index += 1


            else:
                estado = 0
                tokens.append(Token('numero', lexema, row, col))
                lexema = ''

        elif estado == 4:
            tokens.append(Token('numero', lexema, row, col))
            lexema += ''
            if char == "(":
                estado = 5
                index += 1
                lexema += char
                tokens.append(Token('Simbolo', lexema, row, col))
                lexema = ''
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1

        elif estado == 5:
            if char == '[':
                estado = 6
                index += 1
                lexema += char
                tokens.append(Token('Simbolo', lexema, row, col))
                lexema =''

            elif char == ')':
                print("================================")
                print('==NO HAY DATOS EN LA ENTRADA====')
                print('================================')
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1

        elif estado == 6:
            if char == '"':
                estado = 7
                index += 1
                lexema += char
                tokens.append(Token('Simbolo', lexema, row, col))
                lexema = ''
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1

        elif estado == 7:
            if char == '"':
                estado = 8
                tokens.append(Token('Simbolo', char, row, col))
            else:
                estado = 7
                index += 1
                lexema += char
                index += 1


        elif estado == 8:

            estado = 0
            tokens.append(Token('string', lexema, row, col))
            lexema = ''
            if char == ",":
                estado = 9
                tokens.append(Token('Simbolo', char, row, col))
                index += 1

        elif estado == 9:
            if char in numbers:
                estado = 10
                index += 1
                col += 1
                lexema += char
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1

        elif estado == 10:
            if char in numbers:
                estado = 10
                index += 1
                col += 1
                lexema += char
            elif char == ".":
                tokens.append(Token('Simbolo', char, row, col))
                estado == 11
                index += 1
            elif char ==",":
                tokens.append(Token('Simbolo', char, row, col))
                estado == 12
                index += 1
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1

        elif estado == 11:
            if char in numbers:
                estado = 11
                lexema += char
                index += 1
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1


        elif estado == 12:
            if char in numbers:
                estado = 12
                index += 1
                lexema += char
            elif char == "]":
                estado = 13
                tokens.append(Token('Simbolo', char, row, col))
                index += 1

            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1

        elif estado == 13:
            if char == ";":
                estado = 5
                index += 1
                tokens.append(Token('Simbolo', char, row, col))
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1

        elif estado == 14:
            print("Lectura Finalizada")

    return tuple(tokens), tuple(errores)
