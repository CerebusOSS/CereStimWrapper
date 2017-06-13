"""
This script is intended to follow the example provided with the API in simpleExample.cpp
"""
import cerestim
DEV_SER = 15623

result, device_tuple = cerestim.BStimulator.scanForDevices()  # result = 0, device_tuple = (15623,)
if result == 0 and DEV_SER in device_tuple:
    stim = cerestim.BStimulator()
    result = stim.setDevice(device_tuple.index(DEV_SER))
    if result == 0:
        usbParams = cerestim.BUsbParams()
        usbParams.timeout = 1000  # msec
        usbParams.pid = cerestim.PN7655
        # usbParams.vid
        result = stim.connect(cerestim.BINTERFACE_DEFAULT, usbParams)
        if result == 0:
            # TODO: Stimulation.
            stim.disconnect()
