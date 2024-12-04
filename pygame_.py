import random
import pygame


class Point:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y
        self.labels = None

    def distance(self, point):
        return ((self.x - point.x) + (self.y - point.y)) ** 0.5


pygame.init()
screen = pygame.display.set_mode((800, 600))
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()
screen.fill((150, 150, 150))

points = []
play, drawing = True, False
while play:
    clock.tick(80)

    if drawing:
        x, y = pygame.mouse.get_pos()
        for _ in range(random.randint(1, 10)):
            dx, dy = random.randint(-20, 20), random.randint(-20, 20)
            pygame.draw.circle(screen, (150, 0, 0), (x + dx, y + dy), 3)
            points.append(Point(x + dx, y + dy))

    pygame.draw.rect(screen, (100, 100, 100), (50, 500, 150, 50), border_radius=3)
    text = font.render('RESTART', True, (0, 0, 0))
    screen.blit(text, (70, 515))

    pygame.draw.rect(screen, (100, 100, 100), (600, 500, 150, 50), border_radius=3)
    text = font.render('RUN', True, (0, 0, 0))
    screen.blit(text, (650, 515))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if 60 < x < 210 and 500 < y < 550:
                screen.fill((150, 150, 150))
            elif 600 < x < 750 and 500 < y < 550:
                screen.fill((150, 150, 150))
            else:
                drawing = True

        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False

