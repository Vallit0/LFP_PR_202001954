from models.inventario import Inventario
from models.product import Product
from models.instruction import Instruction
from models.inventario import Inventario
from typing import List, Tuple
import matplotlib.pyplot as pl
import string

def instructionsSort(instructions:list[Instruction]) -> Tuple[Instruction]:
    keywords = [
        'NOMBRE', 'GRAFICA', 'TITULOX', 'TITULOY', 'TITULO'
    ]
    orderedInstructions: list = ['','','','','']
    for instruction in instructions:
        print(instruction.instruction)
        #Instruccion Comando
        if instruction.instruction == 'NOMBRE':
            orderedInstructions[0] = instruction
            check1 = True
        elif instruction.instruction == 'GRAFICA':
            orderedInstructions[1] = instruction
            check2 = True
        elif instruction.instruction == 'TITULOX':
            orderedInstructions[2] = instruction
            check3 = True
        elif instruction.instruction == 'TITULOY':
            check4 = True
            orderedInstructions[3] = instruction
        elif instruction.instruction == 'TITULO':
            check5 = True
            orderedInstructions[4] = instruction
        else:
            print("Existe un Error en los datos de entrada")
    return tuple(orderedInstructions)

def sortProducts(products: list[Product]):
        n = len(products)
        productsList = []
        for product in products:
            productsList.append(product)

        for i in range(n - 1):
            for j in range(0, n - i - 1):

                if productsList[j].balance < productsList[j + 1].balance:
                    productsList[j], productsList[j + 1] = productsList[j + 1], productsList[j]

        return productsList

def addlabels(x,y):
    for i in range(len(x)):
        pl.text(i, y[i], y[i], ha = 'center')
def graphBuilder(instructions: list[Instruction], products: list[Product], Inventario) -> None:
    #Vaciado de Productos en listas
    balance: list[int] = []
    productNames: list = []
    nombre: str
    tituloX: str = ''
    tituloY: str = ''
    titulo: str = ''
    nombre = instructions[0].command


    if instructions[2] != '':
        if instructions[2].command != None:
            tituloX = str(instructions[2].command)
    if instructions[3] != '':
        if instructions[3].command != None:
            tituloY = str(instructions[3].command)
    if instructions[4] != '':
        if instructions[4].command != None:
            titulo = str(instructions[4].command)
    else:
        titulo = 'Reporte de Ventas '+ str(Inventario.year)+ ' '+str(Inventario.month)



    for product in products:
        balance.append((float(product.price)*int(product.units)))
        productNames.append(str(product.name))


    if instructions[1].command == 'BARRAS':
        fig = pl.figure()
        pl.bar(productNames, balance)
        print(tituloX)
        print(tituloY)
        pl.xlabel(tituloX, fontweight='bold', color='blue', fontsize='15',
                   horizontalalignment='center')
        pl.ylabel(tituloY, fontweight='bold', color='blue', fontsize='15',
                  horizontalalignment='center')
        pl.suptitle(titulo)
        ax = pl.subplot()
        fig.suptitle(titulo, fontsize=16)
        pl.setp(ax.get_xticklabels(), rotation=40, ha='right')
        nombre += '.png'
        pl.savefig(nombre)
        pl.show()


        pass
    elif instructions[1].command == 'LINEAS':
        fig = pl.figure()

        pl.plot(productNames, balance)
        pl.xlabel(tituloX, fontweight='bold', color='blue', fontsize='15',
                  horizontalalignment='center')
        pl.ylabel(tituloY, fontweight='bold', color='blue', fontsize='15',
                  horizontalalignment='center')

        pl.suptitle(titulo)
        fig.suptitle(titulo, fontsize=16)
        nombre += '.png'
        pl.savefig(nombre)
        pl.show()

        pass
    elif instructions[1].command == 'PIE':
        #Getting the percentages in the list
        percentages = []
        for product in balance:
            percentages.append((product/sum(balance))*100)
        #explode = (0, 0.1, 0, 0)

        fig1, ax1 = pl.subplots()
        ax1.pie(percentages, labels=productNames, autopct='%1.1f%%',
                shadow=True, startangle=90)
        pl.xlabel(tituloX, fontweight='bold', color='blue', fontsize='15',
                  horizontalalignment='center')
        pl.ylabel(tituloY, fontweight='bold', color='blue', fontsize='15',
                  horizontalalignment='center')
        ax1.axis('equal')
        fig1.suptitle(titulo, fontsize=16)
        nombre += '.png'
        pl.savefig(nombre)
        pl.show()

        pass

def reportGenerator(products: list[Product]):
    balance: list[int] = []
    i = 0
    table = '''
<!DOCTYPE html>
<head> <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous"></head>
<title>Reporte de Productos</title>
<meta charset="UTF-8">
<h1><p class="text-center">Analisis de Productos</p></h1>
<h2><p class="text-center">Estuardo Sebastian Valle Bances</p></h2>
<h3><p class="text-center">202001954</p></h3>


    
    <table class="table table-dark table-striped">
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">Product</th>
      <th scope="col">Units</th>
      <th scope="col">Price</th>
      <th scope="col">Balance</th>
    </tr>
    </thead>
      <tbody>
      '''

    for product in products:
        i += 1
        balance.append((float(product.price) * int(product.units)))
        table += ''' <tr>
              <th scope="row">''' + str(i) + '''</th>
              <td>''' + str(product.name) + '''</td>
              <td>''' + str(product.units) + '''</td>
              <td>''' + str(product.price) + '''</td>
              <td>''' + str(round((float(product.price) * int(product.units)), 2))+ '''</td>
            </tr>'''

        if i == len(products):
            table += ''' </tbody></table>'''
    table+='''
    <table class="table">
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">Product</th>
      <th scope="col">Units</th>
      <th scope="col">Price</th>
      <th scope="col">Balance</th>
    </tr>
    </thead>
      <tbody>'''
    table += '''<tbody><div class="alert alert-success" role="alert">Productos con Mayores y Menores Ventas</div>'''
    table += ''' <tr class="table-success">
              <th scope="row">''' + str(1) + '''</th>
              <td>''' + str(products[0].name) + '''</td>
              <td>''' + str(products[0].units) + '''</td>
              <td>''' + str(products[0].price) + '''</td>
              <td>''' + str(round(float(products[0].price) * int(products[0].units), 2))+ '''</td>
            </tr>'''
    table += ''' <tr class="table-danger">
                  <th scope="row">''' + str(2) + '''</th>
                  <td>''' + str(products[-1].name) + '''</td>
                  <td>''' + str(products[-1].units) + '''</td>
                  <td>''' + str(products[-1].price) + '''</td>
                  <td >''' + str(round(float(products[-1].price) * int(products[-1].units), 2)) + '''</td>
                </tr>'''
    table += ''' </tbody></table>'''


    return table






