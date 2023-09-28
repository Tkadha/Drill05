from pico2d import *
import random

TUK_WIDTH, TUK_HEIGHT = 1240, 600
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def char_move():
    global x, y, hand_x, hand_y
    global frame
    x1, y1 = x, y
    x2, y2 = hand_x, hand_y
    for i in range(0, 100 + 1, 3):
        t = i / 100
        x = (1 - t) * x1 + t * x2
        y = (1 - t) * y1 + t * y2
        clear_canvas()
        TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
        if 0 > x2 - x1:
            character.clip_draw(frame * 100, 100 * 0, 100, 100, x, y)
        elif 0 <= x2 - x1:
            character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        frame = (frame + 1) % 8
        hand.draw(hand_x, hand_y)
        update_canvas()
        delay(0.05)


running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0

while running:
    hand_x, hand_y = random.randint(0, TUK_WIDTH), random.randint(0, TUK_HEIGHT)
    char_move()
    handle_events()

close_canvas()
