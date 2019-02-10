"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  This code is the delegate for handling messages from the shared GUI.

  Author:  Your professors (for the framework)
    and Jiadi. Wang, Jingyi.Jia, Chen.Li.
  Winter term, 2018-2019.
"""

class Receiver(object):
    def __init__(self, robot):
        ''':type robot: rosebot.Rosebot'''
        self.robot = robot

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