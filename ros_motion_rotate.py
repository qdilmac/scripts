#!/usr/bin/env python3

import math
import time
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

# Global variables
x = 0
y = 0
yaw = 0

def rotate(vel_publisher, angular_speed_degree, relative_angle_degree, clockwise):
    vel_message = Twist()
    angular_speed = math.radians(abs(angular_speed_degree))

    if clockwise:
        vel_message.angular.z = -abs(angular_speed)  # Saat yönü: açısal hız negatif
    else:
        vel_message.angular.z = abs(angular_speed)

    rate = rospy.Rate(10)
    t0 = rospy.Time.now().to_sec()
    current_angle_degree = 0

    while not rospy.is_shutdown():
        rospy.loginfo("Rotating...")
        vel_publisher.publish(vel_message)

        t1 = rospy.Time.now().to_sec()
        current_angle_degree = math.degrees(yaw)
        if clockwise:
            current_angle_degree = 360 - current_angle_degree

        if current_angle_degree >= relative_angle_degree:
            break

        rate.sleep()

    vel_message.angular.z = 0
    vel_publisher.publish(vel_message)
    rospy.loginfo("Reached the destination")

def poseCallback(pose_message):
    global x, y, yaw
    x = pose_message.x
    y = pose_message.y
    yaw = pose_message.theta

def setDO(publisher, speed_in_degree, desired_angle_degree):
    relative_angle_degrees = desired_angle_degree - math.degrees(yaw)
    clockwise = relative_angle_degrees < 0

    print("Relative angle degrees: {} \nDesired angle degrees: {}".format(relative_angle_degrees, desired_angle_degree))
    rotate(publisher, speed_in_degree, abs(relative_angle_degrees), clockwise)

if __name__ == "__main__":
    try:
        rospy.init_node("turtlesim_motion_pose", anonymous=True)

        cmd_vel_topic = "/turtle1/cmd_vel"
        position_topic = "/turtle1/pose"

        vel_publisher = rospy.Publisher(cmd_vel_topic, Twist, queue_size=10)
        pose_subscriber = rospy.Subscriber(position_topic, Pose, poseCallback)
        time.sleep(2)

        # angular_speed = float(input("Robot's angular speed: "))
        # relative_angle = float(input("Relative angle: "))
        # is_forward = int(input("Forward or not? (1/0): "))

        # rotate(vel_publisher, angular_speed, relative_angle, is_forward)
        
        setDO(vel_publisher, 60, 30)  # Call setDO() function with desired parameters

        rospy.loginfo("Current position >>  \nx: {} \ny: {} \ntheta: {}".format(x, y, yaw))

    except rospy.ROSInterruptException:
        print("Exception occurred")
