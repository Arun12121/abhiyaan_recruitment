#!/usr/bin/env python
import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist

import math
import time


class drive():

    def __init__(self):

        rospy.init_node("drive")

        self.turtle1 = Pose()
        self.abh = Pose()

        self.pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
        rospy.Subscriber("/turtle1/pose", Pose, self.turtleCallback)
        rospy.Subscriber("/abhiyaan/pose", Pose, self.abhiyaanCallback)

    def spin(self):
        time.sleep(0.5)
        self.main()

    def main(self):

        move = Twist()

        ydiff = self.abh.y-self.turtle1.y
        xdiff = self.abh.x-self.turtle1.x

        move.angular.z = math.atan(ydiff/xdiff) - self.turtle1.theta
        if((self.abh.x-self.turtle1.x) < 0):
            move.angular.z = move.angular.z - math.pi
        self.pub.publish(move)

        time.sleep(1)

        move.angular.z = 0.0
        move.linear.x = math.hypot(ydiff, xdiff) - 2
        self.pub.publish(move)

    def turtleCallback(self, msg):
        self.turtle1 = msg

    def abhiyaanCallback(self, msg):
        self.abh = msg


if __name__ == '__main__':
    run = drive()
    run.spin()
