from config import *
import pygame
import math


class Player:
    def __init__(self):
        self.x, self.y = player_pos
        self.angle = player_angle

    def move(self):
        sin_angle = math.sin(self.angle)
        cos_angle = math.cos(self.angle)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.x += player_speed * cos_angle
            self.y += player_speed * sin_angle
        if keys[pygame.K_s]:
            self.x += -player_speed * cos_angle
            self.y += -player_speed * sin_angle
        if keys[pygame.K_a]:
            self.x += player_speed * sin_angle
            self.y += -player_speed * cos_angle
        if keys[pygame.K_d]:
            self.x += -player_speed * sin_angle
            self.y += player_speed * cos_angle
        if keys[pygame.K_LEFT]:
            self.angle -= 0.04
        if keys[pygame.K_RIGHT]:
            self.angle += 0.04

    def pos(self):
        return self.x, self.y
