from pico2d import get_canvas_width, load_image

import game_world


class Ball:
    image = None

    def __init__(self, x, y, direction):
        if Ball.image is None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y = x, y
        self.direction = direction
        self.speed = 8

    def update(self):
        self.x += self.direction * self.speed
        if self.x < -Ball.image.w / 2 or self.x > get_canvas_width() + Ball.image.w / 2:
            game_world.remove_object(self)

    def draw(self):
        Ball.image.draw(self.x, self.y)
