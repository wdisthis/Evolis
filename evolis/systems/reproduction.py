import random

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
                child_class = type(org)
                child = child_class(org.x + random.uniform(-10, 10), 
                                 org.y + random.uniform(-10, 10), 
                                 energy=60, dna=child_dna)
                new_organisms.append(child)
                type_name = child_class.__name__
                world.log_event(f"Tick {world.tick}: {type_name} {org.id} reproduced! Offspring: {child.id}", org.dna.color)
                
        world.organisms.extend(new_organisms)
