class Complex :

    def __init__(self,reel,imaginaire):
        self.__r = reel
        self.__i = imaginaire

    def getR(self):
        return self.__r

    def getI(self):
        return self.__i

    def __add__(self, c2):
        return Complex(self.__r + c2.__r , self.__i + c2.__i)

    def __sub__(self, c2):
        return Complex(self.__r - c2.__r , self.__i - c2.__i)

    def __mul__(self, c2):
        return Complex(self.__r * c2.__r , self.__i * c2.__i)

    def __truediv__(self, c2):
        return Complex(self.__r / c2.__r , self.__i / c2.__i)

    def __abs__(self):
        module = ((self.__r**2)+(self.__i**2))**(1/2)
        return module

    def __eq__(self, c2):
        return self.__r == c2.__r and self.__i == c2.__i

    def __ne__(self, c2):
        return self.__r != c2.__r and self.__i != c2.__i

if __name__== '__main__':
   c1 = Complex(1,1)
   c2 = Complex(2,2)
   c3 = c1 + c2
   c4 = c1 - c2
   c5 = c1 * c2
   c6 = c1 / c2
   c7 = c1 == c2
   c8 = c2 != c3
   c9 = abs(c1)
   print(str(c3.getR()),"+ i",str(c3.getI()),)
   print(str(c4.getR()),"+ i",str(c4.getI()))
   print(str(c5.getR()),"+ i",str(c5.getI()))
   print(str(c6.getR()),"+ i",str(c6.getI()))
   print(c7)
   print(c8)
   print(c9)
