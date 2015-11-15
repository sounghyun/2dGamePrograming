from pico2d import*
import frist_stage

class Weapon:
    def __init__(self):
        self.image = load_image('image\\etc\\ballista.png')
        self.boom = load_image('image\\etc\\boom.png')
        self.locaction = 0
        self.frame = 0
        self.launch = False
        self.x, self.y= 0, 0

    def update(self, frame_time):
        if self.locaction == 0:
            self.x, self.y = 60, 230
        elif self.locaction == 1:
            self.x, self.y = 160, 180
        elif self.locaction == 2:
            self.x, self.y = 260, 130
        elif self.locaction == 3:
            self.x, self.y = 360, 80

        if self.launch == True:
            self.frame += 1
            if self.frame > 6:
                self.frame = 0
                self.launch = False

    def draw(self):
        self.image.clip_draw(0,0,117,134,self.x,self.y)
        if self.launch:
            self.boom.clip_draw(100 * self.frame, 0, 100, 85, self.x + 25, self.y + 40)

class Arrow:
    def __init__(self):
        self.image = load_image('image\\etc\\arrow.png')
        self.locaction = 0
        self.time = 0
        self.timeck = False
        self.launch = False
        self.x , self.y= 0, 0

    def update(self, frame_time):
        if self.time < 100 and self.timeck:
            self.time += 1;
        else:
            self.timeck = False
            self.time = 0
        if self.launch:
            self.x += 2;
            self.y += 1;
            if self.x > 1000:
                self.launch = False
                self.timeck = False
                self.time = 0

            for i in range(8):
                if self.x >= frist_stage.select[i].x + 30 and self.x <= frist_stage.select[i].x + 70 and self.y >= frist_stage.select[i].y + 30 and self.y <= frist_stage.select[i].y + 70:
                    frist_stage.select[i].dieck = True
                    self.launch = False

    def draw(self):
        if self.launch:
            self.image.clip_draw(0,0,50,30,self.x,self.y);