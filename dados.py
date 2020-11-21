#_*_ coding: UTF-8_*_

seguir= True
while seguir:
    import random
    dado1= random.randint(1,6)
    dado2=random.randint(1,6)
    puntos=(dado1+dado2)
    print("dado 1:",dado1)
    print("dado 2:",dado2)
    print("dsuman ambos", puntos)
    seguir= ("s" ==input("¿volveer a tirar? Si o No")).lower()
    