def main():
    #escribe tu código abajo de esta línea
    pesoI = float(input("Dame el peso inicial: "))
    pesoF = float(input("Dame el peso final: "))
    meses = int(input("Dame la cantidad de meses: "))
    bajar = ((pesoI - pesoF)/meses)
    print("Lo que debes bajar por mes es: " + str(bajar))





if __name__ == '__main__':
    main()
