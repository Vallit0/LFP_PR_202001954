from tkinter import Button, Frame, Text, Tk, Label, OptionMenu, StringVar
from tkinter.messagebox import showerror, showinfo
from tkinter.constants import END
from afd import automata
from tkinter.filedialog import askopenfilename
from typing import List
from os import startfile
from tkinter import filedialog as fd
from helpers import process_file, analyzeFile, generateForms



class MainApp:
    def __init__(self) -> None:

        self.root = Tk()
        self.root.title("Proyecto 1 - Lenguajes Formales y de Programacion")
        #self.root.iconbitmap('circle.png')
        self.frame = Frame()
        self.tokens = []
        self.errs = []

        self.root.geometry('1000x640')
        self.root.resizable(0, 0)
        self.frame.place(x=0, y=0)
        self.frame.config(width=1000, height=640)

        Button(self.frame, text='Abrir archivo',
               command=self.load_file).place(x=10, y=10)
        Button(self.frame, text='Analizar archivo',
               command=self.analyze_file).place(x=120, y=10)
        Button(self.frame, text='Reportes en HTML',
               command=self.show_reports).place(x=240, y=10)
        Button(self.frame, text='Manual de Usuario',
               command=self.showManual).place(x=350, y=10)
        Button(self.frame, text='Manual Tecnico',
               command=self.showTechManual).place(x=580, y=10)
        Button(self.frame, text='Generar Forms',
               command=self.generarForms).place(x=620, y=30)
        Label(self.frame, text='Lenguajes Formales y de Programacion').place(x=10, y=40)
        Label(self.frame, text='Estuardo Sebastian Valle Bances').place(x=10, y=60)
        Label(self.frame, text='202001954').place(x=10, y=80)
        self.clicked = StringVar()
        self.drop = OptionMenu(self.root, self.clicked,"Reporte de Tokens", "Reporte de Errores", "Manual de Usuario", "Manual Tecnico" )
        self.drop.place(x=700, y=10)


        self.file: str = ''

        self.txt_input = Text(self.frame, width=120, height=32)
        self.txt_input.place(x=10, y=100)

        #self.txt_console = Text(self.frame, width=60, height=32)
        #self.txt_console.place(x=490, y=60)

        self.valid_str: str = ''
        #self.valid_tokens: List[TokenEntry] = []
        #self.lexical_errs: List[ErrorEntry] = []
        #self.sintax_errs: List[SintaxError] = []

        self.root.mainloop()

    def load_file(self):
        filename = fd.askopenfilename(title="Select file", filetypes=(("Form", "*.form"), ("All", "*.txt")))
        file = open(filename, 'r+', encoding='utf-8')

        self.file = ''
        self.txt_input.delete('1.0', END)

        self.file = file.read()
        self.txt_input.insert(END, self.file)

    def analyze_file(self):
        self.valid_str = ''
        #self.valid_tokens.clear()
        #self.lexical_errs.clear()

        txt = self.txt_input.get('1.0', END)
        file = open('planeiFrame.html', 'w')
        theText = ''
        theText += '''<!DOCTYPE html>
                    <html>
                    <body>\n'''
        theText += '<p>'
        theText += txt
        theText += '</p>\n'
        theText += '''
        </body>
        </html>
        '''

        file.write(theText)
        file.close()
        self.tokens, self.errs = automata(txt)
        if len(self.errs) > 0:
            print("Hay errores en el archivo")

        print("Analisis Lexico Terminado")


    def show_reports(self):
        tokenTable, errsTable = process_file(self.tokens, self.errs)
        tableTokens = open('ReporteTokens.html', 'w')
        tableTokens.write(tokenTable)
        startfile('ReporteTokens.html')
        tableErrors = open('ReporteErrores.html', 'w')
        tableErrors.write(errsTable)
        startfile('ReporteErrores.html')
        tableTokens.close()
        tableErrors.close()
    def showManual(self):
        try:
            startfile('ManualUsuario.pdf')
        except:
            print("No se encontro el archivo")

    def showTechManual(self):
        try:
            startfile('ManualTecnico.pdf')
        except:
            print("No se encontro el archivo")

    def generarForms(self):
        if len(self.errs) == 0:
            self.valid_str = ''
            # self.valid_tokens.clear()
            # self.lexical_errs.clear()

            txt = self.txt_input.get('1.0', END)
            self.tokens, self.errs = automata(txt)
            for i in range(len(self.tokens)):
                print(self.tokens[i].lexema)

            elementos, errores= analyzeFile(self.tokens)
            print(errores)
            if errores == 0:
                print("Se ha pasado el analisis del archivo")
                elementsss, errores = analyzeFile(self.tokens)
                generateForms(elementsss)
            else:
                print("Existe un Error en los Tipos")


            print('No hay Errores')
        else:
            print("Hay Errores en el archivo")
            self.messagebox.askyesno(title=None, message=None)







if __name__ == '__main__':
    MainApp()