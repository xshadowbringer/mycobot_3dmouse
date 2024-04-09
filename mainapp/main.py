#
# by xshadowbringer
#

from logging import error
import usb.core

from mainapp.Utility import initialize_robot, SpaceNavigator, non_linear, process_data

g_Coords = [0, 0, 0, 0, 0, 0]
g_SPEED = 50
g_MODE = 1

# Robot Initialization
myRobot = initialize_robot()

# Initialize SpaceNavigator
space_navigator = SpaceNavigator()

# Check if the SpaceNavigator is connected
space_navigator.check_space_mouse()

print('Exit by pressing any button on the SpaceNavigator')
print('')

run = True
tx = 0
ty = 0
tz = 0
rx = 0
ry = 0
rz = 0

g_tx = 0
g_ty = 0
g_tz = 0
g_rx = 0
g_ry = 0
g_rz = 0

# Main loop
while run:
    try:
        g_Coords = myRobot.get_coords()
        data = space_navigator.read()
        max_val = 0
        max_index = 0

        if data[0] == 1:
            # translation packet
            tx, ty, tz = process_data(data, [1, 3, 5], non_linear)

            # Check if any of the translation values are the maximum
            for i, val in enumerate([tx, ty, tz]):
                if abs(val) > abs(max_val):
                    max_val = val
                    max_index = i

        if data[0] == 2:
            # rotation packet
            rx, ry, rz = process_data(data, [1, 3, 5], non_linear)

            # Check if any of the rotation values are the maximum
            for i, val in enumerate([rx, ry, rz], start=3):
                if abs(val) > abs(max_val):
                    max_val = val
                    max_index = i

        if data[0] == 3 and data[1] == 0:
            data = None
            # button packet - exit on the release
            run = False

        data = None

        # Update the maximum coordinate in g_Coords
        g_Coords[max_index] += max_val

        # send coords to ROBOT
        try:
            print(myRobot.send_coords(g_Coords, g_SPEED, g_MODE))
        except Exception as e:
            error("An error occurred while sending coordinates to the robot: ", str(e))

    except usb.core.USBError:
        error("ReferenceError: USB Device is not found")

# end of main loop

# Close the SpaceNavigator and the Robot
space_navigator.close()
myRobot.close()
