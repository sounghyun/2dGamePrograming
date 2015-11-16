from pico2d import *
import frist_stage
import random
import json

monster_data_file = open('data\\monster_data.txt', 'r')
monster_data = json.load(monster_data_file)
monster_data_file.close()

class Ice_wolf:

    PIXEL_PER_METER = (10.0 / 0.5)           # 10 pixel 50 cm
    RUN_SPEED_KMPH = monster_data['Ice_wolf']['speed']                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 1
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 6

    image = None
    image_die = None

    RUN, HIT, DIE = 0, 1, 2

    def handle_run(self, frame_time):
        self.total_frames += Ice_wolf.FRAMES_PER_ACTION * Ice_wolf.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 6
        self.x -= Ice_wolf.RUN_SPEED_PPS * frame_time
        self.y -= (Ice_wolf.RUN_SPEED_PPS * frame_time)/2

    def handle_hit(self, frame_time):
        self.hit_motion_delay += frame_time
        if(self.hit_motion_delay > 0.3):
            self.hp -= 1
            self.hit_motion_delay = 0.0
            if self.hp == 0:
                self.state = self.DIE
            else:
                self.state = self.RUN

    def handle_die(self, frame_time):
        global frist_stage
        self.location = random.randint(1,4)
        self.create_object()
        self.hp = monster_data['Ice_wolf']['hp']
        frist_stage.score.score += monster_data['Ice_wolf']['score']
        self.state = self.RUN

    handle_state = {
        RUN : handle_run,
        HIT : handle_hit,
        DIE : handle_die
    }

    def create_object(self):
        if self.location == 1:
            self.x, self.y = 1000, 700
        elif self.location == 2:
            self.x, self.y = 1100, 650
        elif self.location == 3:
            self.x, self.y = 1200, 600
        elif self.location == 4:
            self.x, self.y = 1300, 550

    def __init__(self):
        self.location = random.randint(1,4)
        self.create_object()
        self.total_frames = 0.0
        self.frame = 0
        self.state = self.RUN
        self.hp = monster_data['Ice_wolf']['hp']
        self.hit_motion_delay = 0.0
        if Ice_wolf.image == None:
            self.image = load_image('image\\monster\\ice_wolf.png')
        if Ice_wolf.image_die == None:
            self.image_die = load_image('image\\monster\\ice_wolf_die.png')

    def update(self, frame_time):
        self.handle_state[self.state](self, frame_time)

        if self.x < 0:
            self.location = random.randint(1,4)
            frist_stage.Life.life -= 1
            self.create_object()
            self.hp = monster_data['Ice_wolf']['hp']

    def draw(self):
        if self.state == self.HIT:
            self.image_die.clip_draw(0,0,109,110,self.x,self.y)
        else:
            self.image.clip_draw(135 * self.frame, 0, 135, 90, self.x, self.y)

class Yeti:

    PIXEL_PER_METER = (10.0 / 0.5)           # 10 pixel 50 cm
    RUN_SPEED_KMPH = monster_data['Yeti']['speed']                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 1
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 7

    image = None
    image_die = None

    RUN, HIT, DIE = 0, 1, 2

    def handle_run(self, frame_time):
        global frist_stage
        self.total_frames += Yeti.FRAMES_PER_ACTION * Yeti.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 7
        self.x -= Yeti.RUN_SPEED_PPS * frame_time
        self.y -= (Yeti.RUN_SPEED_PPS * frame_time)/2

    def handle_hit(self, frame_time):
        self.hit_motion_delay += frame_time
        if(self.hit_motion_delay > 0.3):
            self.hp -= 1
            self.hit_motion_delay = 0.0
            if self.hp == 0:
                self.state = self.DIE
            else:
                self.state = self.RUN

    def handle_die(self, frame_time):
        global frist_stage
        self.location = random.randint(1,4)
        self.create_object()
        self.hp = monster_data['Yeti']['hp']
        frist_stage.score.score += monster_data['Yeti']['score']
        self.state = self.RUN

    handle_state = {
        RUN : handle_run,
        HIT : handle_hit,
        DIE : handle_die
    }

    def create_object(self):
        if self.location == 1:
            self.x, self.y = 1000, 700
        elif self.location == 2:
            self.x, self.y = 1100, 650
        elif self.location == 3:
            self.x, self.y = 1200, 600
        elif self.location == 4:
            self.x, self.y = 1300, 550

    def __init__(self):
        self.location = random.randint(1,4)
        self.create_object()
        self.total_frames = 0.0
        self.frame = 0
        self.state = self.RUN
        self.hp = monster_data['Yeti']['hp']
        self.hit_motion_delay = 0.0
        if Yeti.image == None:
            self.image = load_image('image\\monster\\yeti.png')
        if Yeti.image_die == None:
            self.image_die = load_image('image\\monster\\yeti_die.png')

    def update(self, frame_time):
        self.handle_state[self.state](self, frame_time)


        if self.x < 0:
            self.location = random.randint(1,4)
            frist_stage.Life.life -=1
            self.create_object()
            self.hp = monster_data['Yeti']['hp']

    def draw(self):
        if self.state == self.HIT:
            self.image_die.clip_draw(0,0,137,120,self.x,self.y)
        else:
            self.image.clip_draw(100 * self.frame, 0, 100, 120, self.x, self.y)

