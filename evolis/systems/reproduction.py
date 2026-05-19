from evolis.entities.organism import Organism

class ReproductionSystem:
    def update(self, world):
        new_organisms = []
        for org in world.organisms:
            if org.is_dead: continue
            
            # Asexual reproduction if enough energy
            if org.energy > 150:
                org.energy -= 80 # Cost of reproduction
                # Create offspring nearby
                child_dna = org.dna.copy()
                # Spawn slightly offset to avoid getting stuck
                child = Organism(org.x + random.uniform(-10, 10), 
                                 org.y + random.uniform(-10, 10), 
                                 energy=60, dna=child_dna)
                new_organisms.append(child)
                
        world.organisms.extend(new_organisms)

import random # Added down here to satisfy the reproduction logic above
