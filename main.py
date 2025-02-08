def on_button_pressed_a():
    if input.light_level() <= 100:
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            """)
    else:
        basic.show_leds("""
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.show_string("" + str((input.temperature())))
    for index in range(4):
        music.play(music.string_playable("G E A F G A C B ", 500),
            music.PlaybackMode.UNTIL_DONE)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    if input.compass_heading() <= 89:
        basic.show_string("NORTE")
    if input.compass_heading() <= 179:
        basic.show_string("LESTE")
    if input.compass_heading() <= 269:
        basic.show_string("SUL")
    else:
        basic.show_string("OESTE")
input.on_button_pressed(Button.B, on_button_pressed_b)
