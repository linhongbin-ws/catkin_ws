#!/usr/bin/env python

import rospy
import rostest

import unittest

#import std_srvs.srv as std_srvs

from smach import *
from smach_ros import *

from smach_msgs.msg import *

from beginner_tutorials.srv import *


def empty_server(req):
    rospy.loginfo("Service called!")
    return std_srvs.EmptyResponse()

### Test harness
class TestServices(unittest.TestCase):
    def test_service_cb(self):
        """Test calling a service with a callback."""

        
        #srv = rospy.Service('/empty', std_srvs.Empty, empty_server)

        sm = StateMachine(outcomes=['succeeded','aborted','preempted','done'])
        with sm:
            def response_two_cb(userdata, response):
                userdata.foo_var_out = 'foo!'
                return 'succeeded'

            def request_two_cb(userdata,request):
                add_two_ints_request = AddTwoIntsRequest(10,30)
                return add_two_ints_request

            def response_three_cb(userdata, response):
                userdata.foo_var_out = 'foo!'
                return 'succeeded'

            def request_three_cb(userdata,request):
                add_three_ints_request = AddThreeIntsRequest(10,30,40)
                return add_three_ints_request

            def response_four_cb(userdata, response):
                userdata.foo_var_out = 'foo!'
                return 'succeeded'

            def request_four_cb(userdata,request):
                add_four_ints_request = AddFourIntsRequest(10,30,30,40)
                return add_four_ints_request

            StateMachine.add('State_two_ints',
                    ServiceState('add_two_ints',
                        AddTwoInts,
                        request_cb=request_two_cb,
                        response_cb=response_two_cb,
                        output_keys=['foo_var_out']),
                    remapping={'foo_var_out':'sm_var'},
                    transitions={'succeeded':'State_three_ints'})

            
            StateMachine.add('State_three_ints',
                    ServiceState('add_three_ints',
                        AddThreeInts,
                        request_cb=request_three_cb,
                        response_cb=response_three_cb,
                        output_keys=['foo_var_out']),
                    remapping={'foo_var_out':'sm_var'},
                    transitions={'succeeded':'State_four_ints'})
            

            StateMachine.add('State_four_ints',
                    ServiceState('add_four_ints',
                        AddFourInts,
                        request_cb=request_four_cb,
                        response_cb=response_four_cb,
                        output_keys=['foo_var_out']),
                    remapping={'foo_var_out':'sm_var'},
                    transitions={'succeeded':'done'})             

        #rospy.wait_for_service('add_two_ints')
        #add_two_ints = rospy.ServiceProxy('add_two_ints', AddTwoInts)
        sis = IntrospectionServer('My_server',sm, '/SM_ROOT')
        sis.start()
        outcome = sm.execute()
        
        rospy.loginfo("OUTCOME: "+outcome)

        assert outcome == 'done'

        rospy.spin()
        sis.stop()


def main():
    rospy.init_node('services_test',log_level=rospy.DEBUG)
    rostest.rosrun('smach', 'services_test', TestServices)

if __name__=="__main__":
    main();
