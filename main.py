def stringtonat(cadena):
  """
  La funcion stringtonat tiene como objetivo convertir una 
  cadena de texto en un número entero.
  """
  suma = 0
  caracter = 0
  ABC = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
  cadenaMayus = cadena.upper()
  for i in cadenaMayus:
    #Si i es mayuscula devolver el lugar que ocupa en el abecedario.
    #Si es un numero, devolver dicho numero trasformado a entero.
    if i in ABC: #si es una letra en mayuscula
      caracter = ABC.index(i)+1

    else:
      caracter = int(i)

    suma += caracter*(37**cadenaMayus.index(i))
  return suma

def hashResto(k,m):
  """
  La fucnión hashResto es la encargada de transformar un codigo en un índice
  para que se pueda almacenar en la tabla hash.
  """
  return k % m


class Node:
  def __init__(self, key = None, element = None, cantidad = None, next = None):
    self.key = key
    self.element = element
    self.next = next
    self.cantidad = cantidad

class HashTable:
    def __init__(self, capacity, hashFunction):
      self.m = capacity
      self.h = hashFunction
      self.T = [None] * self.m

    #--------Estadisticas------------

    def __len__(self):
        #La función mágica __len__ se encarga de devolver la longitud de la tabla.
        length = 0
        for i in range(0,len(self.T)):
          
          if self.T[i] != None:
            length += 1
            head = self.T[i]

            #si la tabla tiene un encadenamiento en ese índice, recorrerlo e
            #ir sumando 1 a length por cada elemento encontrado hasta que el
            #next del ultimo elemento sea None.
            if head.next != None:
               while head.next != None:
                  length += 1
                  head = head.next

        return length
    
    def lista_mas_larga(self):
      """
      La función lista_mas_larga busca entre las distintas listas encadenadas
      que se forman a lo largo de la tabla y devuelve el índice de la que posea más
      elementos o, en el caso de que las que tienen más elementos sean dos,
      devuelve la primera en aparecer (la que tiene un índice más bajo).

      Las listas se guardan en un diccionario en donde sus claves son sus índices,
      y sus valores son sus longitudes o la cantidad de elementos que contienen.
      """
      listas={}

      for i in range(0,len(self.T)):
         length = 0

         if self.T[i] != None:
            length += 1 #Sumo el primer elemento.
            
            if self.T[i].next != None:
              #Si este elemento tiene un elemento enlazado, procedo a recorrerlo.
              head = self.T[i]

              while head.next != None:
                #Mientras el atributo next del elemento no sea None, sigo recorriendo.
                #Cuando sea None (cuando no hayan más elementos), termina el bucle.
                length += 1
                head = head.next

            #Esta línea agrega la longitud total de dicho índice al diccionario.
            listas[i] = length

      if listas: #Compruebo que la lista posea elementos.

        #En esta línea, la función max pide la clave del diccionario que posea
        #un valor mayor.
        clave_maxima = max(listas, key=listas.get)
      
        #Para obtener la longitud de la lista más grande, solo tengo que llamar al
        #diccionario pasándole como clave a la clave_maxima.
        return f"La lista con mayor longitud es la del indice: {clave_maxima}\nSu longitud es de: {listas[clave_maxima]}"
      
      else: #Si la lista no existe.
         return "lista vacia"
    
    def factorDeCarga(self):
      """
      La función factorDeCarga realiza una cuenta sencilla: toma la cantidad de
      elementos en existencia y lo divide por la capacidad total de la tabla
      hash, buscando obtener un número entre 0,6 y 0,75 que nos índique la buena
      performance de nuestra tabla.
      """
      elementos = float(len(self))
      capacidad = float(self.m)
      factor_carga = elementos/capacidad
      return factor_carga
    
    
    #--------METODOS------------
    
    def __str__(self):
      """
      La función __str__ es un método mágico que nos permite imprimir nuestra
      tabla.
      """
      return str(self.T)

    def insert(self, key, element, cantidad):
      """
      El método insert nos permite añadir productos a nuestros inventarios,
      almacenando su código, el nombre del producto y la cantidad que se posee.
      El código del producto no puede ni menor ni mayor a 10 dígitos, y esto
      está restringido a la hora de pedir al usuario que ingrese dicho código.

      Se tomará el código ingresado (alfanumérico) y se lo transformará a mayúsculas.
      """
      #Transformo el código a mayúsculas
      keyMayus = key.upper()


      node = Node(keyMayus, element, cantidad)
      index = self.h(stringtonat(key), self.m) #convierto el codigo a numero
      
      node.next = self.T[index] #establece como next el objeto dentro de el indice index
      self.T[index] = node #se incorpora al elemento node dentro del indice index, de forma que
      #su nodo siguiente es el que anteriormente se encontraba en dicha posicion
      

    def search(self, key):
      """
      El método search recibe un código y lo busca en nuestra tabla Hash. Si el
      código está en nuestra tabla, se devuelve su información (código que lo
      identifica, nombre y cantidad). De lo contrario, se devolverá un mensaje
      informando su ausencia en los inventarios.
      """
      index = self.h(stringtonat(key), self.m)
      exist = "El producto no se encuentra en inventario."
      actual = self.T[index] 
      cantidad = 0
      codigo = None

      while actual != None:
        #El bucle busca en aquellos índices en los que hayan elementos.

        if actual.key == key.upper():
          #Si el código del elemento en el que me encuentro es igual al código
          #del elemento que estoy buscando, devolver la información del elemento
          #(pues es el elemento buscado).

          codigo = actual.key
          cantidad = actual.cantidad
          exist = f"""
          Codigo: {codigo}
          Producto: {actual.element}
          Cantidad: {cantidad}"""
          
        actual = actual.next #actualizo la variable para que continúe el búcle.
    
      return exist
    
    def delete(self,key):
      """
      El método delete pide un código y elimina el elemento al que le pertenece
      dicho código.
      """
      index = self.h(stringtonat(key), self.m)
      nodo_actual = self.T[index]

      if nodo_actual is not None and nodo_actual.key == key:
          #Si el elemento actual existe y su código es igual al buscado...
          #elimino dicha lista enlazada.
          self.T[index] = nodo_actual.next
          return

      #De lo contrario...
      while nodo_actual is not None:
          #Recorro la lista enlazada, y si encuentro uno que coincida el bucle termina.
          if nodo_actual.key == key:
              break

          #actualizo el bucle.
          nodo_anterior = nodo_actual
          nodo_actual = nodo_actual.next

      #Si el elemento en el que estoy es None, se llegó al final de la lsita, termina la función.
      if nodo_actual is None:
          return

      #Si se encuentra el nodo a eliminar, se elimina el nodo:
      nodo_anterior.next = nodo_actual.next

