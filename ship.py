import pygame

class Ship:
    """Una clase para gestionar recursos y comportamiendo de la nave."""

    def __init__(self, ai_game):
        """Inicializa recursos y configuracines de la nave."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Carga la imagen y obtiene su rect.
        self.image = pygame.image.load('imagenes/ship.bmp')
        self.rect = self.image.get_rect()

        # Ubica la nave en el centro del borde inferior de la pantalla.
        self.rect.midbottom = self.screen_rect.midbottom

        # Guarda posición x como flotante.
        self.x = float(self.rect.x)

        # Banderas de movimiento.
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Mueve la nave segun las banderas de movimiento."""
        # Actualiza posición de la imagen.
        if self.moving_right:
            self.x += self.settings.ship_speed
        if self.moving_left:
            self.x -= self.settings.ship_speed

        max_x = self.screen_rect.right - self.rect.width

        if self.x > max_x:
            self.x = max_x
        elif self.x < 0:
            self.x = 0

        # Actualiza posición del rect.
        self.rect.x = int(self.x)

    def center_ship(self):
        """Centra la nave en la pantalla."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def blitme(self):
        """Dibuja la nave en la pantalla."""
        self.screen.blit(self.image, self.rect)