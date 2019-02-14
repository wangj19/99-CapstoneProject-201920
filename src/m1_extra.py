import rosebot
import time

def fasterbeep():
    robot = rosebot.RoseBot()
    robot.drive_system.go(50,50)
    distance = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
    print(distance)
    while True:
        distance = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        delay = 10*distance
        robot.sound_system.tone_maker.play_tone(400,300)
        time.sleep(delay)
        if distance < 40:
            robot.drive_system.stop()
            break

def main():
    fasterbeep()

main()
