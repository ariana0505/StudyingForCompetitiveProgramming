# Crear diccionario
persona = {"nombre": "Ana", "edad": 25, "ciudad": "Lima"}
# nombre = {key: value, key: value, key: value}

# Acceder
print(persona["nombre"])       # Ana
print(persona.get("edad"))     # 25
print(persona.get("altura", "No existe"))  # valor por defecto

# Modificar
persona["edad"] = 26
persona["pais"] = "Perú"       # agrega nueva clave
print(persona)

# Métodos útiles
print(persona.keys())    # dict_keys(['nombre', 'edad', 'ciudad', 'pais'])
print(persona.values())  # dict_values(['Ana', 26, 'Lima', 'Perú'])
print(persona.items())   # dict_items([('nombre','Ana'),('edad',26)...])
persona.pop("ciudad")    # elimina la clave 'ciudad'
print(persona.popitem()) # elimina el ultimo elemento que fue insertado