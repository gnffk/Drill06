from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

def handle_events():
    global running
    global x, y, i, j, list_hand_x, list_hand_y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            list_hand_x.append(event.x)
            list_hand_y.append(TUK_HEIGHT - 1 - event.y)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
i, j = TUK_WIDTH // 2, TUK_HEIGHT // 2
x1, y1 = i, j

list_hand_x = []
list_hand_y = []
frame = 0
hide_cursor()

while running:
    if(len(list_hand_x) !=0):
        for k in range(0, 100 + 1, 1):
            t = k / 100
            i = (1 - t) * x1 + t * list_hand_x[0]
            j = (1 - t) * y1 + t * list_hand_y[0]
            clear_canvas()
            TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
            for n in range(len(list_hand_x)):
                hand_x, hand_y = list_hand_x[n], list_hand_y[n]
                hand.clip_draw(0, 0, 50, 52, hand_x, hand_y)
            if (list_hand_x[0] - i > 0):
                move = 1
            elif (list_hand_x[0] - i < 0):
                move = 0
            hand.clip_draw(0, 0, 50, 52, x, y)
            character.clip_draw(frame * 100, 100 * move, 100, 100, i, j)
            update_canvas()
            frame = (frame + 1) % 8
            delay(0.01)
            handle_events()
        if(i == list_hand_x[0] and j == list_hand_y[0]):
            x1, y1 = i, j
            del list_hand_x[0]
            del list_hand_y[0]


    elif(len(list_hand_x) ==0):
        clear_canvas()
        TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

        hand.clip_draw(0, 0, 50, 52, x, y)
        character.clip_draw(frame * 100, 100 * 1, 100, 100, i, j)
        update_canvas()
        frame = (frame + 1) % 8
        handle_events()
close_canvas()

