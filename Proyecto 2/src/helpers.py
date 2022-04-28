import tkinter
from models.error_entry import ErrorEntry
from models.token import Token
from typing import List, Tuple
from models.element import Element
from os import startfile
from tkinter import filedialog as fd
from datetime import datetime

def process_file(tokens: List[Token], errs: List[ErrorEntry]):
    balance: list[int] = []
    i = 0
    tokenTable = '''
    <!DOCTYPE html>
    <head> <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous"></head>
    <title>Reporte de Productos</title>
    <meta charset="UTF-8">
    <h1><p class="text-center">Reporte de Tokens</p></h1>
    <h2><p class="text-center">Estuardo Sebastian Valle Bances</p></h2>
    <h3><p class="text-center">202001954</p></h3>

        <table class="table table-dark table-striped">
      <thead>
        <tr>
          <th scope="col">ID</th>
          <th scope="col">Token</th>
          <th scope="col">Column</th>
          <th scope="col">Row</th>
          <th scope="col">Tipo</th>
        </tr>
        </thead>
          <tbody>
          '''

    for token in tokens:
        i += 1
        tokenTable += ''' <tr>
                  <th scope="row">''' + str(i) + '''</th>
                  <td>''' + str(token.lexema) + '''</td>
                  <td>''' + str(token.col) + '''</td>
                  <td>''' + str(token.fila) + '''</td>
                  <td>''' + str(token.token) + '''</td>
                </tr>'''

        if i == len(tokens):
            tokenTable += ''' </tbody></table>'''

    errsTable = '''
        <!DOCTYPE html>
        <head> <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous"></head>
        <title>Reporte de Productos</title>
        <meta charset="UTF-8">
        <h1><p class="text-center">Reporte de Errores</p></h1>
        <h2><p class="text-center">Estuardo Sebastian Valle Bances</p></h2>
        <h3><p class="text-center">202001954</p></h3>

            <table class="table table-dark table-striped">
          <thead>
            <tr>
              <th scope="col">ID</th>
              <th scope="col">Error</th>
              <th scope="col">Column</th>
              <th scope="col">Row</th>
            </tr>
            </thead>
              <tbody>
              '''

    for error in errs:
        i += 1
        errsTable += ''' <tr>
                  <th scope="row">''' + str(i) + '''</th>
                  <td>''' + str(error.char) + '''</td>
                  <td>''' + str(error.col) + '''</td>
                  <td>''' + str(error.linea) + '''</td>
                </tr>'''

        if i == len(tokens):
            errsTable += ''' </tbody></table>'''
    return tokenTable, errsTable

def processTokenTable(tokens: List[Token]):
    balance: list[int] = []
    i = 0
    tokenTable = '''
        <!DOCTYPE html>
        <head> <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous"></head>
        <title>Reporte de Productos</title>
        <meta charset="UTF-8">
        <h1><p class="text-center">Reporte de Tokens</p></h1>
        <h2><p class="text-center">Estuardo Sebastian Valle Bances</p></h2>
        <h3><p class="text-center">202001954</p></h3>

            <table class="table table-dark table-striped">
          <thead>
            <tr>
              <th scope="col">ID</th>
              <th scope="col">Token</th>
              <th scope="col">Column</th>
              <th scope="col">Row</th>
              <th scope="col">Tipo</th>
            </tr>
            </thead>
              <tbody>
              '''

    for token in tokens:
        i += 1
        tokenTable += ''' <tr>
                      <th scope="row">''' + str(i) + '''</th>
                      <td>''' + str(token.lexema) + '''</td>
                      <td>''' + str(token.col) + '''</td>
                      <td>''' + str(token.fila) + '''</td>
                      <td>''' + str(token.token) + '''</td>
                    </tr>'''

        if i == len(tokens):
            tokenTable += ''' </tbody></table>'''
    tableTokens = open('ReporteTokens.html', 'w')
    tableTokens.write(tokenTable)
    startfile('ReporteTokens.html')
    tableTokens.close()
    return tokenTable
