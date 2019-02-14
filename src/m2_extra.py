
import shared_gui_delegate_on_robot
import rosebot
import mqtt_remote_method_calls as com
import time
import shared_gui_delegate_on_robot as rec
import m2_run_this_on_robot


def get_closer_tone():
    robot = rosebot.RoseBot()
    robot.drive_system.go(50, 50)
    while True:
        distance = robot.sensor_system.ir_proximity_sensor.get_distance()
        if distance > 40:
            robot.sound_system.tone_maker.play_tone(2000 / distance, 50)
        else:
            robot.drive_system.stop()
            robot.sound_system.tone_maker.play_tone(0, 0).wait()
            break

get_closer_tone()