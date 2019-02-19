import rosebot
import time

def fasterbeep():
    robot = rosebot.RoseBot()
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
    robot = rosebot.RoseBot()
    robot.drive_system.go(50,50)
    while True:
        distance = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        delay = distance / 300
        robot.sound_system.tone_maker.play_tone(distance*3, 200)
        time.sleep(delay)
        if robot.sensor_system.color_sensor.get_color_as_name() != 'Red':
            robot.drive_system.stop()
            break
    time.sleep(0.2)
    robot.drive_system.go(30,30)
    time.sleep(0.3)
    robot.drive_system.stop()
    robot.sound_system.speech_maker.speak('welcome ladies and gentleman')

def dance():
        dance_movement1()
        dance_movement2()
        dance_movement3()
        dance_movement2()

def dance_movement1():
    robot = rosebot.RoseBot()
    robot.drive_system.go(80,-80)
    time.sleep(0.4)
    robot.drive_system.stop()
    robot.arm_and_claw.move_arm_to_position(3500)
    robot.drive_system.go(-80,80)
    time.sleep(0.4)
    robot.drive_system.stop()
    robot.arm_and_claw.lower_arm()


def dance_movement2():
    robot = rosebot.RoseBot()
    robot.arm_and_claw.move_arm_to_position(2000)
    robot.drive_system.go(-30,-30)
    time.sleep(0.5)
    robot.drive_system.stop()
    robot.arm_and_claw.move_arm_to_position(4000)
    robot.drive_system.go(30,30)
    time.sleep(0.5)
    robot.drive_system.stop()
    robot.arm_and_claw.lower_arm()

def dance_movement3():
    robot = rosebot.RoseBot()
    robot.drive_system.go(-80,80)
    time.sleep(0.4)
    robot.drive_system.stop()
    robot.arm_and_claw.move_arm_to_position(3500)
    robot.drive_system.go(80,-80)
    time.sleep(0.4)
    robot.drive_system.stop()
    robot.arm_and_claw.lower_arm()

def play_music():
    robot = rosebot.RoseBot()
    robot.arm_and_claw.move_arm_to_position(2500)
    robot.sound_system.tone_maker.play_tone_sequence([
        (392, 350, 100), (392, 350, 100), (392, 350, 100), (311.1, 250, 100),
        (466.2, 25, 100), (392, 350, 100), (311.1, 250, 100), (466.2, 25, 100),
        (392, 700, 100), (587.32, 350, 100), (587.32, 350, 100),
        (587.32, 350, 100), (622.26, 250, 100), (466.2, 25, 100),
        (369.99, 350, 100), (311.1, 250, 100), (466.2, 25, 100),
        (392, 700, 100),
        (784, 350, 100), (392, 250, 100), (392, 25, 100), (784, 350, 100),
        (739.98, 250, 100), (698.46, 25, 100), (659.26, 25, 100),
        (622.26, 25, 100), (659.26, 50, 400), (415.3, 25, 200),
        (554.36, 350, 100),
        (523.25, 250, 100), (493.88, 25, 100), (466.16, 25, 100),
        (440, 25, 100),
        (466.16, 50, 400), (311.13, 25, 200), (369.99, 350, 100),
        (311.13, 250, 100), (392, 25, 100), (466.16, 350, 100),
        (392, 250, 100),
        (466.16, 25, 100), (587.32, 700, 100), (784, 350, 100),
        (392, 250, 100),
        (392, 25, 100), (784, 350, 100), (739.98, 250, 100),
        (698.46, 25, 100),
        (659.26, 25, 100), (622.26, 25, 100), (659.26, 50, 400),
        (415.3, 25, 200),
        (554.36, 350, 100), (523.25, 250, 100), (493.88, 25, 100),
        (466.16, 25, 100), (440, 25, 100), (466.16, 50, 400),
        (311.13, 25, 200),
        (392, 350, 100), (311.13, 250, 100), (466.16, 25, 100),
        (392.00, 300, 150), (311.13, 250, 100), (466.16, 25, 100), (392, 700)
    ]).wait()
    robot.arm_and_claw.lower_arm()

def hug_fans():
    robot = rosebot.RoseBot()
    robot.drive_system.go(30,30)
    while True:
        time1 = time.time()
        dis = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        if dis < 35:
            robot.drive_system.stop()
            time_d = time.time() - time1
            break
    robot.arm_and_claw.move_arm_to_position(500)
    robot.arm_and_claw.lower_arm()
    robot.drive_system.go(-30,-30)
    time.sleep(time_d)
    robot.drive_system.stop()

def have_five_with_fans():
    robot = rosebot.RoseBot()
    time1 = time.time()
    robot.drive_system.spin_counterclockwise_until_sees_object(50, 200)
    time_d = time.time()-time1
    robot.arm_and_claw.move_arm_to_position(2000)
    robot.drive_system.go(40,40)
    time.sleep(0.8)
    robot.drive_system.stop()
    time.sleep(0.2)
    robot.drive_system.go(-40,-40)
    time.sleep(0.8)
    robot.arm_and_claw.lower_arm()
    robot.drive_system.go(50,-50)
    time.sleep(time_d)
    robot.drive_system.stop()

def leave_stage():
    robot = rosebot.RoseBot()
    robot.sound_system.speech_maker.speak('Goodbye guys')
    robot.drive_system.go(-50,-50)
    time.sleep(1)
    robot.drive_system.stop()