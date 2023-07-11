from colorama import Fore, init #Importamos los módulos que ocupamos 

#Colorama settings
init() #Es necesario para empezar a colorear
FR = Fore.RESET
FRED = Fore.RED
FGREEN = Fore.GREEN
FGREENX = Fore.LIGHTGREEN_EX
FYE = Fore.YELLOW
FYEX = Fore.LIGHTYELLOW_EX
FCYAN = Fore.CYAN

clientes = 'pablo,ricardo,'


def crear_cliente(nombre_cliente):
    global clientes
    if nombre_cliente not in clientes:
        clientes += nombre_cliente
        _add_coma()
    else:
        print('EL cliente ya se encuentra en la lista de clientes')


def lista_clientes():
    global clientes
    print(clientes)


def _add_coma():
    global clientes
    clientes += ','


def _print_welcome():
    print('BIENVENIDO A' + FRED + ' RUGGERI VENTAS' + FR)
    print('*' * 50)
    print('Que quieres hacer hoy?')
    print('[C]rear Cliente')
    print('[B]orrar Cliente')
    print('[S]alir')

if __name__ == '__main__':
   
 while (True):
    _print_welcome()

    command = input()

    if command == 'C':
        nombre_cliente = input('Cual es el nombre del cliente?')
        crear_cliente(nombre_cliente)
        lista_clientes()
    elif command == 'B':
        pass
    elif command == 'S':
        print('Hasta la proxima')
        break;
    else:
        print('Comando Invalido')
