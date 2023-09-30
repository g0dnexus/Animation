import pygame
import random

pygame.init()

infoObject = pygame.display.Info()
WIDTH, HEIGHT = infoObject.current_w, infoObject.current_h
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Wow, Cool!")

BLACK = (0, 0, 0)

class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.z = random.randint(1, 10)
        self.size = random.randint(5, 15) * self.z
        self.color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
        self.speed_x = random.uniform(-1, 1) * self.z
        self.speed_y = random.uniform(-1, 1) * self.z

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.size -= 0.1

        if self.x < 0 or self.x > WIDTH:
            self.speed_x *= -1
        if self.y < 0 or self.y > HEIGHT:
            self.speed_y *= -1

    def draw(self):
        pygame.draw.ellipse(screen, self.color, (int(self.x), int(self.y), int(self.size), int(self.size/2)))

particles = []
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if len(particles) < 500:
        particle = Particle(random.randint(0, WIDTH), random.randint(0, HEIGHT))
        particles.append(particle)

    for particle in particles:
        particle.update()
        particle.draw()
        if particle.size <= 0:
            particles.remove(particle)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
