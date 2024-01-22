input.onButtonPressed(Button.A, function () {
    for (let note of notes) {
        music.play(music.tonePlayable(note, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
    }
})
input.onButtonPressed(Button.B, function () {
    for (let note2 of notes) {
        music.play(music.tonePlayable(note2 + 220, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
    }
})
let notes: number[] = []
notes = [
262,
392,
330,
392,
262,
392,
262,
392,
330,
392,
262,
392
]
basic.forever(function () {
	
})
