import pygame
class Juego:
    def __init__(self, screen):
        self.screen = screen
        self.preguntas = []  # Inicializa la lista de preguntas
        self.pregunta_actual = 0  # Controla cuál pregunta se muestra
        self.respuesta_usuario = None  # Almacena la respuesta del usuario

    def mostrar_pantalla_bienvenida(self):
        self.screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 36)
        text = font.render("BIENVENIDO AL JUEGO DE PREGUNTAS", True, (255, 255, 255))
        self.screen.blit(text, (50, 250))
        pygame.display.flip()
        pygame.time.delay(2000)  # Espera 2 segundos

    def cargar_preguntas(self, preguntas):
        self.preguntas = preguntas

    def dibujar(self):
        self.screen.fill((0, 0, 0))  # Limpiar la pantalla

        # Mostrar la pregunta actual
        if self.pregunta_actual < len(self.preguntas):
            pregunta = self.preguntas[self.pregunta_actual]
            font = pygame.font.Font(None, 36)
            text = font.render(pregunta["pregunta"], True, (255, 255, 255))
            self.screen.blit(text, (50, 50))  # Posición de la pregunta

            # Mostrar las respuestas
            for i, (letra, respuesta) in enumerate(pregunta["respuestas"].items()):
                respuesta_text = font.render(f"{letra}: {respuesta}", True, (255, 255, 255))
                self.screen.blit(respuesta_text, (50, 100 + i * 40))  # Posición de las respuestas
        else:
            # Si no hay más preguntas, mostrar mensaje de finalización
            font = pygame.font.Font(None, 36)
            text = font.render("¡Fin del juego!", True, (255, 255, 255))
            self.screen.blit(text, (50, 250))

        pygame.display.flip()  # Actualizar la pantalla

    def verificar_respuesta(self, respuesta):
        pregunta = self.preguntas[self.pregunta_actual]
        return respuesta == pregunta["respuesta_correcta"]  # Comparar con la respuesta correcta