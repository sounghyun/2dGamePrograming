from pico2d import *
import random
import game_framework
import background
import monster
import friendly
import weapon
import etc

main_background = None
timer = None
score = None
Life = None
monstertype = []
friendlytype = []
select = []
ballistas = []
arrows = []
Ttime = 0

def enter():
    global main_background, timer, score, Life
    global monstertype, select, friendlytype
    global ballistas, arrows
    main_background = background.Background()
    monstertype = [monster.Bonus, monster.Falcon, monster.Ice_wolf, monster.Yeti]
    friendlytype = [friendly.Amazon, friendly.General, friendly.Heroine, friendly.Soldier]

    for i in range(0,8):
        if random.randint(0,1) : select.append(monstertype[random.randint(0,3)]())
        else : select.append(friendlytype[random.randint(0,3)]())

    ballistas = [weapon.Weapon(i) for i in range(4)]
    timer = etc.Clock()
    score = etc.Score()
    Life = etc.Life()

def exit():
    global main_background, timer, score
    global monstertype, select
    global ballistas, arrows
    del(main_background)
    del(timer)
    del(score)
    del(monstertype)
    del(select)
    del(ballistas)
    del(arrows)

def pause():
    pass

def resume():
    pass

def handle_events(frame_time):
    global testing
    global arrows
    global score
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
            if event.key == SDLK_1 and ballistas[0].state == ballistas[0].READY:
                arrows.append(weapon.Arrow(110, 280))
                ballistas[0].state = ballistas[0].LAUNCH
            if event.key == SDLK_2 and ballistas[1].state == ballistas[1].READY:
                arrows.append(weapon.Arrow(210, 230))
                ballistas[1].state = ballistas[1].LAUNCH
            if event.key == SDLK_3 and ballistas[2].state == ballistas[2].READY:
                arrows.append(weapon.Arrow(310, 180))
                ballistas[2].state = ballistas[2].LAUNCH
            if event.key == SDLK_4 and ballistas[3].state == ballistas[3].READY:
                arrows.append(weapon.Arrow(410, 130))
                ballistas[3].state = ballistas[3].LAUNCH
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
    for arrow in arrows:
        arrow.update(frame_time)
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
    for arrow in arrows:
        arrow.draw()

    update_canvas()