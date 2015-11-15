from pico2d import*
import frist_stage
import random

class Heroine:

    PIXEL_PER_METER = (10.0 / 0.5)           # 10 pixel 50 cm
    RUN_SPEED_KMPH = 17.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.8
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 10

    image = None
    image_die = None

    RUN, HIT, DIE = 0, 1, 2

    def handle_run(self, frame_time):
        global frist_stage
        self.total_frames += Heroine.FRAMES_PER_ACTION * Heroine.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 10
        self.x -= Heroine.RUN_SPEED_PPS * frame_time
        self.y -= (Heroine.RUN_SPEED_PPS * frame_time)/2

    def handle_hit(self, frame_time):
        global frist_stage
        if frist_stage.Ttime % 20 == 0:
            self.count += 1
            if self.count > 4:
                self.count = 0
                self.dieck = False
                self.diecount += 1
                if self.diecount == 3:
                    self.state = self.DIE

    def handle_die(self, frame_time):
        global frist_stage
        self.location = random.randint(1,4)
        self.create_object()
        self.diecount = 0
        frist_stage.Life.life -= 5
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
        self.dieck = False
        self.diecount = 0
        self.time = random.randint(0,30)
        self.count = 0
        self.image = load_image('image\\forces\\heroine.png')
        self.image_die = load_image('image\\forces\\heroine_die.png')

    def update(self, frame_time):
        if self.dieck:
            self.state = self.HIT
        elif self.state != self.DIE:
            self.state = self.RUN

        self.handle_state[self.state](self, frame_time)

        if self.x < 0:
            self.location = random.randint(1,4)
            self.create_object()
            self.diecount = 0

    def draw(self):
        if self.dieck:
            if self.diecount < 1:
                self.image_die.clip_draw(0,0,60,87,self.x,self.y)
            else:
                self.image_die.clip_draw(60,0,60,87,self.x,self.y)
        else:
            self.image.clip_draw(50 * self.frame, 0, 50, 90, self.x, self.y)

class Amazon:

    PIXEL_PER_METER = (10.0 / 0.5)           # 10 pixel 50 cm
    RUN_SPEED_KMPH = 20.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 1
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 10

    image = None
    image_die = None

    RUN, HIT, DIE = 0, 1, 2

    def handle_run(self, frame_time):
        global frist_stage
        self.total_frames += Amazon.FRAMES_PER_ACTION * Amazon.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 10
        self.x -= Amazon.RUN_SPEED_PPS * frame_time
        self.y -= (Amazon.RUN_SPEED_PPS * frame_time)/2

    def handle_hit(self, frame_time):
        global frist_stage
        if frist_stage.Ttime % 20 == 0:
            self.count += 1
            if self.count > 4:
                self.count = 0
                self.dieck = False
                self.diecount += 1
                if self.diecount == 2:
                    self.state = self.DIE

    def handle_die(self, frame_time):
        global frist_stage
        self.location = random.randint(1,4)
        self.create_object()
        self.diecount = 0
        frist_stage.score.score -= 500
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
        self.dieck = False
        self.diecount = 0
        self.time = random.randint(0,30)
        self.count = 0
        self.image = load_image('image\\forces\\amazon.png')
        self.image_die = load_image('image\\forces\\amazon_die.png')

    def update(self, frame_time):
        global frist_stage
        if self.dieck:
            self.state = self.HIT
        elif self.state != self.DIE:
            self.state = self.RUN

        self.handle_state[self.state](self, frame_time)

        if self.x < 0:
            self.location = random.randint(1,4)
            self.create_object()
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

    PIXEL_PER_METER = (10.0 / 0.5)           # 10 pixel 50 cm
    RUN_SPEED_KMPH = 10.0                    # Km / Hour
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
        global frist_stage
        self.total_frames += General.FRAMES_PER_ACTION * General.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 6
        self.x -= General.RUN_SPEED_PPS * frame_time
        self.y -= (General.RUN_SPEED_PPS * frame_time)/2

    def handle_hit(self, frame_time):
        global frist_stage
        if frist_stage.Ttime % 20 == 0:
            self.count += 1
            if self.count > 4:
                self.count = 0
                self.dieck = False
                self.diecount += 1
                if self.diecount == 2:
                    self.state = self.DIE

    def handle_die(self, frame_time):
        global frist_stage
        self.location = random.randint(1,4)
        self.create_object()
        self.diecount = 0
        frist_stage.score.score -= 500
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
        self.dieck = False
        self.diecount = 0
        self.time = random.randint(0,30)
        self.count = 0
        self.image = load_image('image\\forces\\general.png')
        self.image_die = load_image('image\\forces\\general_die.png')

    def update(self, frame_time):
        global frist_stage
        if self.dieck:
            self.state = self.HIT
        elif self.state != self.DIE:
            self.state = self.RUN

        self.handle_state[self.state](self, frame_time)


        if self.x < 0:
            self.location = random.randint(1,4)
            self.create_object()
            self.diecount = 0

    def draw(self):
        if self.dieck:
            self.image_die.clip_draw(0,0,86,106,self.x,self.y)
        else:
            self.image.clip_draw(70 * self.frame, 0, 70, 100, self.x, self.y)

class Soldier:

    PIXEL_PER_METER = (10.0 / 0.5)           # 10 pixel 50 cm
    RUN_SPEED_KMPH = 15.0                    # Km / Hour
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
        global frist_stage
        self.total_frames += Soldier.FRAMES_PER_ACTION * Soldier.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 6
        self.x -= Soldier.RUN_SPEED_PPS * frame_time
        self.y -= (Soldier.RUN_SPEED_PPS * frame_time)/2

    def handle_hit(self, frame_time):
        global frist_stage
        if frist_stage.Ttime % 20 == 0:
            self.count += 1
            if self.count > 4:
                self.count = 0
                self.dieck = False
                self.diecount += 1
                if self.diecount == 1:
                    self.state = self.DIE

    def handle_die(self, frame_time):
        global frist_stage
        self.location = random.randint(1,4)
        self.create_object()
        self.diecount = 0
        frist_stage.score.score -= 300
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
        self.dieck = False
        self.time = random.randint(0,30)
        self.diecount = 0
        self.count = 0
        self.image = load_image('image\\forces\\soldier.png')
        self.image_die = load_image('image\\forces\\soldier_die.png')

    def update(self, frame_time):
        global frist_stage
        if self.dieck:
            self.state = self.HIT
        elif self.state != self.DIE:
            self.state = self.RUN

        self.handle_state[self.state](self, frame_time)


        if self.x < 0:
            self.location = random.randint(1,4)
            self.create_object()

    def draw(self):
        if self.dieck:
            self.image_die.clip_draw(0,0,75,87,self.x,self.y)
        else:
            self.image.clip_draw(80 * self.frame, 0, 80, 100, self.x, self.y)