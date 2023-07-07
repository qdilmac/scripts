#!/usr/bin/env python3
import math
import time
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

# python code for turtlesim to go to goal

def go_to_goal(vel_publisher, x_goal, y_goal):
    global x, y, yaw
    
    
    vel_message = Twist()

    while True:
        K_linear = 0.6
        distance = abs(math.sqrt(((x_goal - x) ** 2) + ((y_goal - y) ** 2)))
    
        linear_speed = distance * K_linear

        desired_angle_goal = math.atan2(y_goal - y, x_goal - x)
        angular_speed = 2 * math.atan2(math.sin(desired_angle_goal-yaw), math.cos(desired_angle_goal-yaw))

        vel_message.linear.x = linear_speed
        vel_message.angular.z = angular_speed

        vel_publisher.publish(vel_message)
        print("x: {} y: {} distance to goal: {}".format(x, y, distance))

        if distance < 0.01:
            vel_message.linear.x = 0
            vel_message.angular.z = 0
            vel_publisher.publish(vel_message)
            break

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

        vel_publisher = rospy.Publisher(cmd_vel_topic, Twist, queue_size= 10)
        pose_subscriber = rospy.Subscriber(position_topic, Pose, poseCallback)
        time.sleep(2)
        goal_x = float(input("x value: "))
        goal_y = float(input("y value: "))
        go_to_goal(vel_publisher, goal_x, goal_y)
        
    except rospy.ROSInterruptException:
        print("exception occured")