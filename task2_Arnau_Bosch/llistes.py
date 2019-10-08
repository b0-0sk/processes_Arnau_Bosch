
import random
def llistes_rand():
    novaLlista = []
    for x in range(10):
        novaLlista.append(random.randint(1,100))
    return novaLlista


def llistes_rand2():
    novaLlista = []
    for x in range(100):
        novaLlista.append(random.randint(1,100))
    return novaLlista

prova1 = llistes_rand()
print(prova1)
print(prova1[-1])
prova2 =  llistes_rand2()
print(prova2)
print(prova2[-1])
