import math

size = screen_width, screen_height = 1200, 1200

colors = {
    'Красный': (255, 0, 0),
    'Синий': (0, 0, 255),
    'Зеленый': (0, 255, 0),
    'Белый': (255, 255, 255),
    'Черный': (0, 0, 0),
    'Темно-синий': (110, 110, 110),
    'Фиолетовый': (120, 0, 120),
    'Коричневый': (150, 75, 0),
    'Голубой': (0, 186, 255),
    'Желтый': (255, 255, 0)
}

fps = 75

# start player settings
player_pos = (screen_width // 2, screen_height // 2)
player_angle = 0
player_speed = 2

cell_size = 100

# minimap
minimap_scale = 5
minimap_cell_size = cell_size // minimap_scale

# map
map = [
    'WWWWWWWWWWWW',
    'W..........W',
    'W.....W....W',
    'W..........W',
    'W......WW..W',
    'W.W........W',
    'W..........W',
    'W....WWWW..W',
    'W..........W',
    'W...WWWW...W',
    'W..........W',
    'WWWWWWWWWW..WWW',
]

# cells coordinates
world_map = list()
minimap = list()
for j, row in enumerate(map):
    for i, symb in enumerate(row):
        if symb == 'W':
            world_map.append([i * cell_size, j * cell_size])
            minimap.append([i * minimap_cell_size, j * minimap_cell_size])

# For ray casting
FOV = math.pi / 6
raysNumber = 300
max_depth = 800
# max_depth = int((screen_width ** 2 + screen_height ** 2) ** (1 / 2))
delta_angle = FOV / raysNumber
distance = raysNumber / (2 * math.tan(FOV / 2))
coefficient = distance * cell_size
scale = screen_width // raysNumber


# functions
def find_map(first, second):
    return [(first // cell_size) * cell_size, (second // cell_size) * cell_size]
