#!/usr/bin/env python3
from logging.config import listen
import rospy
import numpy as np
import time
from std_msgs.msg import Int32, Float32
from Quick_script import quickSort
from selection_script import selection_sort
from Merge_script import merge_sort
from insertion_script import insertion_sort





def callback(size):
    n =  size.data
    arr = np.random.randint(1,10000000,n)
    


    start_time = time.time()
    print(arr.tolist())
    merge_sort(arr.tolist())
    end_time = time.time()
    ex_time = end_time - start_time
    merg_pub.publish(ex_time)

    start_time = time.time()
    print(arr.tolist())
    quickSort(arr.tolist(),0,n-1)
    end_time = time.time()
    ex_time = end_time - start_time
    quick_pub.publish(ex_time)

    start_time = time.time()
    print(arr.tolist())
    selection_sort(arr.tolist())
    end_time = time.time()
    ex_time = end_time - start_time
    selection_pub.publish(ex_time)

    start_time = time.time()
    print(arr.tolist())
    insertion_sort(arr.tolist())
    end_time = time.time()
    ex_time = end_time - start_time
    insertion_pub.publish(ex_time)
    

def listener():
    rospy.spin()
    
    
    

if __name__ == '__main__':
    rospy.init_node('sorting_node', anonymous=True)
    rospy.Subscriber('size', Int32, callback)
    merg_pub = rospy.Publisher('Merge_sort_time', Float32, queue_size=10)
    quick_pub = rospy.Publisher('Quick_sort_time', Float32, queue_size=10)
    selection_pub = rospy.Publisher('Selection_sort_time', Float32, queue_size=10)
    insertion_pub = rospy.Publisher('Insertion_sort_time', Float32, queue_size=10)

    try:
        listener()
    except rospy.ROSInterruptException:
        pass
