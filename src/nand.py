#   Para a porta E' - (NAND)
import random
import numpy as np
import matplotlib.pyplot as plt


#   NAND
#   1 - entradas 0 e 0 - saída 1
#   2 - entradas 0 e 1 - saída 1
#   3 - entradas 1 e 0 - saída 1
#   4 - entradas 1 e 1 - saída 0


def rna(entrada1, entrada2):
    global y
    bias = -1
    w0 = round(random.uniform(-1.0, 1.0), 1)
    w1 = round(random.uniform(-1.0, 1.0), 1)
    w2 = round(random.uniform(-1.0, 1.0), 1)
    n_epochs = 100
    n = 0.01
    i = 0
    aux = []

    while i < n_epochs:
        net = ft([bias, entrada1, entrada2], [w0, w1, w2])
        aux.append(net)

        if net > 0:
            y = 1
        else:
            y = 0
#        print("época " + str(i + 1) + " = " + str(net) + " y = " + str(y))

        if ver(entrada1, entrada2, y) == 0:
            w0 = w0 + n * (vc(entrada1, entrada2) - y) * bias
            w1 = w1 + n * (vc(entrada1, entrada2) - y) * entrada1
            w1 = w1 + n * (vc(entrada1, entrada2) - y) * entrada2
#        if i > 2:
#            if aux[i] == aux[i - 2]:
#                i = n_epochs
        i += 1

#    print('y = ' + str(y))
    return y, vc(entrada1, entrada2)


#   Função retorna o valor do produto escalar entre as entradas e os pesos.
def ft(a, b):
    #   a = [bias, entrada1, entrada2]
    #   b = [w0, w1, w2]
    return np.dot(a, b)


#   Função retorna se o valor de entrada é verdadeiro ou não.
def ver(entrada1, entrada2, y_re):
    if entrada1 == 0 and entrada2 == 0:
        if y_re == 1:
            return 1
    if entrada1 == 0 and entrada2 == 1:
        if y_re == 1:
            return 1
    if entrada1 == 1 and entrada2 == 0:
        if y_re == 1:
            return 1
    if entrada1 == 1 and entrada2 == 1:
        if y_re == 0:
            return 1
    else:
        return 0


#   Função retorna o valor esperado para a porta lógica.
def vc(entrada1, entrada2):
    if entrada1 == 0 or entrada2 == 0:
        return 1
    else:
        return 0


y_obtido = []
y_esperado = []
n_y_cer = 0
n_y_err = 0
repeat = 100
for i in range(0, repeat):
    x1 = random.randint(0, 1)
    x2 = random.randint(0, 1)
    y_ob, y_es = rna(x1, x2)
    y_obtido.append(y_ob)
    y_esperado.append(y_es)
    if y_ob == y_es:
        n_y_cer += 1
    else:
        n_y_err += 1


space = np.arange(0, repeat, 1)

plt.scatter(space, y_esperado, label='Valores esperados', color='r', marker='.')
plt.scatter(space, y_obtido, label='Valores obtidos', color='b', marker='.')
plt.title('Repetições do RNA - Para a porta NAND')
plt.xlabel("Taxa de certos: " + str((n_y_cer / repeat) * 100) + '%')
plt.legend()
plt.show()
