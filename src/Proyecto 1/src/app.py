from tkinter import Tk
from tkinter.filedialog import askopenfilename
from typing import List
from afd import automata
from os import startfile
from helpers import process_file
from tkinter import filedialog as fd

if __name__ == '__main__':

    Tk().withdraw()
    while True:
        print('''
---- ---- ---- Menu ---- ---- ----
1. Analizar Archivo y ver reportes

        ''')

        value = input('Ingresa una opción: ')
        if value == '1':

            filename = fd.askopenfilename(title="Select file", filetypes=(("Form Files", "*.form"), ("All", "*.txt")))
            filereader = open(filename, 'r+', encoding='utf-8')
            current_file = filereader.read()
            tokens, errs = automata(current_file)
            for i in range(len(tokens)):
                print(tokens[i].lexema)

            print("Analisis Lexico Terminado")
            #Termina lectura y generacion de Tokens
            tokenTable, errsTable = process_file(tokens, errs)
            #Crear Files para las tablas de Tokens y Errores
            tableTokens = open('ReporteTokens.html', 'w')
            tableTokens.write(tokenTable)
            startfile('ReporteTokens.html')
            tableErrors = open('ReporteErrores.html','w')
            tableErrors.write(errsTable)
            startfile('ReporteErrores.html')
            tableTokens.close()
            tableErrors.close()



