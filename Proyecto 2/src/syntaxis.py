from models.error_entry import ErrorEntry
from models.token import Token
from helpers import matchDayGraph, seasonGraph, seasonStatsGraph
class Team:
    def __init__(self, name):
        self.name = name
        self.goles = 0
        self.puntos = 0
        self.victorias = 0
        self.empates = 0
        self.perdidas = 0

class AnalizadorSintactico:
    def __init__(self):
        self.listaTokens = []
        self.listaErrores = []
        self.i = 0
        self.partidos = []

    def inicio(self, answer):
        if answer != None:
            return answer
        else:
            token = self.listaTokens[self.i]
            if token.token == 'RESULTADO':
                print('RESULTADO')
                return self.bloqueResultado()
            elif token.token == 'JORNADA':
                 return self.bloqueJornada()

            elif token.token == 'GOLES':
                return self.bloqueGoles()
            elif token.token == 'TOP':
                return self.bloqueTOP()
            elif token.token == 'PARTIDOS':
                return self.bloquePartidos()
            elif token.token == 'ADIOS':
                return self.bloqueAdios()
            elif token.token == 'TABLA':
                return self.bloqueTabla()



            elif token.token == '<<EOF>>':
                print('Analisis sintactico exitoso')
                return answer
            else:
                error = ErrorEntry(1, 1, token.lexema)
                error.type = 'Sintactico'
                error.token = token.token
                error.razon = 'Se Esperaba un comando'
                self.listaErrores.append(error)
                return token.lexema + '\n^\nSe Esperaba un comando'

    def bloqueTemporada(self):
        year1 = ''
        year2 = ''
        queja = ''
        #BLOQUETEMPORADA::= temporada menorque year guion year mayorque
        token = self.listaTokens[self.i]
        if token.token == 'TEMPORADA':
            self.i += 1
            token = self.listaTokens[self.i]
            print('Temporada')
            if token.token == 'MENORQUE':
                self.i += 1
                token = self.listaTokens[self.i]
                if token.token == 'YEAR':
                    year1 = token.lexema
                    self.i += 1
                    token = self.listaTokens[self.i]
                    if self.i >= len(self.listaTokens):
                        token = self.listaTokens[self.i - 1]
                    else:
                        token = self.listaTokens[self.i]
                    print(' ' + year1, end='')
                    if token.token == 'GUION':
                        self.i += 1
                        token = self.listaTokens[self.i]
                        print('-')
                        if token.token == 'YEAR':
                            year2 = token.lexema
                            self.i += 1
                            token = self.listaTokens[self.i]
                            print(year2)
                            if token.token == 'MAYORQUE':
                                self.i += 1
                                token = self.listaTokens[self.i]
                            else:
                                error = ErrorEntry(1, token.col, token.lexema)
                                error.type = 'Sintactico'

                                error.token = token.token
                                error.razon = 'Se Esperaba un >'
                                self.listaErrores.append(error)
                                espacio = '   '
                                queja += token.lexema + '\n' + espacio + '^\nSe Esperaba un ">"'
                        else:
                            error = ErrorEntry(1, token.col, token.lexema)
                            error.type = 'Sintactico'

                            error.token = token.token
                            error.razon = 'Se Esperaba un YEAR o Numero 4 digitos'
                            self.listaErrores.append(error)
                            espacio = '   '
                            queja += token.lexema + '\n' + espacio + '^\nSe Esperaba un Numero de 4 Digitos'
                    else:
                        error = ErrorEntry(1, token.col, token.lexema)
                        error.type = 'Sintactico'

                        error.token = token.token
                        error.razon = 'Se Esperaba un -'
                        self.listaErrores.append(error)
                        espacio = '   '
                        queja += token.lexema + '\n' + espacio + '^\nSe Esperaba un "-"'
                else:
                    error = ErrorEntry(1, token.col, token.lexema)
                    error.type = 'Sintactico'

                    error.token = token.token
                    error.razon = 'Se Esperaba un YEAR'
                    self.listaErrores.append(error)
                    espacio = '   '
                    queja += token.lexema + '\n' + espacio + '^\nSe Esperaba un Numero de 4 Digitos'
            else:
                error = ErrorEntry(1, token.col, token.lexema)
                error.type = 'Sintactico'
                error.type = 'Sintactico'
                error.token = token.token
                error.razon = 'Se Esperaba un <'
                self.listaErrores.append(error)
                queja += token.lexema + '\n' + '^\nSe Esperaba un <'

        else:
            error = ErrorEntry(1, token.col, token.lexema)
            error.type = 'Sintactico'
            error.type = 'Sintactico'
            error.token = token.token
            error.razon = 'Se Esperaba TEMPORADA'
            self.listaErrores.append(error)
            return '', '', token.lexema + '\n' + '^\nSe Esperaba un TEMPORADA'


        return year1, year2, queja

    def bloqueResultado(self):
        #BLOQUERESULTADO ::= resultado string versus string BLOQUETEMPORADA
        erroresResultado = []
        print('El resultado de este partido fue: ')
        respuesta = 'El Resultado De Este Partido Fue: '
        token = self.listaTokens[self.i]
        if token.token == 'RESULTADO':
            self.i += 1
            token = self.listaTokens[self.i]
            if token.token == 'STRING':

                equipolocal = token.lexema

                print(equipolocal)
                self.i += 1
                token = self.listaTokens[self.i]
                if token.token == 'VERSUS':
                    self.i += 1
                    token = self.listaTokens[self.i]
                    if token.token == 'STRING':
                        equipoVisitante = token.lexema
                        print(equipoVisitante)
                        self.i += 1
                        token = self.listaTokens[self.i]
                        year1, year2, queja = self.bloqueTemporada()
                        if queja != '':
                            queja = '\n'+ queja
                        if year1 == '' or year2 =='':
                            return 'No Hay Informacion Suficiente' + queja
                        answer1 = self.buscarresultadosxpartido(equipolocal, equipoVisitante, year1, year2)
                        answer = respuesta + '' + answer1 + queja
                        print(answer)
                        return answer
                    else:
                        error = ErrorEntry(1, token.col, token.lexema)
                        error.type = 'Sintactico'
                        error.type = 'Sintactico'
                        error.token = token.token
                        error.razon = 'Se Esperaba un Equipo'
                        self.listaErrores.append(error)
                        espacio = '                      '

                        return token.lexema + '\n' + espacio + '^\nSe Esperaba un Equipo'
                else:
                    error = ErrorEntry(1, token.col, token.lexema)
                    error.type = 'Sintactico'
                    error.type = 'Sintactico'
                    error.token = token.token
                    error.razon = 'Se Esperaba un VS'
                    self.listaErrores.append(error)
                    espacio = '        '

                    return token.lexema + '\n' + espacio + '^\nSe Esperaba VERSUS'
            else:
                error = ErrorEntry(1, token.col, token.lexema)
                error.type = 'Sintactico'
                error.type = 'Sintactico'
                error.token = token.token
                error.razon = 'Se Esperaba un equipo'
                self.listaErrores.append(error)
                espacio = '        '
                return token.lexema + '\n'+espacio+'^\nSe Esperaba un equipo'

    def condicion(self):
        condicionJuego = ''
        queja = ''
        #CONDICION ::= local
                        #| visitante
        token = self.listaTokens[self.i]
        if token.token == 'LOCAL':
            #Set variable local
            condicionJuego = 'LOCAL'
            self.i += 1
        elif token.token == 'VISITANTE':
            #Set variable visitante
            condicionJuego = 'VISITANTE'
            self.i += 1
            local = False
        elif token.token == 'TOTAL':
            #Set variable TOTAL
            condicionJuego = 'TOTAL'
            self.i += 1
        else:
            error = ErrorEntry(1, token.col, token.lexema)
            error.type = 'Sintactico'
            error.type = 'Sintactico'
            error.token = token.token
            error.razon = 'Se Esperaba una CONDICION'
            self.listaErrores.append(error)
            espacio = '        '
            queja += token.lexema + '\n' + espacio + '^\nSe Esperaba una CONDICION'
        return condicionJuego, queja


    def bloqueGoles(self):
        #BLOQUEGOLES ::= goles CONDICION string BLOQUETEMPORADA
        token = self.listaTokens[self.i]
        condicion = ''
        equipo = ''
        queja = ''

        if token.token == 'GOLES':
            self.i += 1
            token = self.listaTokens[self.i]
            condicion, quejaCondiciones = self.condicion()
            if condicion == '':
                condicion = 'LOCAL'
                quejaCondiciones += '\n' + 'Se tomo LOCAL como CONDICION'
            token = self.listaTokens[self.i]
            if token.token == 'STRING':
                equipo = token.lexema
                self.i += 1
                #condicionJuego = self.condicion()
                year1, year2, queja = self.bloqueTemporada()
                if year1 == '' or year2 == '':
                    return 'No hay suficiente Informacion \n' + queja
                if queja == '':
                    queja = '\n' + queja
                goles = self.contarGoles(condicion, equipo, year1, year2)
                return 'Los goles anotados por el '+equipo+' en total en la temporada '+year1+'-'+ year2+' fueron '+str(goles)+str(queja)+ str(quejaCondiciones)
            else:
                error = ErrorEntry(1, token.col, token.lexema)
                error.type = 'Sintactico'
                error.type = 'Sintactico'
                error.token = token.token
                error.razon = 'Se Esperaba un equipo'
                self.listaErrores.append(error)
                espacio = '        '
                return token.lexema + '\n'+espacio+'^\nSe Esperaba un equipo'
    def bloqueTipo(self, classifier):
        queja = ''
        if self.i >= len(self.listaTokens):
            return None, queja
        else:
            token = self.listaTokens[self.i]
        if token.token == 'GUIONF' and classifier == 'name':
            self.i += 1
            token = self.listaTokens[self.i]
            if token.token == 'ARCHIVO':
                nombreArchivo = self.listaTokens[self.i]
                self.i += 1

                if self.i < len(self.listaTokens):
                    token = self.listaTokens[self.i]

                return nombreArchivo.lexema, queja
            else:
                error = ErrorEntry(1, token.col, token.lexema)
                error.type = 'Sintactico'
                error.type = 'Sintactico'
                error.token = token.token
                error.razon = 'Se Esperaba un Entero'
                self.listaErrores.append(error)
                espacio = '   '
                queja += token.lexema + '\n' + espacio + '^\nSe Esperaba se Esperaba un Entero'
                return None, queja
        elif token.token == 'GUIONJI' and classifier == 'ji':
            self.i += 1
            token = self.listaTokens[self.i]
            if token.token == 'INTEGER':
                token = self.listaTokens[self.i]
                limiteinf = int(token.lexema)
                self.i += 1
                if self.i < len(self.listaTokens):
                    token = self.listaTokens[self.i]
                return limiteinf, queja
            else:
                error = ErrorEntry(1, token.col, token.lexema)
                error.type = 'Sintactico'
                error.type = 'Sintactico'
                error.token = token.token
                error.razon = 'Se Esperaba un Entero'
                self.listaErrores.append(error)
                espacio = '   '
                queja += token.lexema + '\n' + espacio + '^\nSe Esperaba se Esperaba un Entero'
                return None, queja


        elif token.token == 'GUIONJF' and classifier == 'jf':
            self.i += 1
            token = self.listaTokens[self.i]
            if token.token == 'INTEGER':
                token = self.listaTokens[self.i]
                limitesup = int(token.lexema)
                self.i += 1
                if self.i < len(self.listaTokens):

                    token = self.listaTokens[self.i]
                return limitesup, queja
            else:
                error = ErrorEntry(1, token.col, token.lexema)
                error.type = 'Sintactico'
                error.type = 'Sintactico'
                error.token = token.token
                error.razon = 'Se Esperaba un Entero'
                self.listaErrores.append(error)
                espacio = '   '
                queja += token.lexema + '\n' + espacio + '^\nSe Esperaba se Esperaba un Entero'
                return None, queja
        elif classifier == 'jf':
            return None, queja
        elif classifier == 'name':
            return None, queja
        elif classifier == 'ji':
            return None, queja
        elif token.token == '<<EOF>>':
            return None, queja
        else:
            error = ErrorEntry(1, token.col, token.lexema)
            error.type = 'Sintactico'
            error.type = 'Sintactico'
            error.token = token.token
            error.razon = 'Se Esperaba un comando'
            self.listaErrores.append(error)
            espacio = '   '
            queja += token.lexema + '\n' + espacio + '^\nSe Esperaba se Esperaba un Comando'
            return None, queja






        pass

    def bloqueJornada(self):
        #BLOQUEJORNADA ::= jornada integer BLOQUETEMPORADA BLOQUETIPO
        token = self.listaTokens[self.i]
        jornada = 0
        year1 = ''
        year2 = ''
        queja = ''
        name = 'jornada'
        if token.token == 'JORNADA':
            self.i += 1
            token = self.listaTokens[self.i]
            if token.token == 'INTEGER':
                jornada = token.lexema
                self.i += 1
                token = self.listaTokens[self.i]
                year1, year2, queja = self.bloqueTemporada()
                if self.i < len(self.listaTokens) or self.i == len(self.listaTokens):

                    token = self.listaTokens[self.i]
                    if token.token == 'GUIONF':
                        self.i += 1
                        if self.i > len(self.listaTokens) or self.i == len(self.listaTokens):
                            return 'Podrias Agregar un Espacio Al Final?'
                        else:
                            token = self.listaTokens[self.i]

                            print(token.lexema)
                            if token.token == 'ARCHIVO':
                                name = token.lexema

                                self.buscarXjornada(name, jornada, year1, year2)
                                return 'Generando Archivo de Resultados jornada' + jornada + 'temporada' + year1 + '-' + year2
                            else:
                                self.buscarXjornada('jornada', jornada, year1, year2)
                                return 'JORNADA '+ jornada +' TEMPORADA <1996-1997> -f \n                              ^\n Se esperaba nombre de un archivo' + '''
                                Generando Archivo de Resultados Jornada''' + jornada + 'temporada' + year1 + '-' + year2
                    elif token.token == '<<EOF>>':
                        self.buscarXjornada('jornada', jornada, year1, year2)
                        return 'Generando Archivo de Resultados jornada' + jornada + 'temporada' + year1 + '-' + year2
                    else:
                        self.buscarXjornada('jornada', jornada, year1, year2)
                        return 'JORNADA ' + jornada + ' TEMPORADA <1996-1997> '+token.lexema+' \n                                                                                                 ^\n Se esperaba "-f"' + '''
                                Generando Archivo de Resultados Jornada''' + jornada + 'temporada' + year1 + '-' + year2
                else:
                    self.buscarXjornada('jornada', jornada, year1, year2)
                    return 'Generando Archivo de Resultados jornada' + jornada + 'temporada' + year1 + '-' + year2
            else:
                error = ErrorEntry(1, token.col, token.lexema)
                error.type = 'Sintactico'
                error.type = 'Sintactico'
                error.token = token.token
                error.razon = 'Se Esperaba un ENTERO'
                self.listaErrores.append(error)
                espacio = '        '
                return token.lexema + '\n'+espacio+'^\nSe Esperaba un ENTERO de uno o dos Digitos'



    def bloqueTabla(self):
        token = self.listaTokens[self.i]
        print(token.lexema)
        self.i += 1
        token = self.listaTokens[self.i]
        name = 'temporada'
        year1, year2, queja = self.bloqueTemporada()
        token = self.listaTokens[self.i]
        if year1 == '' or year2 == '':
            return 'No hay informacion suficiente'
        if queja != '':
            queja = '\n' + queja
        print(token.lexema)
        if token.token == 'GUIONF':
            self.i += 1
            token = self.listaTokens[self.i]
            if token.token == 'ARCHIVO':
                self.i += 1
                self.tablaTemporada(year1, year2, name)
                return 'Generando Archivo de Clasificacion Temporada' + year1 + '-' + year2
            else:
                self.i += 1
                self.tablaTemporada(year1, year2, name)

                error = ErrorEntry(1, token.col, token.lexema)
                error.type = 'Sintactico'
                error.type = 'Sintactico'
                error.token = token.token
                error.razon = 'Se Esperaba un ARCHIVO'
                self.listaErrores.append(error)

                return token.token + '\n ^' + 'Se esperaba ARCHIVO \n' + 'Generando Archivo de Clasificacion Temporada' + year1 + '-' + year2


        elif token.token == '<<EOF>>':
            self.i += 1
            self.tablaTemporada(year1, year2, name)
            return 'Generando Archivo de Clasificacion Temporada' + year1 + '-' + year2
        else:
            self.i += 1
            self.tablaTemporada(year1, year2, name)

            error = ErrorEntry(1, token.col, token.lexema)
            error.type = 'Sintactico'
            error.type = 'Sintactico'
            error.token = token.token
            error.razon = 'Se Esperaba un -f'
            self.listaErrores.append(error)


            return token.token +'\n ^'+'Se esperaba -f \n'+'Generando Archivo de Clasificacion Temporada' + year1 + '-' + year2

    def bloquePartidos(self):
        equipo = ''
        year1 = ''
        year2 = ''
        ji = None
        jf = None
        name = 'partidos'

        token = self.listaTokens[self.i]
        if token.token == 'PARTIDOS':
            self.i += 1
            token = self.listaTokens[self.i]
            if token.token == 'STRING':
                equipo = token.lexema
                self.i += 1
                token = self.listaTokens[self.i]
                year1, year2, queja = self.bloqueTemporada()
                if year1 == '' or year2 == '':
                    return 'No existe suficiente informacion'
                if queja != '':
                    queja = '\n' + queja
                name, queja1 = self.bloqueTipo('name')
                ji, queja2 = self.bloqueTipo('ji')
                jf, queja3 = self.bloqueTipo('jf')
                self.tablaTemporadaEquipo(year1, year2, equipo, name, ji, jf)
                return 'Generando archivo de resultados de ' + equipo + ' ' + year1 + '-' + year2 + ' ' + queja1 + queja2 + queja3
            else:
                error = ErrorEntry(1, token.col, token.lexema)
                error.type = 'Sintactico'
                error.type = 'Sintactico'
                error.token = token.token
                error.razon = 'Se Esperaba un equipo'
                self.listaErrores.append(error)
                espacio = '   '
                return token.lexema + '\n' + espacio + '^\nSe Esperaba un equipo'


    def condicionSup(self):
        queja = ''
        token = self.listaTokens[self.i]
        if token.token == 'SUPERIOR':
            self.i += 1
            return 'SUPERIOR', queja
        elif token.token == 'INFERIOR':
            self.i += 1
            return 'INFERIOR', queja
        else:
            error = ErrorEntry(1, token.col, token.lexema)
            error.type = 'Sintactico'
            error.razon = 'Se Esperaba SUPERIOR o INFERIOR'
            error.token = token.token
            self.listaErrores.append(error)
            espacio = '        '
            queja = token.lexema + '\n' + espacio + '^\nSe Esperaba SUPERIOR o INFERIOR'
            return 'SUPERIOR', queja
    def bloqueGuionN(self):
        token = self.listaTokens[self.i]
        n = 5
        if self.i < len(self.listaTokens):
            if token.token == 'GUIONN':
                self.i += 1
                if self.i < len(self.listaTokens):
                    token = self.listaTokens[self.i]
                else:
                    token = self.listaTokens[self.i - 1]
                if token.token == 'INTEGER':
                    n = int(token.lexema)
            return n
        else:
            return n
    def bloqueTOP(self):
        token = self.listaTokens[self.i]
        if token.token == 'TOP':
            n = 5
            self.i += 1
            token = self.listaTokens[self.i]
            condicion, quejaCondicion = self.condicionSup()
            token = self.listaTokens[self.i]
            year1, year2, queja = self.bloqueTemporada()
            if queja != '':
                queja = '\n' + queja
            if quejaCondicion != '':
                quejaCondicion += '\n' + quejaCondicion
            if year1 == '' or year2 == '':
                return 'NO HAY INFORMACION SUFICIENTE'
            n = self.bloqueGuionN()
            print(n)
            return self.topCalculations(year1, year2, n, condicion) + queja + quejaCondicion




    def bloqueAdios(self):
        token = self.listaTokens[self.i]
        exit()



    def analizar(self, listaTokens, listaErrores, listapartidos):
        self.partidos = listapartidos
        self.listaTokens = listaTokens
        self.listaErrores = list(listaErrores)
        print('Inicia Analisis Sintactico')
        answer = self.inicio(None)
        print('La respuesta es')
        print(answer)
        return answer, self.listaErrores

    def buscarresultadosxpartido(self, local, visitante, anioinicio, aniofin):
        print('Inicia Busqueda')
        elocal = local.replace('"', '')
        evisitante = visitante.replace('"', '')
        print(elocal)
        print(evisitante)
        temporada = str(anioinicio) + '-' + str(aniofin)
        print(temporada)
        for partido in self.partidos:
            if partido['local'] == elocal and partido['visitante'] == evisitante and partido['temporada'] == temporada:
                resultado = partido['local'] +' '+ partido['goleslocal' ] +' - ' + partido['golesvisitante'] + partido['visitante']
                print(resultado)
                return resultado
        return 'No existe resultado'

    def buscarXjornada(self, name, jornada, startyear, endyear):
        temporada = str(startyear) + '-' + str(endyear)
        partidosJornada = []
        for partido in self.partidos:
            if partido['jornada'] == jornada and partido['temporada'] == temporada:
                partidosJornada.append(partido)



        #Creamos el archivo HTML
        matchDayGraph(partidosJornada, jornada,name, temporada )
    def contarGoles(self, condicion, equipo, year1, year2):
        temporada = str(year1) + '-' + str(year2)
        goles = 0
        for partido in self.partidos:
            if condicion == 'LOCAL':
                if partido['local'] == equipo:
                    if partido['temporada'] == temporada:
                        goles += int(partido['goleslocal'])
            elif condicion == 'VISITANTE':
                if partido['visitante'] == equipo:
                    if partido['temporada'] == temporada:
                        goles += int(partido['golesvisitante'])
            elif condicion == 'TOTAL':
                if partido['visitante'] == equipo:
                    if partido['temporada'] == temporada:
                        goles+= int(partido['golesvisitante'])
                elif partido['local'] == equipo:
                    if partido['temporada'] == temporada:
                        goles += int(partido['goleslocal'])

        return goles
    def tablaTemporadaEquipo(self, year1, year2, equipo, name, ji, jf):
        numbers = []
        finalmatches = []
        temporada = str(year1) + '-' + str(year2)
        if ji != None and jf != None:
            for i in range(int(ji), int(jf)):
                numbers.append(i)
        elif ji == None and jf != None:
            for i in range(int(jf)):
                numbers.append(i)
        elif ji != None and jf == None:
            for i in range(int(ji), 40):
                numbers.append(i)
        elif ji == None and jf == None:
            for i in range(0, 40):
                numbers.append(i)

        for partido in self.partidos:
            if partido['local'] == equipo and int(partido['jornada']) in numbers and partido['temporada'] == temporada:
                finalmatches.append(partido)
            elif partido['visitante'] == equipo and int(partido['jornada']) in numbers and partido['temporada'] == temporada:
                finalmatches.append(partido)

        seasonStatsGraph(finalmatches, equipo, name, temporada)






    def topCalculations(self, year1, year2, limit, condicion):
        temporada = str(year1) + '-' + str(year2)
        temporadaPartidos = []
        finalstats = []
        teamStats = []
        teamList = []

        for partido in self.partidos:
            if partido['temporada'] == temporada:
                temporadaPartidos.append(partido)
                # Ya tenemos todos lo partidos que se jugaron en esa temporada
            # Ahora necesitamos Calcular los partidos ganados por cada equipo

        # Guardamos los equipos
        for matchDay in temporadaPartidos:
            if matchDay['local'] not in teamList:
                teamList.append(matchDay['local'])

            if matchDay['visitante'] not in teamList:
                teamList.append(matchDay['visitante'])
        # Media vez se tienen guardados los equipos en una lista auxiliar,
        # Podemos recorrer la lista e ir appendeando las stats en otra
        for this in teamList:
            print(this)
        for teamName in teamList:
            teamGoles = 0
            teamVictory = 0
            teamPerdida = 0
            newTeam = Team(teamName)
            for matchDay in temporadaPartidos:
                if matchDay['local'] == teamName:

                    # Si el equipo fue local, pueden existir 3 escenarios
                    if int(matchDay['goleslocal']) > int(matchDay['golesvisitante']):
                        # 1 que gane el local
                        newTeam.goles += int(matchDay['goleslocal'])
                        newTeam.victorias += 1
                        newTeam.puntos += 3

                    elif int(matchDay['goleslocal']) < int(matchDay['golesvisitante']):
                        # 1 que gane el visitante
                        newTeam.goles += int(matchDay['goleslocal'])
                        newTeam.victorias += 1

                    elif int(matchDay['goleslocal']) == int(matchDay['golesvisitante']):
                        # 1 que gane el visitante
                        newTeam.goles += int(matchDay['goleslocal'])
                        newTeam.empates += 1
                        newTeam.puntos += 1


                elif matchDay['visitante'] == teamName:

                    # Si el equipo fue local, pueden existir 3 escenarios
                    if int(matchDay['goleslocal']) < int(matchDay['golesvisitante']):
                        # 1 que gane el local
                        newTeam.goles += int(matchDay['golesvisitante'])
                        newTeam.victorias += 1
                        newTeam.puntos += 3

                    elif int(matchDay['goleslocal']) > int(matchDay['golesvisitante']):
                        # 1 que gane el visitante
                        newTeam.goles += int(matchDay['golesvisitante'])
                        newTeam.perdidas += 1

                    elif int(matchDay['goleslocal']) == int(matchDay['golesvisitante']):
                        # 1 que gane el visitante
                        newTeam.goles += int(matchDay['golesvisitante'])
                        newTeam.empates += 1
                        newTeam.puntos += 1
            # Luego de haber recopilado toda la data sobre el equipo, se le guarda en una lista
            teamStats.append(newTeam)

        # Finalmente, tenemos una lista en la cual esta toda la data asegurada
        # Debemos ordenar los equipos por puntos

        def bubbleSort(arr):
            n = len(arr)

            # Traverse through all array elements
            for i in range(n - 1):
                # range(n) also work but outer loop will
                # repeat one time more than needed.

                # Last i elements are already in place
                for j in range(0, n - i - 1):

                    # traverse the array from 0 to n-i-1
                    # Swap if the element found is greater
                    # than the next element
                    if arr[j].puntos < arr[j + 1].puntos:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]

        bubbleSort(teamStats)
        j = 0
        print('Equipos Finales')
        for team in teamStats:
            print(j, '. ',team.name)
            j += 1
        #Media vez se tiene la lista final con puntos, es posible realizar lo siguiente

        if condicion == 'SUPERIOR':
            finalstats = teamStats[0:limit]

        elif condicion == 'INFERIOR':
            finalstats = teamStats[-limit:]

        text = 'El Top ' + condicion + 'de la temporada ' + temporada + 'fue:\n'
        i = 1
        for stat in finalstats:
            text += str(i) + '. ' + stat.name + '\n'
            i += 1

        return text
        #Now we need to graph FinalStats
        #FUNCIONQUEIMPRIMA

    def tablaTemporada(self, year1, year2, name):
        temporada = str(year1) + '-' + str(year2)
        temporadaPartidos = []
        finalstats = []
        teamStats = []
        teamList = []

        for partido in self.partidos:
            if partido['temporada'] == temporada:
                temporadaPartidos.append(partido)
                #Ya tenemos todos lo partidos que se jugaron en esa temporada
            #Ahora necesitamos Calcular los partidos ganados por cada equipo

        #Guardamos los equipos
        for matchDay in temporadaPartidos:
            if matchDay['local'] not in teamList:
                teamList.append(matchDay['local'])

            if matchDay['visitante'] not in teamList:
                teamList.append(matchDay['local'])
        #Media vez se tienen guardados los equipos en una lista auxiliar,
        #Podemos recorrer la lista e ir appendeando las stats en otra

        for teamName in teamList:
            teamGoles = 0
            teamVictory = 0
            teamPerdida = 0
            newTeam = Team(teamName)
            for matchDay in temporadaPartidos:
                if matchDay['local'] == teamName:

                    #Si el equipo fue local, pueden existir 3 escenarios
                    if int(matchDay['goleslocal']) > int(matchDay['golesvisitante']):
                        #1 que gane el local
                        newTeam.goles += int(matchDay['goleslocal'])
                        newTeam.victorias += 1
                        newTeam.puntos += 3

                    elif int(matchDay['goleslocal']) < int(matchDay['golesvisitante']):
                        #1 que gane el visitante
                        newTeam.goles += int(matchDay['goleslocal'])
                        newTeam.victorias += 1

                    elif int(matchDay['goleslocal']) == int(matchDay['golesvisitante']):
                        #1 que gane el visitante
                        newTeam.goles += int(matchDay['goleslocal'])
                        newTeam.empates += 1
                        newTeam.puntos += 1


                elif matchDay['visitante'] == teamName:

                    # Si el equipo fue local, pueden existir 3 escenarios
                    if int(matchDay['goleslocal']) < int(matchDay['golesvisitante']):
                        # 1 que gane el local
                        newTeam.goles += int(matchDay['golesvisitante'])
                        newTeam.victorias += 1
                        newTeam.puntos += 3

                    elif int(matchDay['goleslocal']) > int(matchDay['golesvisitante']):
                        # 1 que gane el visitante
                        newTeam.goles += int(matchDay['golesvisitante'])
                        newTeam.perdidas += 1

                    elif int(matchDay['goleslocal']) == int(matchDay['golesvisitante']):
                        # 1 que gane el visitante
                        newTeam.goles += int(matchDay['golesvisitante'])
                        newTeam.empates += 1
                        newTeam.puntos += 1
            #Luego de haber recopilado toda la data sobre el equipo, se le guarda en una lista
            teamStats.append(newTeam)

        #Finalmente, tenemos una lista en la cual esta toda la data asegurada
        #Debemos ordenar los equipos por puntos

        def bubbleSort(arr):
            n = len(arr)

            # Traverse through all array elements
            for i in range(n - 1):
                # range(n) also work but outer loop will
                # repeat one time more than needed.

                # Last i elements are already in place
                for j in range(0, n - i - 1):

                    # traverse the array from 0 to n-i-1
                    # Swap if the element found is greater
                    # than the next element
                    if arr[j].puntos < arr[j + 1].puntos:
                        arr[j+1], arr[j] = arr[j], arr[j+1]

        bubbleSort(teamStats)

        seasonGraph(teamStats, name, temporada)

        #Lo podemos graficar con helperes









        #Funcion para crear archivo



