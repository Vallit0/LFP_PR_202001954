
from typing import List, Tuple
import re
from models.error_entry import ErrorEntry
from models.instruction import Instruction
from models.inventario import Inventario
from models.product import Product

#Definimos las palabras reservadas y simbolos del lenguaje 
keywords = [
                        'NOMBRE', 'GRAFICA', 'TITULOX', 'TITULOY', 'TITULO'
                ]
numbers =['1','2','3','4','5','6','7','8','9','0']

# recibe un string, retorna una lista de productos, errores, y una lista un objeto de inventario
def instructionsAnalyzer(input: str) -> Tuple[Tuple[Instruction], Tuple[ErrorEntry]]:


    #Regex Definition
    W = re.compile(r'[A-Z]')
    col = 0
    temp: List = [] #Lista Temporal previa a la generación de Objetos
    #temp = [Nombre del Producto, Precio, Unidades]
    instructions: List[Instruction] = []  # Lista de objetos de Productos
    errores: List[ErrorEntry] = []  # Lista errores
    estado: int = 0  # Estado inicial
    lexema: str = ''  # lexema actual
    index: int = 0  # indice
    row: int = 1  # fila
    #Before analysis, the verification of Nombre and Grafica needs to be in
    INPUT = input.upper()
    if keywords[0] in INPUT and keywords[1] in INPUT:
        while index < len(INPUT):
            char = INPUT[index]

            # Estado inicial
            if estado == 0:
                #Lista de transicione
                if char == "<":
                    estado = 1
                    index += 1

                # Caracteres ignorados

                elif char == "\n":

                    index += 1


                elif char == "\t":

                    index += 1

                elif char == " ":

                    index += 1


            elif estado == 1:
                if char == "¿":
                    estado = 2
                    index += 1
                elif char==":":
                    estado = 2
                    #tempInventario.append(lexema)
                    #tokens.append(Token('Mes', lexema, row, col))
                    lexema = ''
                    lexema += char
                    lexema = ''
                    index+= 1
                elif char == "\n":
                    index += 1

                elif char == "\t":
                    index += 1
                elif char == " ":
                    index += 1

            elif estado == 2:
                if W.search(char):
                    estado = 2
                    index += 1
                    lexema += char
                elif char == ":":
                    if lexema in keywords:
                        estado = 3
                        temp.append(lexema)
                        lexema = ''
                        index += 1
                    elif char == "\n":
                        index += 1

                    elif char == "\t":
                        index += 1
                    elif char == " ":
                        index += 1
                    else:
                        print("Existe un error en el archivo")
                elif char == "?":
                    estado = 6
                    index +=1
                elif char == "\n":
                    index += 1

                elif char == "\t":
                    index += 1
                elif char == " ":
                    index += 1
                else:
                    errores.append(ErrorEntry(row, col, char))
                    index += 1
                    col += 1

            elif estado == 3:
                if char == '"':
                    estado = 4
                    index += 1
                    lexema += char
                    # tokens.append(Token('Simbolo', lexema, row, col))
                    lexema = ''
                elif char == "\n":
                    index += 1

                elif char == "\t":
                    index += 1
                elif char == " ":
                    index += 1
                else:
                    errores.append(ErrorEntry(row, col, char))
                    index += 1
                    col += 1

            elif estado == 4:
                if char == '"':
                    estado = 5
                    index += 1
                    # tokens.append(Token('Simbolo', char, row, col))
                elif char == "\n":
                    index += 1

                elif char == "\t":
                    index += 1
                elif char == " ":
                    index += 1
                else:
                    estado = 4
                    lexema += char
                    index += 1

            elif estado == 5:
                if char==',':
                    temp.append(lexema)
                    estado = 2
                    index += 1
                    lexema =''
                    instructions.append(Instruction(temp[0], temp[1]))
                    temp.clear()
                elif char == '?':
                    temp.append(lexema)
                    index += 1
                    estado = 6
                elif char == "\n":
                    index += 1

                elif char == "\t":
                    index += 1
                elif char == " ":
                    index += 1

                else:
                    errores.append(ErrorEntry(row, col, char))
                    index += 1
                    col += 1

            elif estado == 6:
                if char=='>':
                    instructions.append(Instruction(temp[0], temp[1]))
                    print("=========== Instrucciones cargadas ========")
                    index += 1
                elif char == "\n":
                    index += 1

                elif char == "\t":
                    index += 1
                elif char == " ":
                    index += 1
                else:
                    errores.append(ErrorEntry(row, col, char))
                    index += 1
                    col += 1
    else:
        print("======EL ANALISIS NO CONTIENE LAS INSTRUCCIONES:========")
        print("1. TITULO")
        print("2. GRAFICA")

    return tuple(instructions), tuple(errores)
