#!/usr/bin/env python3

import rospy
from udemy_pkg.msg import IoTMessage
import random

pub = rospy.Publisher('iot_sensor_topic', IoTMessage, queue_size=10)
rospy.init_node('iot_sensor_publisher_node', anonymous=True)
rate = rospy.Rate(1) # 1hz

i=0
while not rospy.is_shutdown():
    iot_sensor = IoTMessage()
    iot_sensor.id = i
    iot_sensor.name = "iot_parking_" + str(i)
    iot_sensor.temperature = 24.33 + (random.random()*2)
    iot_sensor.humidity = 33.41 + (random.random()*2)
    rospy.loginfo("I publish:")
    rospy.loginfo(iot_sensor)
    pub.publish(iot_sensor)
    rate.sleep()
    i += 1
