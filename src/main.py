from ParticleSwarm import ParticleSwarmOptimization

def main():
    gens : list = ParticleSwarmOptimization(10).calculate(10, 21)
    #[print(gen.particles) for gen in gens]
    
if __name__=="__main__":
    main()
    
