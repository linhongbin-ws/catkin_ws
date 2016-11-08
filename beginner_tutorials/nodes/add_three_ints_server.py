#!/usr/bin/env python

from beginner_tutorials.srv import *
import rospy

def handle_add_three_ints(req):
    rospy.loginfo("Returning [%s + %s + %s= %s]",req.a, req.b, req.c, req.a+req.b+req.c)
    rospy.sleep(1)
    return AddThreeIntsResponse(req.a+req.b+req.c)

def add_three_ints_server():
    rospy.init_node('add_three_ints_server')
    s = rospy.Service('add_three_ints', AddThreeInts, handle_add_three_ints)
    rospy.loginfo("Read to add three ints")
    rospy.spin()

if __name__ == "__main__":
    add_three_ints_server()
