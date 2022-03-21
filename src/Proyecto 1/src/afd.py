
from typing import List, Tuple
from models.error_entry import ErrorEntry
from models.token import Token


# recibe un string, retorna lista de tokens y errores
def automata(input: str) -> Tuple[Tuple[Token], Tuple[ErrorEntry]]:

      # Agregar char al final
    tokens: List[Token] = []  # Lista tokens
    errores: List[ErrorEntry] = []  # Lista errores
    estado: int = 1  # Estado inicial
    lexema: str = ''  # lexema actual
    index: int = 0  # indice

    row: int = 1  # fila
    col: int = 0  # columna
    print("El Archivo>>")
    print(str(len(input)))
    while index < len(input):
        char = input[index]

        # Estado inicial
        if estado == 1:
            #Lista de transiciones
            if char == 'f' or char == 'F':
                estado = 2
                index += 1
                col += 1
                lexema += char

            elif char.upper() == 'N':
                estado = 12
                index += 1
                col += 1
                lexema += char

            elif char.upper() == 'V':
                estado = 13
                index += 1
                col += 1
                lexema += char

            elif char.upper() == 'T':
                estado = 28
                index += 1
                col += 1
                lexema += char

            elif char.upper() == 'E':
                estado = 23
                index += 1
                col += 1
                lexema += char

            elif char.upper() == 'I':
                estado = 50
                index += 1
                col += 1
                lexema += char

            elif char == "~":
                estado = 31
                index += 1
                col += 1
                lexema += char

            elif char == "[":
                col += 1
                estado = 37
                index += 1
                lexema += char
            elif char == "]":
                estado = 37
                index += 1
                col += 1
                lexema += char


            elif char == ":":
                estado = 37
                index += 1
                col += 1
                lexema += char

            elif char == "<":
                estado = 37
                index += 1
                col += 1
                lexema += char
            elif char == '>':
                estado = 37
                index += 1
                col += 1
                lexema += char
            elif char == '"':
                estado = 34
                index += 1
                col += 1

            elif char == ',':
                estado = 1
                index += 1
                col += 1
                lexema += char
                tokens.append(Token('COMA', lexema, row, col))
                lexema = ''





            # Caracteres ignorados
            elif char == '\n':
                row += 1
                col = 0
                index += 1

            elif char == '\t':
                col += 1
                index += 1
            elif char == ' ':
                col += 1
                index += 1
            #Si ninguno de los caracteres anteriores hace presencia, es un error lexico
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''


        #fOrmulario
        elif estado == 2:
            if char == 'o' or char == 'O':
                estado = 3
                index += 1
                col += 1
                lexema += char
            else:
                errores.append(ErrorEntry(row, col, lexema))
                index += 1
                col += 1
                estado = 1
                lexema = ''
        #foRmulario
        elif estado == 3:
            if char == 'r' or char == 'R':
                estado = 4
                index += 1
                col += 1
                lexema += char
            elif char.upper() == 'N':
                estado = 35
                index += 1
                col += 1
                lexema += char
            else:
                errores.append(ErrorEntry(row, col, lexema))
                index += 1
                col += 1
                estado = 1
                lexema = ''
        #forMulario
        elif estado == 4:
            if char == 'm' or char == 'M':
                estado = 5
                index += 1
                col += 1
                lexema += char

            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                lexema = ''
                estado = 1
        #formUlario
        elif estado == 5:
            if char == 'u' or char == 'U':
                estado = 6
                index += 1
                col += 1
                lexema += char
            #Tambien puede ser formA
            elif char.upper() == 'A':
                estado = 11
                index += 1
                col += 1
                lexema += char
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''
        #formuLario
        elif estado == 6:
            if char == 'l' or char == 'L':
                estado = 7
                index += 1
                col += 1
                lexema += char
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''
        #formulArio
        elif estado == 7:
            if char == 'a' or char == 'A':
                estado = 8
                index += 1
                col += 1
                lexema += char
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''
        #formulaRio
        elif estado == 8:
            if char == 'r' or char == 'R':
                estado = 9
                index += 1
                col += 1
                lexema += char
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''
        #formularI
        elif estado == 9:
            if char == 'i' or char == 'I':
                estado = 10
                index += 1
                col += 1
                lexema += char
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''
        # formularIo
        elif estado == 10:
            if char == 'o' or char == 'O':
                estado = 11
                index += 1
                col += 1
                lexema += char
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''

        elif estado == 11:
            #Sera estado de aceptacion para palabras reservadas
            estado = 1
            tokens.append(Token('PALABRA RESERVADA', lexema, row, col))
            lexema = ''
        #nOmbre
        elif estado == 12:
            if char.upper() == 'O':
                estado = 18
                index += 1
                lexema += char
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''

        elif estado == 13:
            if char.upper() == 'A':
                estado = 14
                index += 1
                lexema += char
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                lexema = ''
                col += 1
                estado = 1

        elif estado == 14:
            if char.upper() == 'L':
                estado = 15
                index += 1
                lexema += char
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''

        elif estado == 15:
            if char.upper() == "O":
                estado = 16
                index += 1
                lexema += char
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                lexema = ''
                estado = 1
                col += 1

        elif estado == 16:
            if char.upper() == 'R':
                estado = 17
                index += 1
                lexema += char
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''

        elif estado == 17:
            if char.upper() == 'E':
                estado = 22
                index += 1
                lexema += char
            elif char == ' ':
                estado = 11
                index += 1
                col += 1
            elif char == ':':
                estado = 1
                index += 1
                col += 1
                tokens.append(Token('PALABRA RESERVADA', lexema, row, col))
                tokens.append(Token('SIMBOLO', char, row, col))
                lexema = ''
            elif char == '\n':
                index += 1
                row += 1
            elif char == '\t':
                index += 1
                row += 1
            else:
                #Debe ser un error
                estado = 1
                index += 1
                errores.append(ErrorEntry(row, col, char))
                estado = 1
                lexema = ''


        elif estado == 18:
            if char.upper() == 'M':
                estado = 19
                index += 1
                lexema += char
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''

        elif estado == 19:
            if char.upper() == 'B':
                estado = 20
                index += 1
                lexema += char
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''
        elif estado == 20:
            if char.upper() == 'R':
                estado = 21
                index += 1
                lexema += char
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                estado = 1
                lexema = ''
                col += 1

        elif estado == 21:
            if char.upper() == 'E':
                estado = 11
                index += 1
                lexema += char
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''

        elif estado == 22:
            if char.upper() == 'S':
                estado = 11
                index += 1
                lexema += char
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                estado = 1
                lexema = ''
                col += 1

        elif estado == 23:
            if char.upper() == 'V':
                estado = 24
                index += 1
                lexema += char
            elif char.upper() == 'N':
                estado = 40
                index += 1
                lexema += char
            else:
                errores.append(ErrorEntry(row, col, char))
                lexema = ''
                estado = 1
                index += 1
                col += 1
        elif estado == 24:
            if char.upper() == 'E':
                estado = 26
                index += 1
                lexema += char
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''
        elif estado == 26:
            if char.upper() == 'N':
                estado = 27
                index += 1
                lexema += char
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                estado = 1
                lexema = ''
                col += 1
        elif estado == 27:
            if char.upper() == 'T':
                estado = 27
                index += 1
                lexema += char
            elif char.upper() == 'O':
                index += 1
                lexema += char
            elif char.upper() == ':':
                estado = 1
                index += 1
                col += 1
                tokens.append(Token('PALABRA RESERVADA', lexema, row, col))
                tokens.append(Token('SIMBOLO', char, row, col))
                lexema = ''
            elif char == '\n':
                index += 1
                row += 1
            elif char == '\t':
                index += 1
            elif char == ' ':
                index += 1
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''




        elif estado == 28:
            if char.upper() == 'I':
                estado = 29
                index += 1
                lexema += char
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''
        elif estado == 29:
            if char.upper() == 'P':
                estado = 30
                index += 1
                lexema += char
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                lexema = ''
                estado = 1
                col += 1
        elif estado == 30:
            if char.upper() == 'O':
                estado = 11
                index += 1
                lexema += char
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''
        elif estado == 31:
            if char == '>':
                estado = 32
                index += 1
                lexema += char
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                estado = 1
                lexema = ''
                col += 1
        elif estado == 32:
            if char == '>':
                estado = 33
                index += 1
                lexema+=char
                tokens.append(Token('SIMBOLO', lexema, row, col))
                lexema = ''
                estado = 1
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                estado = 1
                lexema = ''
                col += 1
        elif estado == 37:
            estado = 1
            tokens.append(Token('SIMBOLO', lexema, row, col))
            lexema = ''
        elif estado == 33:
            if char != '>':
                lexema += char
                index += 1
                col += 1
            else:
                estado = 1
                tokens.append(Token('SIMBOLO', char, row, col))
                tokens.append(Token('EVENTO', lexema, row, col))
                lexema = ''
        elif estado == 34:
            if char == '"':

                estado = 1
                tokens.append(Token('STRING', lexema, row, col))
                lexema = ''
                index += 1
            else:
                lexema += char
                index += 1
                col += 1

        elif estado == 35:
            if char.upper() == 'D':
                lexema += char
                index += 1
                col += 1
                estado = 38
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''

        elif estado == 38:
            if char.upper() == 'O':
                lexema += char
                index += 1
                col += 1
                tokens.append(Token('PALABRA RESERVADA', lexema, row, col))
                lexema = ''
                estado = 1
        elif estado == 40:
            if char.upper() == 'T':
                lexema += char
                index += 1
                col += 1
                estado = 41
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''
        elif estado == 41:
            if char.upper() == 'R':
                lexema += char
                index += 1
                col += 1
                estado = 42
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''
        elif estado == 42:
            if char.upper() == 'A':
                lexema += char
                index += 1
                col += 1
                estado = 43
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''
        elif estado == 43:
            if char.upper() == 'D':
                lexema += char
                index += 1
                col += 1
                estado = 44
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''
        elif estado == 44:
            if char.upper() == 'A':
                lexema += char
                index += 1
                col += 1
                estado = 11
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''
        elif estado == 50:
            if char.upper() == 'N':
                lexema += char
                index += 1
                col += 1
                estado = 51
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''
        elif estado == 51:
            if char.upper() == 'F':
                lexema += char
                index += 1
                col += 1
                estado = 52
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''
        elif estado == 52:
            if char.upper() == 'O':
                lexema += char
                index += 1
                col += 1
                estado = 52
            elif char == '>':
                index += 1
                estado = 11
            elif char == ' ':
                index += 1
            elif char == '\n':
                index += 1
                row += 1
            elif char == '\t':
                index += 1

            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''










    return tuple(tokens), tuple(errores)
