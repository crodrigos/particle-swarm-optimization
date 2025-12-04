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
            snapshot = self.calculateSingleGeneration(Particles, self.houses, n=i)
            # Save snapshot
            Particles = snapshot.particles
            snaps.append(snapshot.copy())

        return snaps

    def generateParticles(self, N : int, limits: tuple[float, float, float, float]  = None) -> list[House]:
        if limits is None:
            limits = [0, 100, 0, 100]
        return [House.createRandom(limits[0], limits[1], limits[2], limits[3]) for i in range(N)]

    def calculateSingleGeneration(self, Particles: list[Particle], Houses: list[House], n:int = 0) -> GenerationSnapshot:
        best = self.getBest(Particles, Houses)
        Particles = self.changeAllParticlesDirection(best, Particles)
        Particles = self.moveAlongVectors(Particles)
        return GenerationSnapshot(n, Houses, Particles, best)

    def getBest(self, particles: list[Particle], houses: list[House]) -> Particle:
        best = [math.inf, None]
        for particle in particles:
            distSum = self.evaluate(particle)
            if distSum < best[0]:
                best = [distSum, particle]
        return best[1]        
        

    def changeAllParticlesDirection(self, best: Particle, others: list[Particle]) -> list[Particle]:
        cpy = others.copy()
        #print(best.position)
        for particle in cpy:
            CurrentVelocity = particle.getVelocity()
            VectorToBest = best.getPosition() - particle.getPosition()
            NewVelocity = (CurrentVelocity + VectorToBest).magnitude(1)
            particle.setVelocity(NewVelocity.getX(),NewVelocity.getY())
        return cpy

    def moveAlongVectors(self, particles: list[Particle]) -> list[Particle]:
        ps = particles.copy()
        for part in ps:
            NewPosition = part.getPosition() + part.getVelocity()
            part.setPosition(NewPosition.getX(), NewPosition.getY())
        return ps

    def evaluate(self, p1: Particle) -> float:
        sum = 0
        for house in self.houses:
            sum += p1.distance(house)
        return sum
