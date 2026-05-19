import json
import os
import random
from evolis.entities.food import Food
from evolis.entities.organism import Organism

class World:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.organisms = []
        self.foods = []
        self.tick = 0
        
        self.load_settings()
        self.spawn_initial_entities()

    def load_settings(self):
        settings_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'configs', 'settings.json')
        try:
            with open(settings_path, 'r') as f:
                settings = json.load(f)
                self.width = settings['window']['width']
                self.height = settings['window']['height']
        except Exception as e:
            print(f"Warning: Could not load settings.json. Using defaults. ({e})")

    def spawn_initial_entities(self):
        for _ in range(50):
            x = random.uniform(0, self.width)
            y = random.uniform(0, self.height)
            self.foods.append(Food(x, y))
            
        for _ in range(10):
            x = random.uniform(0, self.width)
            y = random.uniform(0, self.height)
            org = Organism(x, y)
            org.vx = random.uniform(-1, 1)
            org.vy = random.uniform(-1, 1)
            self.organisms.append(org)

    def update(self):
        for org in self.organisms:
            org.update()
            
            # Keep organisms within bounds by bouncing them
            if org.x < 0 or org.x > self.width: org.vx *= -1
            if org.y < 0 or org.y > self.height: org.vy *= -1
            
        self.tick += 1
