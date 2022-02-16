
from typing import List
from analyzer import automata
from instructionsA import instructionsAnalyzer
from helpers import instructionsSort, graphBuilder, reportGenerator, sortProducts
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
from tkinter import filedialog as fd


if __name__ == '__main__':
    inventario = None
    instructions = None
    products = None

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
            file = open(filename, encoding="utf8")
            content = file.read()
            print(content)
            inventario,products= automata(content)
            print('========INVENTARIO DE:==============')
            print('YEAR -> '+ inventario.year)
            print('MONTH -> '+ inventario.month)
            file.close()



            
            #process_file(tokens, errs)
        elif op == '2':
            print("===Cargar Instrucciones====")
            Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
            filename = fd.askopenfilename(title="Select file", filetypes=(("LFP  files", "*.lfp"), ("All", "*.txt")))
            print(filename)
            file = open(filename, encoding="utf8")
            content = file.read()
            print(content)
            instructions, err2 = instructionsAnalyzer(content)
            for instruction in instructions:
                print(instruction.instruction + '->'+instruction.command)


            file.close()

        elif op == '3':
            print("===Analizar====")
            if instructions != None and products != None and inventario != None:
                graphBuilder(instructionsSort(instructions), products, inventario)
            else:
                print('Aun no se ha cargado instrucciones')
        elif op == '4':
            print("===Reportes====")
            file = open('tableReport.html', 'w')
            table = reportGenerator(sortProducts(products))
            file.write(table)
            file.close()
            print('====Se ha generado el reporte====')




        elif op == '5':
            print("==================================")
            print("| Gracias por usar el Analizador |")
            print("==================================")
            break



