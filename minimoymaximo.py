# Crea una función  que reciba una lista con valores numéricos y devuelva
# el valor máximo y el mínimo ingresados

def ObtenerMinimoMaximo(numeros):
    minimo = min(numeros)
    maximo = max(numeros)
    resultado ={minimo,maximo}
    return (resultado)

numeros=[20,30,10,15]

print(ObtenerMinimoMaximo(numeros))