from pico2d import *
import random
import frist_stage

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
        self.diecount = 0
        self.time = random.randint(0,30)
        self.count = 0
        self.image = load_image('image\\monster\\ice_wolf.png')
        self.image_die = load_image('image\\monster\\ice_wolf_die.png')

    def update(self, Ttime):
        global frist_stage
        if self.dieck:
            if Ttime % 20 == 0:
                self.count += 1
                if self.count > 4:
                    self.count = 0
                    self.dieck = False
                    self.x = -1
                    frist_stage.score.score += 200
        else:
            if Ttime % 30 == 0:
                self.frame = (self.frame + 1) % 7
            if Ttime % 4 == 0:
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
            self.image_die.clip_draw(0,0,109,110,self.x,self.y)
        else:
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
        self.diecount = 0
        self.time = random.randint(0,30)
        self.count = 0
        self.image = load_image('image\\monster\\yeti.png')
        self.image_die = load_image('image\\monster\\yeti_die.png')

    def update(self, Ttime):
        global frist_stage
        if self.dieck:
            if Ttime % 20 == 0:
                self.count += 1
                if self.count > 4:
                    self.count = 0
                    self.dieck = False
                    if self.diecount == 4:
                        self.x = -1
                        frist_stage.score.score += 400
                    self.diecount += 1
        else:
            if Ttime % 10 == 0:
                self.frame = (self.frame + 1) % 7
            if Ttime % 10 == 0:
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
            self.diecount = 0

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
        self.diecount = 0
        self.time = random.randint(0,100)
        self.count = 0
        self.image = load_image('image\\monster\\bonus.png')
        self.image_die = load_image('image\\monster\\bonus_die.png')

    def update(self, Ttime):
        global frist_stage
        if self.dieck:
            if Ttime % 20 == 0:
                self.count += 1
                if self.count > 4:
                    self.count = 0
                    self.dieck = False
                    if self.diecount == 1:
                        self.x = -1
                        frist_stage.score.score += 1000
                    self.diecount += 1
        else:
            if Ttime % 25 == 0:
                self.frame = (self.frame + 1) % 6
            if Ttime % 5 == 0:
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
            self.diecount = 0

    def draw(self):
        if self.dieck:
            self.image_die.clip_draw(0,0,90,120,self.x,self.y, 60, 80)
        else:
            self.image.clip_draw(90 * self.frame, 0, 90, 120, self.x, self.y, 60, 80)

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
        self.diecount = 0
        self.time = random.randint(0,100)
        self.count = 0
        self.image = load_image('image\\monster\\falcon.png')
        self.image_die = load_image('image\\monster\\falcon_die.png')

    def update(self, Ttime):
        global frist_stage
        if self.dieck:
            if Ttime % 20 == 0:
                self.count += 1
                if self.count > 4:
                    self.count = 0
                    self.dieck = False
                    if self.diecount == 1:
                        self.x = -1
                        frist_stage.score.score += 300
                    self.diecount += 1
        else:
            if Ttime % 10 == 0:
                self.frame = (self.frame + 1) % 10
            if Ttime % 3 == 0:
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
            self.diecount = 0

    def draw(self):
        if self.dieck:
            if self.diecount < 1:
                self.image_die.clip_draw(0,0,110,85,self.x,self.y)
            else:
                self.image_die.clip_draw(110,0,110,85,self.x,self.y)
        else:
            self.image.clip_draw(150 * self.frame, 0, 150, 121, self.x, self.y)
