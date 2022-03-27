#!/usr/bin/env python 

import sys  

import copy  

import rospy  

from moveit_msgs.srv import GetPositionFK, GetPositionFKRequest  

from std_msgs.msg import Header  

 

### Initialize ros node 

rospy.init_node('get_fk', anonymous=True)  

 
 

### Create ros service  

 

try:  

    moveit_fk=rospy.ServiceProxy('/my_gen3/compute_fk',GetPositionFK)  

except rospy.ServiceException as e:  

    rospy.logerror("Service call failed : %s" %e)  

 

### Create and define the request msg 

 
 

rqst= GetPositionFKRequest()  

rqst.header.frame_id="base_link"  

rqst.fk_link_names=["end_effector_link"]  

rqst.robot_state.joint_state.name=["joint_1", "joint_2", "joint_3", "joint_4", "joint_5", "joint_6"]  

rqst.robot_state.joint_state.position=[]  

 
 
 

### Joint State fake data 

 
 

i=1  

while (i<7):  

    #rqst.robot_state.joint_state.name.append('id_'+str(i))  

    rqst.robot_state.joint_state.position.append(0.8)  

    i+=1  

rospy.loginfo(rqst.robot_state.joint_state.name) 

rospy.loginfo(rqst.robot_state.joint_state.position) 
 

### Display the computed FK of the fake joint state 

 

res=moveit_fk(rqst)  

rospy.loginfo(["computed FK: ", res]) 
