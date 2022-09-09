def on_button_pressed_a():
    global PositionX
    PositionX += 1
    if PositionX <= 0:
        PositionX = 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global PositionX
    PositionX += -1
    if PositionX >= 5:
        PositionX = 5
input.on_button_pressed(Button.B, on_button_pressed_b)

PositionX = 0
basic.show_string("hi!")
PositionX = 3

def on_forever():
    if PositionX == 1:
        basic.show_leds("""
            # . . . .
            # . . . .
            # . . . .
            # . . . .
            # . . . .
            """)
    elif PositionX == 2:
        basic.show_leds("""
            . # . . .
            . # . . .
            . # . . .
            . # . . .
            . # . . .
            """)
    elif PositionX == 3:
        basic.show_leds("""
            . . # . .
            . . # . .
            . . # . .
            . . # . .
            . . # . .
            """)
    elif PositionX == 4:
        basic.show_leds("""
            . . . # .
            . . . # .
            . . . # .
            . . . # .
            . . . # .
            """)
    elif PositionX == 5:
        basic.show_leds("""
            . . . . #
            . . . . #
            . . . . #
            . . . . #
            . . . . #
            """)
basic.forever(on_forever)
