#ejercicio #4
#pedimos el largo y an de el terreno para calcular el area 
largo=float(input("ingrese el largo de el terreno: "))
ancho=float(input("ingrese el ancho de el terreno: "))
area= largo*ancho
reduccion=0.1
#el area reducida se calcula sacando el porcentae y restandole al area total inicial
area_total_reducida= area - (area * reduccion)
adicion=0.5
#al area reducida se le multiplica el porcentaje de la adicion 
area_definitiva= (area_total_reducida * adicion) + area_total_reducida
print(f"el area total del terreno con una reduccion del 10% y una adicion del 50% es: {area_definitiva} ")



#ejercicio #5
#pedimos la cantidad de minutos  
minutos=float(input("ingrese cantidad de minutos"))
#dividimos la cantidad de minutos ingresados por 60
hora = float(minutos / 60)
print(f"{minutos} = a {hora} horas")




#ejercicio #6
#pedimos la cantidad de horas  
horas=float(input("ingrese cantidad de horas"))
#multiplicamos la cantidad de horas ingresados por 60
minutos = float(horas * 60)
print(f"{horas} = a {minutos} minutos")
  



#ejercicio #7
#se hace la operación 
quintales=float(input("ingrese la cantidad de quintales: "))
kilogramos= quintales * 100
print(f"{quintales} quintales equivalen a {kilogramos} kilogramos")
  



#ejercicio #8
#tarifas de los operadores
tarifa_por_min_operador1= 150
tarifa_por_min_operador2= 200
#duración de las llamdas
llamada1_operador1= float(input("cuantos minutos duro la primer llamada al operador 1? "))
llamada2_operador1= float(input ("cuantos minutos duro la segunda llamada al operador 2? "))
 

llamda1_operador2= float(input("cuantos minutos duro la primer llamada al operador 2? "))
llamda2_operador2= float(input("cuantos minutos duro la segunda llamada al operador 2? "))

#se calcula el costo por minuto de cada llamada

costo1 = tarifa_por_min_operador1 * llamada1_operador1
costo2 = tarifa_por_min_operador1 * llamada2_operador1
costo3 = tarifa_por_min_operador2 * llamda1_operador2
costo4 = tarifa_por_min_operador2 * llamda2_operador2

#costos totales de las llamadas

total_operador1 = costo1 + costo2
total_operador2 = costo3 + costo4
total_general= total_operador1 + total_operador2

print(f"las llamadas del operador 1 tuvieron un costo de: {total_operador1}, las llamadas del operador 2 tuvieron un costo de: {total_operador2} y el totatl de las 4 llamdas es de: {total_general}")


#ejercicio #9
paredes = int(input("Cuántos muros tiene el baño? "))
# i equivale a la cantidad de muros
i = 1
area_total = 0

#se realiza el blucle
while i <= paredes:
    print(f"Muro {i}:")
    alto = float(input("Alto: "))
    ancho = float(input("Ancho: "))
    area_total = area_total + (alto * ancho)
    i = i + 1  

print(f"Área total: {area_total:.2f} m²")

#definimos cuanta area cubre una caja de baldosas
area_por_caja = 3.5
baldosas_necesarias = area_total / area_por_caja

print(f"Cada caja de baldosas cubre: {area_por_caja} m² se necesitan {baldosas_necesarias:.2f} baldosas")

#ejercicio #10
#se calcula el tiempo y la disntacia
tiempo_dia1=float(input("cuantos minutos duro el entrenamiento? ")) 
distancia_dia1=float(input("cual fue la distancia recorridea durante el entreanmiento en metros? "))

tiempo_dia2=float(input("cuantos minutos duro el entrenamiento? ")) 
distancia_dia2=float(input("cual fue la distancia recorridea durante el entreanmiento en metros? "))

tiempo_dia3=float(input("cuantos minutos duro el entrenamiento? ")) 
distancia_dia3=float(input("cual fue la distancia recorridea durante el entreanmiento en metros? "))

#se sacan los totales

