class Settings:
    """Clase que gestiona todas las configuraciones del juego."""

    def __init__(self):
        """Inicializa las configuraciones del juego."""
        self.screen_width = 1600
        self.screen_height = 900
        self.bg_color = (230, 230, 230)

        # Configuraciones de la nave.
        self.ship_speed = 7.0