import sys
import os
import pygame

# Ensure the evolis package is in the path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from evolis.engine.world import World
from evolis.engine.renderer import Renderer

def main():
    world = World()
    renderer = Renderer(world)

    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update simulation state
        world.update()

        # Render current state
        renderer.render()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
