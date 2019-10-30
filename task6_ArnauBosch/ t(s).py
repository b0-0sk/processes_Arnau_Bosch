from multiprocessing import Process, Value
from datetime import datetime
import time

a=Value('i',3)

def t(s):
    while(True):
       time.sleep(s)
       print(datetime.now())
       print a.value
       
       
       
def main():
    p = Process(target=t, args=(1,))
    p.start()
    
    for i in range(10):
        time.sleep(0.5)
        print(p.pid)
        a.value=a.value+1

    p.terminate()
    
    print("Hasta luego lucas")
if __name__ == '__main__':
    main()
   
