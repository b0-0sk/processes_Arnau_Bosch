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
      Es definiren els números dels processos segons el rang de números amb els quals és treballant hi hauria dos tipus [Explicació objectiva]:

        - Rang de números dels Càlculs Ràpids: entre 0 a 100 més o menys.

            Quan els números són d'un rang més baix, el que seria més òptim seria posar els mínims processos perquè així no ocupin memòria innecessàriament i que no és demorar
            més temps del necessari.

        - Càlculs lents a partir de 10.000.000 més o menys

            Quan els números són d'un rang alt, el que seria més òptim seria posar els màxims processos possibles i que permeti el teu dispositiu per fer els càlculs en el menor temps.
    """


    start = datetime.now()
    pool = Pool(processes = 2) #Pool(processes = num_processos)

    l = range(4000000, 4000100)#[45445535, 56534563, 43566487, 43635453, 52346557, 53454433, 43546453, 26847357, 54577647]
    numbers = pool.map(primers, l)
    print (datetime.now() - start)
