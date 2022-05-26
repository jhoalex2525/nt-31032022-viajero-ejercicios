# El valle de aburra afronta altas temperaturas año tras año, Cree una que 
# permita calcular la temperatura media de la tierra partir de recibir 20 
# datos diarios de temperatura.

def calcularTemperaturaMedia(temperaturas):
    tMedia = (max(temperaturas)+min(temperaturas))/2
    return (tMedia)

temperaturas=[20,30,10,15]

print(calcularTemperaturaMedia(temperaturas))