from .Vector import Vector2D 
from .Particle import Particle  
import copy

class GenerationSnapshot:


    def __init__(self, n: int, houses: list[Particle], stores: list[Particle], particles: list[Particle], best : Particle = None):
        self.houses = houses
        self.stores = stores
        self.particles = particles
        self.gennum = n
        self.best = best
    
    def copy(self):
        # Deep copy to ensure particle positions are independent
        return GenerationSnapshot(self.gennum,
                                  copy.deepcopy(self.houses),
                                  copy.deepcopy(self.stores),
                                  copy.deepcopy(self.particles),
                                  copy.copy(self.best))
        
    def __repr__(self):
        return f"GenerationSnapshot(generation={self.gennum}, houses={len(self.houses)}, particles={len(self.particles)}, best={self.best.position})"
    
