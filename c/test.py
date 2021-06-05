import ctypes
from ctypes import util
from ctypes import CDLL
import time

# libPath = ctypes.util.find_library("./testOMP")
# testObj = ctypes.CDLL(libPath)

# testObj.compute.argtypes = [ctypes.c_double]
# testObj.compute.restype = ctypes.c_double

# time0 = time.time()

# V = testObj.compute(0.000001)

# print("Python: V = %f (Computed in %.10f sec)" % (V, time.time()-time0))    

libPath = ctypes.util.find_library("./triangle_volume")
triangle_volume = ctypes.CDLL(libPath)

triangle_volume.compute.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double]
triangle_volume.compute.restype = ctypes.c_double

time0 = time.time()
V = triangle_volume.compute(-42.87539243469328, 25.264607565306722, 0, 25.72354414871804, 50, 34.641, 68.14, 0.00001)

print("Volume of the triangle pouch V = %.6f mm3 (Computed in %.10f sec)" % (V, time.time()-time0))  


