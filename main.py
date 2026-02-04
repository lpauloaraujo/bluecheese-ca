import pygame
from cheese import CheeseGrid
from cheese import PERMISSIVE, RESISTANT, LATENT, INFECTIOUS, PIERCED, STAGNANT
from cheese import CELL_STATE


grid = CheeseGrid(width=70, height=70, depth=70, to_pierce=15)

CELL = 10

CORES = {
        PERMISSIVE: (245, 215, 70),    
        RESISTANT:  (190, 155, 40),
        LATENT:     (110, 120, 140),   
        INFECTIOUS: (40, 110, 220),   
        PIERCED:    (245, 245, 245),
        STAGNANT: (28, 54, 68) 
}

pygame.init()
tela = pygame.display.set_mode((grid.width * CELL, grid.height * CELL))
clock = pygame.time.Clock()

slice_z = 1  

PASS_DAY_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(PASS_DAY_EVENT, 100)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == PASS_DAY_EVENT:
            grid.pass_day()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                slice_z = (slice_z + 1) % grid.depth
            if event.key == pygame.K_DOWN:
                slice_z = (slice_z - 1) % grid.depth

    tela.fill((0, 0, 0))

    for y in range(grid.height):
        for x in range(grid.width):
            state = grid.cells[x][y][slice_z][CELL_STATE]

            cor = CORES.get(state, (0, 0, 0))

            pygame.draw.rect(
                tela,
                cor,
                (x * CELL, y * CELL, CELL, CELL)
            )

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
