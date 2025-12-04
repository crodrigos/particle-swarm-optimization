from ..Vector import Vector2D
import random as rand

floatType = float

class Particle:
    
    def __init__(self, X:floatType, Y:floatType):
        self.position = Vector2D(X,Y)
        self.velocity = Vector2D(rand.uniform(-1, 1),rand.uniform(-1, 1)).magnitude(1)

    def getPosition(self):
        return self.position
    def setPosition(self, x:floatType, y:floatType):
        self.position = Vector2D(x,y)

    def getX(self):
        return self.position.x
    def getY(self):
        return self.position.y

    def getVelocity(self):
        return self.velocity
    def setVelocity(self, x:floatType, y:floatType):
        self.velocity = Vector2D(x,y)

    def getVelocityX(self):
        return self.velocity.x
    def getVelocityY(self):
        return self.velocity.y

    def distance(self, other: 'Particle') -> float:
        return abs((other.getPosition().getX() - self.getPosition().getX())**2 + (other.getPosition().getY() - self.getPosition().getY())**2)**0.5

    def __eq__(self, value: 'Particle'):
        p2 = value.getPosition()
        v2 = value.getVelocity()
        return (self.position==p2 and self.velocity==v2)
        
    def __repr__(self):
        return f'[{self.getPosition()} | {self.getVelocity()}]'

    @staticmethod
    def createRandom(XMin:floatType, XMax:floatType, YMin:floatType, YMax:floatType):
        return Particle(rand.randint(XMin, XMax), rand.randint(YMin, YMax))