def matchDayGraph(partidos: list, matchDay, name, temporada):
    i = 0
    tokenTable = '''
            <!DOCTYPE html>
            <head> <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous"></head>
            <title>REPORTE DE JORNADA''' + str(matchDay)+'''</title>
            <meta charset="UTF-8">
            <h1><p class="text-center">Reporte de Jornada ''' + str(matchDay)+'''</p></h1>
            <h2><p class="text-center">La Liga '''+ str(temporada)+'''</p></h2>
            <h3><p class="text-center">Estuardo Sebastian Valle Bances</p></h3>
            <h3><p class="text-center">202001954</p></h3>

                <table class="table table-dark table-striped">
              <thead>
                <tr>
                  <th scope="col">ID</th>
                  <th scope="col">Equipo Local</th>
                  <th scope="col">Goles Equipo Local</th>
                  <th scope="col">Equipo Visitante</th>
                  <th scope="col">Goles Equipo Visitante</th>
                  <th scope="col">Fecha</th>
                </tr>
                </thead>
                  <tbody>
                  '''
    for partido in partidos:
        i += 1
        tokenTable += ''' <tr>
                      <th scope="row">''' + str(i) + '''</th>
                      <td>''' + str(partido['local']) + '''</td>
                      <td>''' + str(partido['goleslocal']) + '''</td>
                      <td>''' + str(partido['visitante']) + '''</td>
                      <td>''' + str(partido['golesvisitante']) + '''</td>
                      <td>''' + str(partido['fecha']) + '''</td>
                    </tr>'''

        if i == len(partidos):
            tokenTable += ''' </tbody></table>'''
    fileName = name + '.html'
    tableMatchDay = open(fileName, 'w')
    tableMatchDay.write(tokenTable)
    startfile(fileName)
    tableMatchDay.close()

def seasonStatsGraph(partidos: list, equipo, name, temporada):
    i = 0
    tokenTable = '''
            <!DOCTYPE html>
            <head> <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous"></head>
            <title>REPORTE DE EQUIPO''' + str(equipo)+'''</title>
            <meta charset="UTF-8">
            <h1><p class="text-center">Reporte de Equipo ''' + str(equipo)+'''</p></h1>
            <h2><p class="text-center">La Liga '''+ str(temporada)+'''</p></h2>
            <h3><p class="text-center">Estuardo Sebastian Valle Bances</p></h3>
            <h3><p class="text-center">202001954</p></h3>

                <table class="table table-dark table-striped">
              <thead>
                <tr>
                  <th scope="col">ID</th>
                  <th scope="col">Local</th>
                  <th scope="col">Goles</th>
                  <th scope="col">Equipo Visitante</th>
                  <th scope="col">Goles Equipo Visitante</th>
                  <th scope="col">Fecha</th>
                  <th scope="col">Jornada</th>
                  
                </tr>
                </thead>
                  <tbody>
                  '''
    for partido in partidos:
        i += 1
        tokenTable += ''' <tr>
                      <th scope="row">''' + str(i) + '''</th>
                      <td>''' + str(partido['local']) + '''</td>
                      <td>''' + str(partido['goleslocal']) + '''</td>
                      <td>''' + str(partido['visitante']) + '''</td>
                      <td>''' + str(partido['golesvisitante']) + '''</td>
                      <td>''' + str(partido['fecha']) + '''</td>
                      <td>''' + str(partido['jornada']) + '''</td>
                    </tr>'''

        if i == len(partidos):
            tokenTable += ''' </tbody></table>'''
    if name == None:
        name = 'partidos'
    fileName = name + '.html'
    tableMatchDay = open(fileName, 'w')
    tableMatchDay.write(tokenTable)
    startfile(fileName)
    tableMatchDay.close()

def seasonGraph(teamStats: list, nombre, temporada):
    i = 0
    tokenTable = '''
            <!DOCTYPE html>
            <head> <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous"></head>
            <title>REPORTE DE TEMPORADA''' + str(temporada)+'''</title>
            <meta charset="UTF-8">
            <h1><p class="text-center">Reporte de Temporada ''' + str(temporada)+'''</p></h1>
            <h2><p class="text-center">La Liga '''+ str(temporada)+'''</p></h2>
            <h3><p class="text-center">Estuardo Sebastian Valle Bances</p></h3>
            <h3><p class="text-center">202001954</p></h3>

                <table class="table table-dark table-striped">
              <thead>
                <tr>
                  <th scope="col">ID</th>
                  <th scope="col">Equipo</th>
                  <th scope="col">Puntos</th>
                  <th scope="col">Goles</th>
                  <th scope="col">Perdidas</th>
                  <th scope="col">Victorias</th>
                  <th scope="col">Empates</th>
                  
                </tr>
                </thead>
                  <tbody>
                  '''
    for team in teamStats:
        i += 1
        tokenTable += ''' <tr>
                      <th scope="row">''' + str(i) + '''</th>
                      <td>''' + str(team.name) + '''</td>
                      <td>''' + str(team.puntos) + '''</td>
                      <td>''' + str(team.goles) + '''</td>
                      <td>''' + str(team.perdidas) + '''</td>
                      <td>''' + str(team.victorias) + '''</td>
                      <td>''' + str(team.empates) + '''</td>
                      </tr>'''

        if i == len(teamStats):
            tokenTable += ''' </tbody></table>'''
    fileName = nombre + '.html'
    tableSeason = open(fileName, 'w')
    tableSeason.write(tokenTable)
    startfile(fileName)
    tableSeason.close()

