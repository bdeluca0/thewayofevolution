from dino_runner.utils.constants import TIRO, TIRO_TYPE
from dino_runner.components.powerups.power_up import PowerUp


class Bullet(PowerUp):
    def __init__(self):
        self.image = TIRO
        self.type = TIRO_TYPE
        super().__init__(self.image, self.type)