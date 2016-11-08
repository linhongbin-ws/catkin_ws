#!/usr/bin/env python

from beginner_tutorials.srv import *
import rospy

def handle_add_two_ints(req):
    rospy.loginfo("Returning [%s + %s = %s]",req.a, req.b, req.a+req.b)
    rospy.sleep(1)
    return AddTwoIntsResponse(req.a+req.b)

def add_two_ints_server():
    rospy.init_node('add_two_ints_server')
    s = rospy.Service('add_two_ints', AddTwoInts, handle_add_two_ints)
    rospy.loginfo("Read to add two ints")
    rospy.spin()

if __name__ == "__main__":
    add_two_ints_server()
