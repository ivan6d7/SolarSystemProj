import main
import pygame

def calculate_velocityBall (planet):
    r = planet.position - main.sun.position
    r_length = r.length()
    velocity_module = (main.G * planet.mass / r_length)**0.5

    v_perp_hat = pygame.Vector2(-r.y, r.x) / r.length

    velocity = v_perp_hat * velocity_module

    return velocity
    
