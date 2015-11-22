from pico2d import *

class Background:
    TIME_PER_ACTION = 30
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 9
    def __init__(self):
        self.x, self.y = 500,300
        self.frame = 0
        self.sum = 1
        self.total_frames = 0.0
        self.image = load_image('image\\main_background.png')
        self.bgm = load_music('sound\\main_stage.ogg')
        self.bgm.set_volume(50)
        self.bgm.repeat_play()

    def update(self, frame_time):
        self.total_frames += self.sum * Background.FRAMES_PER_ACTION * Background.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 9
        if self.total_frames < 0 or self.total_frames > 9:
            self.sum *= -1

    def draw(self):
        self.image.clip_draw(500 * self.frame,0,500,340,self.x,self.y,1000,600)


