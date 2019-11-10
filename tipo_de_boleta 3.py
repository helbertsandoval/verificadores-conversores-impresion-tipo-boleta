#INPUT
costo_fijo=float(input("ingrese el costo fijo:"))
produccion=float(input("ingrese la produccion:"))

# PROCESSING
costo_fijo_medio=(costo_fijo/produccion)

# OUTPUT
print("###############################################")
print("# CALCULAR EL COSTO FIJO MEDIO")
print("###############################################")
print("#")
print("# costo fijo        :  ",        costo_fijo)
print("# produccion        :  ",        produccion)
print("# costo fijo medio  :  ",  costo_fijo_medio)
print("###############################################")
