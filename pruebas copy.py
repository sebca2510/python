directorio_proveedores = {}

def get_proveedor(nit):
    return directorio_proveedores.get(nit, None)

def put_proveedor(nit, proveedor):
    directorio_proveedores[nit] = proveedor

def directorio_size():
    return len(directorio_proveedores)

def is_directorio_empty():
    return len(directorio_proveedores) == 0

def get_proveedor_nits():
    return list(directorio_proveedores.keys())

def get_proveedor_list():
    return list(directorio_proveedores.values())

# Ejemplo de uso
proveedor1 = {"nit": "12345", "nombre": "Proveedor 1", "direccion": "Dirección 1", "correo": "proveedor1@example.com"}
proveedor2 = {"nit": "54321", "nombre": "Proveedor 2", "direccion": "Dirección 2", "correo": "proveedor2@example.com"}

put_proveedor(proveedor1["nit"], proveedor1)
put_proveedor(proveedor2["nit"], proveedor2)

print("Tamaño del directorio:", directorio_size())
print("¿El directorio está vacío?", is_directorio_empty())
print("NITs de los proveedores:", get_proveedor_nits())
print("Proveedores:", get_proveedor_list())