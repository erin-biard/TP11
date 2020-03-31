class Circle:

    def __init__(self,rayon):
        self.__r = rayon

    def getR(self):
        return self.__r

    def __add__(self, r2):
        return Circle(self.__r + r2.__r)

    def __lt__(self, r2):
        return self.__r < r2.__r

    def __gt__(self, r2):
        return self.__r > r2.__r

if __name__== '__main__':
   c1 = Circle(2)
   c2 = Circle(3)
   c3 = c1 + c2
   c4 = c1 < c2
   c5 = c2 > c3
   print(str(c3.getR()))
   print(isinstance(c2,Circle))
   print(c4)
   print(isinstance(c2,Circle))
   print(c5)
   print(isinstance(c2,Circle))
