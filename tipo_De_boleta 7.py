#INPUT
variacion_del_costo_total=float(input("ingrese la variacion del costo total:"))
variacion_de_la_produccion=float(input("ingrese la variacion de la produccion:"))

# PROCESSING
costo_marginal=(variacion_del_costo_total/variacion_de_la_produccion)

# OUTPUT
print("#####################################################################")
print("# CALCULAR EL COSTO MARGINAL")
print("#####################################################################")
print("#")
print("# variacion del costo total  :  ",    variacion_del_costo_total)
print("# variacion de la produccion :  ",   variacion_de_la_produccion)
print("# costo marginal             :  ",               costo_marginal)
print("#####################################################################")
