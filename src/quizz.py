import pygame
from game import Juego  # Asegúrate de que este import sea correcto


def main():
    # Inicializar Pygame
    pygame.init()

    # Configurar la pantalla
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Juego de Preguntas")

    # Crear una instancia de la clase Juego
    juego = Juego(screen)

    # Mostrar la pantalla de bienvenida
    juego.mostrar_pantalla_bienvenida()

    # Bucle principal del juego
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()


if __name__ == "__main__":
    main()