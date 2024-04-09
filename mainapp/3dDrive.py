# import sys
# from time import gmtime, strftime
# import time
# import usb.core
# from logging import error, critical
# from mainapp.Utility import initialize_robot, SpaceNavigator, non_linear
#
# g_Coords = [0, 0, 0, 0, 0, 0]
# g_SPEED = 50
#
# # Robot Initialization
# myRobot = initialize_robot()
#
# # Initialize SpaceNavigator
# space_navigator = SpaceNavigator()
#
# print('Exit by pressing any button on the SpaceNavigator')
# print('')
#
# run = True
# tx = 0
# ty = 0
# tz = 0
# rx = 0
# ry = 0
# rz = 0
#
# g_tx = 0
# g_ty = 0
# g_tz = 0
# g_rx = 0
# g_ry = 0
# g_rz = 0
#
# SPEED = 50
# MODE = 1
# if SPEED > 100:
#     SPEED = 50
# if MODE is not 0 and MODE is not 1:
#     MODE = 1
#
# while run:
#     try:
#         data = space_navigator.read()
#         max_val = 0
#         max_index = 0
#
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
#
#             tx = non_linear(tx)
#             ty = non_linear(ty)
#             tz = non_linear(tz)
#
#             # Check if any of the translation values are the maximum
#             for i, val in enumerate([tx, ty, tz]):
#                 if abs(val) > abs(max_val):
#                     max_val = val
#                     max_index = i
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
#
#             rx = non_linear(rx)
#             ry = non_linear(ry)
#             rz = non_linear(rz)
#
#             # Check if any of the rotation values are the maximum
#             for i, val in enumerate([rx, ry, rz], start=3):
#                 if abs(val) > abs(max_val):
#                     max_val = val
#                     max_index = i
#
#         if data[0] == 3 and data[1] == 0:
#             data = None
#             # button packet - exit on the release
#             run = False
#
#         data = None
#
#         # Update the maximum coordinate in g_Coords
#         g_Coords[max_index] += max_val
#
#         # send coords to ROBOT
#         try:
#             print(myRobot.send_coords(g_Coords, SPEED))
#         except Exception as e:
#             error("An error occurred while sending coordinates to the robot: ", str(e))
#
#     except usb.core.USBError:
#         error("ReferenceError: USB Device is not found")
#
# # end while
# space_navigator.close()
#
#
#
#
#
#
#
#
# # import sys
# # from time import gmtime, strftime
# # import time
# # from logging import error, critical
# # from mainapp.Utility import initialize_robot, initialize_3dmouse
# #
# # # Robot Initialization
# # myRobot = initialize_robot()
# #
# # dev = initialize_3dmouse()
# #
# # cfg = dev.get_active_configuration()
# #
# # print('cfg is ', cfg)
# # intf = cfg[(0, 0)]
# # print('intf is ', intf)
# #
# #
# # print('')
# # print('Exit by pressing any button on the SpaceNavigator')
# # print('')
# # ep = usb.util.find_descriptor(intf, custom_match=lambda e: usb.util.endpoint_direction(
# #     e.bEndpointAddress) == usb.util.ENDPOINT_IN)
# # print('ep is ', ep)
# #
# # reattach = False
# # if dev.is_kernel_driver_active(0):
# #     reattach = True
# #     dev.detach_kernel_driver(0)
# #
# # ep_in = dev[0][(0, 0)][0]
# # ep_out = dev[0][(0, 0)][1]
# #
# #
# #
# # def CheckSpaceMouse():
# #     # Look for SpaceNavigator
# #     if dev is None:
# #         raise ValueError('SpaceNavigator not found');
# #     else:
# #         critical('SpaceNavigator found')
# #         print(dev)
# #         # Don't need all this but may want it for a full implementation
# #
# #
# # CheckSpaceMouse()
# #
# # # Precision
# #
# # def NonLinear(val):
# #     "Warp the incoming data to get more precision at the low end"
# #     val = val*(val*val)/(350*350)
# #
# #     # comment this out if you want to implement a dead zone close to zero.
# #     # it helps to isolate user input
# #     if val > 0 and val < 1:
# #         val = 1
# #
# #     return val
# #
# #
# #
# #
# #
# # JOINT_1_MAX = 165
# # JOINT_1_MIN = -165
# #
# # JOINT_2_MAX = 165
# # JOINT_2_MIN = -165
# #
# # JOINT_3_MAX = 165
# # JOINT_3_MIN = -165
# #
# # JOINT_4_MAX = 165
# # JOINT_4_MIN = -165
# #
# # JOINT_5_MAX = 165
# # JOINT_5_MIN = -165
# #
# # JOINT_6_MAX = 175
# # JOINT_6_MIN = -175
# #
# # run = True
# # tx = 0
# # ty = 0
# # tz = 0
# # rx = 0
# # ry = 0
# # rz = 0
# #
# #
# #
# #
# # g_tx = 0
# # g_ty = 0
# # g_tz = 0
# # g_rx = 0
# # g_ry = 0
# # g_rz = 0
# #
# # #mc.send_angles([0,0,0,0,0,0],30)
# #
# # # type = int(input('=> 1 for JOINT \n=> 2 for COORDS'))
# # SPEED = 50
# # MODE = 1
# # if SPEED > 100:
# #     SPEED = 50
# # if MODE is not 0 and MODE is not 1:
# #     MODE = 1
# #
# #
# # while run:
# #     try:
# #         CheckSpaceMouse()
# #         data = dev.read(ep_in.bEndpointAddress, ep_in.bLength, 0)
# #         # raw data
# #         # print data
# #
# #         # print it correctly T: x,y,z R: x,y,z
# #         if data[0] == 1:
# #             # translation packet
# #             tx = data[1] + (data[2]*256)
# #             ty = data[3] + (data[4]*256)
# #             tz = data[5] + (data[6]*256)
# #
# #             if data[2] > 127:
# #                 tx -= 65536
# #             if data[4] > 127:
# #                 ty -= 65536
# #             if data[6] > 127:
# #                 tz -= 65536
# #
# #             if tx>g_tx:
# #                 g_tx = tx
# #                 if g_tx > 165:
# #                     g_tx = 165
# #                 if g_tx < -165:
# #                     g_tx = -165
# #             if ty>g_ty:
# #                 g_ty = ty
# #                 if g_ty > 165:
# #                     g_ty = 165
# #                 if g_ty < -165:
# #                     g_ty = -165
# #             if tz> g_tz:
# #                 g_tz = tz
# #                 if g_tz > 165:
# #                     g_tz = 165
# #                 if g_tz < -165:
# #                     g_tz = -165
# #
# #             print("T: ", tx, ty, tz)
# #             tx = NonLinear(tx)
# #             ty = NonLinear(ty)
# #             tz = NonLinear(tz)
# #
# #         if data[0] == 2:
# #             # rotation packet
# #             rx = data[1] + (data[2]*256)
# #             ry = data[3] + (data[4]*256)
# #             rz = data[5] + (data[6]*256)
# #
# #             if data[2] > 127:
# #                 rx -= 65536
# #             if data[4] > 127:
# #                 ry -= 65536
# #             if data[6] > 127:
# #                 rz -= 65536
# #
# #
# #             # if rx>g_rx:
# #             #     g_rx = rx
# #             #     if g_rx > 165:
# #             #         g_rx = 165
# #             #     if g_rx < -165:
# #             #         g_rx = -165
# #             # if ry>g_ry:
# #             #     g_ry = ry
# #             #     if g_ry > 165:
# #             #         g_ry = 165
# #             #     if g_ry < -165:
# #             #         g_ry = -165
# #             # if rz> g_rz:
# #             #     g_rz = rz
# #             #     if g_rz > 175:
# #             #         g_rz = 175
# #             #     if g_rz < -175:
# #             #         g_rz = -175
# #
# #
# #             print("R: ", rx, ry, rz)
# #             rx = NonLinear(rx)
# #             ry = NonLinear(ry)
# #             rz = NonLinear(rz)
# #
# #         if data[0] == 3 and data[1] == 0:
# #             # button packet - exit on the release
# #             run = False
# #
# #         # send coords to ROBOT
# #         print(myRobot.send_angles([tx, ty, tz, rx, ry, rz], SPEED))
# #         #critical('Moving Robot to', tx,ty,tz,rx,ry,rz)
# #
# #     except usb.core.USBError:
# #         error("ReferenceError: USB Device is not found")
# #     # except:
# #     #     error("read failed")
# # # end while
# # usb.util.dispose_resources(dev)
# #
# # if reattach:
# #     dev.attach_kernel_driver(0)