def processErrsTable(errs: List[ErrorEntry]):
    #Stating the variables
    i = 0

    errsTable = '''
            <!DOCTYPE html>
            <head> <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous"></head>
            <title>Reporte de Productos</title>
            <meta charset="UTF-8">
            <h1><p class="text-center">Reporte de Errores</p></h1>
            <h2><p class="text-center">Estuardo Sebastian Valle Bances</p></h2>
            <h3><p class="text-center">202001954</p></h3>

                <table class="table table-dark table-striped">
              <thead>
                <tr>
                  <th scope="col">ID</th>
                  <th scope="col">Error</th>
                  <th scope="col">Column</th>
                  <th scope="col">Row</th>
                  <th scope="col">Type</th>
                  <th scope="col">Token</th>
                  <th scope="col">Razon</th>
                </tr>
                </thead>
                  <tbody>
                  '''

    for error in errs:
        i += 1
        errsTable += ''' <tr>
                      <th scope="row">''' + str(i) + '''</th>
                      <td>''' + str(error.char) + '''</td>
                      <td>''' + str(error.col) + '''</td>
                      <td>''' + str(error.linea) + '''</td>
                      <td>''' + str(error.type) + '''</td>
                      <td>''' + str(error.token) + '''</td>
                      <td>''' + str(error.razon) + '''</td>
                    </tr>'''

        if i == len(errs):
            errsTable += ''' </tbody></table>'''



    tableErrors = open('ReporteErrores.html', 'w')
    tableErrors.write(errsTable)
    startfile('ReporteErrores.html')
    tableErrors.close()

    pass
def analyzeFile(tokens: List[Token]):
    elements = []
    errores = 0
    estado = 0
    index = 0
    tipos = ['ETIQUETA','TEXTO','GRUPO-RADIO','GRUPO-OPTION','BOTON']
    eventos = ['ENTRADA','INFO']

    while index < len(tokens):
        print(tokens[index].lexema)
        if estado == 0:
            if tokens[index].lexema == '<':
                element = Element()
                #Se debe crear un objeto nuevo
                estado = 1
                index += 1
            else:
                index += 1
        elif estado == 1:
            if tokens[index].lexema.upper() == 'TIPO':
                print(tokens[index + 2].lexema)
                if tokens[index+2].lexema.upper() in tipos:
                    element.tipo = tokens[index+2].lexema.upper()
                    index += 1
                else:
                    print('NO ES NINGUN TIPO')
                    index += 1
                    errores += 1

            elif tokens[index].lexema.upper() == 'VALOR':
                element.valor = tokens[index + 2].lexema.upper()
                index += 1

            elif tokens[index].lexema.upper() == 'FONDO':
                element.fondo = tokens[index + 2].lexema.upper()
                index += 1
            elif tokens[index].lexema.upper() == 'NOMBRE':
                element.nombre = tokens[index + 2].lexema.upper()
                index += 1
            elif tokens[index].lexema.upper() == 'EVENTO':
                if tokens[index+2].lexema.upper() in eventos:
                    element.evento = tokens[index + 2].lexema.upper()
                    index += 1

                else:
                    print('NO ES NINGUN TIPO')
                    index += 1
                    errores += 1
            elif tokens[index].lexema.upper() == 'VALORES':
                estado = 3


            elif tokens[index].lexema == '>':
                elements.append(element)
                newElement = Element()
                element = newElement

                estado = 0
                index += 1

            else:
                index += 1
        elif estado == 3:
            if tokens[index].lexema.upper() == 'VALORES':
                index += 1
            elif tokens[index].lexema.upper() == ':':
                index += 1
            elif tokens[index].lexema == '[':
                element.valores = []
                index += 1
                i = index
                while tokens[i].lexema != ']':
                    if tokens[i].lexema != ',':
                        element.valores.append(tokens[i].lexema)
                        i+=1
                    else:
                        i += 1
                estado = 1

    return elements, errores


