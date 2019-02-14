import rosebot
import time


def main():
    led()



def led():
    robot = rosebot.RoseBot()
    robot.drive_system.go(50, 50)
    while True:
        distance = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        delay = distance * 10
        robot.led_system.left_led.turn_on()
        time.sleep(delay)
        robot.led_system.left_led.turn_off()
        robot.led_system.right_led.turn_on()
        time.sleep(delay)
        robot.led_system.left_led.turn_on()
        time.sleep(delay)
        robot.led_system.left_led.turn_off()
        robot.led_system.right_led.turn_off()
        if distance < 50:
            robot.drive_system.stop()
            break


# def camera():
#     robot = rosebot.RoseBot()
#     robot.drive_system.display_camera_data()
#     robot.drive_system.spin_counterclockwise_until_sees_object(100, 500)
#     time.sleep(5)
#     robot.drive_system.spin_clockwise_until_sees_object(100, 500)


main()