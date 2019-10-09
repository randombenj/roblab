import time
import random
from pepper import Robot, PepperConfiguration

pepper = Robot(PepperConfiguration("Porter"))

pepper.ALMotion.wakeUp()
pepper.ALLeds.rotateEyes(0x0000FF, 0.0, 0.0)

while not pepper.ALMotion.robotIsWakeUp():
    time.sleep(0.1)


pepper.ALAutonomousLife.setState("disabled")
pepper.ALRobotPosture.goToPosture("StandInit", 1)
pepper.ALTextToSpeech.setLanguage("English")
pepper.ALTextToSpeech.setParameter("speed", 60)
pepper.ALAnimatedSpeech.say("Howdy")
pepper.ALAnimatedSpeech.say("I a very sensitive robot! Don't push me around!")

NORMAL_ACC_X = (-2.5, -0.0)
NORMAL_GYR_X = (-2.0, 2.0)


def was_pushed_x(accx):
    if accx < NORMAL_ACC_X[0] or accx > NORMAL_ACC_X[1]:
        print("push: %.3f < %.3f < %.3f" % (NORMAL_ACC_X[0], accx, NORMAL_ACC_X[1]))
        return True
    return False


def was_turned_x(gyrx):
    if gyrx < NORMAL_GYR_X[0] or gyrx > NORMAL_GYR_X[1]:
        print("turn: %.3f < %.3f < %.3f" % (NORMAL_GYR_X[0], gyrx, NORMAL_GYR_X[1]))
        return True


def my_life_is_awful():
    rand = random.randint(1, 5)
    if not rand % 2:
        if rand == 2:
            pepper.ALAnimatedSpeech.say("i hate my life")
        else:
            pepper.ALAnimatedSpeech.say("why am i even here?")

while True:
    accx = pepper.ALMemory.getData("Device/SubDeviceList/InertialSensorBase/AccX/Sensor/Value")
    accy = pepper.ALMemory.getData("Device/SubDeviceList/InertialSensorBase/AccY/Sensor/Value")
    accz = pepper.ALMemory.getData("Device/SubDeviceList/InertialSensorBase/AccZ/Sensor/Value")
    #print("Acceleration: X: %.3f, Y %.3f, Z%.3f" % (accx, accy, accz))
    if was_pushed_x(accx):
        my_life_is_awful()
        pepper.ALTextToSpeech.say("don't push me!")

    gyx = pepper.ALMemory.getData("Device/SubDeviceList/InertialSensorBase/GyrX/Sensor/Value")
    gyy = pepper.ALMemory.getData("Device/SubDeviceList/InertialSensorBase/GyrY/Sensor/Value")
    gyz = pepper.ALMemory.getData("Device/SubDeviceList/InertialSensorBase/GyrZ/Sensor/Value")
    #print("Gyroscope:  X: %.3f, Y %.3f, Z%.3f" % (gyx, gyy, gyz))
    if was_turned_x(gyx):
        pepper.ALAnimatedSpeech.say("don't turn me!")


