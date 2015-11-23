from pico2d import*
import frist_stage
import random
import json

friendly_data_file = open('data\\friendly_data.txt', 'r')
friendly_data = json.load(friendly_data_file)
friendly_data_file.close()

class Heroine:

    PIXEL_PER_METER = (10.0 / 0.5)           # 10 pixel 50 cm
    RUN_SPEED_KMPH = friendly_data['Heroine']['speed']                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.8
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 10

    image = None
    image_die = None
    hit_sound = None

    RUN, HIT, DIE = 0, 1, 2

    def handle_run(self, frame_time):
        self.total_frames += Heroine.FRAMES_PER_ACTION * Heroine.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 10
        self.x -= Heroine.RUN_SPEED_PPS * frame_time
        self.y -= (Heroine.RUN_SPEED_PPS * frame_time)/2

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
        global frist_stage
        frist_stage.Life.life -= friendly_data['Heroine']['life']
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
        self.location = random.randint(1,4)
        self.create_object()
        self.total_frames = 0.0
        self.frame = 0
        self.state = self.RUN
        self.hp = friendly_data['Heroine']['hp']
        self.hit_motion_delay = 0.0
        if Heroine.image == None:
            self.image = load_image('image\\forces\\heroine.png')
        if Heroine.image_die == None:
            self.image_die = load_image('image\\forces\\heroine_die.png')
        if Heroine.hit_sound == None:
            self.hit_sound = load_wav('sound\\heroine_sound.ogg')
            self.hit_sound.set_volume(40)
        self.alive = True

    def update(self, frame_time):
        self.handle_state[self.state](self, frame_time)

        if self.x < 0:
            self.alive = False

    def draw(self):
        if self.state == self.HIT:
            if self.hp > 1:
                self.image_die.clip_draw(0,0,60,87,self.x,self.y)
            else:
                self.image_die.clip_draw(60,0,60,87,self.x,self.y)
        else:
            self.image.clip_draw(50 * self.frame, 0, 50, 90, self.x, self.y)

class Amazon:

    PIXEL_PER_METER = (10.0 / 0.5)           # 10 pixel 50 cm
    RUN_SPEED_KMPH = friendly_data['Amazon']['speed']                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 1
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 10

    image = None
    image_die = None
    hit_sound = None

    RUN, HIT, DIE = 0, 1, 2

    def handle_run(self, frame_time):
        self.total_frames += Amazon.FRAMES_PER_ACTION * Amazon.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 10
        self.x -= Amazon.RUN_SPEED_PPS * frame_time
        self.y -= (Amazon.RUN_SPEED_PPS * frame_time)/2

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
        global frist_stage
        frist_stage.score.score -= friendly_data['Amazon']['score']
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
        self.location = random.randint(1,4)
        self.create_object()
        self.total_frames = 0.0
        self.frame = 0
        self.state = self.RUN
        self.hp = friendly_data['Amazon']['hp']
        self.hit_motion_delay = 0.0
        if Amazon.image == None:
            self.image = load_image('image\\forces\\amazon.png')
        if Amazon.image_die == None:
            self.image_die = load_image('image\\forces\\amazon_die.png')
        if Amazon.hit_sound == None:
            self.hit_sound = load_wav('sound\\amazon_sound.ogg')
            self.hit_sound.set_volume(40)
        self.alive = True

    def update(self, frame_time):
        self.handle_state[self.state](self, frame_time)

        if self.x < 0:
            self.alive = False

    def draw(self):
        if self.state == self.HIT:
            if self.hp > 1:
                self.image_die.clip_draw(0,0,100,85,self.x,self.y)
            else :
                self.image_die.clip_draw(100,0,100,85,self.x,self.y)
        else:
            self.image.clip_draw(100 * self.frame, 0, 100, 85, self.x, self.y)

class General:

    PIXEL_PER_METER = (10.0 / 0.5)           # 10 pixel 50 cm
    RUN_SPEED_KMPH = friendly_data['General']['speed']                    # Km / Hour
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

    def handle_run(self, frame_time):
        self.total_frames += General.FRAMES_PER_ACTION * General.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 6
        self.x -= General.RUN_SPEED_PPS * frame_time
        self.y -= (General.RUN_SPEED_PPS * frame_time)/2

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
        global frist_stage
        frist_stage.score.score -= friendly_data['General']['score']
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
        self.location = random.randint(1,4)
        self.create_object()
        self.total_frames = 0.0
        self.frame = 0
        self.state = self.RUN
        self.hp = friendly_data['General']['hp']
        self.hit_motion_delay = 0.0
        if General.image == None:
            self.image = load_image('image\\forces\\general.png')
        if General.image_die == None:
            self.image_die = load_image('image\\forces\\general_die.png')
        if General.hit_sound == None:
            self.hit_sound = load_wav('sound\\general_sound.ogg')
            self.hit_sound.set_volume(40)
        self.alive = True

    def update(self, frame_time):
        self.handle_state[self.state](self, frame_time)


        if self.x < 0:
            self.alive = False

    def draw(self):
        if self.state == self.HIT:
            self.image_die.clip_draw(0,0,86,106,self.x,self.y)
        else:
            self.image.clip_draw(70 * self.frame, 0, 70, 100, self.x, self.y)

class Soldier:

    PIXEL_PER_METER = (10.0 / 0.5)           # 10 pixel 50 cm
    RUN_SPEED_KMPH = friendly_data['Soldier']['speed']                    # Km / Hour
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

    def handle_run(self, frame_time):
        self.total_frames += Soldier.FRAMES_PER_ACTION * Soldier.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 6
        self.x -= Soldier.RUN_SPEED_PPS * frame_time
        self.y -= (Soldier.RUN_SPEED_PPS * frame_time)/2

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
        global frist_stage
        frist_stage.score.score -= friendly_data['Soldier']['score']
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
        self.location = random.randint(1,4)
        self.create_object()
        self.total_frames = 0.0
        self.frame = 0
        self.state = self.RUN
        self.hp = friendly_data['Soldier']['hp']
        self.hit_motion_delay = 0.0
        if Soldier.image == None:
            self.image = load_image('image\\forces\\soldier.png')
        if Soldier.image_die == None:
            self.image_die = load_image('image\\forces\\soldier_die.png')
        if Soldier.hit_sound == None:
            self.hit_sound = load_wav('sound\\soldier_sound.ogg')
            self.hit_sound.set_volume(40)
        self.alive = True

    def update(self, frame_time):
        self.handle_state[self.state](self, frame_time)


        if self.x < 0:
            self.alive = False

    def draw(self):
        if self.state == self.HIT:
            self.image_die.clip_draw(0,0,75,87,self.x,self.y)
        else:
            self.image.clip_draw(80 * self.frame, 0, 80, 100, self.x, self.y)