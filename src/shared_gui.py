"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Constructs and returns Frame objects for the basics:
  -- teleoperation
  -- arm movement
  -- stopping the robot program

  This code is SHARED by all team members.  It contains both:
    -- High-level, general-purpose methods for a Snatch3r EV3 robot.
    -- Lower-level code to interact with the EV3 robot library.

  Author:  Your professors (for the framework and lower-level code)
    and Jiadi Wang, Jingyi Jia, and Chen Li.
  Winter term, 2018-2019.
"""

import tkinter
from tkinter import ttk
import time


def get_teleoperation_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame
    has Entry and Button objects that control the EV3 robot's motion
    by passing messages using the given MQTT Sender.
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Teleoperation")
    left_speed_label = ttk.Label(frame, text="Left wheel speed (0 to 100)")
    right_speed_label = ttk.Label(frame, text="Right wheel speed (0 to 100)")
    straight_speed_lebel = ttk.Label(frame, text='Straight speed(0 to 100)')
    time_lebel = ttk.Label(frame, text='Time in seconds')
    distance_lebel = ttk.Label(frame, text ='Distance in inches')

    left_speed_entry = ttk.Entry(frame, width=8)
    left_speed_entry.insert(0, "100")
    right_speed_entry = ttk.Entry(frame, width=8, justify=tkinter.RIGHT)
    right_speed_entry.insert(0, "100")
    time_entry = ttk.Entry(frame,width=8)
    straight_speed_entry = ttk.Entry(frame,width=8)
    straight_speed_entry.insert(0,"100")
    distance_entry = ttk.Entry(frame, width =8)

    forward_button = ttk.Button(frame, text="Forward")
    backward_button = ttk.Button(frame, text="Backward")
    left_button = ttk.Button(frame, text="Left")
    right_button = ttk.Button(frame, text="Right")
    stop_button = ttk.Button(frame, text="Stop")
    go_straight_for_second_button= ttk.Button(frame, text='Go straight for second')
    go_inches_time_button = ttk.Button(frame, text='Go straight for inches using time')
    go_inches_encoder_button = ttk.Button(frame, text='Go straight for inches using encoder')

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    left_speed_label.grid(row=1, column=0)
    right_speed_label.grid(row=1, column=2)
    left_speed_entry.grid(row=2, column=0)
    right_speed_entry.grid(row=2, column=2)

    forward_button.grid(row=3, column=1)
    left_button.grid(row=4, column=0)
    stop_button.grid(row=4, column=1)
    right_button.grid(row=4, column=2)
    backward_button.grid(row=5, column=1)

    time_lebel.grid(row=6, column=0)
    time_entry.grid(row=7, column=0)
    straight_speed_lebel.grid(row=6, column=1)
    straight_speed_entry.grid(row=7, column=1)
    distance_lebel.grid(row=8, column=0)
    distance_entry.grid(row=9, column=0)
    go_straight_for_second_button.grid(row=7, column=2)
    go_inches_time_button.grid(row=8, column=2)
    go_inches_encoder_button.grid(row=9, column=2)


    # Set the button callbacks:
    forward_button["command"] = lambda: handle_forward(
        left_speed_entry, right_speed_entry, mqtt_sender)
    backward_button["command"] = lambda: handle_backward(
        left_speed_entry, right_speed_entry, mqtt_sender)
    left_button["command"] = lambda: handle_left(
        left_speed_entry, right_speed_entry, mqtt_sender)
    right_button["command"] = lambda: handle_right(
        left_speed_entry, right_speed_entry, mqtt_sender)
    stop_button["command"] = lambda: handle_stop(mqtt_sender)
    go_straight_for_second_button['command'] = lambda:handle_go_straight_for_second(time_entry,straight_speed_entry,mqtt_sender)
    go_inches_time_button['command'] = lambda: handle_inches_time(distance_entry, straight_speed_entry, mqtt_sender)
    go_inches_encoder_button['command'] = lambda:handle_inches_encoder(distance_entry, straight_speed_entry, mqtt_sender)

    return frame


def get_arm_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame
    has Entry and Button objects that control the EV3 robot's Arm
    by passing messages using the given MQTT Sender.
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Arm and Claw")
    position_label = ttk.Label(frame, text="Desired arm position:")
    position_entry = ttk.Entry(frame, width=8)

    raise_arm_button = ttk.Button(frame, text="Raise arm")
    lower_arm_button = ttk.Button(frame, text="Lower arm")
    calibrate_arm_button = ttk.Button(frame, text="Calibrate arm")
    move_arm_button = ttk.Button(frame,
                                 text="Move arm to position (0 to 5112)")
    blank_label = ttk.Label(frame, text="")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    position_label.grid(row=1, column=0)
    position_entry.grid(row=1, column=1)
    move_arm_button.grid(row=1, column=2)

    blank_label.grid(row=2, column=1)
    raise_arm_button.grid(row=3, column=0)
    lower_arm_button.grid(row=3, column=1)
    calibrate_arm_button.grid(row=3, column=2)

    # Set the Button callbacks:
    raise_arm_button["command"] = lambda: handle_raise_arm(mqtt_sender)
    lower_arm_button["command"] = lambda: handle_lower_arm(mqtt_sender)
    calibrate_arm_button["command"] = lambda: handle_calibrate_arm(mqtt_sender)
    move_arm_button["command"] = lambda: handle_move_arm_to_position(
        position_entry, mqtt_sender)

    return frame


def get_control_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame has
    Button objects to exit this program and/or the robot's program (via MQTT).
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Control")
    quit_robot_button = ttk.Button(frame, text="Stop the robot's program")
    exit_button = ttk.Button(frame, text="Stop this and the robot's program")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    quit_robot_button.grid(row=1, column=0)
    exit_button.grid(row=1, column=2)

    # Set the Button callbacks:
    quit_robot_button["command"] = lambda: handle_quit(mqtt_sender)
    exit_button["command"] = lambda: handle_exit(mqtt_sender)
    return  frame

def get_sound_control_frame(window, mqtt_sender):
    frame = ttk.Frame(window,padding=10,borderwidth=5,relief='ridge')
    frame.grid()
    frame_label =ttk.Label(frame, text="Sound")
    frame_label.grid(row=0, column=2)
    frequency_label = ttk.Label(frame,text="Frequencey")
    frequency_entry = ttk.Entry(frame, width =8)
    duration_label = ttk.Label(frame, text='Duration')
    duration_entry = ttk.Entry(frame, width=8)
    number_label =  ttk.Label(frame, text = 'Number')
    number_entry = ttk.Entry(frame, width=6)
    frequency_label.grid(row = 1, column =1)
    frequency_entry.grid(row = 2, column =1)
    duration_label.grid(row=1, column = 2)
    duration_entry.grid(row=2, column = 2)
    number_label.grid(row = 1,column = 3)
    number_entry.grid(row = 2, column = 3)
    beep_button = ttk.Button(frame, text="Beep")
    beep_button.grid(row=3, column =3)
    beep_button['command'] = lambda: handle_beep(number_entry, mqtt_sender)
    play_tone_button = ttk.Button(frame,text = "Play Tone")
    play_tone_button.grid(row=3,column = 1)
    play_tone_button['command'] = lambda: handle_play_tone(frequency_entry, duration_entry, mqtt_sender)
    phrase_label = ttk.Label(frame, text = 'Phrase')
    phrase_label.grid(row=4, column = 1)
    phrase_entry = ttk.Entry(frame, width = 16)
    phrase_entry.grid(row=5, column = 1)
    phrase_button = ttk.Button(frame, text="Speak Phrase")
    phrase_button.grid(row=4, column = 2)
    phrase_button['command'] = lambda: handle_speak_phrase(phrase_entry, mqtt_sender)

    return frame

def color_frame(window, mqtt_sender):
    frame = ttk.Frame(window, padding = 10, borderwidth = 5, relief='ridge')
    frame.grid()
    frame_label = ttk.Label(frame, text='Color oontrol')
    frame_label.grid(row=0, column = 2)
    speed_label = ttk.Label(frame, text='Speed')
    speed_label.grid(row=1, column = 1)
    speed_entry = ttk.Entry(frame,width = 8)
    speed_entry.grid(row=2, column = 1)
    speed_entry.insert(0,'100')
    intensity_label = ttk.Label(frame, text = 'Intensity')
    intensity_label.grid(row=1, column = 2)
    intensity_entry = ttk.Entry(frame, width = 8)
    intensity_entry.grid(row=2, column = 2)
    color_label = ttk.Label(frame, text='Color')
    color_label.grid(row=1, column=3)
    color_entry = ttk.Entry(frame, width=12)
    color_entry.grid(row=2, column=3)
    go_inten_less_button = ttk.Button(frame,text='Go until intensity less')
    go_inten_less_button.grid(row=3,column=2)
    go_inten_less_button['command'] = lambda:handle_go_inten_less(intensity_entry,speed_entry,mqtt_sender)
    go_inten_more_button = ttk.Button(frame,text='Go until intensity more')
    go_inten_more_button.grid(row=4,column=2)
    go_inten_more_button['command'] = lambda:handle_go_inten_more(intensity_entry,speed_entry,mqtt_sender)
    go_color_is_button = ttk.Button(frame,text='Go until color is')
    go_color_is_button.grid(row=5,column=2)
    go_color_is_button['command'] = lambda:handle_go_color_is(color_entry,speed_entry,mqtt_sender)
    go_color_not_button = ttk.Button(frame,text='Go until color not')
    go_color_not_button.grid(row=6,column=2)
    go_color_not_button['command'] = lambda:handle_go_color_not(color_entry,speed_entry,mqtt_sender)

    return frame
###############################################################################
###############################################################################
# The following specifies, for each Button,
# what should happen when the Button is pressed.
###############################################################################
###############################################################################

###############################################################################
# Handlers for Buttons in the Teleoperation frame.
###############################################################################
def handle_forward(left_entry_box, right_entry_box, mqtt_sender):
    print('Got Forward', left_entry_box.get(), right_entry_box.get())
    mqtt_sender.send_message('forward',[left_entry_box.get(), right_entry_box.get()])
    """
    Tells the robot to move using the speeds in the given entry boxes,
    with the speeds used as given.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """

def handle_backward(left_entry_box, right_entry_box, mqtt_sender):
    print('Got Backward', -int(left_entry_box.get()), -int(right_entry_box.get()))
    mqtt_sender.send_message('backward',[left_entry_box.get(), right_entry_box.get()])
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negatives of the speeds in the entry boxes.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """

