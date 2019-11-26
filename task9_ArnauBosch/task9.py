#-*- coding: utf8 -*-
#4523

# 40 / 2 = 20
# 40 / 4 = 10
from datetime import datetime
from multiprocessing import Pool

def primers(num):
    for i in range(2, int(num/2)):
        if num % i == 0:
            return False
        else:
            pass
    return True

if __name__ == '__main__':

    """
        Es definiran els numeros dels processos segons el rang de numeros amb els que es treballint hi ha dos tipus:

            - Rang de numeros dels CALCULS RAPIDS: entre 0 a 100 mes o menys.

                Quan els numeros son d'un rang més baix, lo que seria més optim seria posar els minims processos perquè aixi no ocupin memoria innecessariament i que no es demorir
                més temps del necessari.

            - Calculs lents apartir de 10.000.000 mes o menys

                Quan els numeros son d'un rang alt, el que seria més optim seria posar els màxims processos possibles i que permetir el teu dispositiu per fer els calculs
                en el menor temps.
    """


    start = datetime.now()
    pool = Pool(processes = 2) #Pool(processes = num_processos)

    l = range(4000000, 4000100)#[45445535, 56534563, 43566487, 43635453, 52346557, 53454433, 43546453, 26847357, 54577647]
    numbers = pool.map(primers, l)
    print (datetime.now() - start)
