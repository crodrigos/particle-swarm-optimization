from ..Vector import Vector2D
import random as rand

class Particle:
    
    def __init__(self, X:int, Y:int):
        self.position = Vector2D(X,Y)
        self.velocity = Vector2D(rand.uniform(-1, 1),rand.uniform(-1, 1)).magnitude(1)

    def getPosition(self):
        return self.position
    def setPosition(self, x:int, y:int):
        self.position = Vector2D(x,y)


    def getVelocity(self):
        return self.velocity
    def setVelocity(self, x:int, y:int):
        self.velocity = Vector2D(x,y)


    def distance(self, other: 'Particle') -> float:
        return abs((other.getPosition().getX() - self.getPosition().getX())**2 + (other.getPosition().getY() - self.getPosition().getY())**2)**0.5

    def __eq__(self, value: 'Particle'):
        p2 = value.getPosition()
        v2 = value.getVelocity()
        return (self.position==p2 and self.velocity==v2)
        
    def __repr__(self):
        return f'[{self.getPosition()} | {self.getVelocity()}]'

    @staticmethod
    def createRandom(XMin:float, XMax:float, YMin:float, YMax:float):
        return Particle(rand.randint(XMin, XMax), rand.randint(YMin, YMax))