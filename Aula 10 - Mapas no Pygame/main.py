import pygame, sys
from pygame.locals import QUIT

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Hello World!')
clock = pygame.time.Clock()
tile_size = 60
tile_size_joguinho = 64
tileset = pygame.image.load("plataform_tileset.png")
collider_caixa = pygame.Rect(0, 0, 0, 0)
can_walk = True

pos_x = 0
pos_y = 0

mapa = [
  "GGGGGGAGGGGGGG",
  "GGGGGGAGGGGGGG",
  "GGGGGGAGGGGGGG",
  "GGGGGGAGGGGGGG",
  "GGGGGGAAAGGGGG",
  "GGGGGGGGAGGGGG",
  "GGGGGGGGAGGGGG",
  "PPPPPPPPAPPPPP",
  "AAAAAAAAAAAAAA",
  "AAAAAAAAAAAAAA",
]

mapa_joguinho = [
  "XXXXXXXXXXXXXX",
  "XXXXXXXXXXXXXX", 
  "XXXXXXXXXXXXXX", 
  "XXXXXXXXXXXXXX", 
  "XXXXXXXXXXXXXX", 
  "XXXXXXXXXXXXXX", 
  "XXXXBXXXXXXXXX", 
  "GGGGGGGAAGGGGG", 
  "TTTTTTTPPTTTTT", 
  "TTTTTTTPPTTTTT",
]

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    clock.tick(60)
    dt = clock.get_time()

    old_pos_x = pos_x
    old_pos_y = pos_y

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        pos_x = pos_x + 0.1*dt
    elif keys[pygame.K_LEFT]:
        pos_x = pos_x - 0.1*dt
    elif keys[pygame.K_UP]:
        pos_y = pos_y - 0.1*dt
    elif keys[pygame.K_DOWN]:
        pos_y = pos_y + 0.1*dt

    screen.fill((152,209,250))

    collider_jogador = pygame.Rect(pos_x, pos_y, 64, 64)

    if collider_jogador.colliderect(collider_caixa):
        pos_x = old_pos_x
        pos_y = old_pos_y

    pygame.draw.rect(screen, (255, 0, 0), (pos_x, pos_y, 64, 64))
    pygame.draw.rect(screen, (0, 0, 255), collider_jogador, 2)
    
    ## Primeiro mapa
    # for i in range(len(mapa)): # Para cada linha
    #     for j in range(len(mapa[i])): # Para cada coluna (letra)
    #         if mapa[i][j] == "G":
    #             pygame.draw.rect(screen, (39,153,0), (tile_size*j, tile_size*i, tile_size, tile_size))
    #         elif mapa[i][j] == "P":
    #             pygame.draw.rect(screen, (230,235,134), (tile_size*j, tile_size*i, tile_size, tile_size))
    #         elif mapa[i][j] == "A":
    #             pygame.draw.rect(screen, (63,125,232), (tile_size*j, tile_size*i, tile_size, tile_size))

    for i in range(len(mapa_joguinho)): # Para cada linha
        for j in range(len(mapa_joguinho[i])): # Para cada coluna (letra)
            if mapa_joguinho[i][j] == "G":
                screen.blit(tileset, (j * tile_size_joguinho, i * tile_size_joguinho), (0, 0, tile_size_joguinho, tile_size_joguinho))
            elif mapa_joguinho[i][j] == "T":
                screen.blit(tileset, (j * tile_size_joguinho, i * tile_size_joguinho), (64, 0, tile_size_joguinho, tile_size_joguinho))
            elif mapa_joguinho[i][j] == "A":
                screen.blit(tileset, (j * tile_size_joguinho, i * tile_size_joguinho), (128, 0, tile_size_joguinho, tile_size_joguinho))
            elif mapa_joguinho[i][j] == "B":
                screen.blit(tileset, (j * tile_size_joguinho, i * tile_size_joguinho), (0, 128, tile_size_joguinho, tile_size_joguinho))
                collider_caixa = pygame.Rect(j * tile_size_joguinho, i * tile_size_joguinho, 64, 64)
                pygame.draw.rect(screen, (0, 0, 255), collider_caixa, 2)
            elif mapa_joguinho[i][j] == "P":
                screen.blit(tileset, (j * tile_size_joguinho, i * tile_size_joguinho), (128, 64, tile_size_joguinho, tile_size_joguinho))
    

    pygame.display.update()