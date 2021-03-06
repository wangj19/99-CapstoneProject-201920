"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Jingyi.Jia.
  Winter term, 2018-2019.
"""
# update before commit and push

import mqtt_remote_method_calls as com
import tkinter
from tkinter import ttk
import shared_gui




def main():
    """
    This code, which must run on a LAPTOP:
      1. Constructs a GUI for my part of the Capstone Project.
      2. Communicates via MQTT with the code that runs on the EV3 robot.
    """
    # -------------------------------------------------------------------------
    # Construct and connect the MQTT Client:
    # -------------------------------------------------------------------------
    mqtt_sender = com.MqttClient()
    mqtt_sender.connect_to_ev3()


    # -------------------------------------------------------------------------
    # The root TK object for the GUI:
    # -------------------------------------------------------------------------
    root = tkinter.Tk()
    root.title("CSSE 120 Capstone Project")



    # -------------------------------------------------------------------------
    # The main frame, upon which the other frames are placed.
    # -------------------------------------------------------------------------
    main_frame = ttk.Frame(root, padding = 10, borderwidth = 6, relief ="groove")
    main_frame.grid()


    # -------------------------------------------------------------------------
    # Sub-frames for the shared GUI that the team developed:
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    teleop_frame, arm_frame, control_frame,sound_frame, camera_frame = get_shared_frames(main_frame,mqtt_sender)

    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------
    grid_frames(teleop_frame, arm_frame, control_frame, sound_frame, camera_frame)
    get_closer_tone_button = ttk.Button(main_frame, text = "more frequency when get closer")
    get_closer_tone_button.grid(row=1,column=3)
    get_closer_tone_button['command']=lambda: handle_get_closer_tone(mqtt_sender)

    final_week_button = ttk.Button(main_frame, text = "Alan's Final Week Tasks")
    final_week_button.grid(row=2,column = 3)
    final_week_button['command']=lambda: handle_final_week(mqtt_sender)

    # -------------------------------------------------------------------------
    # The event loop:
    # -------------------------------------------------------------------------
    root.mainloop()



def get_shared_frames(main_frame, mqtt_sender):
    teleop_frame = shared_gui.get_teleoperation_frame(main_frame,mqtt_sender)
    arm_frame = shared_gui.get_arm_frame(main_frame, mqtt_sender)
    control_frame = shared_gui.get_control_frame(main_frame, mqtt_sender)
    sound_frame = shared_gui.get_sound_control_frame(main_frame, mqtt_sender)
    camera_frame = shared_gui.camera_frame(main_frame,mqtt_sender)
    return teleop_frame, arm_frame, control_frame,sound_frame,camera_frame

def grid_frames(teleop_frame, arm_frame, control_frame,sound_frame,camera_frame):
    teleop_frame.grid(row=0, column=0)
    arm_frame.grid(row =1, column=0)
    control_frame.grid(row=2,column=0)
    sound_frame.grid(row=3,column=0)
    camera_frame.grid(row=4,column=0)


def handle_get_closer_tone(mqtt_sender):
    print('More frequency when closer')
    mqtt_sender.send_message('get_closer_tone')

def handle_final_week(mqtt_sender):
    print('final week tasks')
    mqtt_sender.send_message('final_week_task')





# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()