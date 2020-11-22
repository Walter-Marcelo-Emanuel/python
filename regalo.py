
import random 

regalos = ['sarten', 'jamon', 'mp4', 'muñeca', 'tv', 'patin', 'balon', 'reloj', 'bicicleta', 'anillo'] 
# regalos   = gift
# muñeca    = doll
# balón     = ball
# bicicleta = bike
# jamón     = ham
# sartén    = skillet
# patín     = roller skate
# anillo    = ring
# reloj     = clock
for sorteo in range(5): regalo = regalos[random.randint(0, 9)] 
print('Sorteo', sorteo + 1, ':', regalos)
# sorteo = draw