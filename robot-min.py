from math import copysign
from os.path import dirname, basename
from wpilib import Joystick, run, TimedRobot, CameraServer
from wpimath.trajectory import TrajectoryUtil
from glob import glob as files
import time


filenames = files(dirname(__file__) + "/paths-good/*.json")
try:
    filenames.sort(key=lambda filename: int(basename(filename).split(".")[0]))
except:
    raise Exception(
        "Files in `path` folder MUST follow 'INTEGER.*.json' pattern, where `INTEGER` is any integer value")

print("Path filenames are:", filenames)
trajectories = list(map(TrajectoryUtil.fromPathweaverJson, filenames))


@run
class Kthugdess(TimedRobot):
    def robotInit(self):
        # CameraServer.launch()
        self.chassis = Chassis()

    def reset(self):
        self.turret.reset()
        self.auto.reset()
        self.auto.start(self.chassis, self.gyro)

    autonomousInit = reset
    teleopInit = reset

    def autonomousPeriodic(self):\
            # Start the turret zeroing process. Make sure it's almost zeroed already (manually)
        pass


    def teleopPeriodic(self):
        pass

    def disabledInit(self):
        # self.turret.hood_goto(0)
        pass

    def disabledPeriodic(self):
        # print("Disabling periodic!")
        pass

