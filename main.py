#DECLARANDO LA FUNCION EN PYTHON
# Los parametros en los parentesis son locales, solo existen para la función
# si no llegan valores en los parametros, por ejemplo por una respuesta erronea en BD 
# puedo poner un valor por defecto
def sumar(numero1=0,numero2=5):
    suma = numero1 + numero2
    return(suma)

#LLAMANDO LA FUNCION EN PYTHON, la llamada de la funcion es en la zona global
numero1 = 30
numero2 = 50
print (sumar(numero1,numero2))