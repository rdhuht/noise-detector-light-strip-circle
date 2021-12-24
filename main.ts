function A灯噪音可视化 () {
    led.setBrightness(input.lightLevel())
    led.plotBarGraph(
    input.soundLevel(),
    255
    )
    strip.showBarGraph(input.soundLevel(), 255)
}
function reset () {
    strip = neopixel.create(DigitalPin.P15, 12, NeoPixelMode.RGB)
    strip.showRainbow(1, 360)
    basic.clearScreen()
}
let level = 0
let noise = 0
let strip: neopixel.Strip = null
reset()
basic.forever(function () {
    noise = Math.map(input.soundLevel(), 0, 255, 0, 100)
    level = Math.map(input.soundLevel(), 0, 255, 0, 180)
    serial.writeValue("noise", noise)
    A灯噪音可视化()
})
