import numpy as np
import random
import rospy
from geometry_msgs.msg import PoseStamped, Quaternion
from std_msgs.msg import String
PKG = 'PX4'

class test_task_env:
    def __init__(self):
        self.dt = 1
        self.env_min = 0
        self.env_max = 10

    def setUp(self):
        self.var = 0
        self.test_pub = rospy.Publisher(
            '/test_string', String, queue_size=1)

    def generate_tasks(self, numtask = 10):
        tasks = np.zeros((2, numtask))
        for i, t in enumerate(tasks):
            tasks[i] = (random.uniform(self.env_min, self.env_max))
        return tasks

    def assign_tasks(self):
        pass

    def test_allocation_alg(self):
        pass


if __name__ == '__main__':
    import rostest
    rospy.init_node('test_allocation_node', anonymous=True)

    rostest.rosrun(PKG, 'allocation_test',
                   test_task_env)

