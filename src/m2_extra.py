
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



def final_week():
    delay = 400
    robot = rosebot.RoseBot()
    task_complete = 0
    robot.sound_system.speech_maker.speak('Final week starts')
    robot.drive_system.go(20, 20)

    distance = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()

    if robot.sensor_system.color_sensor.COLOR_NUMBERS == 1:
        robot.sound_system.speech_maker.speak('Computer Science Project')
        robot.drive_system.stop()
        time.sleep(delay)
        robot.sound_system.tone_maker(500, 500)
        task_complete = task_complete + 1
        robot.drive_system.go_straight_for_seconds(2, 20)

    if robot.sensor_system.color_sensor.COLOR_NUMBERS == 2:
        robot.sound_system.speech_maker.speak('Chemistry Final')
        robot.drive_system.stop()
        time.sleep(delay)
        robot.sound_system.tone_maker(500, 500)
        task_complete = task_complete + 1
        robot.drive_system.go_straight_for_seconds(2, 20)

    if robot.sensor_system.color_sensor.COLOR_NUMBERS == 3:
        robot.sound_system.speech_maker.speak('Math Final')
        robot.drive_system.stop()
        time.sleep(delay)
        robot.sound_system.tone_maker(500, 500)
        task_complete = task_complete + 1
        robot.drive_system.go_straight_for_seconds(2, 20)

    if robot.sensor_system.color_sensor.COLORS == 6:
        robot.sound_system.speech_maker.speak('Electric Engineering Final')
        robot.drive_system.stop()
        time.sleep(delay)
        robot.sound_system.tone_maker(500, 500)
        task_complete = task_complete + 1
        robot.drive_system.go_straight_for_seconds(2, 20)

    if robot.sensor_system.color_sensor.COLOR_NUMBERS == 5:
        robot.sound_system.speech_maker.speak('Physics Final')
        robot.drive_system.stop()
        time.sleep(delay)
        robot.sound_system.tone_maker(500, 500)
        task_complete = task_complete + 1
        robot.drive_system.go_straight_for_seconds(2, 20)


    if task_complete == 5:
        robot.drive_system.go(30, 30)
        if distance < 30:
            robot.drive_system.stop()
            robot.arm_and_claw.raise_arm()
            robot.sound_system.speech_maker.speak('End of Final Week')
            robot.arm_and_claw.lower_arm()