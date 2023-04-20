from dino_runner.utils.constants import BIRD
from dino_runner.components.obstacles.obstacle import Obstacle



class Bird(Obstacle):
    def __init__(self):
        super().__init__(BIRD, 0)
        self.rect.y = 270
        self.step_index = 0
