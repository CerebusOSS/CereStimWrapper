"""
This script is intended to follow the example provided with the API in simpleExample.cpp
"""
import cerestim
DEV_SER = 15623

result, device_tuple = cerestim.BStimulator.scanForDevices()  # result = 0, device_tuple = (15623,)
if result == 0 and DEV_SER in device_tuple:
    stim = cerestim.BStimulator()
    result = stim.setDevice(device_tuple.index(DEV_SER))
    if result == cerestim.BSUCCESS:
        print("Connected successfully")
        usbParams = cerestim.BUsbParams()
        usbParams.timeout = 1000  # msec
        usbParams.pid = cerestim.PN7655
        # usbParams.vid
        result = stim.connect(cerestim.BINTERFACE_DEFAULT, usbParams)
        if result == cerestim.BSUCCESS:
            print("usbParams updated successfully")
            waveform = {'afcf': 1, 'pulses': 255, 'amp1': 500, 'amp2': 500, 'width1': 100, 'width2': 100, 'frequency': 300, 'interphase': 53}
            result = stim.configureStimulusPattern(configID=15, **waveform)
            if result == cerestim.BSUCCESS:
                print("configureStimulusPattern success.")
            elif result == cerestim.BDISCONNECTED:
                print("cerestim disconnected")
            # TODO: Stimulation.
        stim.disconnect()
