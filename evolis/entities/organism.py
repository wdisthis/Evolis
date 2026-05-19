class Organism:
    def __init__(self, x, y, energy=100.0):
        self.x = x
        self.y = y
        self.vx = 0.0
        self.vy = 0.0
        self.energy = energy

    def update(self):
        self.x += self.vx
        self.y += self.vy