def handle_left(left_entry_box, right_entry_box, mqtt_sender):
    print('Go Left', -int(left_entry_box.get()), int(right_entry_box.get()))
    mqtt_sender.send_message('left',[left_entry_box.get(), right_entry_box.get()])
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negative of the speed in the left entry box.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """

def handle_right(left_entry_box, right_entry_box, mqtt_sender):
    print('Go Right', int(left_entry_box.get()), -int(right_entry_box.get()))
    mqtt_sender.send_message('left',[left_entry_box.get(), right_entry_box.get()])
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negative of the speed in the right entry box.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """

def handle_stop(mqtt_sender):
    print('Stop')
    mqtt_sender.send_message('stop')
    """
    Tells the robot to stop.
      :type  mqtt_sender:  com.MqttClient
    """

def handle_go_straight_for_second(time_entry_box, speed_entry_box, mqtt_sender):
    print('Go Staight for seconds', time_entry_box.get(), speed_entry_box.get())
    mqtt_sender.send_message('go_straight_for_seconds', [time_entry_box.get(),speed_entry_box.get()])

def handle_inches_time(inches_entry_box, speed_entry_box, mqtt_sender):
    print('Go Staight for inches using time', inches_entry_box.get(), speed_entry_box.get())
    mqtt_sender.send_message('go_straight_inches_time', [inches_entry_box.get(),speed_entry_box.get()])

