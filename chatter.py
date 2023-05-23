#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def talker():
    # Create a publisher object. Name the topic 'chatter', with message type String queue size 10
    # what does the queue size mean?
    # https://answers.ros.org/question/190357/rospypublisher-whats-a-good-choice-for-queue_size/
    pub = rospy.Publisher('chatter', String, queue_size=10)
    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'talker' node so that multiple talkers can
    # run simultaneously.
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(5) # msg per second

    i = 0
    while not rospy.is_shutdown():
        hello_str = "hello world {}".format(i)
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()
        i += 1

if __name__ == "__main__":
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
