import pygame
from config import *


# def ray_casting(screen, player_position, angle):
#     current_angle = angle - (FOV // 2)
#     start_x, start_y = player_position
#     for i in range(raysNumber):
#         sin_angle = math.sin(current_angle)
#         cos_angle = math.cos(current_angle)
#         for u in range(max_depth):
#             x = start_x + u * cos_angle
#             y = start_y + u * sin_angle
#             # pygame.draw.line(screen, colors['Белый'], player_position, (x, y), 2)
#             if find_map(x, y) in world_map:
#                 u *= math.cos(angle - current_angle)
#                 c = 255 / (1 + u * u * 0.00002)
#                 color = (c, c, c)
#                 height = min(coefficient / (u + 0.000001), screen_height)
#                 pygame.draw.rect(screen, color, (i * scale,
#                                                  (screen_height // 2) - height // 2,
#                                                  scale, height))
#                 break
#         current_angle += delta_angle

def ray_casting(screen, player_position, angle):
    start_x, start_y = player_position
    xm, ym = find_map(start_x, start_y)
    current_angle = angle - (FOV // 2)
    for i in range(raysNumber):
        sin_angle = math.sin(current_angle)
        cos_angle = math.cos(current_angle)
        sin_angle = sin_angle if sin_angle != 0 else 0.000001
        cos_angle = cos_angle if cos_angle != 0 else 0.000001

        if cos_angle >= 0:
            x = xm + cell_size
            dx = 1
        else:
            x = xm
            dx = -1

        for u in range(0, screen_width, cell_size):
            depth_v = (x - start_x) / cos_angle
            y = start_y + depth_v * sin_angle
            if find_map(x + dx, y) in world_map:
                break
            x += dx * cell_size
        if sin_angle >= 0:
            y, dy = (ym + cell_size, 1)
        else:
            y, dy = (ym, -1)

        for o in range(0, screen_height, cell_size):
            depth_h = (y - start_y) / sin_angle
            x = start_x + depth_h * cos_angle
            if find_map(x, y + dy) in world_map:
                break
            y += dy * cell_size

        depth = depth_v
        if depth_v > depth_h:
            depth = depth_h
        depth *= math.cos(angle - current_angle)
        c = 255 / (1 + depth * depth * 0.00002)
        color = (c, c, c)
        height = min(coefficient / (depth + 0.000001), screen_height)
        pygame.draw.rect(screen, color, (i * scale,
                                         (screen_height // 2) - height // 2,
                                         scale, height))
        current_angle += delta_angle


class Drawing:
    def __init__(self, sc, sc_map):
        self.screen = sc
        self.fps_font = pygame.font.SysFont('Times New Roman', 36, bold=True)
        self.sc_map = sc_map

    def background(self):
        pygame.draw.rect(self.screen, colors['Голубой'], (0, 0, screen_width, screen_height // 2))
        pygame.draw.rect(self.screen, colors['Коричневый'], (0, screen_height // 2,
                                                             screen_width, screen_height // 2))

    def makeWorld(self, player_position, player_angle):
        ray_casting(self.screen, player_position, player_angle)

    def fps(self, clock):
        fps_number = str(int(clock.get_fps()))
        image = self.fps_font.render(fps_number, 0, colors['Зеленый'])
        self.screen.blit(image, (screen_width - 40, 5))

    def minimap(self, player):
        self.sc_map.fill(colors['Черный'])
        xm, ym = player.x // minimap_scale, player.y // minimap_scale
        pygame.draw.circle(self.sc_map, colors['Желтый'], (int(xm), int(ym)), 6)
        pygame.draw.line(self.sc_map, colors['Желтый'], (xm, ym),
                         (xm + screen_width * math.cos(player.angle),
                          ym + screen_width * math.sin(player.angle)), 2)
        for x, y in minimap:
            pygame.draw.rect(self.sc_map, colors['Зеленый'], (x, y, minimap_cell_size,
                                                              minimap_cell_size), 2)
        self.screen.blit(self.sc_map, (0, 0))