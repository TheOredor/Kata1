import pygame

#variables
screen_width = 1280
screen_height = 960

#colores
white_color = (200, 200, 200)
light_grey = pygame.Color('grey12')

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((screen_width, screen_height))

rectangulo = pygame.Rect(10, 10, 50, 50)
speed = 0

def mover_rectangulo():
    global speed # para que pueda coger coger la variable speed que de normal no puede coger una funcon lo de fuera
    if rectangulo.top + 50 < screen_height:
        rectangulo.top += speed

while True:
    screen.fill(light_grey)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_UP:
                spped = -3
            elif event.type == pygame.K_DOWN:
                spped = 3
        elif event.type == pygame.KEYUP:
            speed = 0


    mover_rectangulo()
    
    pygame.draw. rect(screen, white_color, rectangulo)

    pygame.display.flip()
    clock.tick(60)

