def stringtonat(cadena):
  suma = 0
  caracter = 0
  ABC = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
  for i in cadena:
    if i in ABC:#si es una letra en mayuscula
      caracter = ABC.index(i)+1

    else: #si es un numero
      #devolver el mismo num
      caracter = int(i)

    suma += caracter*(37**cadena.index(i)) #36 es la base del conjunto de caracteres
  return suma

def hashResto(k,m):
  return k % m

def hashMultiplicacion(k,m):
  return int(k*0.5-int(k*0.5))

class Node:
  def __init__(self, key = None, element = None, next = None):
    self.key = key
    self.element = element
    self.next = next

class HashTable:
    def __init__(self, capacity, hashFunction):
      self.m = capacity
      self.h = hashFunction
      self.T = [None] * self.m
    
    def __str__(self):
      return str(self.T)
    
    def insert(self, key, element):
      node = Node(key, element)
      index = self.h(stringtonat(key), self.m) #convierto el codigo a numero
      node.next = self.T[index]
      self.T[index] = node
    
    def search(self, key):
      index = self.h(stringtonat(key), self.m)
      actual = self.T[index]
      exist = False

      while actual != None:
        if actual.key == key:
          exist = actual.element
        actual = actual.next
      
      return exist
    
    def delete(self,key):
      index = self.h(stringtonat(key), self.m)
      
      nodo_actual = self.T[index]
      if nodo_actual is not None and nodo_actual.key == key:
          self.T[index] = nodo_actual.next
          return

      while nodo_actual is not None:
          if nodo_actual.key == key:
              break
          nodo_anterior = nodo_actual
          nodo_actual = nodo_actual.next

      if nodo_actual is None:
          return

      nodo_anterior.next = nodo_actual.next

def menu() -> None:
    print("1. Add new item")
    print("2. Query item")
    print("3. Delete item")
    print("4. Stats")
    print("5. Exit")
    print()

hashTable = HashTable(1,hashResto)
if __name__ == "__main__":
    while True:
        menu()
        choice = int(input("Enter choice: "))
        if choice == 1:
            producto = input("Que producto desea agregar?: ")
            codigo = input(f"Inserte el codigo del producto {producto}: ")
            print("\nEl producto que busca es:")
            hashTable.insert(codigo,producto)
        
        elif choice == 2:
            codigo = input("Inserte el codigo del producto que busca: ")
            print(hashTable.search(codigo))
            
        elif choice == 3:
            codigo = input("Inserte el codigo del producto que desea eliminar: ")
            hashTable.delete(codigo)
            
        elif choice == 4:
            pass
        elif choice == 5:
            break
        else:
            print("Invalid choice")
        print()

