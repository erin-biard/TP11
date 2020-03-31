class Matrice:

    def __init__(self,data=[]):
        self.__D = data

    def getD(self):
        return self.__D

    def __add__(self, m2):
        for i in range(0,4):
            newMat = self.__D[i] + m2.__D[i]
            print(newMat,end=' ')

    def __sub__(self, m2):
        for i in range(0,4):
            newMat = self.__D[i] - m2.__D[i]
            print(newMat,end=' ')

    def __mul__(self, m2):
        m = []
        if len(self.__D[0]) != len(m2.__D):
            return False
        for i in range (len(self.__D)):
            ligne = []
            for j in range(len(m2.__D[0])): #pour chaque colonne de m2
                for k in range (len(self.__D[0])):
                    element = self.__D[i][j] * m2.__D[i][j]
                    element += self.__D[i][k] * m2.__D[k][i]
            ligne.append(element)
            m.append(ligne)
        return m

if __name__== '__main__':
   data1 = [1,2,3,2]
   data2 = [1,0,2,1]
   m1 = Matrice(data1)
   m2 = Matrice(data2)
   m3 = m1 + m2
   print(" ")
   m4 = m1 - m2
   m5 = m1*m2
