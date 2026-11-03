from pico2d import load_image


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw0(self):
        self.image.draw(400,30)

    def draw1(self):
        self.image.draw(400,40)

    def update(self):
        pass
