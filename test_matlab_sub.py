from __future__ import division

PKG = 'px4'

import unittest
import rospy
import math
import numpy as np
from geometry_msgs.msg import PoseStamped, Quaternion
from mavros_test_common import MavrosTestCommon
from mavros_msgs.msg import Altitude, ExtendedState, HomePosition, State, \
                            WaypointList
from pymavlink import mavutil
from std_msgs.msg import Header
from threading import Thread
from tf.transformations import quaternion_from_euler


class MatlabTaskTest(unittest.TestCase):

    def test_matlab_sub(self):
        rospy.loginfo("successfully initialized")


if __name__ == '__main__':
    import rostest
    rostest.rosrun(PKG, 'test_matlab', MatlabTaskTest)

