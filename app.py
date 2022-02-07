
from typing import List
from afd import automata
from analizador import analizador
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
from tkinter import filedialog as fd

def menu():
    while True:

        print("=============Menu =====================")
        print("|  1. Cargar Data                     |")
        print("|  2. Cargar Instrucciones            |")
        print("|  3. Analizar                        |")
        print("|  4. Reporte                         |")
        print("|  5. Salir                           |")
        print('=======================================')

        op = input('Ingresa una opción: ')
        if op == '1':
            print("===Ha escogido Cargar Data====")
            Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
            filename = fd.askopenfilename(title="Select file", filetypes=(("Data Files", "*.data"), ("All", "*.txt")))
            print(filename)
            current_file = filereader.read(filename)
            tokens, errs = automata(current_file)
            #process_file(tokens, errs)
        elif op == '2':
            print("===Cargar Instrucciones====")
            filename = askopenfilename()
            filereader = open(filename, 'r+', encoding='utf-8')
            current_file = filereader.read()
            tokens, errs = automata(current_file)
            images = analizador(tokens)
            #for img in images:
                #lst_images.append(img)

        elif op == '3':
            print("===Analizar====")
            contador: int = 0
            #for img in lst_images:
                #contador += 1
                #print('{}. {}'.format(contador, img.titulo))
            #select_img = input('Ingresa un numero: ')
            #urrent_img = lst_images[int(select_img) - 1]

            contador_2 = 0
            print('0. NORMAL')
            #for opt in current_img.lista_filtros:
            #    contador_2 += 1
            #    print('{}. {}'.format(contador_2, opt))
            select_opt = input('Ingrese una opción: ')




        elif op == '5':
            print("==================================")
            print("| Gracias por usar el Analizador |")
            print("==================================")
            break

if __name__ == '__main__':
    menu()
