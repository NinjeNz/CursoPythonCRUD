from colorama import Fore, init  # Importamos los módulos que ocupamos

# Colorama settings
init()  # Es necesario para empezar a colorear
FR = Fore.RESET
FRED = Fore.RED
FGREEN = Fore.GREEN
FGREENX = Fore.LIGHTGREEN_EX
FYE = Fore.YELLOW
FYEX = Fore.LIGHTYELLOW_EX
FCYAN = Fore.CYAN


clientes = 'Pablo,Ricardo,'


def crear_cliente(nombre_cliente):
    global clientes
    if nombre_cliente not in clientes:
        clientes += nombre_cliente
        _add_coma()
    else:
        print('EL cliente ya se encuentra en la lista de clientes')


def actualizar_cliente(nombre_cliente, nombre_cliente_actualizado):
    global clientes
    if nombre_cliente in clientes:
        clientes = clientes.replace(
            nombre_cliente + ',', nombre_cliente_actualizado + ',')
    else:
        print('Cliente no se encuentra en la lista de clientes')


def lista_clientes():
    global clientes
    print(clientes)


def _add_coma():
    global clientes
    clientes += ','


def _print_welcome():
    # print('BIENVENIDO A' + FRED + ' RUGGERI VENTAS' + FR)
    # print('*' * 50)
    # print('Que quieres hacer hoy?')
    print(FYE + '[C]rear Cliente' + FR)
    print(FYE + '[B]orrar Cliente' + FR)
    print(FYE + '[A]ctualizara Cliente' + FR)
    print(FYE + '[S]alir' + FR)


def _get_nombre_cliente():
    return input('Cual es el nombre del cliente?').title()


if __name__ == '__main__':
    print('BIENVENIDO A' + FRED + ' RUGGERI VENTAS' + FR)
    print('*' * 50)
    print(FCYAN + 'Que quieres hacer hoy?' + FR)

while (True):
    _print_welcome()

    command = input().upper()

    if command == 'C':
        nombre_cliente = _get_nombre_cliente()
        crear_cliente(nombre_cliente)
        lista_clientes()
    elif command == 'B':
        pass
    elif command == 'A':
        nombre_cliente = _get_nombre_cliente()
        nombre_cliente_actualizado = input('Cual es el nuevo nombre?').title()
        actualizar_cliente(nombre_cliente, nombre_cliente_actualizado)
        lista_clientes()
    elif command == 'S':
        print('Hasta la proxima')
        break
    else:
        print('Comando Invalido')
