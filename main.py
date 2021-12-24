# B控制暂停，舵机归零，灯关闭

def on_button_pressed_b():
    global noise, pause2
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
    noise = 0
    sb.set_servo_position(sb.servo(SBServo.SERVO_A), noise)
    sb.set_rgb_led_color(sb.rgb_led(SBRgbLed.RGB_LED_A), sb.color(SBColor.BLACK))
    sb.set_rgb_led_color(sb.rgb_led(SBRgbLed.RGB_LED_B), sb.color(SBColor.BLACK))
    basic.clear_screen()
    pause2 = not (pause2)
input.on_button_pressed(Button.B, on_button_pressed_b)

def A灯噪音可视化(亮度: number):
    led.set_brightness(亮度)
    led.plot_bar_graph(input.sound_level(), 255)
    sb.set_rgb_led_color_hsb(sb.rgb_led(SBRgbLed.RGB_LED_A),
        0,
        100,
        Math.map(亮度, 0, 255, 0, 100))
    # 设置指示灯A的颜色
    if level <= 30:
        sb.set_rgb_led_color(sb.rgb_led(SBRgbLed.RGB_LED_A), sb.color(SBColor.BLUE))
    elif level <= 60:
        sb.set_rgb_led_color(sb.rgb_led(SBRgbLed.RGB_LED_A), sb.color(SBColor.GREEN))
    elif level <= 90:
        sb.set_rgb_led_color_rgb(sb.rgb_led(SBRgbLed.RGB_LED_A), 80, 83, 27)
    elif level <= 120:
        sb.set_rgb_led_color(sb.rgb_led(SBRgbLed.RGB_LED_A), sb.color(SBColor.YELLOW))
    elif level <= 150:
        sb.set_rgb_led_color(sb.rgb_led(SBRgbLed.RGB_LED_A), sb.color(SBColor.ORANGE))
    else:
        sb.set_rgb_led_color(sb.rgb_led(SBRgbLed.RGB_LED_A), sb.color(SBColor.RED))
def 调整舵机位置(秒数: number):
    index = 0
    while index <= 秒数:
        basic.show_number(秒数 - index)
        basic.pause(1000)
        index += 1
    basic.clear_screen()
level = 0
pause2 = False
noise = 0
music.set_volume(input.light_level())
music.start_melody(music.built_in_melody(Melodies.ENTERTAINER),
    MelodyOptions.ONCE)
noise = 0
sb.set_servo_position(sb.servo(SBServo.SERVO_A), noise)
sb.set_rgb_led_color(sb.rgb_led(SBRgbLed.RGB_LED_A), sb.color(SBColor.BLACK))
sb.set_rgb_led_color(sb.rgb_led(SBRgbLed.RGB_LED_B), sb.color(SBColor.BLACK))
sb.set_servo_position(sb.servo(SBServo.SERVO_A), 0)
sb.set_continuous_servo_speed(sb.servo(SBServo.SERVO_A), 50)
basic.clear_screen()
pause2 = True
调整舵机位置(3)
pause2 = False

def on_forever():
    global noise, level
    noise = Math.map(input.sound_level(), 0, 255, 0, 100)
    level = Math.map(input.sound_level(), 0, 255, 0, 180)
    A灯噪音可视化(input.light_level())
basic.forever(on_forever)

# 设置舵机的位置

def on_forever2():
    while not (pause2):
        sb.set_servo_position(sb.servo(SBServo.SERVO_A), noise)
        basic.pause(200)
basic.forever(on_forever2)

def on_forever3():
    # 暂停时，右侧的B灯亮红灯，不暂停时是绿色
    if pause2:
        sb.set_rgb_led_color(sb.rgb_led(SBRgbLed.RGB_LED_B), sb.color(SBColor.RED))
    else:
        sb.set_rgb_led_color(sb.rgb_led(SBRgbLed.RGB_LED_B), sb.color(SBColor.GREEN))
basic.forever(on_forever3)
