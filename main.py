import pygame
from config import *
from classes import *
import math
import raycastingmodule

pygame.init()
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
player = Player()
sc_map = pygame.Surface((screen_width // minimap_scale, screen_height // minimap_scale))
pen = raycastingmodule.Drawing(screen, sc_map)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(colors['Черный'])

    pen.background()
    pen.fps(clock)

    pen.makeWorld(player.pos(), player.angle)

    player.move()

    pen.minimap(player)

    # pygame.draw.circle(screen, colors['Зеленый'], (int(player.x), int(player.y)), 20)
    # pygame.draw.line(screen, colors['Зеленый'], player.pos(), (
    #     player.x + screen_width * math.cos(player.angle),
    #     player.y + screen_width * math.sin(player.angle)
    # ))
    #
    # for x, y in world_map:
    #     pygame.draw.rect(screen, colors['Белый'], (x, y, cell_size, cell_size), 1)

    pygame.display.flip()
    clock.tick(60)
