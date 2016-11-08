#!usr/bin/local python

import sys
import rospy
from beginner_tutorials.srv import *

def add_two_ints_client(x,y):
    rospy.wait_for_service('add_two_ints')
    try:
        add_two_ints = rospy.ServiceProxy('add_two_ints', AddTwoInts)
        resp1 = add_two_ints(x,y)
        return resp1.sum
    except rospy.ServiceException, e:
        rospy.loginfo( "Service call fail:%s",e)

def usage():
    return "%s [x y]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    else:
        print usage()
        sys.exit(1)
    rospy.loginfo("Requesting %s+%s",x,y)
    rospy.loginfo("%s + %s = %s",x,y,add_two_ints_client(x,y))
