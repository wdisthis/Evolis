import random
import math

class MovementSystem:
    def update(self, organisms, foods, width, height):
        for org in organisms:
            if org.is_dead:
                continue
                
            # Random wandering if no target
            if random.random() < 0.05:
                # change direction
                angle = random.uniform(0, 2 * math.pi)
                org.vx = math.cos(angle) * org.dna.speed
                org.vy = math.sin(angle) * org.dna.speed
            
            # Find target based on type
            closest_target = None
            min_dist = org.dna.sense_radius
            
            if org.type == 'prey':
                for food in foods:
                    dist = math.hypot(food.x - org.x, food.y - org.y)
                    if dist < min_dist:
                        min_dist = dist
                        closest_target = food
            elif org.type == 'predator':
                for other in organisms:
                    if other.is_dead or other.type != 'prey': continue
                    dist = math.hypot(other.x - org.x, other.y - org.y)
                    if dist < min_dist:
                        min_dist = dist
                        closest_target = other
                        
            if closest_target:
                # Steer towards target
                dx = closest_target.x - org.x
                dy = closest_target.y - org.y
                angle = math.atan2(dy, dx)
                org.vx = math.cos(angle) * org.dna.speed
                org.vy = math.sin(angle) * org.dna.speed
                
            # Apply velocity
            org.x += org.vx
            org.y += org.vy
            
            # Energy cost for moving (proportional to speed and size)
            energy_cost = (abs(org.vx) + abs(org.vy)) * (org.dna.size / 10.0) * 0.1
            org.energy -= energy_cost
            
            # Bounce off walls
            if org.x < 0:
                org.x = 0
                org.vx *= -1
            elif org.x > width:
                org.x = width
                org.vx *= -1
                
            if org.y < 0:
                org.y = 0
                org.vy *= -1
            elif org.y > height:
                org.y = height
                org.vy *= -1