total_final_tiempo = tiempo_dia1 + tiempo_dia2 + tiempo_dia3
total_final_disntacia = distancia_dia1 + distancia_dia2 + distancia_dia3

promedio=total_final_disntacia / total_final_tiempo

print(f"en la semana entrenaste {total_final_tiempo} minutos y recorriste {total_final_disntacia} metros. Tu promedio semanal fue: {promedio} m/min")



#ejercicio #11
herencia=float(input("ingrese el valor de la herencia: "))
#el enunciado tiene valores incorrectos porque al sumar los porcentajes da mas del 100%
esposa= 0.40
hijo1=0.30
hijo2=0.20
hijo3=0.40
hijo4=0.10
total_esposa= herencia * esposa
total_hijo1= herencia * hijo1
total_hijo2= herencia * hijo2
total_hijo3= herencia * hijo3
total_hijo4= herencia * hijo4
print(f"a cada cada persona le corresponde: \n esposa: {total_esposa} \n hijo 1: {total_hijo1}\n hijo 2: {total_hijo2}\n hijo 3:{total_hijo3}\n hijo 4: {total_hijo4}")



#ejercicio #13
area_total_lote=float(input("ingrese el area total del lote:  "))

area_cultivos= area_total_lote * 0.40
area_vivienda= area_total_lote * 0.25
area_zonas_verdes = area_total_lote * 0.15

#al area total del lote se le resta la suma de las areas anteriores

area_disponible= area_total_lote - (area_cultivos + area_vivienda + area_zonas_verdes)
print(f"el area disponible para cultivos es de: {area_cultivos} m² \n el area disponible para vivienda es: {area_vivienda} m² \n el area disponible para zonas verdes es de: {area_zonas_verdes} m² ")
print(f"el area disponible para otros proyectos es: {area_disponible}")


#ejercicio #14
 
taller1 = float(input("Ingrese la nota del Taller 1: "))
taller2 = float(input("Ingrese la nota del Taller 2: "))

#promedio de los talleres
nota_1 = (taller1 + taller2) / 2

evaluacion1 = float(input("Ingrese la nota de la Evaluación 1: "))
evaluacion2 = float(input("Ingrese la nota de la Evaluación 2: "))
evaluacion3 = float(input("Ingrese la nota de la Evaluación 3: "))

#promedio de evaluaciones
nota_2 = (evaluacion1 + evaluacion2 + evaluacion3) / 3

nota_3 = float(input("Ingrese la nota del trabajo final: "))

quiz1 = float(input("Ingrese la nota del Quiz 1: "))
quiz2 = float(input("Ingrese la nota del Quiz 2: "))
quiz3 = float(input("Ingrese la nota del Quiz 3: "))
quiz4 = float(input("Ingrese la nota del Quiz 4: "))

nota_4 = (quiz1 + quiz2 + quiz3 + quiz4) / 4

#se calcula el porcentaje de las notas
ponderacion_1 = nota_1 * 0.15
ponderacion_2 = nota_2 * 0.30
ponderacion_3 = nota_3 * 0.30
ponderacion_4 = nota_4 * 0.25

nota_definitiva = ponderacion_1 + ponderacion_2 + ponderacion_3 + ponderacion_4

print(f"la nota definitiva es: {nota_definitiva:.1f}")






#ejercicio #15
#asignaos el valor del pasaje
valor_pasaje= 3000
inicio_dia=int(input("ingrese el número de la registradora al iniciar el día: "))
final_dia=int(input("ingresa el número de la registradora al finalizar el día: "))
num_pasajeros_dia= final_dia  - inicio_dia

total_pasaje_dia= num_pasajeros_dia * valor_pasaje

#las 3/4 partes de la empresa corresponden al 0.75% del total del pasaje recolectado en el dia

total_pasaje_empresa= total_pasaje_dia * 0.75
total_pasaje_conductor= total_pasaje_dia - total_pasaje_empresa

print(f"el total de pasajeros del dia fue: {num_pasajeros_dia} \n el valor liquidado al conductor fue de { total_pasaje_conductor}\n el valor liquidado a la empresa fue: {total_pasaje_empresa}")