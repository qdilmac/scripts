#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist #task 1. import the message type Twist
from turtlesim.msg import Pose #task 2. import the message type Pose
import math
import time
from std_srvs.srv import Empty

x = 0
y = 0
z = 0
yaw = 0

def poseCallback(pose_message): #task 3. create a callback function
    global x, y, z, yaw
    x = pose_message.x
    y = pose_message.y
    yaw = pose_message.theta

def move(speed, distance):
    rospy.loginfo("Moving the turtle")
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10) #task 4. create a publisher object
    velocity_message = Twist()
    x0 = x
    y0 = y
    distance_moved = 0.0
    loop_rate = rospy.Rate(10)

    velocity_message.linear.x = speed

    while True:
        rospy.loginfo("Turtlesim moves forwards")
        velocity_publisher.publish(velocity_message)
        loop_rate.sleep()

        distance_moved = distance_moved + abs(0.5 * math.sqrt(((x - x0) ** 2) + ((y - y0) ** 2)))
        print(distance_moved)

        if not (distance_moved < distance):
            rospy.loginfo("Reached the target distance")
            break

    velocity_message.linear.x = 0.0
    velocity_publisher.publish(velocity_message) #task 5. publish the velocity message

if __name__ == '__main__':
    try:
        rospy.init_node('turtlesim_motion_pose', anonymous=True)
        position_topic = "/turtle1/pose"
        pose_subscriber = rospy.Subscriber(position_topic, Pose, poseCallback)
        time.sleep(2)

        print('Move: ')
        move(1.0, 5.0)
        time.sleep(2)

        print('Start reset: ')
        rospy.wait_for_service('reset')
        reset_turtle = rospy.ServiceProxy('reset', Empty)
        reset_turtle()
        print('End reset: ')

        rospy.spin()

    except rospy.ROSInterruptException:
        rospy.loginfo("Node terminated.")
