"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Jiadi.
  Winter term, 2018-2019.
"""

import mqtt_remote_method_calls as com
import tkinter
from tkinter import ttk
import shared_gui

def project_frame():
    mqtt_sender = com.MqttClient()
    mqtt_sender.connect_to_ev3()
    root = tkinter.Tk()
    root.title('EV3 Super Star')
    project_frame = ttk.Frame(root, padding= 10, borderwidth = 5,relief='groove')
    project_frame.grid()

    stage_label = ttk.Label(project_frame, text = "Stage")
    stage_label.grid(row=1, column = 0)
    find_stage_button = ttk.Button(project_frame, text= 'Find Stage')
    find_stage_button.grid(row = 1, column = 1)
    find_stage_button['command'] = lambda: handle_find_stage(mqtt_sender)
    leave_stage_button = ttk.Button(project_frame, text= 'Leave Stage')
    leave_stage_button.grid(row = 1, column = 2)
    leave_stage_button['command'] = lambda: handle_leave_stage(mqtt_sender)

    concert_label = ttk.Label(project_frame,text='Concert')
    concert_label.grid(row=2, column = 0)
    dance_button = ttk.Button(project_frame, text= 'Dance')
    dance_button.grid(row = 2, column = 1)
    dance_button['command'] = lambda: handle_dance(mqtt_sender)
    play_music_button = ttk.Button(project_frame, text= 'Play Music')
    play_music_button.grid(row = 2, column = 2)
    play_music_button['command'] = lambda: handle_play_music(mqtt_sender)

    fans_label = ttk.Label(project_frame, text='Have fun with fans')
    fans_label.grid(row = 3, column = 0)
    hug_fans_button = ttk.Button(project_frame, text= 'Hug fans')
    hug_fans_button.grid(row = 3, column = 1)
    hug_fans_button['command'] = lambda: handle_hug_fans(mqtt_sender)
    have_five_button = ttk.Button(project_frame, text= 'Have five')
    have_five_button.grid(row = 3, column = 2)
    have_five_button['command'] = lambda: handle_have_five(mqtt_sender)

    control_label = ttk.Label(project_frame,text = 'Control')
    control_label.grid(row = 4, column = 0 )
    quit_robot_button = ttk.Button(project_frame, text="QUIT")
    exit_button = ttk.Button(project_frame, text="EXIT")
    quit_robot_button.grid(row=4, column=1)
    exit_button.grid(row=4, column=2)
    quit_robot_button["command"] = lambda: handle_quit(mqtt_sender)
    exit_button["command"] = lambda: handle_exit(mqtt_sender)

    root.mainloop()




def main():
    mqtt_sender = com.MqttClient()
    mqtt_sender.connect_to_ev3()
    root = tkinter.Tk()
    root.title('CSSE 120 Capstone Project')
    main_frame = ttk.Frame(root, padding = 10, borderwidth = 5,relief='groove')
    main_frame.grid()
    teleop_frame, arm_frame,control_frame, sound_frame, color_frame, distance_frame, camera_frame = get_shared_frames(main_frame, mqtt_sender)
    grid_frames(teleop_frame, arm_frame, control_frame, sound_frame,color_frame, distance_frame, camera_frame)
    fasterbeep_button = ttk.Button(main_frame, text='Faster beep')
    fasterbeep_button. grid(row = 2, column=3)
    fasterbeep_button['command'] = lambda: handle_fasterbeep(mqtt_sender)
    root.mainloop()
def get_shared_frames(main_frame, mqtt_sender):
    teleop_frame = shared_gui.get_teleoperation_frame(main_frame,mqtt_sender)
    arm_frame = shared_gui.get_arm_frame(main_frame, mqtt_sender)
    control_frame = shared_gui.get_control_frame(main_frame, mqtt_sender)
    sound_frame = shared_gui.get_sound_control_frame(main_frame, mqtt_sender)
    color_frame = shared_gui.color_frame(main_frame, mqtt_sender)
    distance_frame = shared_gui.distance_frame(main_frame,mqtt_sender)
    camera_frame = shared_gui.camera_frame(main_frame,mqtt_sender)
    return teleop_frame, arm_frame, control_frame,sound_frame,color_frame,distance_frame, camera_frame
def grid_frames(teleop_frame, arm_frame, control_frame,sound_frame,color_frame,distance_frame,camera_frame):
    teleop_frame.grid(row=0, column=0)
    arm_frame.grid(row =1, column=0)
    control_frame.grid(row=2,column=0)
    sound_frame.grid(row=3,column=0)
    color_frame.grid(row=4, column=0)
    distance_frame.grid(row=0,column=1)
    camera_frame.grid(row=1,column=1)

def handle_fasterbeep(mqtt_sender):
    print('fasterbeep')
    mqtt_sender.send_message('fasterbeep')
# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
def handle_quit(mqtt_sender):
    print('quit')
    mqtt_sender.send_message('quit')
def handle_exit(mqtt_sender):
    print('exit')
    handle_quit(mqtt_sender)
    exit()
def handle_find_stage(mqtt_sender):
    print('find stage')
    mqtt_sender.send_message('find_stage')
def handle_leave_stage(mqtt_sender):
    print('leave stage')
    mqtt_sender.send_message('leave_stage')
def handle_dance(mqtt_sender):
    print('dance')
    mqtt_sender.send_message('dance')
def handle_play_music(mqtt_sender):
    print('play music')
    mqtt_sender.send_message('play_music')
def handle_hug_fans(mqtt_sender):
    print('hug fans')
    mqtt_sender.send_message('hug_fans')
def handle_have_five(mqtt_sender):
    print('have five')
    mqtt_sender.send_message('have_five_with_fans')
project_frame()