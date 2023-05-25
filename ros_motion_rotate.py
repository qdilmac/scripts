#!/usr/bin/env python3

import math
import time
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

def rotate(vel_publisher, angular_speed_degree, relative_angle_degree, clockwise):

    vel_message = Twist()
    angular_speed = math.radians(abs(angular_speed_degree))

    if clockwise:
        vel_message.angular.z = -abs(angular_speed) # saat yönü = açısal hız negatif
    else:
        vel_message.angular.z = abs(angular_speed)

    rate = rospy.Rate(10)
    t0 = rospy.Time.now().to_sec()

    while not rospy.is_shutdown():
        rospy.loginfo("Rotating...")
        vel_publisher.publish(vel_message)

        t1 = rospy.Time.now().to_sec()
        current_angle_degree = (t1-t0) * angular_speed_degree
        rate.sleep()

        if current_angle_degree>relative_angle_degree:
            rospy.loginfo("reached the destination")
            break
        vel_message.angular.z = 0
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

        # açısal hız derecesi bir cismi dönme hızıyla ilgiliyken, 
        # göreceli açı derecesi ise bir cismin veya noktanın başlangıç noktasına göre konumunu ifade eder.
        angular_speed = float(input("Robot's angular speed: "))
        relative_angle = float(input("Relative angle: "))
        is_forward = int(input("Forward or not? (1/0): "))

        # calling the rotate function with the given inputs
        rotate(vel_publisher, angular_speed, relative_angle, is_forward)

        # printing final location of turtlesim
        rospy.loginfo("Current position >>  \nx: {} \ny: {} \ntheta: {}".format(x,y,yaw))

    except rospy.ROSInterruptException:
        print("exception occured")