class Bonus:

    PIXEL_PER_METER = (10.0 / 0.5)           # 10 pixel 50 cm
    RUN_SPEED_KMPH = monster_data['Bonus']['speed']     # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 6

    image = None
    image_die = None

    RUN, HIT, DIE = 0, 1, 2

    def handle_run(self, frame_time):
        global frist_stage
        self.total_frames += Bonus.FRAMES_PER_ACTION * Bonus.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 6
        self.x -= Bonus.RUN_SPEED_PPS * frame_time
        self.y -= (Bonus.RUN_SPEED_PPS * frame_time)/2

    def handle_hit(self, frame_time):
        self.hit_motion_delay += frame_time
        if(self.hit_motion_delay > 0.3):
            self.hp -= 1
            self.hit_motion_delay = 0.0
            if self.hp == 0:
                self.state = self.DIE
            else:
                self.state = self.RUN

    def handle_die(self, frame_time):
        global frist_stage
        self.location = random.randint(1,4)
        self.create_object()
        self.hp = monster_data['Bonus']['hp']
        frist_stage.score.score += monster_data['Bonus']['score']
        self.state = self.RUN

    handle_state = {
        RUN : handle_run,
        HIT : handle_hit,
        DIE : handle_die
    }

    def create_object(self):
        if self.location == 1:
            self.x, self.y = 1000, 700
        elif self.location == 2:
            self.x, self.y = 1100, 650
        elif self.location == 3:
            self.x, self.y = 1200, 600
        elif self.location == 4:
            self.x, self.y = 1300, 550

    def __init__(self):
        self.location = random.randint(1,4)
        self.create_object()
        self.total_frames = 0.0
        self.frame = 0
        self.state = self.RUN
        self.hp = monster_data['Bonus']['hp']
        self.hit_motion_delay = 0.0
        if Bonus.image == None:
            self.image = load_image('image\\monster\\bonus.png')
        if Bonus.image_die == None:
            self.image_die = load_image('image\\monster\\bonus_die.png')

    def update(self, frame_time):
        self.handle_state[self.state](self, frame_time)

        if self.x < 0:
            self.location = random.randint(1,4)
            frist_stage.Life.life -=1
            self.create_object()
            self.hp = monster_data['Bonus']['hp']

    def draw(self):
        if self.state == self.HIT:
            self.image_die.clip_draw(0,0,90,120,self.x,self.y, 60, 80)
        else:
            self.image.clip_draw(90 * self.frame, 0, 90, 120, self.x, self.y, 60, 80)

class Falcon:

    PIXEL_PER_METER = (10.0 / 0.5)           # 10 pixel 50 cm
    RUN_SPEED_KMPH = monster_data['Falcon']['speed']                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 10

    image = None
    image_die = None

    RUN, HIT, DIE = 0, 1, 2

    def handle_run(self, frame_time):
        global frist_stage
        self.total_frames += Falcon.FRAMES_PER_ACTION * Falcon.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 10
        self.x -= Falcon.RUN_SPEED_PPS * frame_time
        self.y -= (Falcon.RUN_SPEED_PPS * frame_time)/2

    def handle_hit(self, frame_time):
        self.hit_motion_delay += frame_time
        if(self.hit_motion_delay > 0.3):
            self.hp -= 1
            self.hit_motion_delay = 0.0
            if self.hp == 0:
                self.state = self.DIE
            else:
                self.state = self.RUN

    def handle_die(self, frame_time):
        global frist_stage
        self.location = random.randint(1,4)
        self.create_object()
        self.hp = monster_data['Falcon']['hp']
        frist_stage.score.score += monster_data['Falcon']['score']
        self.state = self.RUN

    handle_state = {
        RUN : handle_run,
        HIT : handle_hit,
        DIE : handle_die
    }

    def create_object(self):
        if self.location == 1:
            self.x, self.y = 1000, 700
        elif self.location == 2:
            self.x, self.y = 1100, 650
        elif self.location == 3:
            self.x, self.y = 1200, 600
        elif self.location == 4:
            self.x, self.y = 1300, 550

    def __init__(self):
        self.location = random.randint(1,4)
        self.create_object()
        self.total_frames = 0.0
        self.frame = 0
        self.state = self.RUN
        self.hp = monster_data['Falcon']['hp']
        self.hit_motion_delay = 0.0
        if Falcon.image == None:
            self.image = load_image('image\\monster\\falcon.png')
        if Falcon.image_die == None:
            self.image_die = load_image('image\\monster\\falcon_die.png')

    def update(self, frame_time):
        self.handle_state[self.state](self, frame_time)

        if self.x < 0:
            self.location = random.randint(1,4)
            frist_stage.Life.life -=1
            self.create_object()
            self.hp = monster_data['Falcon']['hp']

    def draw(self):
        if self.state == self.HIT:
            if self.hp < 1:
                self.image_die.clip_draw(0,0,110,85,self.x,self.y)
            else:
                self.image_die.clip_draw(110,0,110,85,self.x,self.y)
        else:
            self.image.clip_draw(150 * self.frame, 0, 150, 121, self.x, self.y)
