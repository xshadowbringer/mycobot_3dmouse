#
# by xshadowbringer
#

import usb.core
import usb.util
from pymycobot.mycobot import MyCobot
from logging import error, critical


def initialize_robot():
    """Initialize the Robot Arm"""
    mc = MyCobot('/dev/ttyAMA0', 1000000)

    if mc.is_controller_connected() != 1:
        error("ReferenceError: RobotArm Not Found")
        exit(0)

    return mc


def initialize_3dmouse():
    """Initialize the 3D Mouse"""
    dev = usb.core.find(idVendor=0x46d, idProduct=0xc626)

    if dev is None:
        error('SpaceNavigator not found')

    return dev


def non_linear(val):
    """Non-linear function to process the data from the SpaceNavigator"""
    val = val * (val * val) / (350 * 350)

    if 0 < val < 1:
        val = 1

    return val


def process_data(data, indices, non_linear):
    """Process the data from the SpaceNavigator"""
    processed_values = []
    for i in indices:
        val = data[i] + (data[i+1]*256)
        if data[i+1] > 127:
            val -= 65536
        val = non_linear(val)
        processed_values.append(val)
    return processed_values


class SpaceNavigator:
    """Class to handle the SpaceNavigator 3D Mouse"""
    dev = None
    ep_in = None
    ep_out = None
    cfg = None
    intf = None

    def __init__(self):
        """Initialize the SpaceNavigator 3D Mouse"""
        self.dev = initialize_3dmouse()
        self.cfg = self.dev.get_active_configuration()
        self.intf = self.cfg[(0, 0)]
        self.ep_in = usb.util.find_descriptor(self.intf,
                                              custom_match=lambda e: usb.util.endpoint_direction(
                                                  e.bEndpointAddress) == usb.util.ENDPOINT_IN)
        self.ep_out = usb.util.find_descriptor(self.intf,
                                               custom_match=lambda e: usb.util.endpoint_direction(
                                                   e.bEndpointAddress) == usb.util.ENDPOINT_OUT)

        if self.dev.is_kernel_driver_active(0):
            self.dev.detach_kernel_driver(0)

    def check_space_mouse(self):
        """Check if the SpaceNavigator is connected"""
        if self.dev is None:
            raise ValueError('SpaceNavigator not found')
        else:
            critical('SpaceNavigator found')
            print(self.dev)

    def read(self):
        """Read data from the SpaceNavigator"""
        try:
            return self.dev.read(self.ep_in.bEndpointAddress, self.ep_in.bLength, 0)
        except usb.core.USBError:
            print("USBError: Unable to read from device")

    def write(self, data):
        """Write data to the SpaceNavigator"""
        try:
            self.dev.write(self.ep_out.bEndpointAddress, data, 0)
        except usb.core.USBError:
            print("USBError: Unable to write to device")

    def close(self):
        """Close the connection to the SpaceNavigator"""
        self.dev.attach_kernel_driver(0)
        usb.util.dispose_resources(self.dev)
        self.dev = None
        self.ep_in = None
        self.ep_out = None
        return

    def __del__(self):
        """Destructor to close the connection to the SpaceNavigator"""
        self.close()
        return
