#!/usr/bin/env python3

import math
import time
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

def move(vel_publisher, speed, distance, is_forward):
 
    # Twist message to send vel commands
    vel_message = Twist()
 
    # declaring variables and getting the current position. Later will be used for distance calculation -> sqrt((x1-x0)^2+(y1-y0)^2)
    global  x, y
    x0 = x
    y0 = y

    # +x -> forward motion, -x -> backward motion
    if (is_forward):
        vel_message.linear.x = abs(speed)
    else:
        vel_message.linear.x = -abs(speed) 

    distance_moved = 0.0
    loop_rate = rospy.Rate(10) # we publish the vel at 10hz = 10 times a sec

    while True:
        rospy.loginfo("Robot moving to given direction.")
        vel_publisher.publish(vel_message)
        loop_rate.sleep()
        distance_moved = abs(math.sqrt(( (x-x0) ** 2 + (y-y0) ** 2 )))
        print(distance_moved)
        if not (distance_moved<distance):
            rospy.loginfo("Target reached.")
            break
    # stop the robot after we reached the destination
    vel_message.linear.x = 0
    vel_publisher.publish(vel_message)

def poseCallback(pose_message):
    global x
    global y,yaw
    x = pose_message.x
    y = pose_message.y
    yaw = pose_message.theta
    
if __name__ == "__main__":
    try:
        rospy.init_node("turtlesim_motion_pose", anonymous=True)

        cmd_vel_topic = "/turtle1/cmd_vel"
        position_topic = "/turtle1/pose"

        vel_publisher = rospy.Publisher(cmd_vel_topic, Twist, queue_size= 10)
        pose_subscriber = rospy.Subscriber(position_topic, Pose, poseCallback)
        time.sleep(1)

        speed = float(input("Robot's speed: "))
        distance = float(input("Distance: "))
        is_forward = int(input("Forward or not? (1/0): "))

        # calling the move function with the given inputs
        move(vel_publisher, speed, distance, is_forward)

        # printing final location of turtlesim
        rospy.loginfo("Current position >>  \nx: {} \ny: {} \ntheta: {}".format(x,y,yaw))
        
    except rospy.ROSInterruptException:
        print("exception occured")