from pico2d import*
import game_framework

class Clock:
    def __init__(self):
        self.image = load_image('image\\etc\\number.png')
        self.colon = load_image('image\\etc\\timer1.png')
        self.hx = 480
        self.m1x,self.m2x = 520, 540
        self.y = 550
        self.time = 60

    def update(self, frame_time):
        self.time -= frame_time
        if self.time < 1:
            game_framework.quit()

    def draw(self):
        self.image.clip_draw(23 * (int(self.time / 60)), 0, 23, 34, self.hx, self.y)
        self.image.clip_draw(23 * (int(self.time % 60 / 10)), 0, 23, 34, self.m1x, self.y)
        self.image.clip_draw(23 * (int(self.time) % 10), 0, 23, 34, self.m2x, self.y)
        self.colon.clip_draw(0,0,10,24,500,550,20,24)

class Score:
    def __init__(self):
        self.image = load_image('image\\etc\\score_board.png')
        self.text = load_font('font\\arial.ttf', 30)
        self.score = 0
        self.frame = 0

    def update(self):
        if self.score < 2000: self.frame = 0
        if self.score >= 2000: self.frame = 1
        if self.score >= 4000: self.frame = 2
        if self.score >= 6000: self.frame = 3
        if self.score >= 8000: self.frame = 4
        if self.score >= 10000: self.frame = 5
        if self.score >= 12500: self.frame = 6
        if self.score >= 15000: self.frame = 7

    def draw(self):
        self.image.clip_draw(100 * self.frame,0,100,19,150,500, 300, 50)
        self.text.draw(180,500,"%d" % self.score, color = (255,255,255))

class Life:
    def __init__(self):
        self.life = 20
        self.image = load_image('image\\etc\\Life.png')
        self.font = load_font('font\\arial.ttf', 25)

    def update(self):
        if self.life <= 0:
            game_framework.quit()

    def draw(self):
        self.image.draw(50,550)
        self.font.draw(80, 550, 'X %d'%self.life, color = (255,0,0))