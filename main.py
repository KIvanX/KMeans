import random
import pygame
from sklearn.cluster import DBSCAN


class Point:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y
        self.label = 0

    def distance(self, point):
        return ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5


pygame.init()
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
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

        if event.type == pygame.WINDOWRESIZED:
            screen.fill((150, 150, 150))
            for p in points:
                pygame.draw.circle(screen, (150, 0, 0), (p.x, p.y), 3)

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if 60 < x < 210 and 500 < y < 550:
                screen.fill((150, 150, 150))
                points.clear()
            elif 600 < x < 750 and 500 < y < 550:
                dbscan = DBSCAN(eps=50, min_samples=5)
                dbscan.fit_predict([[p.x, p.y] for p in points])
                screen.fill((150, 150, 150))
                colors = [(150, 0, 0), (0, 150, 0), (0, 0, 150), (150, 0, 150), (0, 150, 150)]
                for i, p in enumerate(points):
                    if dbscan.labels_[i] < len(colors):
                        p.label = dbscan.labels_[i]

                screen.fill((150, 150, 150))
                for p in points:
                    pygame.draw.circle(screen, colors[p.label], (p.x, p.y), 3)
            else:
                drawing = True

        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
