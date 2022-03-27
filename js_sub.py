#!/usr/bin/env python 

 
import rospy 

from sensor_msgs.msg import JointState 

 
 

class JointStateSub(object): 

    def __init__(self): 

        rospy.loginfo("Initalizing node...") 

        self.js_sub = rospy.Subscriber('/my_gen3/joint_states', JointState,self.js_cb, queue_size=1) 

 
 

    def js_cb(self, data): 

        self.last_js = data 

        rospy.loginfo(data) 

 
 

if __name__ == '__main__': 

    rospy.init_node('joint_state_node_subscriber') 

    rospy.loginfo("Start joint state subscriber node") 

    JointStateSub().js_cb 

    try: 

        rospy.spin() 

    except KeyboardInterrupt: 

       print("Shutting down") 
