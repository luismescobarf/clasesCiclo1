estamosFuncionando = True
while estamosFuncionando:
    print("Todo en orden!")
    aux = input("Desea detenerse? (s)")
    aux = aux.lower()
    if aux == 's':
    #if input("Desea detenerse? (s)").lower() == 's':
        estamosFuncionando = False

