from pico2d import*

class Weapon:
    def __init__(self):
        self.image = load_image('image\\etc\\ballista.png')
        self.locaction = 0
        self.launch = False
        self.frame = 0

    def update(self):
#        self.fraem = (self.fraem + 1)
        if self.locaction == 0:
            self.x, self.y = 100, 250
        elif self.locaction == 1:
            self.x, self.y = 200, 200
        elif self.locaction == 2:
            self.x, self.y = 300, 150
        elif self.locaction == 3:
            self.x, self.y = 400, 100

    def draw(self):
        self.image.clip_draw(0,0,117,134,self.x,self.y)
