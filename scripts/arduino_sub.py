#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from std_msgs.msg import Int16

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "Serial In: %d", data.data)


def callServo(data):
    rospy.loginfo(rospy.get_caller_id() + "Servo Out %d", data.data)

def listener():


    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("serialOut", Int16, callback)
    rospy.Subscriber("servoOut", Int16, callServo)

    rospy.spin()

if __name__ == '__main__':
    listener()