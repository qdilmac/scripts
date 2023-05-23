#!/usr/bin/env python3

import rospy
from udemy_pkg.srv import AddTwoInts
from udemy_pkg.srv import AddTwoIntsRequest
from udemy_pkg.srv import AddTwoIntsResponse
import time

def handle_add(req):
    print("Returning {} + {} = {}".format(req.a,req.b,(req.a+req.b)))
    time.sleep(3)
    sum_response = AddTwoIntsResponse(req.a + req.b)
    return sum_response

def add_two_ints_server():
    rospy.init_node("add_two_ints_server")
    s = rospy.Service("add_two_ints", AddTwoInts, handle_add)
    print("Ready to sum")
    rospy.spin()

if __name__ == "__main__":
    add_two_ints_server()