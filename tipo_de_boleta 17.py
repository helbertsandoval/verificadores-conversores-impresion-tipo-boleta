#INPUT
masa=float(input("ingrese la masa:"))
altura=float(input("ingrese la altura:"))
gravedad=float(input("ingrese la gravedad:"))

# PROCESSING
energia_potencial_gravitatoria=(masa*altura*gravedad)

# OUTPUT
print("#########################################################################")
print("# CALCULAR LA ENERGIA POTENCIAL GRAVITATORIA")
print("#########################################################################")
print("#")
print("# masa                           : ",                           masa)
print("# altura                         : ",                          altura)
print("# gravedad                       : ",                        gravedad)
print("# energia potencial gravitatoria : ",  energia_potencial_gravitatoria)
print("#########################################################################")