def generateForms(elements: List[Element]):
    scripts = '''<script>
                function show() {'''
    generalIFrame = ''
    htmlForms = '''
    <html>
  <head>
    <title>5K & 10K Registration Form</title>
    <link href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700" rel="stylesheet">
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.5.0/css/all.css" integrity="sha384-B4dIYHKNBt8Bc12p+WXckhzcICo0wtJAoU8YZTY5qE0Id1GSseTk6S+L3BlXeVIU" crossorigin="anonymous">
    <style>
      html, body {
      min-height: 100%;
      }
      body, div, form, input, select, textarea, label { 
      padding: 0;
      margin: 0;
      outline: none;
      font-family: Roboto, Arial, sans-serif;
      font-size: 14px;
      color: #666;
      line-height: 22px;
      }
      h1 {
      position: absolute;
      margin: 0;
      font-size: 40px;
      color: #fff;
      z-index: 2;
      line-height: 83px;
      }
      .testbox {
      display: flex;
      justify-content: center;
      align-items: center;
      height: inherit;
      padding: 20px;
      }
      form {
      width: 100%;
      padding: 20px;
      border-radius: 6px;
      background: #fff;
      box-shadow: 0 0 8px  #cc7a00; 
      }
      .banner {
      position: relative;
      height: 300px;
      background-image: url("/uploads/media/default/0001/02/234656e7acbca4625305dd37e7344af8eff32383.jpeg");  
      background-size: cover;
      display: flex;
      justify-content: center;
      align-items: center;
      text-align: center;
      }
      .banner::after {
      content: "";
      background-color: rgba(0, 0, 0, 0.2); 
      position: absolute;
      width: 100%;
      height: 100%;
      }
      input, select, textarea {
      margin-bottom: 10px;
      border: 1px solid #ccc;
      border-radius: 3px;
      }
      input {
      width: calc(100% - 10px);
      padding: 5px;
      }
      input[type="date"] {
      padding: 4px 5px;
      }
      textarea {
      width: calc(100% - 12px);
      padding: 5px;
      }
      .item:hover p, .item:hover i, .question:hover p, .question label:hover, input:hover::placeholder {
      color: #cc7a00;
      }
      .item input:hover, .item select:hover, .item textarea:hover {
      border: 1px solid transparent;
      box-shadow: 0 0 3px 0 #cc7a00;
      color: #cc7a00;
      }
      .item {
      position: relative;
      margin: 10px 0;
      }
      .item span {
      color: red;
      }
      input[type="date"]::-webkit-inner-spin-button {
      display: none;
      }
      .item i, input[type="date"]::-webkit-calendar-picker-indicator {
      position: absolute;
      font-size: 20px;
      color: #cc7a00;
      }
      .item i {
      right: 1%;
      top: 30px;
      z-index: 1;
      }
      [type="date"]::-webkit-calendar-picker-indicator {
      right: 1%;
      z-index: 2;
      opacity: 0;
      cursor: pointer;
      }
      input[type=radio], input[type=checkbox]  {
      display: none;
      }
      label.radio {
      position: relative;
      display: inline-block;
      margin: 5px 20px 15px 0;
      cursor: pointer;
      }
      .question span {
      margin-left: 30px;
      }
      .question-answer label {
      display: block;
      }
      label.radio:before {
      content: "";
      position: absolute;
      left: 0;
      width: 17px;
      height: 17px;
      border-radius: 50%;
      border: 2px solid #ccc;
      }
      input[type=radio]:checked + label:before, label.radio:hover:before {
      border: 2px solid #cc7a00;
      }
      label.radio:after {
      content: "";
      position: absolute;
      top: 6px;
      left: 5px;
      width: 8px;
      height: 4px;
      border: 3px solid #cc7a00;
      border-top: none;
      border-right: none;
      transform: rotate(-45deg);
      opacity: 0;
      }
      input[type=radio]:checked + label:after {
      opacity: 1;
      }
      .btn-block {
      margin-top: 10px;
      text-align: center;
      }
      button {
      width: 150px;
      padding: 10px;
      border: none;
      border-radius: 5px; 
      background: #cc7a00;
      font-size: 16px;
      color: #fff;
      cursor: pointer;
      }
      button:hover {
      background: #ff9800;
      }
      @media (min-width: 568px) {
      .name-item, .city-item {
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      }
      .name-item input, .name-item div {
      width: calc(50% - 20px);
      }
      .name-item div input {
      width:97%;}
      .name-item div label {
      display:block;
      padding-bottom:5px;
      }
      }
    </style>
  </head>
    <body>
    <div class="testbox">
      <form action="/">
        <div class="banner">
          <h1>Formulario</h1>
        </div>
        <p>Inicio Personalizacion</p>

    '''
    for element in elements:
        htmlForms += '''<div class="item">\n'''

        if element.tipo != None:
            if element.tipo.upper() == 'ETIQUETA':
                if element.valor != None:
                    htmlForms += '''\t<label for="'''+str(element.valor)+'''">'''+str(element.valor)+'''<span>*</span></label>\n'''

                else:
                    htmlForms += '''<label for="pred"> Valor Predeterminado <span>*</span></label>'''

            elif element.tipo.upper() == 'TEXTO':
                if element.fondo != None:
                    htmlForms += '''<input id="'''+str(element.valor)+'''" type="text" placeholder="''' +str(element.fondo)+'''"name="name" required/>'''
                    scripts += "let " + str(element.valor) + " = document.getElementById('" + str(element.valor) + "').value;"
                    scripts += "console.log('" + str(element.valor) + "');"
                else:
                    htmlForms += '''<input id="valor" type="text" name="name" required/>'''
                    scripts += "let valor = document.getElementById('valor').value;"
                    scripts += "console.log('valor');"

            elif element.tipo.upper().replace(' ','' ) == 'GRUPO-OPTION':
                htmlForms += '''<div class="item">
                                <select>
                                <option selected value="" disabled selected></option>'''
                if element.valores != None:
                    for option in element.valores:
                        htmlForms += '''<option value="course-type" >'''+str(option)+'''</option>'''

                    htmlForms += '''</select>
                                    </div>'''

            elif element.tipo.upper().replace(' ','' ) == 'GRUPO-RADIO':
                htmlForms += '''<div class="question-answer">'''

                if element.valores != None:
                    for option in element.valores:
                        htmlForms += '''
                        <div>
                        <input type="radio" value="none" id="radio_1" name="'''+str(element.valores[0])+'''"/>
                        <label for="radio_1" class="radio"><span>'''+str(option)+'''</span></label>
                        </div>
                        '''
                    htmlForms += ''' </div>'''
                    scripts += "let " + str(element.valores[0]) + ''' = document.querySelector('input[name="'''+str(element.valores[0])+'''"'''+"]:checked').value;"
                    scripts += "console.log(" + str(element.valores[0])+")"
                else:
                    print("No existen valores para el Grupo-Radio")

            elif element.tipo.upper() == 'BOTON':
                if element.valor != None:
                    htmlForms += '''<div class="btn-block">
                                    <button onclick="show()" type="submit" href="/">'''+str(element.valor)+'''</button>
                                    </div>'''
                else:
                    htmlForms += '''<div class="btn-block">
                                    <button onclick="show()" type="submit" href="/"> Valor Predeterminado</button>
                                    </div>'''

            else:
                print("No contiene ningun tipo predeterminado")
        if element.evento != None:
            #Anadir iFrame con Codigo
            if element.evento.upper() == 'INFO':
                htmlForms += scripts
                htmlForms += "}</script>"
                #1 - Se debe recopilar la data
                #2 - Se debe crear el iFrame
                #3 - Se debe Mostrar el iFrame
                pass
            elif element.evento.upper() == 'ENTRADA':
                htmlForms += '''<iframe src="planeiFrame.html" id="myframe" height="200" width="300" title="Archivo Entrada" style="display: none;"></iframe>'''
                htmlForms += '''
                <script> 
                function show(){
                    var x = document.getElementById("myframe");
                    if (x.style.display === "none") {
                        x.style.display = "block";
                    } else {
                        x.style.display = "none";
                        }
                    }
                </script> 
                '''

            pass
    htmlForms += '''  </form>
            </div>
            </body>
            </html>'''

    file = open('Frame.html','w')
    file.write(htmlForms)
    file.close()
    startfile('Frame.html')


def processCSV():
    
    filename = fd.askopenfilename(title="Select file", filetypes=(("CSV", "*.csv"), ("All", "*.txt")))
    filereader = open(filename, 'r+', encoding='utf-8')
    current_file = filereader.read()
    # Debemos iniciar la lectura del archivo que se indicó
    def leerArchivo(ruta):
        file = open(ruta, 'r')
        contenido = file.read()
        return contenido

    ligainfo = leerArchivo(filename)
    partidos = ligainfo.split('\n')
    objPartidos = []
    for partido in partidos:
        datos = partido.split(',')
        p = {
            'fecha': datos[0],
            'temporada': datos[1],
            'jornada': datos[2],
            'local': datos[3],
            'visitante': datos[4],
            'goleslocal': datos[5],
            'golesvisitante': datos[6],
        }
        objPartidos.append(p)
    return True, objPartidos





