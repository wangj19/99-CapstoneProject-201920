"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  This code is the delegate for handling messages from the shared GUI.

  Author:  Your professors (for the framework)
    and Jiadi. Wang, Jingyi.Jia, Chen.Li.
  Winter term, 2018-2019.
"""
import m1_extra
import m2_extra
import m3_extra

class Receiver(object):
    def __init__(self, robot):
        ''':type robot: rosebot.Rosebot'''
        self.robot = robot
        self.is_time_to_stop = False

    def forward(self,left_wheel_speed, right_wheel_speed):
        print('Got Forward', left_wheel_speed,right_wheel_speed)
        self.robot.drive_system.go(int(left_wheel_speed), int(right_wheel_speed))

    def stop(self):
        print("Stop")
        self.robot.drive_system.stop()

    def backward(self,left_wheel_speed, right_wheel_speed):
        print('Got Backward', -int(left_wheel_speed),-int(right_wheel_speed))
        self.robot.drive_system.go(-int(left_wheel_speed), -int(right_wheel_speed))

    def left(self,left_wheel_speed, right_wheel_speed):
        print('Go Left', -int(left_wheel_speed), right_wheel_speed)
        self.robot.drive_system.go(-int(left_wheel_speed), int(right_wheel_speed))

    def right(self,left_wheel_speed, right_wheel_speed):
        print('Go right', left_wheel_speed, -int(right_wheel_speed))
        self.robot.drive_system.go(int(left_wheel_speed), -int(right_wheel_speed))

    def raise_arm(self):
        print('Raise Arm')
        self.robot.arm_and_claw.raise_arm()

    def lower_arm(self):
        print('Lower Arm')
        self.robot.arm_and_claw.lower_arm()

    def calibrate_arm(self):
        print('Calibrate Arm')
        self.robot.arm_and_claw.calibrate_arm()

    def move_arm_to_position(self, desired_arm_position):
        print('Move Arm To', int(desired_arm_position))
        self.robot.arm_and_claw.move_arm_to_position(int(desired_arm_position))

    def go_straight_for_seconds(self, second, speed):
        print('Go Straight for', int(second), 'seconds with speed', int(speed))
        self.robot.drive_system.go_straight_for_seconds(int(second), int(speed))

    def go_straight_inches_time(self, distance, speed):
        print('Go Straight for inches using time', int(distance), int(speed))
        self.robot.drive_system.go_straight_for_inches_using_time(int(distance), int(speed))

    def go_straight_inches_encoder(self, distance, speed):
        print('Go Straight for inches using encoder', int(distance), int(speed))
        self.robot.drive_system.go_straight_for_inches_using_encoder(int(distance), int(speed))

    def beep(self,n):
        print('beep')
        for _ in range(int(n)):
            self.robot.sound_system.beeper.beep().wait()

    def play_tone(self, frequency, duration):
        print('play tone')
        self.robot.sound_system.tone_maker.play_tone(int(frequency), int(duration))

    def speak_phrase(self, phrase):
        print('speak',phrase)
        self.robot.sound_system.speech_maker.speak(str(phrase))

    def quit(self):
        print('Got quit')
        self.is_time_to_sleep = True

    def go_inten_less(self, intensity, speed):
        print("go straight until intensity is less than", int(intensity))
        self.robot.drive_system.go_straight_until_intensity_is_less_than(int(intensity),int(speed))

    def go_inten_more(self, intensity, speed):
        print("go straight until intensity is more than", int(intensity))
        self.robot.drive_system.go_straight_until_intensity_is_greater_than(int(intensity),int(speed))

    def go_color_is(self, color, speed):
        print('go straight until color is', str(color))
        self.robot.drive_system.go_straight_until_color_is(str(color), int(speed))

    def go_color_not(self, color, speed):
        print('go straight until color is not', str(color))
        self.robot.drive_system.go_straight_until_color_is_not(str(color), int(speed))

    def go_for_less(self, inches, speed):
        print('go forward until distance is less than', int(inches))
        self.robot.drive_system.go_forward_until_distance_is_less_than(int(inches), int(speed))

    def go_back_more(self, inches, speed):
        print('go backward until distance is more than', int(inches))
        self.robot.drive_system.go_backward_until_distance_is_greater_than(int(inches), int(speed))

    def go_until_within(self, delta, inches, speed):
        print('go until distance is within', int(delta), int(inches))
        self.robot.drive_system.go_until_distance_is_within(int(delta), int(inches), int(speed))

    def clockwise_area(self, speed, area):
        print('Go clockwise until area', int(area))
        self.robot.drive_system.spin_clockwise_until_sees_object(int(speed),int(area))

    def counterclockwise_area(self, speed, area):
        print('Go counterclockwise until area', int(area))
        self.robot.drive_system.spin_counterclockwise_until_sees_object(int(speed),int(area))

    def fasterbeep(self):
        print('fasterbeep')
        m1_extra.fasterbeep()

    def get_closer_tone(self):
        print('Get closer and tone more frequency')
        m2_extra.get_closer_tone()

    def led(self):
        print('caonima')
        m3_extra.led()



    def final_week (self):
        print('Final Week Tasks')
        m2_extra.final_week()




