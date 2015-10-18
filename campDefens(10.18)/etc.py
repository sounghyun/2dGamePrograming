from pico2d import*

class Clock:
    def __init__(self):
        self.image = load_image('image\\etc\\number.png')
        self.colon = load_image('image\\etc\\timer1.png')
        self.hx = 480
        self.m1x,self.m2x = 520, 540
        self.y = 550
        self.time = 1200
        self.h = 1
        self.m1, self.m2 = 6, 0

    def update(self):
        global testing
        if self.time % 1200 == 0:
            self.h -= 1
        if self.time % 200 == 0:
            self.m1 = (self.m1 -1) % 6
        if self.time % 20 == 0:
            self.m2 = (self.m2 - 1) % 10
        self.time -= 1
        if self.time == 0:
            testing = False

    def draw(self):
        self.image.clip_draw(23 * self.h, 0, 23, 34, self.hx, self.y)
        self.image.clip_draw(23 * self.m1, 0, 23, 34, self.m1x, self.y)
        self.image.clip_draw(23 * self.m2, 0, 23, 34, self.m2x, self.y)
        self.colon.clip_draw(0,0,10,24,500,550,20,24)

class Score:
    def __init__(self):
        self.image = load_image('image\\etc\\score_board.png')
        self.text = load_font('font\\arial.ttf', 30)
        self.score = 0

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(0,0,100,19,150,400, 300, 50)
        self.text.draw(180,400,"%d" % self.score)

