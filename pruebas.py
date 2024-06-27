def crear_nodo(identificador, nombre, jefe):
    return {'identificador': identificador, 'nombre': nombre, 'jefe': jefe, 'izquierdo': None, 'derecho': None}

def mostrar_ramas(nodo):
    print(f"Identificador: {nodo['identificador']}, Nombre: {nodo['nombre']}, Jefe: {nodo['jefe']}")
    if nodo['izquierdo']:
        mostrar_ramas(nodo['izquierdo'])
    if nodo['derecho']:
        mostrar_ramas(nodo['derecho'])

def mostrar_raiz(raiz):
    print(f"Identificador: {raiz['identificador']}, Nombre: {raiz['nombre']}, Jefe: {raiz['jefe']}")

def mostrar_ultimos_nodos(nodo):
    if not nodo['izquierdo'] and not nodo['derecho']:
        print(f"Identificador: {nodo['identificador']}, Nombre: {nodo['nombre']}, Jefe: {nodo['jefe']}")
    if nodo['izquierdo']:
        mostrar_ultimos_nodos(nodo['izquierdo'])
    if nodo['derecho']:
        mostrar_ultimos_nodos(nodo['derecho'])

# Crear el árbol de ejemplo
raiz = crear_nodo(1, "CEO", "Ninguno")
raiz['izquierdo'] = crear_nodo(2, "Gerente General", "CEO")
raiz['izquierdo']['izquierdo'] = crear_nodo(3, "Gerente de Ventas", "Gerente General")
raiz['izquierdo']['derecho'] = crear_nodo(4, "Gerente de Marketing", "Gerente General")
raiz['derecho'] = crear_nodo(5, "Gerente de Producción", "Gerente General")
raiz['derecho']['izquierdo'] = crear_nodo(6, "Supervisor de Ventas", "Gerente de Ventas")
raiz['derecho']['izquierdo']['izquierdo'] = crear_nodo(9, "Vendedor 1", "Supervisor de Ventas")
raiz['derecho']['derecho'] = crear_nodo(7, "Supervisor de Marketing", "Gerente de Marketing")
raiz['derecho']['derecho']['izquierdo'] = crear_nodo(10, "Marketero 1", "Supervisor de Marketing")
raiz['derecho']['derecho']['derecho'] = crear_nodo(11, "Marketero 2", "Supervisor de Marketing")
raiz['derecho']['derecho']['izquierdo']['izquierdo'] = crear_nodo(12, "Marketero 3", "Marketero 1")
raiz['derecho']['derecho']['izquierdo']['derecho'] = crear_nodo(13, "Marketero 4", "Marketero 1")
raiz['derecho']['derecho']['derecho']['izquierdo'] = crear_nodo(14, "Marketero 5", "Marketero 2")
raiz['derecho']['derecho']['derecho']['derecho'] = crear_nodo(15, "Marketero 6", "Marketero 2")

# Mostrar las ramas del árbol
print("Ramas del árbol:")
mostrar_ramas(raiz)

# Mostrar la raíz del árbol
print("\nRaíz del árbol:")
mostrar_raiz(raiz)

# Mostrar los últimos nodos del árbol
print("\nÚltimos nodos del árbol:")
mostrar_ultimos_nodos(raiz)