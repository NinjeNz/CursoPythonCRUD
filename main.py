import sys
from colorama import Fore, init  # Importamos los módulos que ocupamos
from tabulate import tabulate

# Colorama settings
init()  # Es necesario para empezar a colorear
FR = Fore.RESET
FRED = Fore.RED
FGREEN = Fore.GREEN
FGREENX = Fore.LIGHTGREEN_EX
FYE = Fore.YELLOW
FYEX = Fore.LIGHTYELLOW_EX
FCYAN = Fore.CYAN


# clientes = ['Pablo', 'Ricardo'] -- Esto es una lista
clientes = [
    {
        'nombre': 'Abilene',
        'empresa': 'Ruggeri Gelato',
        'email': 'abilene.gaxiola@ruggerigelato.com',
        'puesto': 'Gerente de ventas',
    },
    {
        'nombre': 'David',
        'empresa': 'Ruggeri Gelato',
        'email': 'david.hernandez@ruggerigelato.com',
        'puesto': 'Director',
    },
    {
        'nombre': 'Luis',
        'empresa': 'Ruggeri Gelato',
        'email': 'luis.urias@ruggerigelato.com',
        'puesto': 'Gerente de sistemas',
    }
]


def crear_cliente(client):  # def crear_cliente(nombre_cliente):
    global clientes
    if client not in clientes:
        clientes.append(client)  # clientes += nombre_cliente
        # _add_coma() -- Ya no se necesita desde que la variable clientes paso de ser string a una lista.
    else:
        print('EL cliente ya se encuentra en la lista de clientes')


def actualizar_cliente(nombre_cliente, nombre_cliente_actualizado):
    global clientes
    if nombre_cliente in clientes:
        index = clientes.index(nombre_cliente)
        clientes[index] = nombre_cliente_actualizado
    else:
        print('Cliente no se encuentra en la lista de clientes')


def borrar_cliente(nombre_cliente):
    global clientes
    if nombre_cliente in clientes:
        clientes.remove(nombre_cliente)
    else:
        print('El cliente no se encuentra registrado en la lista de clientes')


def buscar_cliente(nombre_cliente):
    for cliente in clientes:
        if cliente != nombre_cliente:
            continue
        else:
            return True


def lista_clientes():
    """if clientes:
        print('Lista de Clientes :')
        show = []
        for idx, name in enumerate(clientes):
            show.append([idx+1, name])
        print(tabulate(show, headers=['N°', 'Name'], tablefmt='fancy_grid'))
    else:
        print(' No hay clientes registrados')"""

    for idx, cliente in enumerate(clientes):
        print('{uid} | {nombre} | {empresa} | {email} | {puesto}'.format(
            uid=idx,
            nombre=cliente['nombre'],
            empresa=cliente['empresa'],
            email=cliente['email'],
            puesto=cliente['puesto'])
        )


def _print_welcome():
    # print('BIENVENIDO A' + FRED + ' RUGGERI VENTAS' + FR)
    # print('*' * 50)
    # print('Que quieres hacer hoy?')
    print(FYE + '[C]rear Cliente' + FR)
    print(FYE + '[L]ista Clientes' + FR)
    print(FYE + '[E]liminar Cliente' + FR)
    print(FYE + '[A]ctualizara Cliente' + FR)
    print(FYE + '[B]uscar' + FR)
    print(FYE + '[S]alir' + FR)


def _get_client_field(field_name):
    field = None
    while not field:
        field = input('Cual es la/el {} del cliente?'.format(field_name))
    return field


def _get_nombre_cliente():
    nombre_cliente = None
    while not nombre_cliente:
        nombre_cliente = input(
            'Cual es el nombre del cliente?').title().strip()

        if nombre_cliente == 'Exit':
            nombre_cliente = None
            break

    if not nombre_cliente:
        sys.exit()

    return nombre_cliente


if __name__ == '__main__':
    print('BIENVENIDO A' + FRED + ' RUGGERI VENTAS' + FR)
    print('*' * 50)
    print(FCYAN + 'Que quieres hacer hoy?' + FR)

while (True):
    _print_welcome()

    command = input().upper()

    if command == 'C':
        cliente = {
            'nombre': _get_client_field('nombre'),
            'empresa': _get_client_field('empresa'),
            'email': _get_client_field('email'),
            'puesto': _get_client_field('puesto'),
        }
        crear_cliente(cliente)
        lista_clientes()
    elif command == 'L':
        lista_clientes()
    elif command == 'E':
        nombre_cliente = _get_nombre_cliente()
        borrar_cliente(nombre_cliente)
        lista_clientes()
    elif command == 'A':
        nombre_cliente = _get_nombre_cliente()
        nombre_cliente_actualizado = input('Cual es el nuevo nombre?').title()
        actualizar_cliente(nombre_cliente, nombre_cliente_actualizado)
        lista_clientes()
    elif command == 'B':
        nombre_cliente = _get_nombre_cliente()
        found = buscar_cliente(nombre_cliente)

        if found:
            print('El cliente se encuentra registrado en la lista de clientes')
        else:
            print('El cliente {} no se encuentra registrado en la lista de clientes'.format(
                nombre_cliente))

    elif command == 'S':
        print('Hasta la proxima')
        break
    else:
        print('Comando Invalido')
