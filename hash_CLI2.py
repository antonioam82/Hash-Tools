import hashlib
from colorama import Fore, Back, init
 
class HASH:
    def generateHash(h):
        digest=h.hexdigest()
        return digest
 
init()
algoritmos = list(hashlib.algorithms_guaranteed)
print(len(algoritmos))
 
print(Back.BLUE+"-"*56+"HASH CLI"+"-"*56+Back.RESET)
while True:
    c=1
    print(Back.GREEN+Fore.BLACK+" "*10+"ELIJA NÚMERO DE OPCIÓN"+" "*10+Back.RESET+Fore.GREEN)
    for i in algoritmos:
        print(f"{c}-Generar hash usando algoritmo {i.upper()}")
        c+=1
    print(f"{c}-Finalizar programa")

    try:
        nAlgoritmo = int(input("Introducir opción: "))
 
        if nAlgoritmo > 0 and nAlgoritmo <= len(algoritmos)+1:
 
            if nAlgoritmo != len(algoritmos)+1:
                datos=input("Introducir información a hashear: ")
                algoritmo = algoritmos[nAlgoritmo-1]
                bdatos = bytes(datos, 'utf-8')
                h = hashlib.new(algoritmo,bdatos)
                hash1=HASH.generateHash(h)
                print(Fore.BLUE+f"\nALGORITMO: {algoritmo.upper()}"+Fore.RESET)
                print(Fore.YELLOW+hash1+Fore.RESET+"\n")
            else:
                break
        else:
            print("\n"+Back.RED+Fore.BLACK+"VALOR FUERA DE RANGO."+Fore.RESET+Back.RESET+"\n")
 
    except Exception as e:
        print("\n"+Back.RED+Fore.BLACK+str(e)+Fore.RESET+Back.RESET+"\n")
 
print("PROGRAM FINISHED")
