import geometricasMatematicas as gc
# 8- Calcular el promedio de cuatro notas entre 0,0 y 5,0.
#Reportar la mayor nota y también reportar la menor.
nota_1 = 5.0
nota_2 = 3.1
nota_3 = 3.8
nota_4 = 4.0
#promedio = (nota_1 + nota_2 + nota_3 + nota_4)/4
#promedio = sum( (nota_1,nota_2,nota_3,nota_4) )/ len((nota_1,nota_2,nota_3,nota_4))
#promedio = gc.promedioNotas(nota_1,nota_2,nota_3,nota_4)
print("El promedio es: ", gc.promedioNotas(nota_1,nota_2,nota_3,nota_4))
print("La mayor nota es:", max( (nota_1,nota_2,nota_3,nota_4) ) )
print("La menor nota es:", min( (nota_1,nota_2,nota_3,nota_4) ) )

