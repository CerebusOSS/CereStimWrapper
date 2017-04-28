"""
This script is intended to follow the example provided with the API in simpleExample.cpp
"""
import cerestim

result, device_tuple = cerestim.BStimulator.scanForDevices()  # result = 0, device_tuple = (15623,)
if len(device_tuple) > 0:
    stimulator = cerestim.BStimulator()
    result = stimulator.setDevice(device_tuple[0])
    # usbParams = cerestim.BUsbParams()
    # usbParams.timeout = 1000  # msec
    # usbParams.pid = cerestim.PN7655
    # usbParams.vid
    # result = stimulator.connect(cerestim.BINTERFACE_DEFAULT, usbParams)
