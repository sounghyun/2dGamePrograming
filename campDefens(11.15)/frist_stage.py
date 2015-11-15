from pico2d import *
import random
import game_framework
import background
import monster
import friendly
import weapon
import etc

main_background = None
monstertype = None
friendlytype = None
select = []
ballistas = None
arrow = None
timer = None
score = None
Life = None
Ttime = 0

def enter():
    global main_background, timer, score, Life
    global monstertype, select, friendlytype
    global ballistas, arrow
    main_background = background.Background()
    monstertype = [monster.Bonus, monster.Falcon, monster.Ice_wolf, monster.Yeti]
    friendlytype = [friendly.Amazon, friendly.General, friendly.Heroine, friendly.Soldier]

    for i in range(0,8):
        if random.randint(0,0) : select.append(monstertype[random.randint(0,3)]())
        else : select.append(friendlytype[random.randint(0,3)]())

    ballistas = [weapon.Weapon() for i in range(4)]
    for i in range(0,4):
        ballistas[i].locaction = i
    arrow = [weapon.Arrow() for i in range(4)]
    timer = etc.Clock()
    score = etc.Score()
    Life = etc.Life()

def exit():
    global main_background, timer, score
    global monstertype, select
    global ballistas, arrow
    del(main_background)
    del(timer)
    del(score)
    del(monstertype)
    del(select)
    del(ballistas)
    del(arrow)

def pause():
    pass

def resume():
    pass

def handle_events(frame_time):
    global testing
    global arrow
    global score
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
            if event.key == SDLK_1 and arrow[0].launch == False and arrow[0].timeck == False:
                arrow[0].launch, ballistas[0].launch, arrow[0].timeck = True, True, True
                arrow[0].x, arrow[0].y = 110, 280
            if event.key == SDLK_2 and arrow[1].launch == False and arrow[1].timeck == False:
                arrow[1].launch, ballistas[1].launch, arrow[1].timeck = True, True, True
                arrow[1].x, arrow[1].y = 210, 230
            if event.key == SDLK_3 and arrow[2].launch == False and arrow[2].timeck == False:
                arrow[2].launch, ballistas[2].launch, arrow[2].timeck = True, True, True
                arrow[2].x, arrow[2].y = 310, 180
            if event.key == SDLK_4 and arrow[3].launch == False and arrow[3].timeck == False:
                arrow[3].launch, ballistas[3].launch, arrow[3].timeck = True, True, True
                arrow[3].x, arrow[3].y = 410, 130
            if event.key == SDLK_u:
                score.score += 1000
            if event.key == SDLK_b:
                score.score -= 1000

def update(frame_time):
    global Ttime
    main_background.update(frame_time)
    timer.update(frame_time)
    score.update()
#    Life.update()
    for mon in select:
        mon.update(frame_time)
    for i in range(4):
        ballistas[i].update(frame_time)
        arrow[i].update(frame_time)
    Ttime += 1

def draw(frame_time):
    clear_canvas()
    main_background.draw()
    timer.draw()
    score.draw()
    Life.draw()
    for mon in select:
        mon.draw()
    for i in range(0,4):
        ballistas[i].draw()
        arrow[i].draw()

    update_canvas()