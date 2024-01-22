def on_button_pressed_a():
    for note in notes:
        music.play(music.tone_playable(note, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    for note2 in notes:
        music.play(music.tone_playable(note2 + 220, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
input.on_button_pressed(Button.B, on_button_pressed_b)

notes: List[number] = []
notes = [262, 392, 330, 392, 262, 392,262, 392, 330, 392, 262, 392]

def on_forever():
    pass
basic.forever(on_forever)
