import math

class CollisionSystem:
    def update(self, organisms, foods):
        foods_to_remove = []
        
        for org in organisms:
            if org.is_dead: continue
            
            if org.type == 'prey':
                for food in foods:
                    if food in foods_to_remove: continue
                    
                    # Collision check using sizes
                    dist = math.hypot(food.x - org.x, food.y - org.y)
                    if dist < org.dna.size + 3: # 3 is food radius
                        org.energy += food.energy
                        # Cap energy
                        org.energy = min(org.energy, 200)
                        foods_to_remove.append(food)
                        
            elif org.type == 'predator':
                for other in organisms:
                    if other.is_dead or other.type != 'prey': continue
                    
                    dist = math.hypot(other.x - org.x, other.y - org.y)
                    if dist < org.dna.size + other.dna.size:
                        org.energy += other.energy * 0.5 + 50 # Predators gain a lot of energy from prey
                        org.energy = min(org.energy, 300)
                        other.is_dead = True
                        
        for food in foods_to_remove:
            if food in foods:
                foods.remove(food)
