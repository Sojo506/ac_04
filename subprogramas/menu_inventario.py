def lineaSup(largo):
    linea = "   ╔"
    for i in range(1, largo-1):
        linea += "═"
    linea += "╗"
    print(linea)


def lineaMed(largo):
    linea = "   ╠"
    for i in range(1, largo-1):
        linea += "═"
    linea += "╣"
    print(linea)


def lineaInf(largo):
    linea = "   ╚"
    for i in range(1, largo-1):
        linea += "═"
    linea += "╝" + "\n"
    print(linea)


def lineaBlanco(largo):
    linea = "   ║"
    for i in range(1, largo-1):
        linea += " "
    linea += "║"
    print(linea)


def lineaDato(d, largo):
    linea = ""
    linea += "   ║ "
    linea += d
    blancos = largo - len(d)
    for i in range(1, blancos-2):
        linea += " "
    linea += "║"
    print(linea)


def menu_inventario():
    lineaSup(60)
    lineaBlanco(60)
    lineaDato("                 Inventario", 60)
    lineaBlanco(60)
    lineaMed(60)
    lineaBlanco(60)
    lineaDato("01. Ingresar Mercadería", 60)
    lineaDato("02. Egresar Mercadería", 60)
    lineaDato("03. Eliminar Mecardería", 60)
    lineaDato("04. Buscar Mercadería", 60)
    lineaDato("05. Reporte De Mercadería", 60)
    lineaDato("06. Salir", 60)

    lineaBlanco(60)
    lineaInf(60)
