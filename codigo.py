def partida_ajedrez(nombre_fichero):
    tablero_inicial = '♜\t♞\t♝\t♛\t♚\t♝\t♞\t♜\n♟\t♟\t♟\t♟\t♟\t♟\t♟\t♟\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n♙\t♙\t♙\t♙\t♙\t♙\t♙\t♙\n♖\t♘\t♗\t♕\t♔\t♗\t♘\t♖'
    print(tablero_inicial)
    tablero = []
    for i in tablero_inicial.split('\n'):
        tablero.append(i.split('\t'))
    print(tablero)
    f = open(nombre_fichero, 'w')
    for i in tablero:
        f.write('\t'.join(i) + '\n')
        f.close()
    return tablero

movimiento = 0
while True:
    continuar = input('¿Desea continuar? (s/n): ')
    if continuar == 's':
        movimiento += 1
        print('Movimiento', movimiento)
        partida_ajedrez('tablero.txt')