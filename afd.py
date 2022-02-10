
from typing import List, Tuple
import re
from models.error_entry import ErrorEntry
from models.token import Token
from models.inventario import Inventario
from models.product import Product

#Definimos las palabras reservadas y simbolos del lenguaje 
meses = [
                        'ENERO', 'FEBRERO', 'MARZO', 'ABRIL', 'MAYO',
                        'JUNIO', 'JULIO', 'AGOSTO', 'SEPTIEMBRE', 'OCTUBRE',
                        'NOVIEMBRE', 'DICIEMBRE'
                ]
numbers =['1','2','3','4','5','6','7','8','9','0']

# recibe un string, retorna una lista de productos, errores, y una lista un objeto de inventario
def automata(input: str) -> Tuple[Inventario,Tuple[Product], Tuple[ErrorEntry]]:
    #Regex Definition
    W = re.compile(r'[A-Z]')
    inventario = 0
    tempInventario: List = [] #Lista temporal previa a la creación del objeto
    col = 0
    temp: List = [] #Lista Temporal previa a la generación de Objetos
    #temp = [Nombre del Producto, Precio, Unidades]
    products: List[Product] = []  # Lista de objetos de Productos
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

            if W.search(char):
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

            elif char is '"':
                estado = 4
                index += 1
                col += 1
                lexema += char

            elif char is '@':
                estado = 5
                index += 1
                col += 1
                lexema += char

            elif char is "<":
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

            elif char=="\t":
                col += 1
                index += 1
            

        elif estado == 1:
            if W.search(char):
                estado = 1
                index += 1
                lexema += char
            elif char==":":
                estado = 2
                tempInventario.append(lexema)
                #tokens.append(Token('Mes', lexema, row, col))
                lexema = ''
                lexema += char
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
            elif char=="=":
                estado = 4
                index += 1


            else:
                estado = 0
                #tokens.append(Token('numero', lexema, row, col))
                lexema = ''

        elif estado == 4:
            estado = 4
            tempInventario.append(lexema)
            lexema = ''
            if char=="(":
                estado = 5
                index += 1
                lexema += char
                #tokens.append(Token('Simbolo', lexema, row, col))
                lexema = ''
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1

        elif estado == 5:
            if char=='[':
                estado = 6
                index += 1
                lexema += char
                #tokens.append(Token('Simbolo', lexema, row, col))
                lexema =''

            elif char==')':
                print("===============Carga Terminada=================")
                index += 1
                inventario = Inventario(tempInventario[0],tempInventario[1], products)


            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1

        elif estado == 6:
            if char=='"':
                estado = 7
                index += 1
                lexema += char
                #tokens.append(Token('Simbolo', lexema, row, col))
                lexema = ''
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1

        elif estado == 7:
            if char=='"':
                estado = 8
                index +=1
                #tokens.append(Token('Simbolo', char, row, col))
            else:
                estado = 7
                lexema += char
                index += 1



        elif estado == 8:

            #estado = 0
            temp.append(lexema)

            #tokens.append(Token('string', lexema, row, col))
            lexema = ''
            if char==",":
                estado = 9
                #tokens.append(Token('Simbolo', char, row, col))
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
            elif char==".":
                lexema += char
                #tokens.append(Token('Simbolo', char, row, col))
                estado = 11
                index += 1
            elif char==",":
                temp.append(lexema)
                lexema = ''
                estado = 12
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
            elif char==',':
                temp.append(lexema)
                lexema = ''
                estado = 12

            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1


        elif estado == 12:

            if char in numbers:
                estado = 12
                index += 1
                lexema += char
            elif char=="]":
                estado = 13
                temp.append(lexema)
                lexema = ''
                #tokens.append(Token('Simbolo', char, row, col))
                index += 1

            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1

        elif estado == 13:
            if char==";":
                estado = 5
                index += 1
                products.append(Product(temp[0],temp[1],temp[2]))
                temp.clear()
                #tokens.append(Token('Simbolo', char, row, col))
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1

        elif estado == 14:
            print("Lectura Finalizada")

    return inventario, tuple(products), tuple(errores)
