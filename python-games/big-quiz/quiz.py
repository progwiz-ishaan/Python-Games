WIDTH = 1208
HEIGHT = 720

main_box = Rect(0, 0, 820, 240)
timer_box = Rect(0, 0, 240, 240)
answer_box1 = Rect(0, 0, 485, 165)
answer_box2 = Rect(0, 0, 485, 155)
answer_box3 = Rect(0, 0, 485, 155)
answer_box4 = Rect(0, 0, 485, 155)

main_box.move_ip(50, 40)
timer_box.move_ip(990, 40)
answer_box1.move_ip(50, 358)
answer_box2.move_ip(735, 358)
answer_box3.move_ip(50, 538)
answer_box4.move_ip(735, 538)
answer_boxes = [answer_box1, answer_box2, answer_box3, answer_box4]

def draw():
    screen.fill('dim grey')
    screen.draw.filled_rect(main_box, 'sky blue')
    screen.draw.filled_rect(timer_box, 'sky blue')

    for box in answer_boxes:
        screen.draw.filled_rect(box, 'orange')

def game_over():
    pass

def correct_answer():
    pass

def on_mouse_down():
    pass

def update_time_left():
    pass