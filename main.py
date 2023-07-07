

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


if __name__ == '__main__':
    lista_clientes()

    crear_cliente('Luis')
   
    lista_clientes()