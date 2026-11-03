from pico2d import *
from boy import Boy
from ball import Ball
from grass import Grass
import game_world # 게임 월드 모듈 임포트

# Game object class here


def handle_events():
    global running

    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif (event.type == SDL_KEYDOWN and event.key == SDLK_SPACE
              and boy.state in ('IDLE', 'RUN')):
            ball = Ball(boy.x + boy.face_dir * 30, boy.y - 25, boy.face_dir)
            game_world.add_object(ball)
        else:
            boy.handle_event(event)



def reset_world():
    global boy


    boy = Boy()
    game_world.add_object(boy, 1)

    grass = Grass().draw
    game_world.add_object(grass,0) # 게임 월드에 객체를 담는 함수 호출
    grass = Grass()
    game_world.add_object(grass,1) # 게임 월드에 객체를 담는 함수 호출

def update_world():
    game_world.update()
    pass

def render_world():
    clear_canvas()
    game_world.rander()
    update_canvas()


running = True



open_canvas()
reset_world()
# game loop
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.01)
# finalization code
close_canvas()
