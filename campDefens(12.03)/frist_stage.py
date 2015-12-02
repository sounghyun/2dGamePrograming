from pico2d import *
import random
import game_framework
import background
import monster
import friendly
import weapon
import etc

total_time = 0.0
main_background = None
weather = None
timer = None
score = None
Life = None
buff = None
Bouns_monster = None
Heroine = None
monstertype = []
friendlytype = []
select = []
ballistas = []
arrows = []

def enter():
    global main_background, timer, score, Life, buff
    global monstertype, select, friendlytype, Bouns_monster, Heroine
    global ballistas, arrows
    main_background = background.Background()
    monstertype = [monster.Falcon, monster.Ice_wolf, monster.Yeti]
    friendlytype = [friendly.Amazon, friendly.General, friendly.Soldier]
    Bouns_monster = monster.Bonus()
    Heroine = friendly.Heroine()
    ballistas = [weapon.Weapon(i) for i in range(4)]
    timer = etc.Clock()
    score = etc.Score()
    Life = etc.Life()
    buff = etc.Buff()
    select = [Bouns_monster, Heroine]
    arrows = []

def exit():
    global main_background, timer, score, Life, snow
    global monstertype, friendlytype, select
    global ballistas, arrows
    del(main_background)
    del(snow)
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
    global score, weather
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
            if event.key == SDLK_5:
                weather = background.Snow()
            if event.key == SDLK_6:
                weather = background.Rain()
            if event.key == SDLK_u:
                Life.life -= 20
            if event.key == SDLK_b:
                score.score -= 1000

def update(frame_time):
    main_background.update(frame_time)
    if weather != None:
        weather.update(frame_time)
    score.update()
    create_object(frame_time, select)
    for mon in select:
        mon.update(frame_time)
    for i in range(4):
        ballistas[i].update(frame_time)
    for arrow in arrows:
        arrow.update(frame_time)
    delete_object(select)
    delete_object(arrows)
    buff.update(frame_time, select)
    Life.update()
    timer.update(frame_time)

def draw(frame_time):
    clear_canvas()
    main_background.draw()
    if weather != None:
        weather.draw()
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

def create_object(frame_time, objects):
    global total_time
    total_time += frame_time
    if total_time > (random.randint(20, 30) * 0.1):
        if random.randint(0,2) : objects.append(monstertype[random.randint(0,2)]())
        else : objects.append(friendlytype[random.randint(0,2)]())
        total_time = 0.0

def delete_object(objects):
    for object in objects:
        if object.alive == False:
            if object.name == 'Bouns':
                objects.append(monster.Bonus())
                if object.hp < 1:
                    if random.randint(0,1):
                        if buff.speed_buff == buff.speed_normal:
                            if random.randint(0,1) : speed_up(buff)
                            else : speed_down(buff)
                    else:
                        if buff.hp_buff == buff.hp_normal:
                            if random.randint(0,1) : hp_up(buff)
                            else : hp_down(buff)

            elif object.name == 'Heroine':
                objects.append(friendly.Heroine())

            objects.remove(object)

def speed_up(buff):
    buff.speed_buff = buff.speed_up
    print('speed_up! \n')

def speed_down(buff):
    buff.speed_buff = buff.speed_up
    print('speed_down! \n')

def hp_up(buff):
    buff.hp_buff = buff.hp_up
    print('hp_up! \n')

def hp_down(buff):
    buff.hp_buff = buff.hp_down
    print('hp_down! \n')