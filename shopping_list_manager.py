compras = ["leche", "harian", "huevos", "aceite", "pasta", "frijoles", "azucar"]

def ver(compras):
    print("Lista de compras:")
    for i, item in enumerate(compras, start=1):
        print(f"{i}. {item}")
        
def agregar(compras):
     
    nuevo = input("Ingresa el objeto: ")
    compras.append(nuevo)
        
    #print("Lista actual:", compras)
    ver(compras)


def quitar(compras):

    eliminar= int(input("Ingresa el numero de posición en la lista: "))-1

    """ eliminarDeLista = compras[eliminar]
    compras.remove(eliminarDeLista) """

    compras.pop(eliminar)
    print(eliminar)
   
    ver(compras)


def ejecutarTodo():
    queQuieres= (input("hola, que deseas hacer, leer la lista(R), añadir(A), o quitar(D)"))

    if queQuieres == "R":
        print ("vamos a leer")
        ver(compras)

    if queQuieres == "A":
        print ("vamos a añadir")
        agregar(compras)

    if queQuieres == "D":
        print ("vamos a quitar")
        quitar(compras)
    
while compras:
    ejecutarTodo()
    

    

