from pico2d import *
import random

class Ice_wolf:
    def __init__(self):
        self.location = random.randint(1,4)
        if self.location == 1:
            self.x, self.y = 1000, 700
        elif self.location == 2:
            self.x, self.y = 1100, 650
        elif self.location == 3:
            self.x, self.y = 1200, 600
        elif self.location == 4:
            self.x, self.y = 1300, 550
        self.frame = 0
        self.dieck = False
        self.time = random.randint(0,30)
        self.count = 0
        self.image = load_image('image\\monster\\ice_wolf.png')
#        self.image_die = load_image('image\\monster\\falcon_die.png')

    def update(self):
        if self.dieck:
            self.count += 1
            if self.count > 4:
                self.count = 0
                self.dieck = False
        else:
            self.frame = (self.frame + 1) % 7
            self.x -= 8
            self.y -= 4
        if self.x < 0:
            self.location = random.randint(1,4)
            if self.location == 1:
                self.x, self.y = 1000, 700
            elif self.location == 2:
                self.x, self.y = 1100, 650
            elif self.location == 3:
                self.x, self.y = 1200, 600
            elif self.location == 4:
                self.x, self.y = 1300, 550

    def draw(self):
#        if self.dieck:
#            self.image_die.clip_draw(90 * self.count,0,90,120,self.x,self.y)
#        else:
            self.image.clip_draw(135 * self.frame, 0, 135, 90, self.x, self.y)

class Yeti:
    def __init__(self):
        self.location = random.randint(1,4)
        if self.location == 1:
            self.x, self.y = 1000, 700
        elif self.location == 2:
            self.x, self.y = 1100, 650
        elif self.location == 3:
            self.x, self.y = 1200, 600
        elif self.location == 4:
            self.x, self.y = 1300, 550
        self.frame = 0
        self.dieck = False
        self.time = random.randint(0,30)
        self.count = 0
        self.image = load_image('image\\monster\\yeti.png')
        self.image_die = load_image('image\\monster\\yeti_die.png')

    def update(self):
        if self.dieck:
            self.count += 1
            if self.count > 4:
                self.count = 0
                self.dieck = False
        else:
            self.frame = (self.frame + 1) % 7
            self.x -= 2
            self.y -= 1
        if self.x < 0:
            self.location = random.randint(1,4)
            if self.location == 1:
                self.x, self.y = 1000, 700
            elif self.location == 2:
                self.x, self.y = 1100, 650
            elif self.location == 3:
                self.x, self.y = 1200, 600
            elif self.location == 4:
                self.x, self.y = 1300, 550

    def draw(self):
        if self.dieck:
            self.image_die.clip_draw(0,0,137,120,self.x,self.y)
        else:
            self.image.clip_draw(100 * self.frame, 0, 100, 120, self.x, self.y)

class Bonus:
    def __init__(self):
        self.location = random.randint(1,4)
        if self.location == 1:
            self.x, self.y = 1000, 700
        elif self.location == 2:
            self.x, self.y = 1100, 650
        elif self.location == 3:
            self.x, self.y = 1200, 600
        elif self.location == 4:
            self.x, self.y = 1300, 550
        self.frame = 0
        self.dieck = False
        self.time = random.randint(0,100)
        self.count = 0
        self.image = load_image('image\\monster\\bonus.png')
        self.image_die = load_image('image\\monster\\bonus_die.png')

    def update(self):
        if self.dieck:
            self.count += 1
            if self.count > 4:
                self.count = 0
                self.dieck = False
        else:
            self.frame = (self.frame + 1) % 6
            self.x -= 6
            self.y -= 3
        if self.x < 0:
            self.location = random.randint(1,4)
            if self.location == 1:
                self.x, self.y = 1000, 700
            elif self.location == 2:
                self.x, self.y = 1100, 650
            elif self.location == 3:
                self.x, self.y = 1200, 600
            elif self.location == 4:
                self.x, self.y = 1300, 550

    def draw(self):
        if self.dieck:
            self.image_die.clip_draw(90 * self.count,0,90,120,self.x,self.y)
        else:
            self.image.clip_draw(90 * self.frame, 0, 90, 120, self.x, self.y)

class Falcon:
    def __init__(self):
        self.location = random.randint(1,4)
        if self.location == 1:
            self.x, self.y = 1000, 700
        elif self.location == 2:
            self.x, self.y = 1100, 650
        elif self.location == 3:
            self.x, self.y = 1200, 600
        elif self.location == 4:
            self.x, self.y = 1300, 550
        self.frame = 0
        self.dieck = False
        self.time = random.randint(0,100)
        self.count = 0
        self.image = load_image('image\\monster\\falcon.png')
#        self.image_die = load_image('image\\monster\\falcon_die.png')

    def update(self):
        if self.dieck:
            self.count += 1
            if self.count > 4:
                self.count = 0
                self.dieck = False
        else:
            self.frame = (self.frame + 1) % 10
            self.x -= 8
            self.y -= 4
        if self.x < 0:
            self.location = random.randint(1,4)
            if self.location == 1:
                self.x, self.y = 1000, 700
            elif self.location == 2:
                self.x, self.y = 1100, 650
            elif self.location == 3:
                self.x, self.y = 1200, 600
            elif self.location == 4:
                self.x, self.y = 1300, 550

    def draw(self):
#        if self.dieck:
#            self.image_die.clip_draw(90 * self.count,0,90,120,self.x,self.y)
#        else:
            self.image.clip_draw(150 * self.frame, 0, 150, 121, self.x, self.y)
