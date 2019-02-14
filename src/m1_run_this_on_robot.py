"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Jiadi Wang.
  Winter term, 2018-2019.
"""

import rosebot
import mqtt_remote_method_calls as com
import time
import shared_gui_delegate_on_robot as rec


def main():

    real_thing()




def real_thing():
    robot = rosebot.RoseBot()
    receiver = rec.Receiver(robot)
    mqtt_receiver = com.MqttClient(receiver)
    mqtt_receiver.connect_to_pc()


    while True:
        time.sleep(0.01)
        if receiver.is_time_to_stop:
            break

def fasterbeep():
    robot = rosebot.RoseBot()
    robot.drive_system.go(50,50)
    distance = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
    print(distance)
    while True:
        distance = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        delay = 1000-1010/distance
        robot.sound_system.beeper.beep()
        time.sleep(delay)
        if distance < 1:
            robot.drive_system.stop()
            break

def camera():
    robot = rosebot.RoseBot()
    robot.drive_system.display_camera_data()
    robot.drive_system.spin_counterclockwise_until_beacon_heading_is_nonpositive(100, 500)
    time.sleep(5)
    robot.drive_system.spin_clockwise_until_beacon_heading_is_nonnegative(50, 500)

def feature_10():
    robot = rosebot.RoseBot()
    robot.drive_system.go(50,50)
    distance = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
    print(distance)
    while True:
        distance = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        delay = 1000-1010/distance
        robot.sound_system.beeper.beep()
        time.sleep(delay)
        if distance < 1:
            robot.drive_system.stop()
            break
    while True:
        if distance > 1:
            robot.sound_system.tone_maker.play_tone(2000 / distance, 50)
        else:
            robot.drive_system.stop()
            robot.sound_system.tone_maker.play_tone(0, 0).wait()
            break
    while True:
        distance = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        delay = distance * 100
        robot.led_system.left_led.turn_on()
        time.sleep(delay)
        robot.led_system.left_led.turn_off()
        robot.led_system.right_led.turn_on()
        time.sleep(delay)
        robot.led_system.left_led.turn_on()
        time.sleep(delay)
        robot.led_system.left_led.turn_off()
        robot.led_system.right_led.turn_off()
        if distance < 1:
            robot.drive_system.stop()
            break
    robot.drive_system.arm_and_claw.raise_arm






# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()