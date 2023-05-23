#!/usr/bin/env python3

import rospy
from turtlesim.msg import Pose #task 1. import the message type Pose

def poseCallback(pose_message):

   #task 4. display the x, y, and theta received from the message
    print("Pose callback")
    print('x = {}'.format(pose_message.x))
    print('y = {}'.format(pose_message.y))
    print('yaw = {}'.format(pose_message.theta))

if __name__ == '__main__':
    try:
        
        rospy.init_node('turtlesim_motion_pose', anonymous=True)        

        rospy.Subscriber("/turtle1/pose", Pose, poseCallback) #task 2. subscribe to the topic /turtle1/pose

        rospy.spin() #task 3. spin the node
       
    except rospy.ROSInterruptException:
        rospy.loginfo("node terminated.")