import rospy
from std_msgs.msg import String, Int32, Bool
from geometry_msgs.msg import Pose, PoseStamped

# class Master:
#     def __init__(self):
#         self.tasks = [(0, 0, 20), (20, 20, 20), (15, 25, 20)]
#         self.curr_task = self.tasks[0]
#         self.uav0_idle = False
#
#     def status_callback(self, data):
#         rospy.loginfo('robot idling: ' + str(data))
#         if not data:
#             self.uav0_idle = True
#
#     def check_task_status(self, task_status_pub, task_status):
#         task_status_pub.publish(task_status)

# global variable
tasks = [(0, 0, 20), (20, 20, 20), (15, 25, 20)]
curr_task = tasks[0]
count = 0
task_done = False

curr_task_pub = rospy.Publisher('/uav0_curr_task', PoseStamped, queue_size=1)

rem_task_pub = rospy.Publisher('/rem_task', Int32, queue_size=1)
task_complete_pub = rospy.Publisher('/task_bool', Bool, queue_size=1)
mission_complete_pub = rospy.Publisher('/mission_bool', Bool, queue_size=1)
remTasks = 10

def callback(data):
    rospy.loginfo('num of remaining tasks '+str(data))


def status_callback(data):
    rospy.loginfo('robot idling: '+str(data))
    if data:
        global task_done, curr_task, count
        curr_task = tasks[count+1]
        count += 1
        publish_task_position(curr_task_pub, curr_task)

def publish_task_position(curr_task_pub, pos):
    waypoint = PoseStamped()
    waypoint.header.stamp = rospy.Time.now()
    waypoint.pose.position.x = pos[0]
    waypoint.pose.position.y = pos[1]
    waypoint.pose.position.z = pos[2]
    curr_task_pub.publish(waypoint)
    rospy.loginfo('current task position {}'.format(pos))

def pub_task_status(task_status_pub, task_status):
    task_status_pub.publish(task_status)


def publish_tasks(pub, remTasks):
    pub.publish(remTasks)


if __name__ == '__main__':
    try:
        rospy.init_node('talker2', anonymous=True)
        pub_task_status(task_complete_pub, False)

        rem_task_sub = rospy.Subscriber('/rem_task', Int32, callback)
        robot_status_sub = rospy.Subscriber('/task_bool', Bool, status_callback)

        rate = rospy.Rate(1)
        while not rospy.is_shutdown():
            publish_tasks(rem_task_pub, remTasks)
            if remTasks % 10 == 0:
                pub_task_status(task_complete_pub, True)

            publish_task_position(curr_task_pub, curr_task)
            # pub = rospy.Publisher('/rem_task', Int32, queue_size=1)
            remTasks -= 1

            if count == len(tasks):
                rospy.loginfo('tasks completed!')
                mission_complete_pub.publish(True)
                break
            mission_complete_pub.publish(False)
            rate.sleep()
    except rospy.ROSInterruptException:
        pass
