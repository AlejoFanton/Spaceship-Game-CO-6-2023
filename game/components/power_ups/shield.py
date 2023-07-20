from game.utils.constants import SHIELD, SHIELD_TYPE
from game.components.power_ups.power_up import PowerUp

class Shield(PowerUp):
    def __init__(self):
        self.image = SHIELD
        super().__init__(self.image)