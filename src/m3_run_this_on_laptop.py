"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Chen Li.
  Winter term, 2018-2019.
"""

import mqtt_remote_method_calls as com
import tkinter
from tkinter import ttk
import shared_gui


def main():
    mqtt_sender = com.MqttClient()
    mqtt_sender.connect_to_ev3()
    root = tkinter.Tk()
    root.title('CSSE 120 Capstone Project')
    main_frame = ttk.Frame(root, padding=10, borderwidth = 5,relief='groove')
    main_frame.grid()
    teleop_frame, arm_frame,camera_frame = get_shared_frames(main_frame, mqtt_sender)
    grid_frames(teleop_frame, arm_frame, camera_frame)
    led_button = ttk.Button(main_frame, text = 'led')
    led_button.grid(row = 2, column = 2)
    led_button['command'] = lambda:handle_led(mqtt_sender)
    root.mainloop()
def get_shared_frames(main_frame, mqtt_sender):
    teleop_frame = shared_gui.get_teleoperation_frame(main_frame,mqtt_sender)
    arm_frame = shared_gui.get_arm_frame(main_frame, mqtt_sender)
    camera_frame = shared_gui.camera_frame(main_frame,mqtt_sender)
    return teleop_frame, arm_frame, camera_frame
def grid_frames(teleop_frame, arm_frame,camera_frame):
    teleop_frame.grid(row=0, column=0)
    arm_frame.grid(row =1, column=0)
    camera_frame.grid(row=1,column=1)

def handle_led(mqtt_sender):
    print('led')
    mqtt_sender.send_message('led')



# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()