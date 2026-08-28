import pygame

from pygame.sprite import Sprite

class Alien(Sprite):
    """Clase que crea y gestiona los aliens del juego."""

    def __init__(self, ai_game):
        """Inicializa el alien y sus configuraciones."""
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Carga la imagen y obtiene su rect
        self.image = pygame.image.load('imagenes/alien.bmp')
        self.rect = self.image.get_rect()

        # Ubica el alien cerca de la parte superior izquierda de la pantalla.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Guarda posición x como flotante.
        self.x = float(self.rect.x)

    def update(self):
        """Mueve los aliens hacia la derecha de la pantalla."""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = int(self.x)

    def check_edges(self):
        """Comprueba si un alien ha llegado al borde de la pantalla."""
        return (
            self.rect.right >= self.screen_rect.right or 
            self.rect.left <= 0
        )