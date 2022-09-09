input.onButtonPressed(Button.A, function () {
    PositionX += -1
    if (PositionX <= 0) {
        PositionX = 1
    }
})
input.onButtonPressed(Button.B, function () {
    PositionX += 1
    if (PositionX >= 5) {
        PositionX = 5
    }
})
let PositionX = 0
basic.showString("hi!")
PositionX = 3
basic.forever(function () {
    if (PositionX == 1) {
        basic.showLeds(`
            # . . . .
            # . . . .
            # . . . .
            # . . . .
            # . . . .
            `)
    } else if (PositionX == 2) {
        basic.showLeds(`
            . # . . .
            . # . . .
            . # . . .
            . # . . .
            . # . . .
            `)
    } else if (PositionX == 3) {
        basic.showLeds(`
            . . # . .
            . . # . .
            . . # . .
            . . # . .
            . . # . .
            `)
    } else if (PositionX == 4) {
        basic.showLeds(`
            . . . # .
            . . . # .
            . . . # .
            . . . # .
            . . . # .
            `)
    } else if (PositionX == 5) {
        basic.showLeds(`
            . . . . #
            . . . . #
            . . . . #
            . . . . #
            . . . . #
            `)
    }
})
