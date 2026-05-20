from evolis.entities.organism import Organism
import random

class Predator(Organism):
    def __init__(self, x, y, energy=150.0, dna=None):
        super().__init__(x, y, energy, dna)
        self.type = 'predator'
        
        # Give predators a reddish initial color if no dna is provided
        if dna is None:
            self.dna.color = (random.randint(200, 255), random.randint(30, 80), random.randint(30, 80))
            # Slightly buff their sense radius so they can hunt effectively
            self.dna.sense_radius *= 1.5

    def update(self):
        super().update()
        # Predators lose extra energy compared to prey
        self.energy -= 0.002 # additional passive drain
