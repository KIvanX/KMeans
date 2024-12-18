import random
import time

import pygame


class Point:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y
        self.label = 0

    def distance(self, point):
        return ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5


def my_dbscan(data, radius, min_k):
    for point in data:
        point.label = -1

    work = True
    while work:
        work = False
        roots = []
        nbs = []
        for i, point in enumerate(data):
            nb = [e for e in data if 0 < point.distance(e) < radius]
            if len(nb) >= min_k:
                roots.append(point)
            nbs.append(nb)

        borders = []
        for i, point in enumerate(data):
            if len(nbs[i]) < min_k and [e for e in nbs[i] if e in roots]:
                borders.append(point)

        v = 0
        for i in range(len(roots)):
            for j in range(i + 1, len(roots)):
                if roots[i].distance(roots[j]) < radius:
                    k = min(roots[i].label, roots[j].label)
                    if k == -1:
                        k = v
                        v += 1
                    if roots[i].label != k or roots[j].label != k:
                        work = True
                    roots[i].label = k
                    roots[j].label = k

        for i, point in enumerate(borders):
            p_roots = [e for e in nbs[i] if e in roots]
            if p_roots:
                if point.label != p_roots[0].label:
                    work = True
                point.label = p_roots[0].label

        ind = list({p.label for p in data})
        for point in data:
            point.label = ind.index(point.label)

        screen.fill((150, 150, 150))
        colors = [(0, 150, 0), (150, 0, 0), (0, 0, 150), (150, 0, 150), (0, 150, 150)]
        screen.fill((150, 150, 150))
        for p in points:
            if p.label < len(colors):
                pygame.draw.circle(screen, colors[p.label], (p.x, p.y), 3)
        pygame.display.update()
        time.sleep(0.5)


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
                my_dbscan(points, radius=50, min_k=5)
            else:
                drawing = True

        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
