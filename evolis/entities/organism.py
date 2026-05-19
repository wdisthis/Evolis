from evolis.engine.genetics import DNA

class Organism:
    def __init__(self, x, y, energy=100.0, dna=None):
        self.x = x
        self.y = y
        self.vx = 0.0
        self.vy = 0.0
        self.energy = energy
        self.dna = dna if dna else DNA()
        self.age = 0
        self.is_dead = False

    def update(self):
        self.age += 1
        # Passive energy drain
        self.energy -= 0.05
        if self.energy <= 0:
            self.is_dead = True
