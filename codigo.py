def partida_ajedrez(nombre_fichero):
    fichero = open(nombre_fichero, 'r')
    partida = fichero.read()
    fichero.close()
    return partida