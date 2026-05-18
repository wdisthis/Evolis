import json
import os

class World:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.organisms = []
        self.foods = []
        self.tick = 0
        
        self.load_settings()

    def load_settings(self):
        settings_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'configs', 'settings.json')
        try:
            with open(settings_path, 'r') as f:
                settings = json.load(f)
                self.width = settings['window']['width']
                self.height = settings['window']['height']
        except Exception as e:
            print(f"Warning: Could not load settings.json. Using defaults. ({e})")

    def update(self):
        # Logic for updating entities will go here
        self.tick += 1
