import rosebot
import time

def fasterbeep():
    robot = rosebot.RoseBot()
    robot.drive_system.go(30,30)
    while True:
        distance = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        delay =distance/200
        robot.sound_system.tone_maker.play_tone(400,300)
        time.sleep(delay)
        if distance < 50:
            robot.drive_system.stop()
            break


