import rosebot
import time

robot = rosebot.RoseBot
def fasterbeep():
    robot.drive_system.go(30,30)
    while True:
        distance = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        delay = distance/300
        robot.sound_system.tone_maker.play_tone(400,300)
        time.sleep(delay)
        if distance < 40:
            robot.drive_system.stop()
            break

def find_stage():
    robot.drive_system.go(50,50)
    while True:
        distance = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        delay = distance / 300
        robot.sound_system.tone_maker.play_tone(distance*3, 200)
        time.sleep(delay)
        if robot.sensor_system.color_sensorget_color_as_name() != 'Red':
            robot.drive_system.stop()
            break
    time.sleep(0.2)
    robot.drive_system.go(30,30)
    time.sleep(0.3)
    robot.sound_system.speech_maker.speak('welcome ladies and gentleman')
