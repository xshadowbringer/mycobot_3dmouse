import usb.core
from mainapp.Utility import SpaceNavigator
from logging import error, critical

# Create an instance of the SpaceNavigator class
space_navigator = SpaceNavigator()

# Check if the SpaceNavigator is found
space_navigator.check_space_mouse()

print('Exit by pressing any button on the SpaceNavigator')

run = True

while run:
    try:
        data = space_navigator.read()

        if data[0] == 1:
            # translation packet
            tx = data[1] + (data[2]*256)
            ty = data[3] + (data[4]*256)
            tz = data[5] + (data[6]*256)

            if data[2] > 127:
                tx -= 65536
            if data[4] > 127:
                ty -= 65536
            if data[6] > 127:
                tz -= 65536
            print("T: ", tx, ty, tz)

        if data[0] == 2:
            # rotation packet
            rx = data[1] + (data[2]*256)
            ry = data[3] + (data[4]*256)
            rz = data[5] + (data[6]*256)

            if data[2] > 127:
                rx -= 65536
            if data[4] > 127:
                ry -= 65536
            if data[6] > 127:
                rz -= 65536
            print("R: ", rx, ry, rz)

        if data[0] == 3 and data[1] == 0:
            data = None
            # button packet - exit on the release
            run = False

        data = None

    except usb.core.USBError:
        error("ReferenceError: USB Device is not found")

# When you're done, close the connection to the SpaceNavigator
space_navigator.close()










# import usb.core


# import usb.util
# import sys
# from time import gmtime, strftime
# import time
# from logging import error, critical
#
# # Look for SpaceNavigator
# dev = usb.core.find(idVendor=0x46d, idProduct=0xc626)
# if dev is None:
#     raise ValueError('SpaceNavigator not found')
# else:
#     critical('SpaceNavigator found')
#     print(dev)
#
#
# # Precision
#
# def NonLinear(val):
#     "Warp the incoming data to get more precision at the low end"
#     val = val*(val*val)/(350*350)
#
#     # comment this out if you want to implement a dead zone close to zero.
#     # it helps to isolate user input
#     if val > 0 and val < 1:
#         val = 1
#
#     return val
#
#
# # Don't need all this but may want it for a full implementation
#
# cfg = dev.get_active_configuration()
# print('cfg is ', cfg)
# intf = cfg[(0, 0)]
# print('intf is ', intf)
# ep = usb.util.find_descriptor(intf, custom_match=lambda e: usb.util.endpoint_direction(
#     e.bEndpointAddress) == usb.util.ENDPOINT_IN)
# print('ep is ', ep)
#
# reattach = False
# if dev.is_kernel_driver_active(0):
#     reattach = True
#     dev.detach_kernel_driver(0)
#
# ep_in = dev[0][(0, 0)][0]
# # ep_out = dev[0][(0, 0)][1]
#
# print('')
# print('Exit by pressing any button on the SpaceNavigator')
# print('')
#
# run = True
#
#
# while run:
#     try:
#         data = dev.read(ep_in.bEndpointAddress, ep_in.bLength, 0)
#         # raw data
#         # print data
#
#         # print it correctly T: x,y,z R: x,y,z
#         if data[0] == 1:
#             # translation packet
#             tx = data[1] + (data[2]*256)
#             ty = data[3] + (data[4]*256)
#             tz = data[5] + (data[6]*256)
#
#             if data[2] > 127:
#                 tx -= 65536
#             if data[4] > 127:
#                 ty -= 65536
#             if data[6] > 127:
#                 tz -= 65536
#             print("T: ", tx, ty, tz)
#             # tx = NonLinear(tx)
#             # ty = NonLinear(ty)
#             # tz = NonLinear(tz)
#
#         if data[0] == 2:
#             # rotation packet
#             rx = data[1] + (data[2]*256)
#             ry = data[3] + (data[4]*256)
#             rz = data[5] + (data[6]*256)
#
#             if data[2] > 127:
#                 rx -= 65536
#             if data[4] > 127:
#                 ry -= 65536
#             if data[6] > 127:
#                 rz -= 65536
#             print("R: ", rx, ry, rz)
#             # rx = NonLinear(rx)
#             # ry = NonLinear(ry)
#             # rz = NonLinear(rz)
#
#         if data[0] == 3 and data[1] == 0:
#             # button packet - exit on the release
#             run = False
#
#     except usb.core.USBError:
#         error("ReferenceError: USB Device is not found")
# # end while
# usb.util.dispose_resources(dev)
#
# if reattach:
#     dev.attach_kernel_driver(0)
