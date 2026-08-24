import sys

import pygame

pygame.init()

# ventana
ancho = 800
alto = 600
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("HELLO PYGAME")

reloj = pygame.time.Clock()

# Definir colores (R, G, B)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
BLANCO = (255, 255, 255)
GRIS = (30, 30, 30)

print("Iniciando")
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            run = False
            print("Cerrando la ventana")

    # Limpiar la pantalla con el color gris
    ventana.fill(GRIS)

    # Dibujar en circulo pantalla
    pygame.draw.circle(ventana, BLANCO, (400, 300), 40, 3)

    # Mostrar los cambios en la pantalla
    pygame.display.flip()

    # controlar los fps
    reloj.tick(60)

pygame.quit()
sys.exit()