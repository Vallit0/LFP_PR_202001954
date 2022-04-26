from afd import automata
from os import startfile
from helpers import process_file

def responseLoad(msg):
    tokens, errs = automata(msg)
    for i in range(len(tokens)):
        print(tokens[i].lexema)

    print("Analisis Lexico Terminado")
    # Termina lectura y generacion de Tokens
    tokenTable, errsTable = process_file(tokens, errs)
    return tokenTable, errsTable

def get_response(msg):
    #Get response RECIBE UN TEXTO
    #//Analizador Lexico
    tokens, errs = automata(msg)
    for i in range(len(tokens)):
        print(tokens[i].lexema)

    print("Analisis Lexico Terminado")
    # Termina lectura y generacion de Tokens
    tokenTable, errsTable = process_file(tokens, errs)
    return 'Ok'
    # Crear Files para las tablas de Tokens y Errores


    #ANALISIS LEXICO FINALIZADO





    return "No entiendo lo que dijiste, debe haber algun Error"

    