from tkinter import *
from chat import get_response
from os import startfile
from helpers import process_file, processErrsTable, processTokenTable, processCSV
from afd import automata
bots = ['Fernando Palomo', 'MessiBOT',
        'Maradona (Desde el cielito)', 'NeyBOT', 'Mario Kempes', 'El de Chiringuito',
        'El de Chiringuito que hace caras', 'Mbot', 'Siu', 'Jose Antonio Corado ', 'El Fifas']

bot_name = 'El Fifas'

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"
FONT_BOLD

class ChatApplication:
    
    def __init__(self):
        self.window = Tk()
        self._setup_main_window()
        self.errList = []
        self.tokenList = []
        self.loaded = False
        self.objects = []

        
    def run(self):
        self.window.mainloop()
        
    def _setup_main_window(self):
        self.window.title("La Liga Bot")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=1000, height=600, bg=BG_COLOR)
        
        # head label
        head_label = Label(self.window, bg=BG_COLOR, fg=TEXT_COLOR,
                           text="Proyecto 2 - LFP League Bot", font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1)
        
        # tiny divider
        line = Label(self.window, width=450, bg=BG_GRAY)
        line.place(relwidth=1, rely=0.07, relheight=0.012)
        
        # text widget
        self.text_widget = Text(self.window, width=20, height=2, bg=BG_COLOR, fg=TEXT_COLOR,
                                font=FONT, padx=5, pady=5)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)
        
        # scroll bar
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)
        
        # bottom label
        bottom_label = Label(self.window, bg=BG_GRAY, height=80)
        bottom_label.place(relwidth=1, rely=0.825)



        #load Button
        load_button = Button(self.window, text="Load", font=FONT_BOLD, width=20, bg=BG_GRAY,
                             command=lambda: self.loadCSV())
        load_button.place(relx=0.01, rely=0.08, relheight=0.06, relwidth=0.22)

        #Reporte Errs  Button
        errsReport_button = Button(self.window, text="Reporte de Errores", font=FONT_BOLD, width=20, bg=BG_GRAY,
                             command=lambda: self.errorReport())
        errsReport_button.place(relx=0.16, rely=0.08, relheight=0.06, relwidth=0.22)

        #Limpiar Log Errores
        cleanErrs_button = Button(self.window, text="Limpiar Errores", font=FONT_BOLD, width=20, bg=BG_GRAY,
                             command=lambda: self.cleanErrors())
        cleanErrs_button.place(relx=0.32, rely=0.08, relheight=0.06, relwidth=0.22)

        #Reporte Tokens
        tokenReport_button = Button(self.window, text="Reporte Tokens", font=FONT_BOLD, width=20, bg=BG_GRAY,
                             command=lambda: self.processTokens())
        tokenReport_button.place(relx=0.48, rely=0.08, relheight=0.06, relwidth=0.22)

        #Limpiar Tokens
        cleanTokens_button = Button(self.window, text="Limpiar Tokens", font=FONT_BOLD, width=20, bg=BG_GRAY,
                             command=lambda: self.cleanTokens())
        cleanTokens_button.place(relx=0.64, rely=0.08, relheight=0.06, relwidth=0.22)

        #Manual de Usuario
        user_button = Button(self.window, text="Manual Usuario", font=FONT_BOLD, width=20, bg=BG_GRAY,
                             command=lambda: self.showUserManual())
        user_button.place(relx=0.80, rely=0.08, relheight=0.06, relwidth=0.22)

        # Manual de Tecnico
        manualTech_button = Button(self.window, text="Manual Tecnico", font=FONT_BOLD, width=20, bg=BG_GRAY,
                             command=lambda: self.showTechManual())

        manualTech_button.place(relx=0.80, rely=0.02, relheight=0.06, relwidth=0.22)

        # message entry box
        self.msg_entry = Entry(bottom_label, bg="#2C3E50", fg=TEXT_COLOR, font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)
        
        # send button
        send_button = Button(bottom_label, text="Send", font=FONT_BOLD, width=20, bg=BG_GRAY,
                             command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)

    def errorReport(self):
        if len(self.errList) == 0:
            self._insert_messageNone('No he encontrado Errores mi rey', 'El Fifas')
            self._insert_messageNone('No hay morras chidas', 'El Fifas')

        else:
            processErrsTable(self.errList)

    def processTokens(self):
        if len(self.tokenList) == 0:
            self._insert_messageNone('No he encontrado palabras, puedes escribir algo', 'El Fifas')
            self._insert_messageNone('De seguro sos mi hijo en Fifa', 'El Fifas')
        else:
            processTokenTable(self.tokenList)

    def cleanErrors(self):
        self.errList = []

    def cleanTokens(self):
        self.tokenList = []

    def showUserManual(self):
        try:
            startfile('ManualUsuario.pdf')
        except:
            print("No se encontro el archivo")

    def showTechManual(self):
        try:
            startfile('ManualTecnico.pdf')
        except:
            print("No se encontro el archivo")
    def loadCSV(self):
        self.loaded, self.objects = processCSV()
        self._insert_messageNone(' ', ' ')
        self._insert_messageNone('BIENVENIDO a La Liga Bot, soy El Fifas y te podre ayudar en lo que necesites', 'El Fifas')




    def _on_enter_pressed(self, event):
        if self.loaded == True:


            msg = self.msg_entry.get()
            self._insert_message(msg, "Tu")
        else:
            self._insert_messageNone(' ', ' ')
            self._insert_messageNone('Bienvenido a La Liga Bot', 'El Fifas')
            self._insert_messageNone('Por favor ingresa con LOAD la base de datos', 'El Fifas')
        
    def _insert_message(self, msg, sender):
        if not msg:
            return
        
        self.msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)
        #Se realiza el analisis lexico
        tokens, errs = automata(msg)
        #Se anade el analisis lexico a la lista principal
        self.tokenList.extend(tokens)
        self.errList.extend(errs)

        #Se anade el analisis sintactico
        msg2 = f"{bot_name}: {get_response(msg)}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)
        
        self.text_widget.see(END)
    def _insert_messageNone(self, msg, sender):
        if not msg:
            return

        self.msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)


        self.text_widget.see(END)
             
        
if __name__ == "__main__":
    app = ChatApplication()
    app.run()