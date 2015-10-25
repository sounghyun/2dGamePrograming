from pico2d import*
import random
import frist_stage

class Heroine:
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
        self.image = load_image('image\\forces\\heroine.png')
        self.image_die = load_image('image\\forces\\heroine_die.png')

    def update(self, Ttime):
        global frist_stage
        if self.dieck:
            if Ttime % 20 == 0:
                self.count += 1
                if self.count > 4:
                    self.count = 0
                    self.dieck = False
                    if self.diecount == 2:
                        self.x = -1
                        frist_stage.score.score -= 10000
                    self.diecount += 1
        else:
            if Ttime % 10 == 0:
                self.frame = (self.frame + 1) % 10
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
            if self.diecount < 2:
                self.image_die.clip_draw(0,0,60,87,self.x,self.y)
            else:
                self.image_die.clip_draw(60,0,60,87,self.x,self.y)
        else:
            self.image.clip_draw(50 * self.frame, 0, 50, 90, self.x, self.y)

class Amazon:
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
        self.image = load_image('image\\forces\\amazon.png')
        self.image_die = load_image('image\\forces\\amazon_die.png')

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
                        frist_stage.score.score -= 500
                    self.diecount += 1
        else:
            if Ttime % 13 == 0:
                self.frame = (self.frame + 1) % 10
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
            if self.diecount < 1:
                self.image_die.clip_draw(0,0,100,85,self.x,self.y)
            else :
                self.image_die.clip_draw(100,0,100,85,self.x,self.y)
        else:
            self.image.clip_draw(100 * self.frame, 0, 100, 85, self.x, self.y)

class General:
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
        self.image = load_image('image\\forces\\general.png')
        self.image_die = load_image('image\\forces\\general_die.png')

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
                        frist_stage.score.score -= 500
                    self.diecount += 1
        else:
            if Ttime % 25 == 0:
                self.frame = (self.frame + 1) % 6
            if Ttime % 6 == 0:
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
            self.image_die.clip_draw(0,0,86,106,self.x,self.y)
        else:
            self.image.clip_draw(70 * self.frame, 0, 70, 100, self.x, self.y)

class Soldier:
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
        self.image = load_image('image\\forces\\soldier.png')
        self.image_die = load_image('image\\forces\\soldier_die.png')

    def update(self, Ttime):
        global frist_stage
        if self.dieck:
            if Ttime % 20 == 0:
                self.count += 1
                if self.count > 4:
                    self.count = 0
                    self.dieck = False
                    self.x = -1
                    frist_stage.score.score -= 300
        else:
            if Ttime % 25 == 0:
                self.frame = (self.frame + 1) % 6
            if Ttime % 7 == 0:
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
            self.image_die.clip_draw(0,0,75,87,self.x,self.y)
        else:
            self.image.clip_draw(80 * self.frame, 0, 80, 100, self.x, self.y)