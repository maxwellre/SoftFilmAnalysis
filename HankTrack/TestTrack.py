import ctypes
import numpy as np
from ctypes import util
from ctypes import CDLL
from os import path

'''Import LeapC libraray'''
sdkPath = path.join(path.dirname(__file__), 'LeapSDK')

libPath = ctypes.util.find_library(path.join(sdkPath, 'LeapC'))
leapc = ctypes.CDLL(libPath)

libPath = ctypes.util.find_library(path.join(sdkPath, 'libExampleConnection'))
leapc_lib = ctypes.CDLL(libPath)

leapc_lib.getOneFrame.argtypes = [ctypes.POINTER(ctypes.c_float)]
leapc_lib.getOneFrame.restype = ctypes.c_int

'''------------------------------------------------------------------------------------------------------------------'''

if __name__ == '__main__':
    leapc_lib.OpenConnection()

    while not leapc_lib.IsConnected:
        leapc_lib.millisleep(100)

    print("Leap Motion Connected")

    # oneFrame = LEAP_TRACKING_EVENT()

    while True:
        data1f = np.zeros((9,), dtype=np.float32)

        trackres = leapc_lib.getOneFrame(data1f.ctypes.data_as(ctypes.POINTER(ctypes.c_float)))

        if(trackres == 1):
            print(data1f)

        leapc_lib.millisleep(100)




    # End
    leapc_lib.DestroyConnection()

