import math

class CollisionSystem:
    def update(self, organisms, foods):
        # Organism vs Food
        foods_to_remove = []
        for org in organisms:
            if org.is_dead: continue
            
            for food in foods:
                if food in foods_to_remove: continue
                
                # Collision check using sizes
                dist = math.hypot(food.x - org.x, food.y - org.y)
                if dist < org.dna.size + 3: # 3 is food radius
                    org.energy += food.energy
                    # Cap energy
                    org.energy = min(org.energy, 200)
                    foods_to_remove.append(food)
                    
        for food in foods_to_remove:
            if food in foods:
                foods.remove(food)
