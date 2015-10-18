from pico2d import *
import random

class Falcon:
    def __init__(self):
        self.location = random.randint(1,4)
        if self.location == 1:
            self.x, self.y = 900, 800
        elif self.location == 2:
            self.x, self.y = 1000, 750
        elif self.location == 3:
            self.x, self.y = 1100, 700
        elif self.location == 4:
            self.x, self.y = 1200, 650
        self.frame = 0
        self.dieck = False
        self.count = 0
        self.image = load_image('image\\monster\\falcon.png')
#        self.image_die = load_image('image\\monster\\falcon_die.png')

    def update(self):
        if self.dieck:
            self.count += 1
            if self.count > 4:
                self.count = 0
                self.dieck = False
        else:
            self.frame = (self.frame + 1) % 10
            self.x -= 16
            self.y -= 8
        if self.x < 0:
            self.location = random.randint(1,4)
            if self.location == 1:
                self.x, self.y = 800, 800
            elif self.location == 2:
                self.x, self.y = 900, 750
            elif self.location == 3:
                self.x, self.y = 1000, 700
            elif self.location == 4:
                self.x, self.y = 1100, 650

    def draw(self):
#        if self.dieck:
#            self.image_die.clip_draw(90 * self.count,0,90,120,self.x,self.y)
#        else:
            self.image.clip_draw(150 * self.frame, 0, 150, 121, self.x, self.y)

def handle_events():
    global testing
    global team
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            testing = False
        elif event.type == SDL_KEYDOWN :
            if event.key == SDLK_ESCAPE:
                testing = False
            for falcon in team:
                if event.key == SDLK_q and random.randint(1,4) == falcon.location:
                    falcon.dieck = True

open_canvas(1000,800)

team = [Falcon() for i in range(4)]

testing = True

while testing:
    handle_events()

    for falcon in team:
        falcon.update()

    clear_canvas()
    for falcon in team:
        falcon.draw()
    update_canvas()

    delay(0.05)

close_canvas()
