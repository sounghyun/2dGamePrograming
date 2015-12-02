from pico2d import*
import frist_stage

class Weapon:

    TIME_PER_ACTION = 0.3
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 6

    READY, CHARGING, LAUNCH = 0, 1, 2

    def handle_ready(self, frame_time):
        pass
    def handle_launch(self, frame_time):
        if self.frame == 0:
            self.launch_sound = load_wav('sound\\launch.ogg')
            self.launch_sound.set_volume(50)
            self.launch_sound.play()
        self.frame += Weapon.FRAMES_PER_ACTION * Weapon.ACTION_PER_TIME * frame_time
        if(self.frame > 7):
            self.state = self.CHARGING
            self.frame = 0.0

    def handle_charging(self, frame_time):
        self.charge_time += frame_time
        if(self.charge_time > 0.5):
            self.state = self.READY
            self.charge_time = 0.0

    handle_state = {
        READY : handle_ready,
        CHARGING : handle_charging,
        LAUNCH : handle_launch
    }

    def __init__(self, locaction):
        self.image = load_image('image\\etc\\ballista.png')
        self.boom = load_image('image\\etc\\boom.png')
        self.total_frames = 0.0
        self.frame = 0
        self.charge_time = 0.0
        self.state = self.READY


        if locaction == 0:
            self.x, self.y = 60, 230
        elif locaction == 1:
            self.x, self.y = 160, 180
        elif locaction == 2:
            self.x, self.y = 260, 130
        elif locaction == 3:
            self.x, self.y = 360, 80

    def update(self, frame_time):
        self.handle_state[self.state](self, frame_time)

    def draw(self):
        self.image.clip_draw(0,0,117,134,self.x,self.y)
        if self.state == self.LAUNCH:
            self.boom.clip_draw(100 * int(self.frame), 0, 100, 85, self.x + 25, self.y + 40)

class Arrow:

    PIXEL_PER_METER = (10.0 / 0.5)           # 10 pixel 50 cm
    RUN_SPEED_KMPH = 100                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    image = None

    def __init__(self,x,y):
        self.name = 'Arrow'
        if(Arrow.image == None):
            Arrow.image = load_image('image\\etc\\arrow.png')
        self.x , self.y= x, y
        self.alive = True

    def update(self, frame_time):
        self.x += Arrow.RUN_SPEED_PPS * frame_time
        self.y += (Arrow.RUN_SPEED_PPS * frame_time)/2

        if self.x > 1000:
            frist_stage.arrows.remove(self)

        for object in frist_stage.select:
            if self.x >= object.x + 30 and self.x <= object.x + 70 and self.y >= object.y + 30 and self.y <= object.y + 70:
                object.state = object.HIT
                self.alive = False
                break

    def draw(self):
        self.image.clip_draw(0,0,50,30,self.x,self.y)