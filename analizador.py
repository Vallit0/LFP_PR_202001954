from typing import List
from models.token import Token
from models.product import *



def analizador(tokens: List[Token]):
    lista_images: list = []
    lst_img_return: List[ImageEntry] = []

    image: list = []  # Imagen 0, por defecto
    lista_images.append(image)

    for i in range(len(tokens)):
        if tokens[i].token == 'separador':
            new_image: list = []
            lista_images.append(new_image)
            continue

        lista_images[-1].append(tokens[i])

    for image in lista_images:
        lst_img_return.append(analizar_imagen(image))

    return lst_img_return


def analizar_imagen(tokens: List[Token]) -> ImageEntry:
    image = ImageEntry()

    # Leer titulo
    for i in range(len(tokens)):
        if tokens[i].token == 'reservada' and tokens[i].lexema == 'TITULO' \
            and tokens[i+1].token == 'simbolo' and tokens[i+1].lexema == '=' \
                and tokens[i+2].token == 'string' \
                    and tokens[i+3].token == 'simbolo' and tokens[i+3].lexema == ';':

            image.titulo = tokens[i + 2].lexema.replace('"', '')
            break

    # Leer ancho
    for i in range(len(tokens)):
        if tokens[i].token == 'reservada' and tokens[i].lexema == 'ANCHO' \
            and tokens[i+1].token == 'simbolo' and tokens[i+1].lexema == '=' \
                and tokens[i+2].token == 'numero' \
                    and tokens[i+3].token == 'simbolo' and tokens[i+3].lexema == ';':

            image.ancho = int(tokens[i + 2].lexema)
            break

    # Leer alto
    for i in range(len(tokens)):
        if tokens[i].token == 'reservada' and tokens[i].lexema == 'ALTO' \
            and tokens[i+1].token == 'simbolo' and tokens[i+1].lexema == '=' \
                and tokens[i+2].token == 'numero' \
                    and tokens[i+3].token == 'simbolo' and tokens[i+3].lexema == ';':

            image.alto = int(tokens[i + 2].lexema)
            break

    # Leer filas
    for i in range(len(tokens)):
        if tokens[i].token == 'reservada' and tokens[i].lexema == 'FILAS' \
            and tokens[i+1].token == 'simbolo' and tokens[i+1].lexema == '=' \
                and tokens[i+2].token == 'numero' \
                    and tokens[i+3].token == 'simbolo' and tokens[i+3].lexema == ';':

            image.filas = int(tokens[i + 2].lexema)
            break

    # Leer columnas
    for i in range(len(tokens)):
        if tokens[i].token == 'reservada' and tokens[i].lexema == 'COLUMNAS' \
            and tokens[i+1].token == 'simbolo' and tokens[i+1].lexema == '=' \
                and tokens[i+2].token == 'numero' \
                    and tokens[i+3].token == 'simbolo' and tokens[i+3].lexema == ';':

            image.columnas = int(tokens[i + 2].lexema)
            break

    j: int = 0
    flag_celdas: bool = False  # detecta si celdas fue encontrado
    tokens_celdas: List[Token] = []
    # Leer todos los tokens de celda
    while j < len(tokens):
        if tokens[j].token == 'reservada' and tokens[j].lexema == 'CELDAS' \
           and tokens[j+1].token == 'simbolo' and tokens[j+1].lexema == '=' \
               and tokens[j+2].token == 'simbolo' and tokens[j+2].lexema == '{':
            flag_celdas = True
            j += 3
            continue

        if tokens[j].token == 'simbolo' and tokens[j].lexema == '}' \
            and tokens[j+1].token == 'simbolo' and tokens[j+1].lexema == ';':
            flag_celdas = False
            j += 2
            continue

        if flag_celdas:
            tokens_celdas.append(tokens[j])

        j += 1

    image.celdas = analizar_celdas(tokens_celdas)

    j: int = 0
    flag_filtros: bool = False
    tokens_filtros: List[Token] = []
    # Leer filtros
    while j < len(tokens):
        if tokens[j].token == 'reservada' and tokens[j].lexema == 'FILTROS' \
           and tokens[j+1].token == 'simbolo' and tokens[j+1].lexema == '=':
            flag_filtros = True
            j += 2
            continue

        if tokens[j].token == 'simbolo' and tokens[j].lexema == ';':
            flag_filtros = False
            j += 1
            continue

        if flag_filtros:
            tokens_filtros.append(tokens[j])

        j += 1

    image.lista_filtros = analizar_filtros(tokens_filtros)

    return image


def analizar_celdas(tokens: List[Token]) -> List[Celda]:
    tokens_celdas: List[List[Token]] = []
    lst_celdas: List[Celda] = []
    flag: bool = False

    celda: List[Token] = []
    for i in range(len(tokens)):
        if tokens[i].token == 'simbolo' and tokens[i].lexema == '[':
            flag = True
            celda.append(tokens[i])
            continue

        if tokens[i].token == 'simbolo' and tokens[i].lexema == ']':
            flag = False
            celda.append(tokens[i])
            tokens_celdas.append(celda.copy())
            celda.clear()
            continue

        if flag:
            celda.append(tokens[i])

    for celda in tokens_celdas:
        obj_celda: Celda = Celda()
        obj_celda.pos_x = int(celda[1].lexema)
        obj_celda.pos_y = int(celda[3].lexema)
        obj_celda.is_draw = True if celda[5].lexema == 'TRUE' else False
        obj_celda.color = celda[7].lexema

        lst_celdas.append(obj_celda)

    return lst_celdas


def analizar_filtros(tokens: List[Token]):
    lst_filtros: List[str] = []

    for i in range(len(tokens)):
        if tokens[i].token == 'reservada':
            lst_filtros.append(tokens[i].lexema)

    return lst_filtros