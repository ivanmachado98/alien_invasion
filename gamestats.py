class GameStats:
    """Clase que sigue las estadísticas del juego."""

    def __init__(self, ai_game):
        """Inicializa estadístcias que pueden cambiar."""
        self.settings = ai_game.settings
        self.prep_stats()

    def prep_stats(self):
        """Prepara estadísticas de la nave."""
        self.ships_left = self.settings.allowed_ships