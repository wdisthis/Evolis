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
        self.font_bold = pygame.font.SysFont("Consolas", 12, bold=True)

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
            x, y = int(org.x), int(org.y)
            radius = max(2, int(org.dna.size))
            if getattr(org, 'type', 'prey') == 'predator':
                # Glowing effect for predator
                pygame.draw.circle(self.screen, (255, 50, 50), (x, y), radius + 4, 1)
                pygame.draw.circle(self.screen, (255, 100, 100), (x, y), radius + 2, 2)
                pygame.draw.circle(self.screen, org.dna.color, (x, y), radius)
            else:
                pygame.draw.circle(self.screen, org.dna.color, (x, y), radius)
            
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
        for log_data in self.world.event_log:
            if isinstance(log_data, tuple):
                log_msg, base_color = log_data
            else:
                log_msg, base_color = log_data, (180, 180, 180)
                
            words = log_msg.split(' ')
            word_objects = []
            for word in words:
                color = base_color
                is_bold = False
                if "died" in word:
                    color = (255, 100, 100)
                    is_bold = True
                elif "reproduced" in word:
                    color = (100, 255, 100)
                    is_bold = True
                    
                word_objects.append((word, color, is_bold))
                
            current_line = []
            current_width = 0
            for word_obj in word_objects:
                font = self.font_bold if word_obj[2] else self.font
                word_width, _ = font.size(word_obj[0] + " ")
                
                if current_width + word_width <= max_text_width:
                    current_line.append(word_obj)
                    current_width += word_width
                else:
                    if not current_line:
                        all_lines.append([word_obj])
                        current_line = []
                        current_width = 0
                    else:
                        all_lines.append(current_line)
                        current_line = [word_obj]
                        current_width = word_width
            if current_line:
                all_lines.append(current_line)
                
        max_lines = (self.world.height - y_offset - 10) // 18
        for line in all_lines[-max_lines:]:
            x_cursor = self.world.width + 10
            for word, color, is_bold in line:
                font = self.font_bold if is_bold else self.font
                word_surf = font.render(word + " ", True, color)
                self.screen.blit(word_surf, (x_cursor, y_offset))
                x_cursor += word_surf.get_width()
            y_offset += 18
        
        # Update display
        pygame.display.flip()
        
        # Control framerate
        self.clock.tick(self.fps)
