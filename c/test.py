import ctypes
from ctypes import util
from ctypes import CDLL
import time


libPath = ctypes.util.find_library("./triangle_volume")
triangle_volume = ctypes.CDLL(libPath)

triangle_volume.compute.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, 
                                    ctypes.c_double, ctypes.c_double]
triangle_volume.compute.restype = ctypes.c_double

time0 = time.time()
V = triangle_volume.compute(26.296411310760284, 21.843588689239716, 50, 42.52644767877184, 25.158589393088, 1e-06)

print("Volume of the triangle pouch V = %.3f mm3 (Computed in %.10f sec)" % (V, time.time()-time0))    

# triangle_volume.sphereCorner.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double]
# triangle_volume.sphereCorner.restype = ctypes.c_double
# V = triangle_volume.sphereCorner(691.501248, 22, 2500, 0.01)
# print("Volume of test = %.3f mm3" % (V))  

###8336.3940992213 89.63727525290695 2213.014366250316


# libPath = ctypes.util.find_library("./testOMP")
# testObj = ctypes.CDLL(libPath)

# testObj.compute.argtypes = [ctypes.c_double]
# testObj.compute.restype = ctypes.c_double

# time0 = time.time()

# V = testObj.compute(0.000001)

# print("Python: V = %f (Computed in %.10f sec)" % (V, time.time()-time0))    

# libPath = ctypes.util.find_library("./triangle_volume")
# triangle_volume = ctypes.CDLL(libPath)

# triangle_volume.compute.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double]
# triangle_volume.compute.restype = ctypes.c_double

# time0 = time.time()
# V = triangle_volume.compute(-42.87539243469328, 25.264607565306722, 0, 25.72354414871804, 50, 34.641, 68.14, 0.00001)

# print("Volume of the triangle pouch V = %.6f mm3 (Computed in %.10f sec)" % (V, time.time()-time0))  


