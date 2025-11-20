aprendices = []
edades = []

cantidad = int(input(" ¿cuantos apprendices deseas ingresar?: "))
for i in range(cantidad): 
    nombre = input(f"ingrese el nombre de los aprendices {i+1}: ")
    edad = int(input(f"ingrese la edad de  {nombre}: "))
    aprendices.append(nombre)
    edades.append(edad)
  
    
print("aprendices", aprendices)
print("edades", edades)
 
mayor_edad = max(edades)
print(mayor_edad)

posicion_mayor = edades.index(mayor_edad)
print(f"el aprendiz con mayor edad es: {aprendices[posicion_mayor]}")

instru=input("ingrese el nombre del instructor: ")
aprendices.insert(1, instru)
print(aprendices)

misma_edad= edades.count(18)
print(f"los aprendices que tienen 18 son: {misma_edad}")

instru=input("ingrese el nombre del instructor: ")
aprendices.insert(1, instru)
print(aprendices)

nuevo_aprendiz= input("ingrese el nombre del nuevo aprendiz: ")
aprendices.append(nuevo_aprendiz)
print(aprendices)

aprendices.remove(instru)
print(aprendices)

elemento=input("Digite el aprendiz a buscar: ")
if elemento in aprendices:
    print(f"{elemento} el se encuentra en la lista")
else:
    print(f"{elemento} el no se encuentra en la lista")


print(aprendices[:10])
print(aprendices[-10:])
print(aprendices[9:20])

for e in (edades):
    if e % 2 == 0:
        print(e)

