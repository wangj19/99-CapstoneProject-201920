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
import rosebot



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
    teleop_frame, arm_frame, control_frame,sound_frame = get_shared_frames(main_frame,mqtt_sender)

    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------
    grid_frames(teleop_frame, arm_frame, control_frame, sound_frame)

    # -------------------------------------------------------------------------
    # The event loop:
    # -------------------------------------------------------------------------
    root.mainloop()



def get_shared_frames(main_frame, mqtt_sender):
    teleop_frame = shared_gui.get_teleoperation_frame(main_frame,mqtt_sender)
    arm_frame = shared_gui.get_arm_frame(main_frame, mqtt_sender)
    control_frame = shared_gui.get_control_frame(main_frame, mqtt_sender)
    sound_frame = shared_gui.get_sound_control_frame(main_frame, mqtt_sender)
    return teleop_frame, arm_frame, control_frame,sound_frame

def grid_frames(teleop_frame, arm_frame, control_frame,sound_frame):
    teleop_frame.grid(row=0, column=0)
    arm_frame.grid(row =1, column=0)
    control_frame.grid(row=2,column=0)
    sound_frame.grid(row=3,column=0)

def get_closer_tone(frequency):
    robot = rosebot.RoseBot()
    distance = robot.sensor_system.ir_proximity_sensor.get_distance()
    print(distance)

    speakerr = robot.sound_system.tone_maker.play_tone_sequence(frequency / distance, 50)
    robot.drive_system.go(50,50)

    while True:
        if frequency>0:
            return speakerr
        else:
            return None

get_closer_tone(100)






# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()