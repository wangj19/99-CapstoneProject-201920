"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Jingyi.Jia.
  Winter term, 2018-2019.
"""

import rosebot
import mqtt_remote_method_calls as com
import time
import shared_gui_delegate_on_robot as rec


def main():
    """
    This code, which must run on the EV3 ROBOT:
      1. Makes the EV3 robot to various things.
      2. Communicates via MQTT with the GUI code that runs on the LAPTOP.
    """
def real_thing():
    robot = rosebot.RoseBot()
    receiver = rec.Receiver(robot)
    mqtt_receiver = com.MqttClient(receiver)
    mqtt_receiver.connect_to_pc()

    while True:
        time.sleep(0.01)
        if receiver.is_time_to_stop:
            break

def get_closer_tone():
    robot = rosebot.RoseBot()
    distance = robot.sensor_system.ir_proximity_sensor.get_distance()
    print(distance)
    speakerr = robot.sound_system.tone_maker.play_tone_sequence(100/distance, 50)

    robot.drive_system.go(50,50)

    while True:
        if distance>0:
            return speakerr
        else:
            return None

get_closer_tone()





# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()