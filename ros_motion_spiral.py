#!/usr/bin/env python3

import math
import time
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose


def spiral(vel_publisher, wk, rk):
    vel_msg = Twist()
    loop_rate = rospy.Rate(1)

    while rk < 10.5:
        rk = rk + 0.2
        wk = wk + 0.3
        vel_msg.linear.x = rk
        vel_msg.angular.z = wk
        vel_publisher.publish(vel_msg)

        loop_rate.sleep()

    vel_msg.linear.x = 0
    vel_msg.angular.z = 0
    vel_publisher.publish(vel_msg)


def poseCallback(pose_message):
    global x, y, yaw
    x = pose_message.x
    y = pose_message.y
    yaw = pose_message.theta


if __name__ == "__main__":
    try:
        rospy.init_node("turtlesim_motion_pose", anonymous=True)

        cmd_vel_topic = "/turtle1/cmd_vel"
        position_topic = "/turtle1/pose"

        vel_publisher = rospy.Publisher(cmd_vel_topic, Twist, queue_size=10)
        pose_subscriber = rospy.Subscriber(position_topic, Pose, poseCallback)
        time.sleep(2)

        spiral(vel_publisher, 0.2, 0)

    except rospy.ROSInterruptException:
        print("Exception occurred")
