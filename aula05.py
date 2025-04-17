peso=float(input("digite seu peso:"))
altura=float(input("digite sua altura:"))
repetir="s"
formula= peso/altura**2
while repetir == "s":
    if formula < 18.6:
        print("voce esta abaixo do seu peso:")
    elif  formula >= 18.6 and formula >=24.9:
        print("voce esta no seu peso ideal")
    elif formula >= 25.0 and 29.9:
        print("voce esta levemente acima do peso")
    elif formula >= 30.0 and 34.9:
        print("voce esta com obesidade grau 1")
    elif formula >= 35.0 and 39.9:
        print("muito cuidado voce esta com obsesidade grau 2")
    elif formula >=40:
        print("voce esta em obesidade grau 3")
else:
    print("voce esta muito acima de seu peso")
repetir= input("deseja verificar outro numero")