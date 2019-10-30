from multiprocessing import Process
from datetime import datetime
import time

def t(s):
    while(True):
       time.sleep(s)
       print(datetime.now())

       
def main():
    p = Process(target=t, args=(1,))
    p.start()
    
    for i in range(10):
        time.sleep(0.5)
        print(p.pid)

    #p.terminate()
    
    print("Hasta luego lucas")
if __name__ == '__main__':
    main()
   
