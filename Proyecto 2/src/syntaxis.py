from models.error_entry import ErrorEntry
from models.token import Token
class AnalizadorSintactico:
    def __init__(self):
        self.listaTokens = []
        self.listaErrores = []
        self.i = 0
        self.partidos = []

    def inicio(self, answer):
        # print('inicio')
        token = self.listaTokens[self.i]
        if token.tipo == 'RESULTADO':
            self.bloqueResultado()
        elif token.tipo == 'JORNADA':
            self.bloqueJornada()
        elif token.tipo == 'GOLES':
            self.bloqueGoles()
        elif token.tipo == 'TOP':
            self.bloqueTOP()
        elif token.tipo == 'PARTIDOS':
            self.bloquePartidos()
        elif token.tipo == 'ADIOS':
            self.bloqueAdios()
        elif token.tipo == 'TABLA':
            self.bloqueTabla()



        elif token.tipo == '<<EOF>>':
            print('Analisis sintactico exitoso')
            return answer
    def bloqueTemporada(self):
        year1 = ''
        year2 = ''
        #BLOQUETEMPORADA::= temporada menorque year guion year mayorque
        token = self.listaTokens[self.i]
        if token.tipo == 'TEMPORADA':
            self.i += 1
            token = self.listaTokens[self.i]
            if token.tipo == 'MENORQUE':
                self.i += 1
                token = self.listaTokens[self.i]
                if token.tipo == 'YEAR':
                    year1 = token.lexema
                    self.i += 1
                    token = self.listaTokens[self.i]
                    if token.tipo == 'GUION':
                        self.i += 1
                        token = self.listaTokens[self.i]
                        if token.tipo == 'YEAR':
                            year2 = token.lexema
                            self.i += 1
                            token = self.listaTokens[self.i]
                            if token.tipo == 'MAYORQUE':
                                self.i += 1
                                token = self.listaTokens[self.i]
        return year1, year2

    def bloqueResultado(self):
        #BLOQUERESULTADO ::= resultado string versus string BLOQUETEMPORADA
        token = self.listaTokens[self.i]
        if token.tipo == 'RESULTADO':
            self.i += 1
            token = self.listaTokens[self.i]
            if token.tipo == 'STRING':
                equipolocal = token.lexema
                self.i += 1
                token = self.listaTokens[self.i]
                if token.tipo == 'VERSUS':
                    self.i += 1
                    token = self.listaTokens[self.i]
                    if token.tipo == 'STRING':
                        equipoVisitante = token.lexema
                        self.i += 1
                        token = self.listaTokens[self.i]
                        year1, year2 = self.bloqueTemporada()
                        answer = self.buscarresultadosxpartido(equipolocal, equipoVisitante, year1, year2)
                        self.inicio(answer)
    def condicion(self):
        #CONDICION ::= local
                        #| visitante
        token = self.listaTokens[self.i]
        if token.tipo == 'LOCAL':
            #Set variable local
            self.i += 1
        elif token.tipo == 'VISITANTE':
            #Set variable visitante
            self.i += 1
        elif token.tipo == 'TOTAL':
            #Set variable TOTAL
            self.i += 1


    def bloqueGoles(self):
        #BLOQUEGOLES ::= goles CONDICION string BLOQUETEMPORADA
        token = self.listaTokens[self.i]
        if token.tipo == 'GOLES':
            self.i += 1
            token = self.listaTokens[self.i]
            self.condicion()
            token = self.listaTokens[self.i]
            if token.tipo == 'STRING':
                self.i += 1
                self.bloqueTemporada()
                self.inicio()
    def bloqueTipo(self):
        token = self.listaTokens[self.i]
        if token.tipo == 'GUIONF':
            self.i += 1
            token = self.listaTokens[self.i]
            if token.tipo == 'ARCHIVO':
                self.i += 1
                token = self.listaTokens[self.i]
                self.bloqueTipo()
        elif token.tipo == 'GUIONJI':
            self.i += 1
            token = self.listaTokens[self.i]
            if token.tipo == 'INTEGER':
                self.i += 1
                token = self.listaTokens[self.i]
                self.bloqueTipo()

        elif token.tipo == 'GUIONJF':
            self.i += 1
            token = self.listaTokens[self.i]
            if token.tipo == 'INTEGER':
                self.i += 1
                token = self.listaTokens[self.i]
                self.bloqueTipo()
        elif token.tipo == '<<EOF>>':
            self.inicio()





        pass

    def bloqueJornada(self):
        #BLOQUEJORNADA ::= jornada integer BLOQUETEMPORADA BLOQUETIPO
        token = self.listaTokens[self.i]
        if token.tipo == 'JORNADA':
            self.i += 1
            token = self.listaTokens[self.i]
            if token.tipo == 'INTEGER':
                self.i += 1
                token = self.listaTokens[self.i]
                self.bloqueTemporada()
                token = self.listaTokens[self.i]
                if token.tipo == 'GUIONF':
                    self.i += 1
                    token = self.listaTokens[self.i]
                    if token.tipo == 'ARCHIVO':
                        self.i += 1
                        token = self.listaTokens[self.i]
                        self.inicio()
    def bloqueTabla(self):
        token = self.listaTokens[self.i]
        self.bloqueTemporada()
        token = self.listaTokens[self.i]
        if token.tipo == 'GUIONF':
            self.i += 1
            token = self.listaTokens[self.i]
            if token.tipo == 'ARCHIVO':
                self.i += 1
                self.inicio()
        else:
            self.i += 1
            #Hacer accion
            self.inicio()
    def bloquePartidos(self):
        token = self.listaTokens[self.i]
        if token.tipo == 'PARTIDOS':
            self.i += 1
            token = self.listaTokens[self.i]
            if token.tipo == 'STRING':
                self.i += 1
                token = self.listaTokens[self.i]
                self.bloqueTipo()
    def condicionSup(self):
        token = self.listaTokens[self.i]
        if token.tipo == 'SUPERIOR':
            self.i += 1
            #Acciones
        elif token.tipo == 'INFERIOR':
            self.i += 1
            #Acciones

    def bloqueTOP(self):
        token = self.listaTokens[self.i]
        if token.tipo == 'TOP':
            self.i += 1
            token = self.listaTokens[self.i]
            self.condicionSup()
    def bloqueAdios(self):
        token = self.listaTokens[self.i]
        #FUNCION DE CERRAR



    def analizar(self, listaTokens, listaErrores, listapartidos):
        self.partidos = listapartidos
        self.listaTokens = listaTokens
        self.listaErrores = listaErrores
        self.inicio()

    def buscarresultadosxpartido(self, local, visitante, anioinicio, aniofin):
        elocal = local.replace('"', '')
        evisitante = visitante.replace('"', '')
        temporada = str(anioinicio) + '-' + str(aniofin)
        for partido in self.partidos:
            if partido['local'] == elocal and partido['visitante'] == evisitante and partido['temporada'] == temporada :
                resultado = partido['goleslocal' ] +'- ' +partido['golesvisitante']
                return resultado
        return 'No existe resultado'