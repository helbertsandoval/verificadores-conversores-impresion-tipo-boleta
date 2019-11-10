#INPUT
velocidad_inicial=float(input("ingrese la velocidad inicial:"))
aceleracion=float(input("ingrese la aceleracion:"))
tiempo=float(input("ingrese el tiempo:"))

# PROCESSING
velocidad_final=(velocidad_inicial+aceleracion*tiempo)

# OUTPUT
print("###################################################")
print("# CALCULAR LA VELOCIDAD FINAL")
print("###################################################")
print("#")
print("# velocidad inicial  : ",  velocidad_inicial)
print("# aceleracion        : ",        aceleracion)
print("# tiempo             : ",             tiempo)
print("# velocidad final    : ",    velocidad_final)
print("###################################################")
