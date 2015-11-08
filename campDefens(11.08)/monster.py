from pico2d import *
import frist_stage
import random

class Ice_wolf:

    RUN, HIT, DIE = 0, 1, 2

    def handle_run(self):
        global frist_stage
        if frist_stage.Ttime % 30 == 0:
            self.frame = (self.frame + 1) % 7
        if frist_stage.Ttime % 4 == 0:
            self.x -= 2
            self.y -= 1

    def handle_hit(self):
        global frist_stage
        if frist_stage.Ttime % 20 == 0:
            self.count += 1
            if self.count > 4:
                self.count = 0
                self.dieck = False
                self.diecount += 1
                if self.diecount == 1:
                    self.state = self.DIE

    def handle_die(self):
        global frist_stage
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
        frist_stage.score.score += 300
        self.state = self.RUN

    handle_state = {
        RUN : handle_run,
        HIT : handle_hit,
        DIE : handle_die
    }

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
        self.state = self.RUN
        self.dieck = False
        self.diecount = 0
        self.time = random.randint(0,30)
        self.count = 0
        self.image = load_image('image\\monster\\ice_wolf.png')
        self.image_die = load_image('image\\monster\\ice_wolf_die.png')

    def update(self):
        if self.dieck:
            self.state = self.HIT
        elif self.state != self.DIE:
            self.state = self.RUN

        self.handle_state[self.state](self)

        if self.x < 0:
            self.location = random.randint(1,4)
            frist_stage.Life.life -=1
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
    RUN, HIT, DIE = 0, 1, 2

    def handle_run(self):
        global frist_stage
        if frist_stage.Ttime % 10 == 0:
            self.frame = (self.frame + 1) % 7
        if frist_stage.Ttime % 10 == 0:
            self.x -= 2
            self.y -= 1

    def handle_hit(self):
        global frist_stage
        if frist_stage.Ttime % 20 == 0:
            self.count += 1
            if self.count > 4:
                self.count = 0
                self.dieck = False
                self.diecount += 1
                if self.diecount == 5:
                    self.state = self.DIE

    def handle_die(self):
        global frist_stage
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
        frist_stage.score.score += 1000
        self.state = self.RUN

    handle_state = {
        RUN : handle_run,
        HIT : handle_hit,
        DIE : handle_die
    }

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
        self.state = self.RUN
        self.dieck = False
        self.diecount = 0
        self.time = random.randint(0,30)
        self.count = 0
        self.image = load_image('image\\monster\\yeti.png')
        self.image_die = load_image('image\\monster\\yeti_die.png')

    def update(self):
        if self.dieck:
            self.state = self.HIT
        elif self.state != self.DIE:
            self.state = self.RUN

        self.handle_state[self.state](self)


        if self.x < 0:
            self.location = random.randint(1,4)
            frist_stage.Life.life -=1
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
    RUN, HIT, DIE = 0, 1, 2

    def handle_run(self):
        global frist_stage
        if frist_stage.Ttime % 25 == 0:
            self.frame = (self.frame + 1) % 6
        if frist_stage.Ttime % 5 == 0:
            self.x -= 2
            self.y -= 1

    def handle_hit(self):
        global frist_stage
        if frist_stage.Ttime % 20 == 0:
            self.count += 1
            if self.count > 4:
                self.count = 0
                self.dieck = False
                self.diecount += 1
                if self.diecount == 1:
                    self.state = self.DIE

    def handle_die(self):
        global frist_stage
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
        frist_stage.score.score += 3000
        self.state = self.RUN

    handle_state = {
        RUN : handle_run,
        HIT : handle_hit,
        DIE : handle_die
    }

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
        self.state = self.RUN
        self.dieck = False
        self.diecount = 0
        self.time = random.randint(0,100)
        self.count = 0
        self.image = load_image('image\\monster\\bonus.png')
        self.image_die = load_image('image\\monster\\bonus_die.png')

    def update(self):
        if self.dieck:
            self.state = self.HIT
        elif self.state != self.DIE:
            self.state = self.RUN

        self.handle_state[self.state](self)

        if self.x < 0:
            self.location = random.randint(1,4)
            frist_stage.Life.life -=1
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
    RUN, HIT, DIE = 0, 1, 2

    def handle_run(self):
        global frist_stage
        if frist_stage.Ttime % 10 == 0:
            self.frame = (self.frame + 1) % 10
        if frist_stage.Ttime % 3 == 0:
            self.x -= 2
            self.y -= 1

    def handle_hit(self):
        global frist_stage
        if frist_stage.Ttime % 20 == 0:
            self.count += 1
            if self.count > 4:
                self.count = 0
                self.dieck = False
                self.diecount += 1
                if self.diecount == 2:
                    self.state = self.DIE

    def handle_die(self):
        global frist_stage
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
        frist_stage.score.score += 300
        self.state = self.RUN

    handle_state = {
        RUN : handle_run,
        HIT : handle_hit,
        DIE : handle_die
    }

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
        self.state = self.RUN
        self.dieck = False
        self.diecount = 0
        self.time = random.randint(0,100)
        self.count = 0
        self.image = load_image('image\\monster\\falcon.png')
        self.image_die = load_image('image\\monster\\falcon_die.png')

    def update(self):
        if self.dieck:
            self.state = self.HIT
        elif self.state != self.DIE:
            self.state = self.RUN

        self.handle_state[self.state](self)

        if self.x < 0:
            self.location = random.randint(1,4)
            frist_stage.Life.life -=1
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
