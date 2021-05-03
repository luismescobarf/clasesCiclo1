import geometricasMatematicas as gc
# 6- Calcular el volumen de un cono.
radio_2 = 5
alto_cono = 9   
#pi = 3.1416
#vol_cilindro = (((pi * radio_2 ** 2) / 3) * alto_cilindro)
vol_cilindro = gc.volumenCono(radio_2,alto_cono)
print(vol_cilindro)