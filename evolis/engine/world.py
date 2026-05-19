import json
import os
import random
from evolis.entities.food import Food
from evolis.entities.organism import Organism
from evolis.systems.movement import MovementSystem
from evolis.systems.collision import CollisionSystem
from evolis.systems.reproduction import ReproductionSystem

class World:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.organisms = []
        self.foods = []
        self.tick = 0
        self.event_log = []
        
        self.movement_system = MovementSystem()
        self.collision_system = CollisionSystem()
        self.reproduction_system = ReproductionSystem()
        
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

    def log_event(self, message, color=(180, 180, 180)):
        self.event_log.append((message, color))
        if len(self.event_log) > 50:
            self.event_log.pop(0)

    def update(self):
        # Run systems
        self.movement_system.update(self.organisms, self.foods, self.width, self.height)
        self.collision_system.update(self.organisms, self.foods)
        self.reproduction_system.update(self)
        
        # Remove dead organisms and log deaths
        for org in self.organisms:
            if org.is_dead:
                self.log_event(f"Tick {self.tick}: Organism {org.id} died (Age: {org.age})", org.dna.color)
                
        self.organisms = [org for org in self.organisms if not org.is_dead]
        
        # Spawn some food periodically
        if self.tick % 10 == 0 and len(self.foods) < 100:
            self.foods.append(Food(random.uniform(0, self.width), random.uniform(0, self.height)))
            
        self.tick += 1
