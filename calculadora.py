#metodo suma
def suma (num1, num2):
    suma = num1 + num2
    return (suma)


#metodo resta
def resta (num1, num2):
    resta = num1 - num2
    return (resta)


#metodo multiplicacion
def multiplicacion (num1, num2):
    multiplicacion = num1 * num2
    return (multiplicacion)


#metodo division
def division (num1, num2):
    division = num1 / num2
    return (division)


#metodo raiz
def raiz (num):
    
    x = 1.0
    
    for k in range (1, 10):
        x = (x + num/x)/2
    
    return (x)

