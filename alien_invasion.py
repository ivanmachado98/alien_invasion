import sys
import pygame

from time import sleep

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

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

        # Crea la bolsa de las balas y aliens.
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        """Inicia el bucle principal del juego."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Responde a las pulsaciones de teclas y eventos del ratón."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
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
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Responde a levantamientos de teclas."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Crea una bala y la añade al grupo de balas."""
        if len(self.bullets) < self.settings.allowed_bullets:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Actualiza posición de las balas y se deshace se las viejas."""
        self._check_bullet_alien_collisions()
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)

    def _check_bullet_alien_collisions(self):
        """Responde a colisiones bala alien."""
        collision = pygame.sprite.groupcollide(self.bullets, self.aliens,
            False, True)

        if not self.aliens:
            # Borra las balas restantes y crea una nueva flota.
            self.bullets.empty()
            self._create_fleet()

    def _create_fleet(self):
        """Crea la flota de aliens."""
        # Hace un alien y lo agrega a la fila.
        # La distancia entre cada alien es igual a su anchura.
        alien = Alien(self)
        alien_width, alien_heigth = alien.rect.size

        current_x, current_y = alien_width, 2 * alien_heigth
        while current_y < (self.settings.screen_height - 4 * alien_heigth):
            while current_x < (self.settings.screen_width - alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width

            # Fila terminada; resetea (x) y aumenta (y).
            current_x = alien_width
            current_y += 2 * alien_heigth

    def _create_alien(self, x_position, y_position):
        """Crea un alien y lo agrega a la bolsa de aliens"""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _update_aliens(self):
        """Actualiza la posición de cada alien."""
        # Comprueba colisiones nave-alien.
        self._check_alien_ship_collisions()
        self.aliens.update()

        # Comprueba bordes del alien.
        self._check_alien_edges()

        # Comprueba si los aliens han llegado al fonde de la pantalla.
        self._check_alien_bottom()

    def _check_alien_ship_collisions(self):
        """Responde si un alien choco con la nave."""
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

    def _ship_hit(self):
        """Responde si la nave ha sido alcanzada."""
        # Elimina balas y aliens restantes.
        self.aliens.empty()
        self.bullets.empty()

        # Crea una nueva flota y centra la nave.
        self._create_fleet()
        self.ship.center_ship()

        # Pausa.
        sleep(0.5)

    def _check_alien_edges(self):
        """Responde si un alien llego al borde"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Baja toda la flota y cambia su dirección."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_alien_bottom(self):
        """Responde si un alien ha llegado al fondo de la pantalla."""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                # Trata esto como si la nave hubiese sido alcanzada.
                self._ship_hit()
                break

    def _update_screen(self):
        """Actualiza las imágenes en la pantalla y pasa a la nueva pantalla."""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()

        # Dibuja los aliens.
        self.aliens.draw(self.screen)

        pygame.display.flip()

if __name__ == '__main__':
    # Crea una instancia del juego y lo ejecuta.
    ai = AlienInvasion()
    ai.run_game()