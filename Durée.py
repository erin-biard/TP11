class Duree:

    def __init__(self,heure,minute,seconde):
        self.__H = heure
        self.__M = minute
        self.__S = seconde

    def getH(self):
        return self.__H

    def getM(self):
        return self.__M

    def getS(self):
        return self.__S

    def __str__(self):
        return str(self.__H),"h",str(self.__M),"min",str(self.__S),"s"

    def __add__(self, h2):
        s = self.__S + h2.__S
        min = self.__M + h2.__M + (s//60)
        h = self.__H + h2.__H + (min//60)
        return Duree(h,min%60,s%60)

if __name__== '__main__':
   h1 = Duree(1,42,45)
   h2 = Duree(2,56,21)
   h3 = h1 + h2
   print(h3.getH(),"h",h3.getM(),"min",h3.getS(),"s")
