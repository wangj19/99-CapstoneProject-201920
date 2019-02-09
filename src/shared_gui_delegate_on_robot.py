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
        print('Got Backward', left_wheel_speed,right_wheel_speed)
        self.robot.drive_system.go(-int(left_wheel_speed), -int(right_wheel_speed))