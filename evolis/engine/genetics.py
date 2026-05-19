import random

class DNA:
    def __init__(self, speed=None, size=None, sense_radius=None, color=None):
        # Initialize with random genes if not provided
        self.speed = speed if speed is not None else random.uniform(0.5, 2.0)
        self.size = size if size is not None else random.uniform(3.0, 7.0)
        self.sense_radius = sense_radius if sense_radius is not None else random.uniform(20.0, 100.0)
        
        # Lineage color starts random but inherits and mutates slightly
        if color is None:
            self.color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
        else:
            self.color = color

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
            
        if random.random() < mutation_rate:
            # Shift color slightly to show relation
            r = max(20, min(255, self.color[0] + random.randint(-15, 15)))
            g = max(20, min(255, self.color[1] + random.randint(-15, 15)))
            b = max(20, min(255, self.color[2] + random.randint(-15, 15)))
            self.color = (r, g, b)

    def crossover(self, other_dna):
        # Create new DNA by mixing this and other
        new_speed = random.choice([self.speed, other_dna.speed])
        new_size = random.choice([self.size, other_dna.size])
        new_sense = random.choice([self.sense_radius, other_dna.sense_radius])
        new_color = random.choice([self.color, other_dna.color])
        
        child_dna = DNA(new_speed, new_size, new_sense, new_color)
        child_dna.mutate()
        return child_dna

    def copy(self):
        # Asexual reproduction copy with mutation
        child_dna = DNA(self.speed, self.size, self.sense_radius, self.color)
        child_dna.mutate()
        return child_dna
