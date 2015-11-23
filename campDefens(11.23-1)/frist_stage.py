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
total_time = 0.0
monstertype = []
friendlytype = []
select = []
ballistas = []
arrows = []

def enter():
    global main_background, timer, score, Life
    global monstertype, select, friendlytype
    global ballistas, arrows
    main_background = background.Background()
    monstertype = [monster.Bonus, monster.Falcon, monster.Ice_wolf, monster.Yeti]
    friendlytype = [friendly.Amazon, friendly.General, friendly.Heroine, friendly.Soldier]

    ballistas = [weapon.Weapon(i) for i in range(4)]
    timer = etc.Clock()
    score = etc.Score()
    Life = etc.Life()
    select = []
    arrows = []

def exit():
    global main_background, timer, score, Life
    global monstertype, friendlytype, select
    global ballistas, arrows
    del(main_background)
    del(timer)
    del(score)
    del(Life)
    del(monstertype)
    del(friendlytype)
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
                Life.life -= 20
            if event.key == SDLK_b:
                score.score -= 1000

def update(frame_time):
    main_background.update(frame_time)
    score.update()
    create_object(frame_time)
    for mon in select:
        mon.update(frame_time)
    for i in range(4):
        ballistas[i].update(frame_time)
    for arrow in arrows:
        arrow.update(frame_time)
    delete_object(select)
    delete_object(arrows)
    Life.update()
    timer.update(frame_time)

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

def create_object(frame_time):
    global total_time
    global select
    total_time += frame_time
    if total_time > (random.randint(10, 30) * 0.1):
        if random.randint(0,2) : select.append(monstertype[random.randint(0,3)]())
        else : select.append(friendlytype[random.randint(0,3)]())
        total_time = 0.0

def delete_object(objects):
    for object in objects:
        if object.alive == False:
            objects.remove(object)