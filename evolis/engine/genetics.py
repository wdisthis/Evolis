import random

class DNA:
    def __init__(self, speed=None, size=None, sense_radius=None):
        # Initialize with random genes if not provided
        self.speed = speed if speed is not None else random.uniform(0.5, 2.0)
        self.size = size if size is not None else random.uniform(3.0, 7.0)
        self.sense_radius = sense_radius if sense_radius is not None else random.uniform(20.0, 100.0)

    def mutate(self):
        # 10% chance to mutate each gene slightly
        mutation_rate = 0.1
        if random.random() < mutation_rate:
            self.speed += random.uniform(-0.2, 0.2)
            self.speed = max(0.1, self.speed) # Keep above 0
            
        if random.random() < mutation_rate:
            self.size += random.uniform(-1.0, 1.0)
            self.size = max(1.0, self.size)
            
        if random.random() < mutation_rate:
            self.sense_radius += random.uniform(-10.0, 10.0)
            self.sense_radius = max(5.0, self.sense_radius)

    def crossover(self, other_dna):
        # Create new DNA by mixing this and other
        new_speed = random.choice([self.speed, other_dna.speed])
        new_size = random.choice([self.size, other_dna.size])
        new_sense = random.choice([self.sense_radius, other_dna.sense_radius])
        
        child_dna = DNA(new_speed, new_size, new_sense)
        child_dna.mutate()
        return child_dna

    def copy(self):
        # Asexual reproduction copy with mutation
        child_dna = DNA(self.speed, self.size, self.sense_radius)
        child_dna.mutate()
        return child_dna
