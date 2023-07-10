

clientes = 'pablo,ricardo,'


def crear_cliente(nombre_cliente):
    global clientes
    clientes += nombre_cliente
    _add_coma()


def lista_clientes():
    global clientes
    print(clientes)


def _add_coma():
    global clientes
    clientes += ','


def _print_welcome():
    print('BIENVENIDO A RUGGERI VENTAS')
    print('*' * 50)
    print('Que quieres hacer hoy?')
    print('[C]rear Cliente')
    print('[B]orrar Cliente')


if __name__ == '__main__':
    _print_welcome()

    command = input()

    if command == 'C':
        nombre_cliente = input('Cual es el nombre del cliente?')
        crear_cliente(nombre_cliente)
        lista_clientes()
    elif command == 'B':
        pass
    else:
        print('Comando Invalido')
