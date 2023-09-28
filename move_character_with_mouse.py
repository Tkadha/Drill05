from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1240, 600
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')


def char_move():
    pass


while True:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    hand.draw()
    char_move()
    update_canvas()


close_canvas()
