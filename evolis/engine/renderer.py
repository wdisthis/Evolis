import pygame
import json
import os

class Renderer:
    def __init__(self, world):
        self.world = world
        pygame.init()
        
        self.load_settings()
        
        self.sidebar_width = 320
        self.screen = pygame.display.set_mode((self.world.width + self.sidebar_width, self.world.height))
        pygame.display.set_caption(self.title)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Consolas", 12)

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
            
        # Draw organisms (color based on lineage/dna, size based on dna)
        for org in self.world.organisms:
            pygame.draw.circle(self.screen, org.dna.color, (int(org.x), int(org.y)), max(2, int(org.dna.size)))
            
        # Draw Sidebar
        sidebar_rect = pygame.Rect(self.world.width, 0, self.sidebar_width, self.world.height)
        pygame.draw.rect(self.screen, (40, 40, 40), sidebar_rect)
        pygame.draw.line(self.screen, (100, 100, 100), (self.world.width, 0), (self.world.width, self.world.height), 2)
        
        y_offset = 10
        title_surf = self.font.render("--- Event Log ---", True, (200, 200, 200))
        self.screen.blit(title_surf, (self.world.width + 10, y_offset))
        y_offset += 25
        
        all_lines = []
        max_text_width = self.sidebar_width - 20
        for log in self.world.event_log:
            color = (180, 180, 180)
            if "died" in log:
                color = (255, 100, 100)
            elif "reproduced" in log:
                color = (100, 255, 100)
                
            words = log.split(' ')
            current_line = []
            for word in words:
                test_line = ' '.join(current_line + [word])
                width, _ = self.font.size(test_line)
                if width <= max_text_width:
                    current_line.append(word)
                else:
                    if not current_line:
                        all_lines.append((word, color))
                        current_line = []
                    else:
                        all_lines.append((' '.join(current_line), color))
                        current_line = [word]
            if current_line:
                all_lines.append((' '.join(current_line), color))
                
        max_lines = (self.world.height - y_offset - 10) // 18
        for line, color in all_lines[-max_lines:]:
            log_surf = self.font.render(line, True, color)
            self.screen.blit(log_surf, (self.world.width + 10, y_offset))
            y_offset += 18
        
        # Update display
        pygame.display.flip()
        
        # Control framerate
        self.clock.tick(self.fps)
