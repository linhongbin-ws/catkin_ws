#!/usr/bin/env python

from beginner_tutorials.srv import *
import rospy

def handle_add_four_ints(req):
    rospy.loginfo("Returning [%s + %s +%s + %s= %s]",
                  req.a, req.b, req.c, req.d, req.a+req.b+req.c+req.d)
    rospy.sleep(1)
    return AddFourIntsResponse(req.a+req.b+req.c+req.d)

def add_four_ints_server():
    rospy.init_node('add_four_ints_server')
    s = rospy.Service('add_four_ints', AddFourInts, handle_add_four_ints)
    rospy.loginfo("Read to add Four ints")
    rospy.spin()

if __name__ == "__main__":
    add_four_ints_server()
