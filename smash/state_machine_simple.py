#!/usr/bin/env python
   2 
   3 import roslib; roslib.load_manifest('smach_tutorials')
   4 import rospy
   5 import smach
   6 import smach_ros
   7 
   8 # define state Foo
   9 class Foo(smach.State):
  10     def __init__(self):
  11         smach.State.__init__(self, outcomes=['outcome1','outcome2'])
  12         self.counter = 0
  13 
  14     def execute(self, userdata):
  15         rospy.loginfo('Executing state FOO')
  16         if self.counter < 3:
  17             self.counter += 1
  18             return 'outcome1'
  19         else:
  20             return 'outcome2'
  21 
  22 
  23 # define state Bar
  24 class Bar(smach.State):
  25     def __init__(self):
  26         smach.State.__init__(self, outcomes=['outcome2'])
  27 
  28     def execute(self, userdata):
  29         rospy.loginfo('Executing state BAR')
  30         return 'outcome2'
  31         
  32 
  33 
  34 
  35 # main
  36 def main():
  37     rospy.init_node('smach_example_state_machine')
  38 
  39     # Create a SMACH state machine
  40     sm = smach.StateMachine(outcomes=['outcome4', 'outcome5'])
  41 
  42     # Open the container
  43     with sm:
  44         # Add states to the container
  45         smach.StateMachine.add('FOO', Foo(), 
  46                                transitions={'outcome1':'BAR', 
  47                                             'outcome2':'outcome4'})
  48         smach.StateMachine.add('BAR', Bar(), 
  49                                transitions={'outcome2':'FOO'})
  50 
  51     # Execute SMACH plan
  52     outcome = sm.execute()
  53 
  54 
  55 if __name__ == '__main__':
  56     main()
