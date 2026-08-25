import pygame

from settings import Settings

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

    def run_game(self):
        """Inicia el bucle principal del juego."""
        while True:
            self._check_events()
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

    def _check_keydown_events(self, event):
        """Responde a las pulsaciones de teclas."""
        if event.key == pygame.K_q:
            pygame.quit()
            exit()

    def _update_screen(self):
        """Actualiza las imágenes en la pantalla y pasa a la nueva pantalla."""
        self.screen.fill(self.settings.bg_color)
        pygame.display.flip()

if __name__ == '__main__':
    # Crea una instancia del juego y lo ejecuta.
    ai = AlienInvasion()
    ai.run_game()