def handle_inches_encoder(inches_entry_box, speed_entry_box, mqtt_sender):
    print('Go Staight for inches using encoder', inches_entry_box.get(), speed_entry_box.get())
    mqtt_sender.send_message('go_straight_inches_encoder', [inches_entry_box.get(),speed_entry_box.get()])

###############################################################################
# Handlers for Buttons in the ArmAndClaw frame.
###############################################################################
def handle_raise_arm(mqtt_sender):
    print('Raise Arm')
    mqtt_sender.send_message('raise_arm')
    """
    Tells the robot to raise its Arm until its touch sensor is pressed.
      :type  mqtt_sender:  com.MqttClient
    """


def handle_lower_arm(mqtt_sender):
    print('Lower Arm')
    mqtt_sender.send_message('lower_arm')
    """
    Tells the robot to lower its Arm until it is all the way down.
      :type  mqtt_sender:  com.MqttClient
    """


def handle_calibrate_arm(mqtt_sender):
    print('Calibrate Arm')
    mqtt_sender.send_message('calibrate_arm')
    """
    Tells the robot to calibrate its Arm, that is, first to raise its Arm
    until its touch sensor is pressed, then to lower its Arm until it is
    all the way down, and then to mark taht position as position 0.
      :type  mqtt_sender:  com.MqttClient
    """


