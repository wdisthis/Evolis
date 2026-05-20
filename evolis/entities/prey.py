from evolis.entities.organism import Organism

class Prey(Organism):
    def __init__(self, x, y, energy=100.0, dna=None):
        super().__init__(x, y, energy, dna)
        self.type = 'prey'
