# -*- coding: utf8 -*-
import md5, random, sys, time
import pipes
from multiprocessing import Process, Semaphore, Pipe
import time
def busca(x, s):
    s.acquire()
    f = open('fitxer.txt', 'r')
    fr = f.read()
    index = fr.find('\n'+x+',')
    index2 = fr.find('\n', index+1)
    if index == -1:
        pass
    else:
        print fr[index+1:index2]
        f.close()
    s.release()

def substitueix(x, y, s):
    s.acquire()
    f = open('fitxer.txt', 'r')
    fr = f.read()
    f.close()
    index = fr.find('\n'+x+',')
    index2 = fr.find('\n', index+1)
    if index == -1:
        print 'Aquest nombre no existeix'
        s.release()
    else:
        print fr[index+1:index2]
        f = open('fitxer.txt', 'w')
        f.write(fr[:index+1])
        f.write(y + ',' + md5.md5(y).hexdigest()+ "\n")
        f.write(fr[index2+1:])
        f.close()
        s.release()
        busca(y, s)

def fill(f,s):
    while True:
        x = f.recv()
        if x == 'q':
            break

        y = f.recv()
        if y == 'q':
            break
        substitueix(str(x),str(y),s)


def inici():
    f = open('fitxer.txt', 'w')
    for i in range(100):
        f.write(str(i)+ ',' + md5.md5(str(i)).hexdigest()+ "\n")
    f.close()


    #print open('fitxer.txt', 'ro').read()



if __name__ == '__main__' :


    i,f = Pipe()
    s = Semaphore()

    p = Process(target=fill, args=(f,s))

    inici()
    p.start()

    while True:
        x = raw_input("Introdueix el numero que vols substituir\n")

        i.send(x)

        if x == 'q':
            break

        y = raw_input("Introdueix per quin vols substituir\n")

        i.send(y)

        if y == 'q' :
            break

        time.sleep(1)



    p.join()
