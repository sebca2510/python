def identificador(identificador, nombre, jefe):
    return{'identificador': identificador,'nombre': nombre, 'jefe': jefe, 'izquierdo': None, 'derecho': None}

def ramas (nodo):
    print(f"identificador: ", {nodo['identificador']}, "Nombre: ", {nodo['nombre']}, "jefe: ", {nodo['jefe']})
    if nodo['izquierdo']:
        ramas(nodo['izquierdo'])
    if nodo['derecho']:
        ramas(nodo['derecho'])

def mostrar_raiz(raiz):
    print(f"Identificador: {raiz['identificador']}, Nombre: {raiz['nombre']}, Jefe: {raiz['jefe']}")

def ultimos_nodos(nodo):
    if not nodo['izquierdo'] and not nodo['derecho']:
        print(f"Identificador: {nodo['identificador']}, Nombre: {nodo['nombre']}, Jefe: {nodo['jefe']}")
    if nodo['izquierdo']:
        ultimos_nodos(nodo['izquierdo'])
    if nodo['derecho']:
       ultimos_nodos(nodo['derecho'])

raiz = identificador(1, "CEO", "Ninguno")
raiz['izquierdo'] = identificador(2, "Gerente General", "CEO")
raiz['izquierdo']['izquierdo'] = identificador(3, "Gerente de Ventas", "Gerente General")
raiz['izquierdo']['derecho'] = identificador(4, "Gerente de Marketing", "Gerente General")
raiz['derecho'] = identificador(5, "Gerente de Producción", "Gerente General")
raiz['derecho']['izquierdo'] = identificador(6, "Supervisor de Ventas", "Gerente de Ventas")
raiz['derecho']['izquierdo']['izquierdo'] = identificador(9, "Vendedor 1", "Supervisor de Ventas")
raiz['derecho']['derecho'] = identificador(7, "Supervisor de Marketing", "Gerente de Marketing")
raiz['derecho']['derecho']['izquierdo'] = identificador(10, "Marketero 1", "Supervisor de Marketing")
raiz['derecho']['derecho']['derecho'] = identificador(11, "Marketero 2", "Supervisor de Marketing")
raiz['derecho']['derecho']['izquierdo']['izquierdo'] = identificador(12, "Marketero 3", "Marketero 1")
raiz['derecho']['derecho']['izquierdo']['derecho'] = identificador(13, "Marketero 4", "Marketero 1")
raiz['derecho']['derecho']['derecho']['izquierdo'] = identificador(14, "Marketero 5", "Marketero 2")
raiz['derecho']['derecho']['derecho']['derecho'] = identificador(15, "Marketero 6", "Marketero 2")     

print("las ramas son: ")
ramas(raiz)

print("\nLa raíz es: ")
mostrar_raiz(raiz)

print("\nLos ultimos nodos son: ")
ultimos_nodos(raiz)