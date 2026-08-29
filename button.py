import pygame.font

class Button:
    """Clase que sirve para crear botones."""

    def __init__(self, ai_game, msg):
        """Inicializa un objeto rect y sus configuraciones."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Configuracines y propiedades del botón.
        self.width, self.height = 200, 40
        self.button_color = (0, 0 , 0)
        self.text_color = (255, 0, 0)
        self.font = pygame.font.SysFont(None, 38)

        # Crea el objeto rect para el botón y lo centra.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Solo hay que preparar el mensaje una vez.
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Convierte msg en una imagen renderizada."""
        self.msg_image = self.font.render(msg, True, self.text_color,
            self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Dibuja el objeto rect y luego el texto."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)