
import rosebot
import time




def get_closer_tone():
    robot = rosebot.RoseBot()
    robot.drive_system.go(50, 50)
    while True:
        distance = robot.sensor_system.ir_proximity_sensor.get_distance()
        if distance > 20:
            robot.sound_system.tone_maker.play_tone(distance*3, 100)
        else:
            robot.drive_system.stop()
            robot.sound_system.tone_maker.play_tone(0, 0).wait()
            break


def final_week(robot):
    distance = robot.sensor_system.ir_proximity_sensor.get_distance()

    robot.sound_system.speech_maker.speak('Final week starts').wait()

    if distance >20:
        line_follower(robot)


    else:
        robot.drive_system.stop()
        time.sleep(0.2)
        robot.sound_system.speech_maker.speak('Cannot go forward').wait()


def line_follower(robot):
    distance = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()

    while True:
            if abs(robot.sensor_system.color_sensor.get_reflected_light_intensity()) < 10:
                robot.drive_system.go(20, 45)
                robot.led_system.right_led.turn_on()
                robot.led_system.right_led.turn_off()
                robot.led_system.right_led.turn_on()

            else:
                robot.drive_system.go(45, 20)
                robot.sound_system.tone_maker.play_tone(distance * 5, 100)
                robot.led_system.left_led.turn_on()
                robot.led_system.left_led.turn_off()
                robot.led_system.left_led.turn_on()
