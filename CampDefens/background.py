from pico2d import *
import random
import monster
import weapon

class Background:
    def __init__(self):
        self.x, self.y = 500,300
        self.frame = 0
        self.sum = 1
        self.time = 0
        self.image = load_image('image\\main_background.png')

    def update(self):
        self.time += 1
        if self.time % 20 == 0:
            self.frame = (self.frame + self.sum) % 10
            if self.frame == 0 or self.frame == 9:
               self.sum *= -1

    def draw(self):
        main_background.image.clip_draw(500 * self.frame,0,500,340,self.x,self.y,1000,600)

class Clock:
    def __init__(self):
        self.image = load_image('image\\etc\\number.png')
        self.colon = load_image('image\\etc\\timer1.png')
        self.hx = 480
        self.m1x,self.m2x = 520, 540
        self.y = 550
        self.h = 3
        self.m1, self.m2 = 6, 0
        self.time = 1800

    def update(self):
        if self.time % 600 == 0:
            self.h -= 1
        if self.time % 100 == 0:
            self.m1 = (self.m1 -1) % 6
        if self.time % 10 == 0:
            self.m2 = (self.m2 - 1) % 10
        self.time -= 1

    def draw(self):
        self.image.clip_draw(23 * self.h, 0, 23, 34, self.hx, self.y)
        self.image.clip_draw(23 * self.m1, 0, 23, 34, self.m1x, self.y)
        self.image.clip_draw(23 * self.m2, 0, 23, 34, self.m2x, self.y)
        self.colon.clip_draw(0,0,10,24,500,550,20,24)

def handle_events():
    global testing
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT or (event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE):
            testing = False

open_canvas(1000,600)

main_background = Background()
monster = [monster.Bonus(), monster.Falcon(), monster.Ice_wolf(), monster.Yeti()]
select = [monster[i % 4] for i in range(10)]
ballistas = [weapon.Weapon() for i in range(4)]
timer = Clock()
testing = True

while (testing):
    handle_events()

    main_background.update()
    timer.update()
    for mon in select:
        if(main_background.time > mon.time):
            mon.update()
    for i in range(0,4):
        ballistas[i].locaction = i
        ballistas[i].update()

    clear_canvas()

    main_background.draw()
    timer.draw()

    for mon in select:
        mon.draw()
    for i in range(0,4):
        ballistas[i].draw()

    update_canvas() # ㅁㄴㅇㄹ

    delay(0.1)

close_canvas()

