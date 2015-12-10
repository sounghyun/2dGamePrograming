from pico2d import*
import game_framework
import end_state

class Clock:
    def __init__(self):
        self.image = load_image('image\\etc\\number.png')
        self.colon = load_image('image\\etc\\timer1.png')
        self.hx = 480
        self.m1x,self.m2x = 520, 540
        self.y = 550
        self.time = 60
        self.time_over = False

    def update(self, frame_time):
        self.time -= frame_time
        if self.time < 1:
            self.time_over = True

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

    def update(self, stage):
        score_frame = 2000 * stage
        print(score_frame)
        if self.score < score_frame / 8: self.frame = 0
        if self.score > score_frame / 8: self.frame = 1
        if self.score > score_frame / 8 * 2: self.frame = 2
        if self.score > score_frame / 8 * 3: self.frame = 3
        if self.score > score_frame / 8 * 4: self.frame = 4
        if self.score > score_frame / 8 * 5: self.frame = 5
        if self.score > score_frame / 8 * 6: self.frame = 6
        if self.score >= score_frame: self.frame = 7

    def draw(self):
        self.image.clip_draw(100 * self.frame,0,100,19,150,500, 300, 50)
        self.text.draw(180,500,("%d") % self.score, color = (255,255,255))

class Life:
    def __init__(self):
        self.life = 20
        self.image = load_image('image\\etc\\Life.png')
        self.font = load_font('font\\arial.ttf', 25)

    def update(self):
        if self.life <= 0:
            game_framework.push_state(end_state)

    def draw(self):
        self.image.draw(50,550)
        self.font.draw(80, 550, 'X %d'%self.life, color = (255,0,0))

class Buff:
    speed_normal, speed_up, speed_down = 1, 2, 3
    hp_normal, hp_up, hp_down = 1, 2, 3

    def handle_speed_normal(self, objects, frame_time):
        for object in objects:
            object.speed_state = object.normal

    def handle_speed_up(self, objects, frame_time):
        self.speed_buff_time += frame_time
        for object in objects:
            object.speed_state = object.speed_up
        if self.speed_buff_time > 3:
            self.speed_buff = self.speed_normal
            self.speed_buff_time = 0

    def handle_speed_down(self, objects, frame_time):
        self.speed_buff_time += frame_time
        for object in objects:
            object.speed_state = object.speed_down
        if self.speed_buff_time > 3:
            self.speed_buff = self.speed_normal
            self.speed_buff_time = 0

    speed_state_tabel = {
        speed_normal : handle_speed_normal,
        speed_up : handle_speed_up,
        speed_down : handle_speed_down
    }

    def handle_hp_normal(self, objects):
        pass

    def handle_hp_up(self, objects):
        for object in objects:
            object.hp += 1
        self.hp_buff = self.hp_normal

    def handle_hp_down(self, objects):
        for object in objects:
            if object.hp > 1:
                object.hp -= 1
        self.hp_buff = self.hp_normal

    hp_state_tabel = {
        speed_normal : handle_hp_normal,
        speed_up : handle_hp_up,
        speed_down : handle_hp_down
    }

    def __init__(self):
        self.speed_buff = Buff.speed_normal
        self.hp_buff = Buff.hp_normal
        self.speed_buff_time = 0.0

    def update(self, frame_time, objects):
        self.speed_state_tabel[self.speed_buff](self,objects, frame_time)
        self.hp_state_tabel[self.hp_buff](self,objects)

    def drow(self):
        pass