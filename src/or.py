#   Para a porta OU - (OR)
import random
import numpy as np


#   OR
#   1 - entradas 0 e 0 - saída 0
#   2 - entradas 0 e 1 - saída 1
#   3 - entradas 1 e 0 - saída 1
#   4 - entradas 1 e 1 - saída 1


def rna(entrada1, entrada2):
    global y
    bias = -1
    w0 = round(random.uniform(-1.0, 1.0), 1)
    w1 = round(random.uniform(-1.0, 1.0), 1)
    w2 = round(random.uniform(-1.0, 1.0), 1)
    n_epochs = 100
    n = 0.1
    i = 0
    aux = []

    while i < n_epochs:
        net = ft([bias, entrada1, entrada2], [w0, w1, w2])
        aux.append(net)

        if net > 0:
            y = 1
        else:
            y = 0
        print("época " + str(i + 1) + " = " + str(net) + " y = " + str(y))

        if ver(entrada1, entrada2, y) == 0:
            w0 = w0 + n * (vc(entrada1, entrada2) - y) * bias
            w1 = w1 + n * (vc(entrada1, entrada2) - y) * entrada1
            w1 = w1 + n * (vc(entrada1, entrada2) - y) * entrada2
        if i > 2:
            if aux[i] == aux[i - 2]:
                i = n_epochs
        i += 1

    print('y = ' + str(y))
    return w0, w1, w2


#   Função retorna o valor do produto escalar entre as entradas e os pesos.
def ft(a, b):
    #   a = [bias, entrada1, entrada2]
    #   b = [w0, w1, w2]
    return np.dot(a, b)


#   Função retorna se o valor de entrada é verdadeiro ou não.
def ver(entrada1, entrada2, y_re):
    if entrada1 == 0 and entrada2 == 0:
        if y_re == 0:
            return 1
    if entrada1 == 0 and entrada2 == 1:
        if y_re == 1:
            return 1
    if entrada1 == 1 and entrada2 == 0:
        if y_re == 1:
            return 1
    if entrada1 == 1 and entrada2 == 1:
        if y_re == 1:
            return 1
    else:
        return 0


#   Função retorna o valor esperado para a porta lógica.
def vc(entrada1, entrada2):
    if entrada1 == 1 or entrada2 == 1:
        return 1
    else:
        return 0


x1 = input("Entre com o valor de x1:")
x2 = input("Entre com o valor de x2:")
rna(int(x1), int(x2))