def menu() -> None:
    print("1. Add new item")
    print("2. Query item")
    print("3. Delete item")
    print("4. Stats")
    print("5. Exit")
    print()

hashTable = HashTable(65609,hashResto)

if __name__ == "__main__":
    while True:
        menu()
        choice = input("Enter choice: ")

        if choice == '1':
            producto = input("Que producto desea agregar?: ")

            while True: #bucle que verifica que el codigo tenga 10 digitos
              codigo = input(f"Inserte el codigo del producto {producto}: ")
              if len(codigo) == 10:
                break
              else:
                print("El codigo debe tener 10 digitos.\n")
            
            while True:
              cantidad = input("Inserte la cantidad del producto a ingresar: ")
              if cantidad.isdigit() == False:
                print("Inserte una cantidad valida.")
              else:
                break


            hashTable.insert(codigo,producto, cantidad)
        
        elif choice == '2':

            codigo = input("Inserte el codigo del producto que busca: ")

            while True:
              if len(codigo) == 10:
                break
                
              else:
                print("Inserte un codigo valido.\n")
                codigo = input("Inserte el codigo del producto que busca: ")

            print(hashTable.search(codigo))
            print("""
            ### 
            Si desea agregar cantidades al producto, por favor
            eliminelo e ingreselo como un producto nuevo.
            ###""")
            
        elif choice == '3':
            codigo = input("Inserte el codigo del producto que desea eliminar: ")
            hashTable.delete(codigo)
            
        elif choice == '4':
            print(f"Elementos de la tabla\nCantidad: {len(hashTable)}")
            print("\nLista mas larga:")
            
            print(hashTable.lista_mas_larga())

            print(f"\nRendimiento de factor de carga de la tabla hash\nRendimiento: {hashTable.factorDeCarga()}")
            pass
        elif choice == '5':
            break
        else:
            print("Invalid choice")
        print()
