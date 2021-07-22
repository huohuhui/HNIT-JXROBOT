# coding=utf-8
import time

from naoqi import ALProxy

IP = "192.168.1.107"
PORT = 9559

period = 200
memoryProxy = ALProxy("ALMemory", IP, PORT)
sonarProxy = ALProxy("ALSonar", IP, PORT)
sonarProxy.subscribe("Test_InertialSensor", period, 0.0)

memValueX = "Device/SubDeviceList/InertialSensor/AngleX/Sensor/Value"
memValueY = "Device/SubDeviceList/InertialSensor/AngleY/Sensor/Value"
memValueZ = "Device/SubDeviceList/InertialSensor/AngleZ/Sensor/Value"

print
try:
    while True:
        time.sleep(period / 1000)
        valX = memoryProxy.getData(memValueX)
        valY = memoryProxy.getData(memValueY)
        valZ = memoryProxy.getData(memValueZ)
        print "\rAngleX = {}, AngleY = {}, AngleZ = {}".format(valX, valY, valZ),

finally:
    sonarProxy.unsubscribe("Test_InertialSensor")
