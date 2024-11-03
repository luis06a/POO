import pygame
import json
from game import Juego  # Asegúrate de que este import sea correcto

# Cargar preguntas desde un archivo JSON
def cargar_preguntas(archivo):
    with open(archivo, 'r', encoding='utf-8') as f:
        preguntas = json.load(f)
    return preguntas

def main():
    # Inicializar Pygame
    pygame.init()

    # Configurar la pantalla
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Juego de Preguntas")

    # Crear una instancia de la clase Juego
    juego = Juego(screen)

    # Cargar preguntas
    preguntas = cargar_preguntas('preguntas.json')
    juego.cargar_preguntas(preguntas)

    # Mostrar la pantalla de bienvenida
    juego.mostrar_pantalla_bienvenida()

    # Reloj para controlar los FPS
    clock = pygame.time.Clock()

    # Bucle principal del juego
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:  # Captura el evento de tecla
                if event.key in [pygame.K_a, pygame.K_b, pygame.K_c, pygame.K_d]:  # Suponiendo que las respuestas son A, B, C, D
                    letra_respuesta = pygame.key.name(event.key).upper()  # Convierte la tecla a letra
                    if juego.verificar_respuesta(letra_respuesta):
                        print("¡Respuesta correcta!")
                    else:
                        print("Respuesta incorrecta.")
                    juego.pregunta_actual += 1  # Avanza a la siguiente pregunta

        # Dibujar la pantalla
        juego.dibujar()  # Llama al método para dibujar preguntas y respuestas

        # Controlar la condición de fin de juego
        if juego.pregunta_actual >= len(juego.preguntas):
            # Si se han respondido todas las preguntas, puedes mostrar un mensaje de fin
            juego.screen.fill((0, 0, 0))  # Limpiar la pantalla
            font = pygame.font.Font(None, 36)
            text = font.render("¡Fin del juego!", True, (255, 255, 255))
            juego.screen.blit(text, (50, 250))
            pygame.display.flip()
            pygame.time.delay(3000)  # Espera 3 segundos antes de salir
            running = False

        # Controlar los FPS
        clock.tick(60)  # Limita el juego a 60 FPS

    pygame.quit()

if __name__ == "__main__":
    main()

