#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('/welcome_message', String, queue_size=10)
    rospy.init_node('pub', anonymous=True)
    str1 = "Welcome to Abhiyaan"
    pub.publish(str1)

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
