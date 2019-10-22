import sys
class firts_list:
    """
    El programa et retornar els numeros primers que desitgis.Si el usuari introduiex com a argument un 4 
    el programa et retornara els 4 primers numeros primaris.
    
    >>> firts_list(4)
    [2, 3, 5, 7]
    >>> firts_list(65)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
    103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
    211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313]
  
    """
    
    def __init__(self, n):
        """
        Inicialitzcio de les variables i crida de la funcio search().
        """
        self.n = n
        self.list = []
        self.search()
   

    def search(self):
        """
        Es determinar la llargada de la llista i quins numeros son primers i quins no.
        """
        if (len(self.list) == 0):
            """
            Si la llargada de la llista [list] es 0 afageix el numero 2 en la llista [list] i tornar a crida la funcio search()
            """
            self.list.append(2)
            self.search()
        elif (len(self.list) < self.n):
            """
            Si la llarga de la llista [list] es mes petita que el numero que ha introduit el usuari determinar si el numero es primer i afegeixlo a la llista [list] i si no sumali u al numero que s'esta operant i tornar a cridar la funcio search()
            """
            found = False
            next = self.list[-1]+1
            while not found:
                for i in self.list:
                    if next%i == 0:
                        next += 1
                        found = False
                        break
                    else:
                        found = True
            self.list.append(next)
            self.search()


if __name__ == '__main__':
    """
    Si ejecutes el fitxer [firsts_list.py] com a principal[main] entra.    
    """
    l = firts_list(int(sys.argv[1]))
    print(l.list)
