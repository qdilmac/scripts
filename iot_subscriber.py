#!/usr/bin/env python3

import rospy
from udemy_pkg.msg import IoTMessage

def iot_callback(iot_data):
    rospy.loginfo("IoT Id: {}\n IoT Name: {}\n IoT Temperature: {}\n IoT Humidity: {}".format(iot_data.id,iot_data.name,iot_data.temperature,iot_data.humidity))

rospy.init_node("iot_sensor_subscriber_node",anonymous=True)

rospy.Subscriber("iot_sensor_topic", IoTMessage, iot_callback)

rospy.spin()