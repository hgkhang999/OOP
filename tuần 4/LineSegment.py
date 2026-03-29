import math

class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def getX(self):
        return self.__x
    def setX(self, x):
        self.__x = x

    def getY(self):
        return self.__y
    def setY(self, y):
        self.__y = y


class LineSegment:
    def __init__(self, d1=None, d2=None, x1=None, y1=None, x2=None, y2=None, S=None):
        if S != None:
            self.__d1 = Point(S.getD1().getX(), S.getD1().getY())
            self.__d2 = Point(S.getD2().getX(), S.getD2().getY())

        elif x1 != None and y1 != None and x2 != None and y2 != None:
            self.__d1 = Point(x1, y1)
            self.__d2 = Point(x2, y2)

        elif d1 != None and d2 != None:
            self.__d1 = d1
            self.__d2 = d2

        else:
            self.__d1 = Point(8, 5)
            self.__d2 = Point(1, 0)

    def getD1(self):
        return self.__d1
    def setD1(self, d1):
        self.__d1 = d1

    def getD2(self):
        return self.__d2
    def setD2(self, d2):
        self.__d2 = d2

    def inTTin(self):
        print("Diem dau d1: (" + str(self.__d1.getX()) + ", " + str(self.__d1.getY()) + ")")
        print("Diem dau d2: (" + str(self.__d2.getX()) + ", " + str(self.__d2.getY()) + ")")


ls1 = LineSegment()
print("Mac dinh:")
ls1.inTTin()

print("---")
p1 = Point(3, 4)
p2 = Point(7, 9)
ls2 = LineSegment(d1=p1, d2=p2)
print("Truyen 2 Point:")
ls2.inTTin()

print("---")
ls3 = LineSegment(x1=1, y1=2, x2=5, y2=6)
print("Truyen 4 so nguyen:")
ls3.inTTin()

print("---")
ls4 = LineSegment(S=ls3)
print("Sao chep tu ls3:")
ls4.inTTin()