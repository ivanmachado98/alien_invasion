class Settings:
    """Clase que gestiona todas las configuraciones del juego."""

    def __init__(self):
        """Inicializa las configuraciones del juego."""
        self.screen_width = 1600
        self.screen_height = 900
        self.bg_color = (230, 230, 230)

        # Configuraciones de la nave.
        self.ship_speed = 10.0

        # Configuraciones de las balas.
        self.bullet_speed = 12.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.allowed_bullets = 3