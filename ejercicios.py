# ejercicio #1
#ingresar sus datos
print("datos del empleado")
nombre=input("ingrese su nombre de usuario: ")
salario=int(input("ingrese su salario: "))
#calculamos la retención del 18%
retencion= 0.18
total_descuento= salario * retencion / 100
print(f"{salario} menos una retención del 18% seria: {total_descuento} ")


#calculamos la bonificacion
bonificacion= 1.13
total_bonificacion= salario * bonificacion
print(f"el total de su bonificación es: {total_bonificacion}")

#salario final
salario_final= salario - retencion + bonificacion
print(f"tu salario total es: {salario_final}")







#ejercicio #2
#pedimos el largo de la cancha
largo=float(input("ingrese el largo de la cancha en metros: "))

#pedimos el ancho de la cancha
ancho=float(input("ingrese el ancho de la cancha en metros: "))

#calculamos el area
area= largo * ancho
ampliacion= 0.2
area_total= (area * ampliacion) + area
print(f"el area total de la cancha con una ampliación del 20% es: {area_total}m²")




#ejercicio #3
#en el primer trimestre aumento:
primer_tri= 1 + 0.095
segundo_tri= primer_tri * (1 - 0.015)
valor_total= primer_tri * segundo_tri

print(f"el valor del desempleo actual es: {valor_total:.2f}%")


#ejercicio #4














