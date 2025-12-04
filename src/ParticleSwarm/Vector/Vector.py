floatType = float

class Vector2D:

    x = 0
    y = 0

    def __init__(self, X: floatType, Y: floatType):
        self.x = X
        self.y = Y

    def getX(self) -> floatType:
        return self.x

    def setX(self, X: floatType):
        self.x = X


    def getY(self) -> floatType:
        return self.y

    def setY(self, Y: floatType):
        self.y = Y


    def __add__(a, b:'Vector2D'):
        xcoord = a.getX() + b.getX()
        ycoord = a.getY() + b.getY()
        return Vector2D(xcoord, ycoord)
    
    def __sub__(a, b: 'Vector2D'):
        xcoord = a.getX() - b.getX()
        ycoord = a.getY() - b.getY()
        return Vector2D(xcoord, ycoord)
    
    def __mul__(a, b: floatType):
        xcoord = a.getX() * b
        ycoord = a.getY() * b
        return Vector2D(xcoord, ycoord)

    def __eq__(self, value: 'Vector2D'):
        return (self.x==value.getX() and self.y==value.getY())

    def __repr__(self):
        return f'[{self.x}, {self.y}]'

    def getMagnitude(self) -> floatType:
        return (self.x**2 + self.y**2)**0.5

    def magnitude(self, magnitude: floatType) -> 'Vector2D':
        if (magnitude==0):
            return self
        xval =  magnitude * self.x / self.getMagnitude()
        yval = magnitude * self.y / self.getMagnitude()
        return Vector2D(xval, yval)

if __name__=="__main__":
    print(Vector2D(1,1)-Vector2D(1,1))