def handle_move_arm_to_position(arm_position_entry, mqtt_sender):
    print('Move Arm To', arm_position_entry.get())
    mqtt_sender.send_message('move_arm_to_position', [arm_position_entry.get()])
    """
    Tells the robot to move its Arm to the position in the given Entry box.
    The robot must have previously calibrated its Arm.
      :type  arm_position_entry  ttk.Entry
      :type  mqtt_sender:        com.MqttClient
    """

###############################################################################
# Sound Part
###############################################################################
def handle_beep(number_entry, mqtt_sender):
    print('Beep', number_entry.get())
    mqtt_sender.send_message('beep', [number_entry.get()])
def handle_play_tone(frequency, duration, mqtt_sender):
    print('Play Tone', frequency.get(), duration.get())
    mqtt_sender.send_message('play_tone', [frequency.get(), duration.get()])
def handle_speak_phrase(phrase, mqtt_sender):
    print('Speak Phrase', phrase.get())
    mqtt_sender.send_message('speak_phrase', [phrase.get()])



###############################################################################
# Color Part
###############################################################################
def handle_go_inten_less(intensity_entry,speed_entry,mqtt_sender):
    print("Go Straight Until Intensity is less than", intensity_entry.get())
    mqtt_sender.send_message('go_inten_less', [intensity_entry.get(),speed_entry.get()])
def handle_go_inten_more(intensity_entry,speed_entry,mqtt_sender):
    print("Go Straight Until Intensity is more than", intensity_entry.get())
    mqtt_sender.send_message('go_inten_more', [intensity_entry.get(), speed_entry.get()])
def handle_go_color_is(color_entry,speed_entry,mqtt_sender):
    print("Go straight untile color is", color_entry.get())
    mqtt_sender.send_message('go_color_is',[color_entry.get(), speed_entry.get()])
def handle_go_color_not(color_entry,speed_entry,mqtt_sender):
    print("Go straight untile color is not", color_entry.get())
    mqtt_sender.send_message('go_color_not',[color_entry.get(), speed_entry.get()])

###############################################################################
# Handlers for Buttons in the Control frame.
###############################################################################
def handle_quit(mqtt_sender):
    """
    Tell the robot's program to stop its loop (and hence quit).
      :type  mqtt_sender:  com.MqttClient
    """
    print('quit')
    mqtt_sender.send_message('quit')


def handle_exit(mqtt_sender):
    """
    Tell the robot's program to stop its loop (and hence quit).
    Then exit this program.
      :type mqtt_sender: com.MqttClient
    """
    print('exit')
    handle_quit(mqtt_sender)
    exit()
