from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

def handle_events():
    global running
    global x, y,i,j,list_hand_x,list_hand_y
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
    pass



running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
i, j = TUK_WIDTH // 2, TUK_HEIGHT // 2
x1,y1 = i,j

list_hand_x = []
list_hand_y = []
frame = 0
hide_cursor()




while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    hand.clip_draw(0,0,50,52,x,y)
    if len(list_hand_x) > 0 and i == list_hand_x[0] and j == list_hand_y[0]:
        removed_value = list_hand_x.pop(0)
        x1, y1 = i, j

    if len(list_hand_x) > 0 and len(list_hand_y) > 0:
        for k in range(0, 100 + 1, 1):
            t = k / 100
            i = (1 - t) * x1 + t * list_hand_x[0]
            j = (1 - t) * y1 + t * list_hand_y[0]
    character.clip_draw(frame * 100, 100 * 1, 100, 100, i, j)
    
    for i in range(0,len(list_hand_x)-1):
        hand.clip_draw(0, 0, 50, 52, list_hand_x[i], list_hand_y[i])
    update_canvas()
    frame = (frame + 1) % 8

    handle_events()

close_canvas()




