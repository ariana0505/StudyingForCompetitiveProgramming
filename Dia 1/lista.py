# Crear una lista
nums = [1, 5, 3]

# Se comienza a contar desde el indice 0 
print(nums[0]) # 1
print(nums[-1]) # es una forma facil de cojer el ultimo elemento

# Modificar
nums[1] = 2
print(nums)  # [1, 2, 3]

# Métodos útiles
nums.append(4)                # Agrega al final → [1, 2, 3, 4]
numero_eliminado = nums.pop() # Saca último (O(1)) → [1, 2, 3]
nums.pop(0)                   # Saca por índice (O(n))
nums.insert(1, 99)            # Inserta en índice → [1, 99, 2, 3]
nums.remove(2)                # Elimina primer 2 encontrado → [1, 99, 3]
nums.sort()                   # Ordena en su lugar (O(n log n))
nums.reverse()                # Invierte → [3, 99, 1]
nums.count(99)                # Cuenta ocurrencias → 1
nums.index(3)                 # Índice de 3 → 2
