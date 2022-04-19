
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
            #RESULTADO
            if char == 'R':
                estado = 2
                index += 1
                col += 1
                lexema += char
            #TEMPORADA /  TOTAL / TABLA TEMPORADA / TOP
            elif char == 'T':
                estado = 10
                index += 1
                col += 1
                lexema += char
            #VS / VISITANTE
            elif char == 'V':
                estado = 18
                index += 1
                col += 1
                lexema += char

            #JORNADA
            elif char == 'J':
                estado = 19
                index += 1
                col += 1
                lexema += char

            elif char == '-':
                estado = 25
                index += 1
                col += 1
                lexema += char

            elif char.upper() == 'G':
                estado = 56
                index += 1
                col += 1
                lexema += char

            elif char.upper() == 'L':
                estado = 56
                index += 1
                col += 1
                lexema += char
            elif char.upper() == 'P':
                estado = 56
                index += 1
                col += 1
                lexema += char
            elif char.upper() == 'S':
                estado = 56
                index += 1
                col += 1
                lexema += char
            elif char.upper() == 'I':
                estado = 56
                index += 1
                col += 1
                lexema += char
            elif char.upper() == 'A':
                estado = 56
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


        #Estado 2
        elif estado == 2:
            if char == 'E':
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
            if char == 'S':
                estado = 4
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
            if char == 'U':
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
            if char == 'L':
                estado = 6
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
            if char == 'T':
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
            if char == 'A':
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
            if char == 'D':
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

        #Se Guarda la palabra RESULTADO
        elif estado == 9:
            if char == 'O':
                estado = 1
                lexema += char
                tokens.append(Token('RESULTADO', lexema, row, col))
                lexema = ''


            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''
        # formularIo
        elif estado == 10:
            if char == 'E':
                estado = 11
                index += 1
                col += 1
                lexema += char
            elif char == 'O':
                estado = 40
                index += 1
                col += 1
                lexema += char
            elif char == 'A':
                estado = 44
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
            if char == 'M':
                estado = 12
                index += 1
                col += 1
                lexema += char
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''

        #nOmbre
        elif estado == 12:
            if char == 'P':
                estado = 13
                index += 1
                lexema += char
                col += 1
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''

        elif estado == 13:
            if char == 'O':
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
            if char == 'R':
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
            if char == "A":
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
            if char == 'D':
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
            if char == 'A':
                estado = 1
                index += 1
                lexema += char
                tokens.append(Token('TEMPORADA', lexema, row, col))


            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''


        elif estado == 18:
            if char.upper() == 'S':
                estado = 1

                index += 1
                lexema += char
                tokens.append(Token('VERSUS', lexema, row, col))
                lexema = ''

            elif char== 'I':
                estado = 28

                index += 1
                lexema += char
                tokens.append(Token('VERSUS', lexema, row, col))
                lexema = ''

            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''

        elif estado == 19:
            if char == 'O':
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
            if char == 'R':
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
            if char == 'N':
                estado = 22
                index += 1
                lexema += char
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''

        elif estado == 22:
            if char == 'A':
                estado = 23
                index += 1
                lexema += char
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                estado = 1
                lexema = ''
                col += 1

        elif estado == 23:
            if char == 'D':
                estado = 24
                index += 1
                lexema += char

            else:
                errores.append(ErrorEntry(row, col, char))
                lexema = ''
                estado = 1
                index += 1
                col += 1
        elif estado == 24:
            if char == 'A':
                estado = 1
                index += 1
                lexema += char
                tokens.append(Token('JORNADA', lexema, row, col))
                lexema = ''

            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''

        elif estado == 25:
            if char.upper() == 'F':

                index += 1
                lexema += char
                tokens.append(Token('GUIONF', lexema, row, col))
                lexema = ''
                estado = 1
            elif char.upper() == 'J':
                estado = 26
                index += 1
                lexema += char
            elif char.upper() == 'N':
                estado = 1
                index += 1
                lexema += char
                tokens.append(Token('GUIONN', lexema, row, col))
                lexema = ''
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                estado = 1
                lexema = ''
                col += 1
        elif estado == 26:
            if char.upper() == 'I':
                estado = 1
                index += 1
                lexema += char
                tokens.append(Token('GUIONJI', lexema, row, col))
                lexema = ''
            elif char.upper() == 'F':
                estado = 1
                index += 1
                lexema += char
                tokens.append(Token('GUIONJF', lexema, row, col))
                lexema = ''

            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''




        elif estado == 27:
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
        elif estado == 28:
            if char.upper() == 'S':
                estado = 29
                index += 1
                lexema += char
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                lexema = ''
                estado = 1
                col += 1

        elif estado == 29:
            if char.upper() == 'I':
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
            if char.upper() == 'T':
                estado = 31
                index += 1
                lexema += char
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                lexema = ''
                estado = 1
                col += 1
        elif estado == 31:
            if char.upper() == 'A':
                estado = 32
                index += 1
                lexema += char
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                lexema = ''
                estado = 1
                col += 1

        elif estado == 32:
            if char.upper() == 'N':
                estado = 33
                index += 1
                lexema += char
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                lexema = ''
                estado = 1
                col += 1
        elif estado == 33:
            if char.upper() == 'T':
                estado = 34
                index += 1
                lexema += char
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                lexema = ''
                estado = 1
                col += 1
        elif estado == 34:
            if char.upper() == 'E':
                estado = 1
                index += 1
                lexema += char
                tokens.append(Token('VISITANTE', lexema, row, col))
                lexema = ''
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                lexema = ''
                estado = 1
                col += 1

        elif estado == 38:
            if char.upper() == 'O':
                lexema += char
                index += 1
                col += 1
                tokens.append(Token('PALABRA RESERVADA', lexema, row, col))
                lexema = ''
                estado = 1
        elif estado == 40:
            if char == 'T':
                lexema += char
                index += 1
                col += 1
                estado = 41
            elif char == 'P':
                lexema += char
                index += 1
                col += 1
                estado = 1
                tokens.append(Token('TOP', lexema, row, col))
                lexema = ''
                estado = 1

            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''
        elif estado == 41:
            if char.upper() == 'A':
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
            if char.upper() == 'L':
                lexema += char
                index += 1
                col += 1
                tokens.append(Token('TOTAL', lexema, row, col))
                lexema = ''
                estado = 1
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''
        elif estado == 44:
            if char.upper() == 'B':
                lexema += char
                index += 1
                col += 1
                estado = 45
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''
        elif estado == 45:
            if char.upper() == 'L':
                lexema += char
                index += 1
                col += 1
                estado = 46
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''
        elif estado == 46:
            if char.upper() == 'A':
                lexema += char
                index += 1
                col += 1
                estado = 47
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''
        elif estado == 47:
            if char.upper() == '\n':
                index += 1
                col = 0
                row += 1
            elif char.upper() == '\t':
                index += 1
                col += 1
            elif char == ' ':
                index += 1
                col += 1
            elif char == 'T':
                lexema += char
                index += 1
                col += 1
                estado = 48

            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''
        elif estado == 48:
            if char.upper() == 'E':
                lexema += char
                index += 1
                col += 1
                estado = 49
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''
        elif estado == 49:
            if char.upper() == 'M':
                lexema += char
                index += 1
                col += 1
                estado = 49
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''
        elif estado == 50:
            if char.upper() == 'P':
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
            if char.upper() == 'O':
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
            if char.upper() == 'R':
                lexema += char
                index += 1
                col += 1
                estado = 53
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''
        elif estado == 53:
            if char.upper() == 'A':
                lexema += char
                index += 1
                col += 1
                estado = 53
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''
        elif estado == 54:
            if char.upper() == 'D':
                lexema += char
                index += 1
                col += 1
                estado = 55
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''
        elif estado == 55:
            if char.upper() == 'A':
                lexema += char
                index += 1
                col += 1
                tokens.append(Token('TABLATEMPORADA', lexema, row, col))
                lexema = ''

            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''

        elif estado == 56:
            if char.upper() == 'A':
                lexema += char
                index += 1
                col += 1
                tokens.append(Token('TABLATEMPORADA', lexema, row, col))
                lexema = ''

            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''
        elif estado == 57:
            if char.upper() == 'O':
                lexema += char
                index += 1
                col += 1
                estado = 58
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''
        elif estado == 58:
            if char.upper() == 'L':
                lexema += char
                index += 1
                col += 1
                estado = 59
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''
        elif estado == 59:
            if char.upper() == 'E':
                lexema += char
                index += 1
                col += 1
                estado = 60
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''
        elif estado == 60:
            if char.upper() == 'S':
                lexema += char
                index += 1
                col += 1
                tokens.append(Token('GOLES', lexema, row, col))

            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''
        elif estado == 61:
            if char.upper() == 'O':
                lexema += char
                index += 1
                col += 1
                estado = 62

            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''
        elif estado == 62:
            if char.upper() == 'O':
                lexema += char
                index += 1
                col += 1
                estado = 63

            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''
        elif estado == 63:
            if char.upper() == 'C':
                lexema += char
                index += 1
                col += 1
                estado = 64

            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''
        elif estado == 64:
            if char.upper() == 'A':
                lexema += char
                index += 1
                col += 1
                estado = 65

            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''
        elif estado == 65:
            if char.upper() == 'L':
                lexema += char
                index += 1
                col += 1
                tokens.append(Token('COMA', lexema, row, col))
                lexema = ''
                estado = 1


            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''

        elif estado == 66:
            if char.upper() == 'A':
                lexema += char
                index += 1
                col += 1
                estado = 67


            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''
        elif estado == 67:
            if char.upper() == 'R':
                lexema += char
                index += 1
                col += 1
                estado = 68


            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''
        elif estado == 68:
            if char.upper() == 'T':
                lexema += char
                index += 1
                col += 1
                estado = 69


            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''
        elif estado == 69:
            if char.upper() == 'I':
                lexema += char
                index += 1
                col += 1
                estado = 70


            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''
        elif estado == 70:
            if char.upper() == 'D':
                lexema += char
                index += 1
                col += 1
                estado = 71


            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''
        elif estado == 71:
            if char.upper() == 'S':
                lexema += char
                index += 1
                tokens.append(Token('PARTIDOS', lexema, row, col))
                lexema = ''
                estado = 1



            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''
        elif estado == 72:
            if char.upper() == 'U':
                lexema += char
                index += 1
                estado = 73



            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''
        elif estado == 73:
            if char.upper() == 'P':
                lexema += char
                index += 1
                estado = 74



            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''
        elif estado == 74:
            if char.upper() == 'E':
                lexema += char
                index += 1
                estado = 75



            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''
        elif estado == 75:
            if char.upper() == 'R':
                lexema += char
                index += 1
                estado = 76



            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''
        elif estado == 76:
            if char.upper() == 'I':
                lexema += char
                index += 1
                estado = 77



            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''
        elif estado == 77:
            if char.upper() == 'O':
                lexema += char
                index += 1
                estado = 78



            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''
        elif estado == 78:
            if char.upper() == 'R':
                lexema += char
                index += 1
                tokens.append(Token('SUPERIOR', lexema, row, col))
                lexema = ''
                estado = 1




            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''

        elif estado == 79:
            if char.upper() == 'N':
                lexema += char
                index += 1

                estado = 80




            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''
        elif estado == 80:
            if char.upper() == 'F':
                lexema += char
                index += 1

                estado = 81

            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''
        elif estado == 81:
            if char.upper() == 'E':
                lexema += char
                index += 1

                estado = 82

            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''
        elif estado == 82:
            if char.upper() == 'R':
                lexema += char
                index += 1

                estado = 83

            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''
        elif estado == 83:
            if char.upper() == 'I':
                lexema += char
                index += 1

                estado = 84

            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''
        elif estado == 84:
            if char.upper() == 'O':
                lexema += char
                index += 1

                estado = 85

            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''
        elif estado == 85:
            if char.upper() == 'R':
                lexema += char
                index += 1
                tokens.append(Token('INFERIOR', lexema, row, col))
                lexema = ''
                estado = 1
                estado = 1

            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''
        elif estado == 86:
            if char.upper() == 'D':
                lexema += char
                index += 1

                estado = 87

            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''
        elif estado == 87:
            if char.upper() == 'I':
                lexema += char
                index += 1

                estado = 88

            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''
        elif estado == 88:
            if char.upper() == 'O':
                lexema += char
                index += 1

                estado = 89

            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''
        elif estado == 89:
            if char.upper() == 'S':
                lexema += char
                index += 1


                tokens.append(Token('ADIOS', lexema, row, col))
                lexema = ''
                estado = 1
                estado = 1

            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                estado = 1
                lexema = ''













    return tuple(tokens), tuple(errores)
