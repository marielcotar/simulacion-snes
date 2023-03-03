import pygame

pygame.init()

clk = pygame.time.Clock()

size = width, height = 600, 600
screen = pygame.display.set_mode(size)
background_image = pygame.image.load("control.png").convert()
frameRect = pygame.Rect((0,0), (width,height))

crosshairy = pygame.surface.Surface((15,15), pygame.SRCALPHA)
pygame.draw.circle(crosshairy, pygame.Color("#026014"), (10, 10), 5, 0) #botón Y, color verde

crosshairx = pygame.surface.Surface((15,15), pygame.SRCALPHA)
pygame.draw.circle(crosshairx, pygame.Color("#080357"), (10, 10), 5, 0) #botón X, color azul

crosshairb = pygame.surface.Surface((15,15), pygame.SRCALPHA)
pygame.draw.circle(crosshairb, pygame.Color("#FFFF00"), (10, 10), 5, 0) #botón B, color amarillo

crosshaira = pygame.surface.Surface((15,15), pygame.SRCALPHA)
pygame.draw.circle(crosshaira, pygame.Color("#FF0000"), (10, 10), 5, 0) #botón A, color rojo

crosshairf = pygame.surface.Surface((15,15), pygame.SRCALPHA)
pygame.draw.circle(crosshairf, pygame.Color("#000000"), (10, 10), 5, 0) #flechas, color negro

crosshairl = pygame.surface.Surface((15,15), pygame.SRCALPHA)
pygame.draw.circle(crosshairl, pygame.Color("#470024"), (10, 10), 5, 0) #botón izquierdo (L) color morado

crosshairr = pygame.surface.Surface((15,15), pygame.SRCALPHA)
pygame.draw.circle(crosshairr, pygame.Color("#470024"), (10, 10), 5, 0) #botón derecho (R), color morado

crosshairs = pygame.surface.Surface((15,15), pygame.SRCALPHA)
pygame.draw.circle(crosshairs, pygame.Color("#EF3054"), (10, 10), 5, 0) #botón start (S), color rosa

crosshaire = pygame.surface.Surface((15,15), pygame.SRCALPHA)
pygame.draw.circle(crosshaire, pygame.Color("#EF3054"), (10, 10), 5, 0) #botón select (E), color rosa


while True:
    pygame.event.pump()
    screen.blit(background_image, (0,0))

    Keys = pygame.key.get_pressed()

    if Keys [pygame.K_y]: screen.blit(crosshairy, (385, 287))
    if Keys [pygame.K_x]: screen.blit(crosshairx, (435, 246))
    if Keys [pygame.K_b]: screen.blit(crosshairb, (438, 329))
    if Keys [pygame.K_a]: screen.blit(crosshaira, (488, 288))
    if Keys [pygame.K_l]: screen.blit(crosshairl, (130, 170))
    if Keys [pygame.K_r]: screen.blit(crosshairr, (430, 170))
    if Keys [pygame.K_s]: screen.blit(crosshairs, (290, 305))
    if Keys [pygame.K_e]: screen.blit(crosshaire, (230, 305))

    x = -1 if Keys[pygame.K_LEFT] else 1 if Keys[pygame.K_RIGHT] else 0
    y = -1 if Keys[pygame.K_UP] else 1 if Keys[pygame.K_DOWN] else 0

    print(x)
    print(y)

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(crosshairf,((x*30)+130-5,(y*30)+295-5))

    pygame.display.flip()

    clk.tick(40)