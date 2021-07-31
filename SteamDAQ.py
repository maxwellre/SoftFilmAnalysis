'''
https://nidaqmx-python.readthedocs.io/en/latest/
'''
#import nidaqmx
# with nidaqmx.Task() as task:
#     task.ai_channels.add_ai_voltage_chan("Dev1/ai3")
    #task.read(number_of_samples_per_channel=1000)
'''
PyDAQmx Info: https://www.pythonforthelab.com/blog/controlling-a-national-instruments-card-with-python/
DAQmxCreateAIVoltageChan: https://zone.ni.com/reference/en-XX/help/370471AA-01/daqmxcfunc/daqmxcreateaivoltagechan/
'''
import time
import numpy as np
import matplotlib.pyplot as plt
import PyDAQmx as nidaq

Fs = 1000 # Samples_Per_Sec =5000
TimeOut = 5 # The amount of time, in seconds, to wait for the function to read.
showPressure = True

'''-------------------------------------------------------------------------------'''
readLen = TimeOut * Fs # The number of samples, per channel, to read

calib = np.loadtxt('Calibration20210719.txt')
print("Calibration line a = %.16f, b = %.16f" % (calib[0],calib[1]))

daqdata = np.zeros((readLen,), dtype=np.float64)
actualReadNum = nidaq.int32()  # It holds the total number of dataFs1000Old points read per channel
with nidaq.Task() as task0:
    task0.CreateAIVoltageChan("Dev1/ai3", None, nidaq.DAQmx_Val_Diff, -1, 9, nidaq.DAQmx_Val_Volts, None)
    task0.CfgSampClkTiming("", Fs, nidaq.DAQmx_Val_Rising, nidaq.DAQmx_Val_FiniteSamps, readLen)
    task0.StartTask()
    print("Start sampling...")
    time0 = time.time()
    task0.ReadAnalogF64(readLen, TimeOut, nidaq.DAQmx_Val_GroupByChannel, daqdata, len(daqdata),
                        nidaq.byref(actualReadNum), None)
    print("Sample time = %.3f sec - Actual readed sample number = %d" % (time.time() - time0, actualReadNum.value))
    task0.StopTask()

fig1 = plt.figure(figsize = (16,6))
fig1.suptitle(("Fs = %.0f Hz" % Fs), fontsize=12)
ax = fig1.add_subplot(111) # projection='3d'
ax.set_xlabel('Samples')

if(showPressure):
    ax.set_ylabel('Pressure (Bar)')
else:
    ax.set_ylabel('Voltage (V)')

t = np.arange(actualReadNum.value)/Fs
if(showPressure):
    ax.plot(t, (daqdata-calib[1])*calib[0], '-', color='tab:red')
else:
    ax.plot(t, daqdata, '-', color='tab:red')
plt.show()

'''-------------------------------------------------------------------------------'''
currentTime = time.strftime("%H-%M-%S", time.localtime())

trial = 0

np.savetxt(("Data_Fs%d_at%s_BOPP20U9kV_t%02d.csv" % (Fs, currentTime, trial)), daqdata, delimiter=",")

# bar = 0.05
#
# np.savetxt(("%.2fbar_%d.csv" % (bar, trial)), daqdata, delimiter=",")

print("Data saved on %s" % currentTime)