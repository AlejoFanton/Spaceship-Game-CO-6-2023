from game.components.enemies.enemy_handler import EnemyHandler

class Level:
    def __init__(self, enemy_handler, enemy_count):
        self.enemy_handler = enemy_handler
        self.enemy_count = enemy_count
        self.time_elapsed = 0

    def update(self, bullet_handler):
        self.enemy_handler.update(bullet_handler)
        self.time_elapsed += 1

    def draw(self, screen):
        self.enemy_handler.draw(screen)

    def is_completed(self):
        return self.enemy_handler.number_enemy_destroyed >= self.enemy_count

    def reset(self):
        self.enemy_handler.reset()
        self.time_elapsed = 0