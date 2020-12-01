import rospy
from std_msgs.msg import String, Int32, Bool

class Master:
    def __init__(self):
        self.tasks = [(0, 0, 20), (20, 20, 20), (15, 25, 20)]
        self.curr_task = self.tasks[0]
        self.uav0_idle = False

    def status_callback(self, data):
        rospy.loginfo('robot idling: ' + str(data))
        if not data:
            self.uav0_idle = True

    def check_task_status(self, task_status_pub, task_status):
        task_status_pub.publish(task_status)


global tasks
global curr_task
global count
tasks = [(0, 0, 20), (20, 20, 20), (15, 25, 20)]
curr_task = tasks[0]
count = 0


def test_func():
    ans = 1+1
    return ans


def callback(data):
    rospy.loginfo('num of remaining tasks '+str(data))


def status_callback(data):
    rospy.loginfo('robot idling: '+str(data))
    if not data:
        curr_task = tasks[count+1]
        count += 1


def check_task_status(task_status_pub, task_status):
    task_status_pub.publish(task_status)


def publish_tasks(pub, remTasks):
    pub.publish(remTasks)


if __name__ == '__main__':
    try:
        robot_status_sub = rospy.Subscriber('/uav0/task_status', Bool, status_callback)

        rospy.init_node('talker2', anonymous=True)
        pub = rospy.Publisher('/rem_task', Int32, queue_size=1)
        task_complete_pub = rospy.Publisher('/task_bool', Bool, queue_size=1)
        remTasks = 10
        rate = rospy.Rate(0.5)
        sub = rospy.Subscriber('/rem_task', Int32, callback)
        check_task_status(task_complete_pub, False)
        while not rospy.is_shutdown():
            publish_tasks(pub, remTasks)

            if remTasks <= 0:
                check_task_status(task_complete_pub, True)

            # pub = rospy.Publisher('/rem_task', Int32, queue_size=1)
            remTasks -= 1
            rate.sleep()
    except rospy.ROSInterruptException:
        pass
