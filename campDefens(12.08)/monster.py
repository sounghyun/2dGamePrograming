from pico2d import *
import random
import json


monster_data_file = open('data\\monster_data.txt', 'r')
monster_data = json.load(monster_data_file)
monster_data_file.close()

stage_life = None
stage_score = None

def stage_set(life, score):
    global stage_life, stage_score
    stage_life = life
    stage_score = score

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
    hit_sound = None

    RUN, HIT, DIE = 0, 1, 2
    normal, speed_up, speed_down = 1.0, 1.5, 0.5

    def handle_run(self, frame_time):
        self.total_frames += Bonus.FRAMES_PER_ACTION * Bonus.ACTION_PER_TIME * frame_time * self.speed_state
        self.frame = int(self.total_frames) % 6
        self.x -= Bonus.RUN_SPEED_PPS * frame_time * self.speed_state
        self.y -= (Bonus.RUN_SPEED_PPS * frame_time)/2 * self.speed_state

    def handle_hit(self, frame_time):
        if self.hit_motion_delay == 0:
            self.hit_sound.play()
        self.hit_motion_delay += frame_time
        if(self.hit_motion_delay > 0.3):
            self.hp -= 1
            self.hit_motion_delay = 0.0
            if self.hp == 0:
                self.state = self.DIE
            else:
                self.state = self.RUN

    def handle_die(self, frame_time):
        global stage_life
        stage_life.life += monster_data['Bonus']['life']
        self.alive = False

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
        self.name = 'Bouns'
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
        if Bonus.hit_sound == None:
            self.hit_sound = load_wav('sound\\bonus_sound.ogg')
            self.hit_sound.set_volume(40)
        self.alive = True
        self.speed_state = self.normal
        self.buff_time = 0.0

    def update(self, frame_time):
        global stage_life
        self.handle_state[self.state](self, frame_time)

        if self.x < 0:
            stage_life.life -=1
            self.alive = False

    def draw(self):
        if self.state == self.HIT:
            self.image_die.clip_draw(0,0,90,120,self.x,self.y, 60, 80)
        else:
            self.image.clip_draw(90 * self.frame, 0, 90, 120, self.x, self.y, 60, 80)


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
    hit_sound = None

    RUN, HIT, DIE = 0, 1, 2
    normal, speed_up, speed_down = 1.0, 1.5, 0.5

    def handle_run(self, frame_time):
        self.total_frames += Ice_wolf.FRAMES_PER_ACTION * Ice_wolf.ACTION_PER_TIME * frame_time * self.speed_state
        self.frame = int(self.total_frames) % 6
        self.x -= Ice_wolf.RUN_SPEED_PPS * frame_time * self.speed_state
        self.y -= (Ice_wolf.RUN_SPEED_PPS * frame_time)/2 * self.speed_state

    def handle_hit(self, frame_time):
        if self.hit_motion_delay == 0:
            self.hit_sound.play()
        self.hit_motion_delay += frame_time
        if(self.hit_motion_delay > 0.3):
            self.hp -= 1
            self.hit_motion_delay = 0.0
            if self.hp == 0:
                self.state = self.DIE
            else:
                self.state = self.RUN

    def handle_die(self, frame_time):
        global stage_score
        stage_score.score += monster_data['Ice_wolf']['score']
        self.alive = False

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
        self.name = 'Ice_wolf'
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
        if Ice_wolf.hit_sound == None:
            self.hit_sound = load_wav('sound\\ice_wolf_sound.ogg')
            self.hit_sound.set_volume(40)
        self.alive = True
        self.speed_state = self.normal
        self.buff_time = 0.0

    def update(self, frame_time):
        global stage_life
        self.handle_state[self.state](self, frame_time)

        if self.x < 0:
            stage_life.life -= 1
            self.alive = False

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
    hit_sound = None

    RUN, HIT, DIE = 0, 1, 2
    normal, speed_up, speed_down = 1.0, 1.5, 0.5

    def handle_run(self, frame_time):
        self.total_frames += Yeti.FRAMES_PER_ACTION * Yeti.ACTION_PER_TIME * frame_time  * self.speed_state
        self.frame = int(self.total_frames) % 7
        self.x -= Yeti.RUN_SPEED_PPS * frame_time * self.speed_state
        self.y -= (Yeti.RUN_SPEED_PPS * frame_time)/2 * self.speed_state

    def handle_hit(self, frame_time):
        if self.hit_motion_delay == 0:
            self.hit_sound.play()
        self.hit_motion_delay += frame_time
        if(self.hit_motion_delay > 0.3):
            self.hp -= 1
            self.hit_motion_delay = 0.0
            if self.hp == 0:
                self.state = self.DIE
            else:
                self.state = self.RUN

    def handle_die(self, frame_time):
        global stage_score
        stage_score.score += monster_data['Yeti']['score']
        self.alive = False

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
        self.name = 'Yeti'
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
        if Yeti.hit_sound == None:
            self.hit_sound = load_wav('sound\\yeti_sound.ogg')
            self.hit_sound.set_volume(40)
        self.alive = True
        self.speed_state = self.normal
        self.buff_time = 0.0

    def update(self, frame_time):
        global stage_life
        self.handle_state[self.state](self, frame_time)


        if self.x < 0:
            stage_life.life -=1
            self.alive = False

    def draw(self):
        if self.state == self.HIT:
            self.image_die.clip_draw(0,0,137,120,self.x,self.y)
        else:
            self.image.clip_draw(100 * self.frame, 0, 100, 120, self.x, self.y)

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
    hit_sound = None

    RUN, HIT, DIE = 0, 1, 2
    normal, speed_up, speed_down = 1.0, 1.5, 0.5

    def handle_run(self, frame_time):
        self.total_frames += Falcon.FRAMES_PER_ACTION * Falcon.ACTION_PER_TIME * frame_time * self.speed_state
        self.frame = int(self.total_frames) % 10
        self.x -= Falcon.RUN_SPEED_PPS * frame_time * self.speed_state
        self.y -= (Falcon.RUN_SPEED_PPS * frame_time)/2 * self.speed_state

    def handle_hit(self, frame_time):
        if self.hit_motion_delay == 0:
            self.hit_sound.play()
        self.hit_motion_delay += frame_time
        if(self.hit_motion_delay > 0.3):
            self.hp -= 1
            self.hit_motion_delay = 0.0
            if self.hp == 0:
                self.state = self.DIE
            else:
                self.state = self.RUN

    def handle_die(self, frame_time):
        global stage_score
        stage_score.score += monster_data['Falcon']['score']
        self.alive = False

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
        self.name = 'Falcon'
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
        if Falcon.hit_sound == None:
            self.hit_sound = load_wav('sound\\falcon_sound.ogg')
            self.hit_sound.set_volume(70)
        self.alive = True
        self.speed_state = self.normal
        self.buff_time = 0.0

    def update(self, frame_time):
        global stage_life
        self.handle_state[self.state](self, frame_time)

        if self.x < 0:
            stage_life.life -=1
            self.alive = False

    def draw(self):
        if self.state == self.HIT:
            if self.hp < 1:
                self.image_die.clip_draw(0,0,110,85,self.x,self.y)
            else:
                self.image_die.clip_draw(110,0,110,85,self.x,self.y)
        else:
            self.image.clip_draw(150 * self.frame, 0, 150, 121, self.x, self.y)
