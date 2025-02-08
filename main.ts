input.onButtonPressed(Button.A, function () {
    if (input.lightLevel() <= 100) {
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            `)
    } else {
        basic.showLeds(`
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
    }
})
input.onButtonPressed(Button.AB, function () {
    basic.showString("" + (input.temperature()))
    for (let index = 0; index < 4; index++) {
        music.play(music.stringPlayable("G E A F G A C B ", 500), music.PlaybackMode.UntilDone)
    }
})
input.onButtonPressed(Button.B, function () {
    if (input.compassHeading() <= 89) {
        basic.showString("NORTE")
    }
    if (input.compassHeading() <= 179) {
        basic.showString("LESTE")
    }
    if (input.compassHeading() <= 269) {
        basic.showString("SUL")
    } else {
        basic.showString("OESTE")
    }
})
