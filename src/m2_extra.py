import shared_gui_delegate_on_robot as rec
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

delay = 400
robot = rosebot.RoseBot
receiver = rec.Receiver(robot)
distance = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
task_complete = 0

def final_week():
    robot.drive_system.go(30,30)
    if task_complete == 5:
        robot.drive_system.go(30,30)
        if distance < 30:
            robot.sound_system.speech_maker.speak('End of Final Week')
            robot.arm_and_claw.raise_arm()





def math_final_exam(task_complete):
    if robot.sensor_system.color_sensor.get_reflected_light_intensity == 1:
        robot.sound_system.speech_maker.speak('Math Final Exam')

        while True:
            robot.drive_system.stop()
            time.sleep(delay)
            robot.sound_system.speech_maker.speak('Finish')
            task_complete = task_complete + 1
            break
    return task_complete


def physics_final_exam(task_complete):
    if robot.sensor_system.color_sensor.get_reflected_light_intensity == 2:
        robot.sound_system.speech_maker.speak('Physics Final Exam')

        while True:
            robot.drive_system.stop()
            time.sleep(delay)
            robot.sound_system.speech_maker.speak('Finish')
            task_complete = task_complete + 1
            break
    return task_complete


def ece_final_exam(task_complete):
    if robot.sensor_system.color_sensor.get_reflected_light_intensity == 3:
        robot.sound_system.speech_maker.speak('ECE Final Exam')

        while True:
            robot.drive_system.stop()
            time.sleep(delay)
            robot.sound_system.speech_maker.speak('Finish')
            task_complete = task_complete + 1
            break
    return task_complete

















