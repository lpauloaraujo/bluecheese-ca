import random
import math

PERMISSIVE = 0
RESISTANT = 1
LATENT = 2
INFECTIOUS = 3
PIERCED = 5
STAGNANT = 6

CELL_STATE = 0
DAYS_INFECTED = 1
O2_AVALIABILITY = 2
NUTRIENT_AVALIABILITY = 3

class CheeseGrid:
    def __init__(self, width, height, depth, to_pierce):
        self.width = width
        self.height = height
        self.depth = depth
        self.cells = None
        self.to_pierce = to_pierce
        self.initialize()

    def initialize(self):
        self.cells = [[[None for _ in range(self.depth)] for _ in range(self.height)] for _ in range(self.width)]
        for x in range(self.width):
            for y in range(self.height):
                for z in range(self.depth):
                    if z == 0 and x % self.to_pierce == 0 and y % self.to_pierce == 0:
                        self.pierce(x, y)
                        break
                    if (z == 0 or x == 0 or x == self.width-1 or y == 0 or y == self.height-1):
                        self.cells[x][y][z] = [PIERCED, 0, 100, 0] 
                        continue
                    p = random.random()
                    if p < 0.4:
                        self.cells[x][y][z] = [RESISTANT, 0, None, random.randint(30, 70)]
                    else:
                        self.cells[x][y][z] = [PERMISSIVE, 0, None, random.randint(80, 100)]
                    avaliability = self.get_o2_avaliability(x, y, z)
                    base_probability = (self.cells[x][y][z][NUTRIENT_AVALIABILITY] / 100.0) * (avaliability / 100.0)
                    K = 0.02 
                    final_probability = base_probability * K
                    if random.random() < final_probability:
                        self.cells[x][y][z][CELL_STATE] = LATENT  

    def pierce(self, x, y):
        for z in range(self.depth):
            self.cells[x][y][z] = [PIERCED, 0, 100, 0] 

    def pass_day(self):
        for x in range(self.width):
            for y in range(self.height):
                for z in range(self.depth):
                    cell = self.cells[x][y][z]
                    state = cell[CELL_STATE]
                    if state in (LATENT, INFECTIOUS):
                        cell[DAYS_INFECTED] += 1
                        custo = 2 if state == LATENT else 7
                        cell[NUTRIENT_AVALIABILITY] = max(0, cell[NUTRIENT_AVALIABILITY] - custo)
                        if cell[NUTRIENT_AVALIABILITY] < 20:
                            cell[CELL_STATE] = STAGNANT
                            continue 
                        if state == LATENT and cell[DAYS_INFECTED] >= 10:
                            cell[CELL_STATE] = INFECTIOUS
                        if cell[CELL_STATE] == INFECTIOUS:
                            self.try_infect(x, y, z)

    def get_o2_avaliability(self, x, y, z):
        cell = self.cells[x][y][z]
        if cell[CELL_STATE] == PIERCED:
            return 100
        distance = self.get_o2_distance(x, y, z)
        avaliability = max(0, 100 - distance * 10)
        cell[O2_AVALIABILITY] = avaliability
        return avaliability

    def get_o2_distance(self, x, y, z):
        dx = x % self.to_pierce
        dy = y % self.to_pierce
        x_distance = min(dx, self.to_pierce - dx)
        y_distance = min(dy, self.to_pierce - dy)
        xy_distance = math.sqrt(x_distance**2 + y_distance**2)
        return min(xy_distance, self.get_border_distance(x, y, z))
    
    def get_border_distance(self, x, y, z):
        dist_x = min(x, self.width - 1 - x)
        dist_y = min(y, self.height - 1 - y)
        dist_z = z
        return min(dist_x, dist_y, dist_z)

    def try_infect(self, x, y, z):
        neighbours = self.get_neighbours(x, y, z)
        fungus_count = sum(1 for n in neighbours if n[CELL_STATE] in (LATENT, INFECTIOUS))
        competition_factor = 1.0 / (1.0 + 0.5 * fungus_count)
        for neighbour in neighbours:
            if neighbour[CELL_STATE] in (PERMISSIVE, RESISTANT):
                self.cells[x][y][z][NUTRIENT_AVALIABILITY] -= 5
                if self.cells[x][y][z][NUTRIENT_AVALIABILITY] < 20:
                    break
                o2_factor = (neighbour[O2_AVALIABILITY] / 100.0) ** 2
                nut_factor = neighbour[NUTRIENT_AVALIABILITY] / 100.0
                base = 0.5 if neighbour[CELL_STATE] == PERMISSIVE else 0.1
                success_probability = base * o2_factor * nut_factor * competition_factor
                if random.random() < success_probability:
                    neighbour[CELL_STATE] = LATENT
                    neighbour[DAYS_INFECTED] = 0

    def get_neighbours(self, x, y, z):
        neighbours = []
        directions = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]
        for dx, dy, dz in directions:
            nx, ny, nz = x + dx, y + dy, z + dz
            if 0 <= nx < self.width and 0 <= ny < self.height and 0 <= nz < self.depth:
                neighbour = self.cells[nx][ny][nz]
                if neighbour[CELL_STATE] != PIERCED:
                    neighbours.append(neighbour)
        return neighbours
