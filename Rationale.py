class Rational:

    def __init__(self,numerateur,denominateur):
        self.__N = numerateur
        self.__D = denominateur

    def getN(self):
        return self.__N

    def getD(self):
        return self.__D

    def __add__(self, f2):
        if self.__D == 0 or f2.__D == 0:
            print("La fraction est impossible")

        else:
            denom = self.__D * f2.__D
            return Rational((self.__N * f2.__D)+(f2.__N * self.__D),denom)

    def __sub__(self, f2):
        if self.__D == 0 or f2.__D == 0:
            print("La fraction est impossible")

        else:
            denom = self.__D * f2.__D
            return Rational((self.__N * f2.__D)-(f2.__N * self.__D),denom)

    def __mul__(self, f2):
        return Rational(self.__N*f2.__N, self.__D*f2.__D)

    def __eq__(self, f2):
        return (self.__N == f2.__N and self.__D == f2.__D) or (self.__N/self.__D == 1 and f2.__N/f2.__D == 1)

if __name__== '__main__':
   f1 = Rational(1,4)
   #print(isinstance(f1,Rational))
   f2 = Rational(2,3)
   #print(isinstance(f2,Rational))
   f3 = f1 + f2
   f4 = f2 - f1
   f5 = f1 * f2
   f6 = f1 == f2
   print("+:",f3.getN(),"/",f3.getD())
   #print(isinstance(f3,Rational))
   print("-:",f4.getN(),"/",f4.getD())
   #print(isinstance(f4,Rational))
   print("*:",f5.getN(),"/",f5.getD())
   #print(isinstance(f5,Rational))
   print(f6)


