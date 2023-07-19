from game.utils.constants import SHIELD, SHIELD_TYPE
from game.components.power.power import Power

class Shield(Power):
    def __init__(self):
        super().__init__(SHIELD,SHIELD_TYPE)