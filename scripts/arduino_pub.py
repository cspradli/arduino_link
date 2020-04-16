#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from std_msgs.msg import Int16
import random

def arduino_pub():
    rospy.init_node('arduino_pub', anonymous=True)

    serOut = rospy.Publisher('serialOut', Int16, queue_size=10)
    servoOut = rospy.Publisher('servoOut', Int16, queue_size=10)
    analogPinsOut = rospy.Publisher('analogPinsOut', Int16, queue_size=10)
    digitalPinsOut = rospy.Publisher('digitalPinsOut', Int16, queue_size=10)
    
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():

        num = random.randint(0,2048)

        
        rospy.loginfo(num)
        serOut.publish(num)
        servoOut.publish(num)
        analogPinsOut.publish(num)
        digitalPinsOut.publish(num)
        
        rate.sleep()
    
if __name__ == '__main__':
    try:
        arduino_pub()
    except rospy.ROSInterruptException:
        pass