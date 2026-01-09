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
a = 500


# number of balls
balls_number = 10


g = 100000

balls = []

class Ball():
    def __init__(self, id, mass, initial_position, initial_velocity):
        self.id = id
        self.mass = mass
        self.position = initial_position
        self.velocity = initial_velocity
        self.acceleration = 0
        self.radius = mass**(2/3)*4
        balls.append(self)


for i in range(balls_number):
    Ball(i, randrange(10, 50), pygame.Vector2(randrange(0, screen.get_width() * 3 / 4), randrange(0, screen.get_height() * 2 / 3)), pygame.Vector2(randrange(-50, 50), randrange(-50, 50)))


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
            ball.acceleration = g * other_ball.mass / dist**2
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
    dt = clock.tick(120) / 1000

pygame.quit()