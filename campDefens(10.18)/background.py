from pico2d import *
import random
import monster
import weapon
import arrow
import etc
class Background:
    def __init__(self):
        self.x, self.y = 500,300
        self.frame = 0
        self.sum = 1
        self.time = 0
        self.image = load_image('image\\main_background.png')

    def update(self):
        self.time += 1
        if self.time % 60 == 0:
            self.frame = (self.frame + self.sum) % 10
            if self.frame == 0 or self.frame == 9:
               self.sum *= -1

    def draw(self):
        main_background.image.clip_draw(500 * self.frame,0,500,340,self.x,self.y,1000,600)

def handle_events():
    global testing
    global arrow
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            testing = False
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                testing = False
            if event.key == SDLK_1 and arrow[0].launch == False:
                arrow[0].launch = True
                arrow[0].x, arrow[0].y = 100, 250
            if event.key == SDLK_2 and arrow[1].launch == False:
                arrow[1].launch = True
                arrow[1].x, arrow[1].y = 200, 200
            if event.key == SDLK_3 and arrow[2].launch == False:
                arrow[2].launch = True
                arrow[2].x, arrow[2].y = 300, 150
            if event.key == SDLK_4 and arrow[3].launch == False:
                arrow[3].launch = True
                arrow[3].x, arrow[3].y = 400, 100


open_canvas(1000,600)

main_background = Background()
monster = [monster.Bonus(), monster.Falcon(), monster.Ice_wolf(), monster.Yeti()]
select = [monster[i % 4] for i in range(10)]
ballistas = [weapon.Weapon() for i in range(4)]
arrow = [arrow.Arrow() for i in range(4)]
timer = etc.Clock()
score = etc.Score()
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
        arrow[i].update()

    clear_canvas()

    main_background.draw()
    timer.draw()
    score.draw()
    for mon in select:
        mon.draw()
    for i in range(0,4):
        ballistas[i].draw()
        arrow[i].draw()

    update_canvas()

    delay(0.05)

close_canvas()

