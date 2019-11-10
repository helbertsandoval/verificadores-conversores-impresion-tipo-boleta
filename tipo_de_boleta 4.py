#INPUT
costo_variable=float(input("ingrese el costo variable:"))
produccion=float(input("inggrese la produccion:"))

# PROCESSING
costo_variable_medio=(costo_variable/produccion)

# OUTPUT
print("###########################################################")
print("# CALCULAR EL COSTO VARIABLE MEDIO")
print("###########################################################")
print("#")
print("# costo variable        :   ",        costo_variable)
print("# produccion            :   ",           produccion)
print("# costo variable medio  :   ",  costo_variable_medio)
print("###########################################################")
