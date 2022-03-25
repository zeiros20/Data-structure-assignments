#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32


def publish_size():
    while not rospy.is_shutdown():
        for i in range(10,10000000,100):
            size = i
            size_publisher.publish(size)
            rate.sleep()



if __name__ == '__main__':
    size_publisher = rospy.Publisher('size', Int32, queue_size=10)
    rospy.init_node('size_publisher',anonymous = True)
    rate = rospy.Rate(1)
    try:
        publish_size()
    except rospy.ROSInterruptException:
        pass