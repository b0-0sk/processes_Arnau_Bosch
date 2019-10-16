import sys
import pdb; pdb.set_trace();

class firts_list:
    def __init__(self, n):
        self.n = n
        self.list = []
        self.search()

    def search(self):
        if (len(self.list) == 0):
            self.list.append(2)
            self.search()
        elif (len(self.list) < self.n):
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
    l = firts_list(int(sys.argv[1]))
    print l.list
