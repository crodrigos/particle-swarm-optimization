from typing import List
import random as rand
import math as math
import matplotlib.pyplot as plt
import copy

from flatbuffers.flexbuffers import Vector

from .Vector import Vector2D 
from .Particle import Particle  
from .GenerationSnapshot import GenerationSnapshot

class House(Particle):
    def __init__(self, X, Y):
        super().__init__(X, Y)

class ParticleSwarmOptimization:

    _DEFAULT_DIMENSIONS : tuple[float,float,float,float] = [0,100,0,100]

    def __init__(self, NHouses:int, Dimensions: tuple[float,float,float,float] = None):
        self.dimensions = Dimensions
        if not Dimensions:
            self.dimensions = self._DEFAULT_DIMENSIONS

        self.houses = self.generateParticles(NHouses, limits=self.dimensions)

    def getHouses(self) -> List[Particle]:
        return self.houses

    def calculate(self, NParticles:int, Generation:int) -> list[GenerationSnapshot]:
        Particles = self.generateParticles(NParticles, limits=self.dimensions)
        snaps = []
        for i in range(Generation):
            snapshot = ParticleSwarmOptimization._calculateSingleGeneration(Particles, self.houses, n=i)
            # Save snapshot
            Particles = snapshot.particles
            snaps.append(snapshot.copy())

        return snaps

    def generateParticles(self, N : int, limits: tuple[float, float, float, float]  = None) -> list[House]:
        if limits is None:
            limits = [0, 100, 0, 100]
        return [House.createRandom(limits[0], limits[1], limits[2], limits[3]) for i in range(N)]

    @staticmethod
    def _calculateSingleGeneration(Particles: list[Particle], Houses: list[House], n:int = 0) -> GenerationSnapshot:    
        best = ParticleSwarmOptimization._getBest(Particles, Houses)
        Particles = ParticleSwarmOptimization._changeAllParticlesDirection(best,Particles)
        Particles = ParticleSwarmOptimization._moveAlongVectors(Particles)
        return GenerationSnapshot(n, Houses, Particles, best)

    @staticmethod
    def _getBest(particles: list[Particle], houses: list[House]) -> Particle: 
        best = [math.inf, None]
        for particle in particles:
            distSum = 0
            for house in houses:
                distSum += house.distance(particle)
            if (distSum < best[0]):
                best = [distSum, particle]
        return best[1]        
        

    @staticmethod
    def _changeAllParticlesDirection(best: Particle, others: list[Particle]) -> list[Particle]:
        cpy = others.copy()
        #print(best.position)
        for particle in cpy:
            CurrentVelocity = particle.getVelocity()
            VectorToBest = best.getPosition() - particle.getPosition()
            NewVelocity = (CurrentVelocity + VectorToBest).magnitude(1)
            particle.setVelocity(NewVelocity.getX(),NewVelocity.getY())
        return cpy
    
    @staticmethod
    def _moveAlongVectors(particles: list[Particle]) -> list[Particle]:
        ps = particles.copy()
        for part in ps:
            newpos = part.getPosition() + part.getVelocity()
            part.setPosition(newpos.getX(), newpos.getY())
        return ps
    
    @staticmethod
    def evaluate(p1: Particle, p2: Particle) -> float:
        return p1.distance(p2)

    @staticmethod
    def evaluateCoords(x1: float, y1: float, x2: float, y2: float) -> float:
        return Particle(x1, y1).distance(Particle(x2,y2))
