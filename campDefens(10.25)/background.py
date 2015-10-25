from pico2d import *

class Background:
    def __init__(self):
        self.x, self.y = 500,300
        self.frame = 0
        self.sum = 1
        self.time = 0
        self.image = load_image('image\\main_background.png')

    def update(self):
        self.time += 1
        if self.time % 300 == 0:
            self.frame = (self.frame + self.sum) % 10
            if self.frame == 0 or self.frame == 9:
               self.sum *= -1

    def draw(self):
        self.image.clip_draw(500 * self.frame,0,500,340,self.x,self.y,1000,600)


