
import rosebot
import time




#def get_closer_tone():
    #robot = rosebot.RoseBot()
   # robot.drive_system.go(50, 50)
   # while True:
       # distance = robot.sensor_system.ir_proximity_sensor.get_distance()
       # if distance > 20:
       #     robot.sound_system.tone_maker.play_tone(distance*3, 100)
       # else:
         #   robot.drive_system.stop()
         #   robot.sound_system.tone_maker.play_tone(0, 0).wait()
         #   break

delay = 400

def final_week():
    task_complete = 0
    robot = rosebot.RoseBot()
    distance = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
    robot.sound_system.speech_maker.speak('Final week starts')

    if robot.sensor_system.color_sensor.get_reflected_light_intensity == 1 & abs(task_complete) == 5:
        robot.drive_system.go(30, 30)
        if distance < 30:
            robot.drive_system.stop()
            robot.arm_and_claw.raise_arm()
            robot.sound_system.speech_maker.speak('End of Final Week')
            robot.arm_and_claw.lower_arm()

    if robot.sensor_system.color_sensor.get_reflected_light_intensity == 1:
        robot.sound_system.speech_maker.speak('Did not complete all tasks')



    def math_final_exam(task_complete):
        if robot.sensor_system.color_sensor.get_reflected_light_intensity == 3:
            robot.sound_system.speech_maker.speak('Math Final')

            while True:
                robot.drive_system.stop()
                time.sleep(delay)
                robot.sound_system.tone_maker(500, 500)
                task_complete = task_complete + 1
                robot.drive_system.go_straight_for_seconds(2, 20)
                break
        return math_final_exam(task_complete)

    def physics_final_exam(task_complete):
        if robot.sensor_system.color_sensor.get_reflected_light_intensity == 5:
            robot.sound_system.speech_maker.speak('Physics Final')

            while True:
                robot.drive_system.stop()
                time.sleep(delay)
                robot.sound_system.tone_maker(500, 500)
                task_complete = task_complete + 1
                robot.drive_system.go_straight_for_seconds(2, 20)
                break
        return physics_final_exam(task_complete)

    def ece_final_exam(task_complete):
        if robot.sensor_system.color_sensor.get_reflected_light_intensity == 4:
            robot.sound_system.speech_maker.speak('Electric Engineering Final')

            while True:
                robot.drive_system.stop()
                time.sleep(delay)
                robot.sound_system.tone_maker(500, 500)
                task_complete = task_complete + 1
                robot.drive_system.go_straight_for_seconds(2, 20)
                break
        return ece_final_exam(task_complete)

    def chemistry_final_exam(task_complete):
        if robot.sensor_system.color_sensor.get_reflected_light_intensity == 2:
            robot.sound_system.speech_maker.speak('Chemistry')

            while True:
                robot.drive_system.stop()
                time.sleep(delay)
                robot.sound_system.tone_maker(500, 500)
                task_complete = task_complete + 1
                robot.drive_system.go_straight_for_seconds(2,20)
                break
        return chemistry_final_exam(task_complete)

    def csse_project(task_complete):
        if robot.sensor_system.color_sensor.get_reflected_light_intensity == 1:
            robot.sound_system.speech_maker.speak('Computer Science')

            while True:
                robot.drive_system.stop()
                time.sleep(delay)
                robot.sound_system.tone_maker(500, 500)
                task_complete = task_complete + 1
                robot.drive_system.go_straight_for_seconds(2, 20)
                break
        return csse_project(task_complete)

