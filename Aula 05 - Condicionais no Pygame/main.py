from pygame import *

init()
screen = display.set_mode((1280, 720))
running = True
clock = time.Clock()

## Carregamento de recursos
fonte = font.Font("batmfa__.ttf", 50)
image = image.load("batman.png")
image = transform.scale(image, (200, 200))
# mixer.music.load("batman_1966.mp3")
# mixer.music.play(-1)
cus_im_batman_sfx = mixer.Sound("cus-im-batman.mp3")


## Definição de variáveis
pos_x = 300
background_color = "#97D1FA"
texto = "I am BATMAN!"

while running:
    clock.tick(60)

    for ev in event.get():
        if ev.type == QUIT:
            running = False
        
        if ev.type == MOUSEBUTTONUP:
            if ev.button == 1:
                texto = "I said I AM BATMAN!"
            elif ev.button == 3:
                texto = "I AM BATMAN!"

        # AÇÕES INSTANTÂNEAS
        if ev.type == KEYDOWN:
            key_pressed = ev.key
            if key_pressed == K_SPACE:
                background_color = (245, 178, 64)
            elif key_pressed == K_m:
                cus_im_batman_sfx.play()

    ## Update
    dt = clock.get_time()/1000
    keys = key.get_pressed()

    mouse_x, mouse_y = mouse.get_pos()
    
    # AÇÕES CONTÍNUAS
    if keys[K_d]:
        pos_x = pos_x + 100 * dt
    elif keys[K_a]:
        pos_x = pos_x - 100 * dt

    ## NÃO FAÇAM O PLAY DO SFX DA FORMA ABAIXO, FAÇAM DENTRO DO FOR DE EVENTOS
    # elif keys[K_m]:
    #     cus_im_batman_sfx.play()
    
    ## Draw
    screen.fill(background_color)
    draw.rect(screen, "#0D1664", (100, 200, 200, 50))
    draw.circle(screen, "#FFF251", (mouse_x, mouse_y), 50)
    draw.polygon(screen, "#F2883B", [(400, 300), (450, 300), (425, 250)])
    draw.line(screen, "#FFF251", (10, 150), (100, 20), 4)

    draw.circle(screen, "#FFFFFF", (pos_x, 80), 70)
    draw.circle(screen, "#FFFFFF", (pos_x + 70, 80), 70)
    draw.circle(screen, "#FFFFFF", (pos_x + 140, 80), 70)
    draw.circle(screen, "#FFFFFF", (pos_x + 210, 80), 70)

    screen.blit(image, (500, 300))

    steve_text = fonte.render(texto, True, "#000000")
    screen.blit(steve_text, (500, 250))

    display.update()