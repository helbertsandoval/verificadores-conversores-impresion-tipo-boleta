#INPUT
velocidad_final=float(input("ingrese la velocidad final:"))
velocidaad_inicial=float(input("ingrese la velocidad inicial:"))
tiempo=float(input("ingrese el tiempo:"))

# PROCESSING
aceleracion=(velocidad_final-velocidaad_inicial)/tiempo

# OUTPUT
print("#######################################################")
print("# CALCULAR LA ACELERACION")
print("#######################################################")
print("#")
print("# velocidad final   :  m/s  ",     velocidad_final)
print("# velocidad inicial :  m/S  ",  velocidaad_inicial)
print("# tiempo            :   s   ",              tiempo)
print("# aceleracion       :  s^2  ",         aceleracion)
print("#######################################################")
