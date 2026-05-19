import pygame
import json
import os

class Renderer:
    def __init__(self, world):
        self.world = world
        pygame.init()
        
        self.load_settings()
        
        self.screen = pygame.display.set_mode((self.world.width, self.world.height))
        pygame.display.set_caption(self.title)
        self.clock = pygame.time.Clock()

    def load_settings(self):
        self.title = "Evolis Simulation"
        self.fps = 60
        self.bg_color = (30, 30, 30)
        
        settings_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'configs', 'settings.json')
        try:
            with open(settings_path, 'r') as f:
                settings = json.load(f)
                self.title = settings['window']['title']
                self.fps = settings['window']['fps']
                self.bg_color = tuple(settings['colors']['background'])
        except Exception as e:
            print(f"Warning: Could not load settings for renderer. Using defaults. ({e})")

    def render(self):
        # Clear screen with background color
        self.screen.fill(self.bg_color)
        
        # Draw foods (green circles)
        for food in self.world.foods:
            pygame.draw.circle(self.screen, (0, 255, 0), (int(food.x), int(food.y)), 3)
            
        # Draw organisms (color based on energy, size based on dna)
        for org in self.world.organisms:
            r = max(0, min(255, 255 - int(org.energy)))
            g = max(0, min(255, int(org.energy)))
            color = (r, g, 255)
            pygame.draw.circle(self.screen, color, (int(org.x), int(org.y)), max(2, int(org.dna.size)))
        
        # Update display
        pygame.display.flip()
        
        # Control framerate
        self.clock.tick(self.fps)
