# Example file showing a circle moving on screen
import pygame
from random import randrange as randrange



# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

dt = 0

#acceleration constant
a = 0.001


# number of balls
balls_number = 10


G = 0.1

'''
M_sun = 1.9885e30

M_mercury = 3.3011e23
M_venus   = 4.8675e24
M_earth   = 5.97237e24
M_mars    = 6.4171e23
M_jupiter = 1.8982e27
M_saturn  = 5.6834e26
M_uranus  = 8.6810e25
M_neptune = 1.02413e26
'''

planets = [
    {
        "name": "Mercury",
        "radius": 38.7,
        "velocity": 4.74,
        "mass": 0.330
    },
    {
        "name": "Venus",
        "radius": 72.3,
        "velocity": 3.50,
        "mass": 4.87
    },
    {
        "name": "Earth",
        "radius": 100.0,
        "velocity": 2.98,
        "mass": 5.97
    },
    {
        "name": "Mars",
        "radius": 152.0,
        "velocity": 2.41,
        "mass": 0.642
    },
    {
        "name": "Jupiter",
        "radius": 520.0,
        "velocity": 1.31,
        "mass": 1898.0
    },
    {
        "name": "Saturn",
        "radius": 958.0,
        "velocity": 0.97,
        "mass": 568.0
    },
    {
        "name": "Uranus",
        "radius": 1920.0,
        "velocity": 0.68,
        "mass": 86.8
    },
    {
        "name": "Neptune",
        "radius": 3000.0,
        "velocity": 0.54,
        "mass": 102.0
    }
]

sun = {
    "name": "Sun",
    "position": (0.0, 0.0),
    "velocity": (0.0, 0.0),
    "mass": 1989000.0  
}

balls = []

class Ball():
    def __init__(self, id, mass, initial_position, initial_velocity):
        self.id = id
        self.mass = mass
        self.position = initial_position
        self.velocity = initial_velocity
        self.acceleration = 0
        self.radius = 5
        balls.append(self)

<<<<<<< HEAD
sun = Ball(1, sun["mass"], pygame.Vector2(screen.get_width()/2, screen.get_height() / 2), pygame.Vector2(0, 0))
mercury = Ball(3, planets[0]["mass"], pygame.Vector2(screen.get_width()/2 + planets[0]["radius"], screen.get_height() / 2), pygame.Vector2(0, planets[0]["velocity"]))
venus = Ball(4, planets[1]["mass"], pygame.Vector2(screen.get_width()/2 + planets[1]["radius"], screen.get_height() / 2), pygame.Vector2(0, planets[1]["velocity"]))
earth = Ball(2, planets[2]["mass"], pygame.Vector2(screen.get_width()/2 + planets[2]["radius"], screen.get_height() / 2), pygame.Vector2(0, planets[2]["velocity"]))
mars = Ball(5, planets[3]["mass"], pygame.Vector2(screen.get_width()/2 + planets[3]["radius"], screen.get_height() / 2), pygame.Vector2(0, planets[3]["velocity"]))
jupiter = Ball(6, planets[4]["mass"], pygame.Vector2(screen.get_width()/2 + planets[4]["radius"], screen.get_height() / 2), pygame.Vector2(0, planets[4]["velocity"]))
#saturn = Ball(7, planets[5]["mass"], pygame.Vector2(screen.get_width()/2 + planets[5]["radius"], screen.get_height() / 2), pygame.Vector2(0, planets[5]["velocity"]))
#uranus = Ball(8, planets[6]["mass"], pygame.Vector2(screen.get_width()/2 + planets[6]["radius"], screen.get_height() / 2), pygame.Vector2(0, planets[6]["velocity"]))
#neptune = Ball(9, planets[7]["mass"], pygame.Vector2(screen.get_width()/2 + planets[7]["radius"], screen.get_height() / 2), pygame.Vector2(0, planets[7]["velocity"]))
=======

# Initialize sun and earth
sun = Ball(1, M_sun, pygame.Vector2(screen.get_width()/2, screen.get_height() / 2), pygame.Vector2(0, 0))
>>>>>>> 8919eeb (tang vel file)



#for i in range(balls_number):
#    Ball(i, randrange(10, 50), pygame.Vector2(randrange(0, screen.get_width() * 3 // 4), randrange(0, screen.get_height() * 2 // 3)), pygame.Vector2(randrange(-50, 50), randrange(-50, 50)))



while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")
    width = screen.get_width()
    height = screen.get_height()
    for ball in balls:
        #draw the ball on the canvas
        
        pygame.draw.circle(screen, "blue", ball.position , ball.radius)

        # scam_list = balls.copy()
        # scam_list.pop(balls.index(ball))
        # bouncing from the edges
    
            

        for other_ball in balls:
            if other_ball.id == ball.id:
                continue 
            dist = (other_ball.position - ball.position).length()
            if dist < (ball.radius + other_ball.radius): 
                dist = (ball.radius + other_ball.radius)
            ball.acceleration = G * other_ball.mass / dist**2
            # print(ball.acceleration)

            ball.velocity += ball.acceleration * dt * (other_ball.position - ball.position).normalize()

        if ball.position.x < 0 and ball.velocity.x < 0: 
            ball.velocity.x = -ball.velocity.x

        if ball.position.y < 0 and ball.velocity.y < 0: 
            ball.velocity.y = -ball.velocity.y

        if ball.position.x > width and ball.velocity.x > 0: 
            ball.velocity.x = -ball.velocity.x

        if ball.position.y > height and ball.velocity.y > 0: 
            ball.velocity.y = -ball.velocity.y

        #do the moving
        ball.position += ball.velocity * dt




    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(120)/1000

pygame.quit()