import game_framework
import frist_stage

from pico2d import *


name = "TitleState"
image = None
bgm = None

def enter():
    global image
    global bgm
    image = load_image('image\\start_background.png')
    bgm = load_music('sound\\intro.ogg')
    bgm.set_volume(50)
    bgm.repeat_play()

def exit():
    global image
    global bgm
    del(image)
    del(bgm)

def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(frist_stage)


def draw(frame_time):
    clear_canvas()
    image.draw(500,300, 1000, 600)
    update_canvas()

def update(frame_time):
    pass


def pause():
    pass


def resume():
    pass






