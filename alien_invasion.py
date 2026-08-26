import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """Clase general para gestionar los recursos y el comportamiento del juego."""

    def __init__(self):
        """Inicializa el juego y crea los recursos del juego."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        # Configuración de la pantalla
        self.screen = pygame.display.set_mode((self.settings.screen_width,
            self.settings.screen_height), vsync=1)
        pygame.display.set_caption("Alien Invasion")

        # Crea instancia de la nave.
        self.ship = Ship(self)

    def run_game(self):
        """Inicia el bucle principal del juego."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Responde a las pulsaciones de teclas y eventos del ratón."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Responde a las pulsaciones de teclas."""
        if event.key == pygame.K_q:
            pygame.quit()
            exit()
        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True

    def _check_keyup_events(self, event):
        """Responde a levantamientos de teclas."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        """Actualiza las imágenes en la pantalla y pasa a la nueva pantalla."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        pygame.display.flip()

if __name__ == '__main__':
    # Crea una instancia del juego y lo ejecuta.
    ai = AlienInvasion()
    ai.run_game()