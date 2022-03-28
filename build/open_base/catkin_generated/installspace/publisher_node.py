#!/usr/bin/env python3
import rospy
import roslib
import sys
#from geometry_msgs.msg import Twist
#from std_msgs.msg import String
#from open_base.msg import Movement

    # def move_platform(line_vel,ang_vel):
    #     rospy.init_node('platform_move', anonymous=True)
    #    # pub = rospy.Publisher('/open_base/command',String, queue_size=10)
    #     pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    #     rate = rospy.Rate(10)
    #     vel = String()
    #     while True:
    #         vel.linear.x= line_vel
    #         vel.linear.y = 0
    #         vel.linear.z = 0
    #
    #         vel.angular.x=0
    #         vel.angular.y=0
    #         vel.angular.z=ang_vel
    #
    #         pub.publish(vel)
    #         rate.sleep()
    # move_platform(1.0,2.0)


from open_base.msg import Movement
from sensor_msgs.msg import Range
from gazebo_msgs.msg import LinkStates

def callback(msg):
    rospy.loginfo("Message = ", msg.range)
def sharp_1():
    rospy.init_node('sharp_1', anonymous=True)
    rospy.Subscriber('/open_base/one_sonar', Range, callback)
    rospy.spin()

sharp_1()

def move_platform(x,y,z):
    rospy.init_node('platform_move', anonymous=True)
    pub = rospy.Publisher('/open_base/command', Movement, queue_size=10)
    rate = rospy.Rate(10)
    vel = Movement()
    while True:
        vel.wheel.v_left = x
        vel.wheel.v_back = y
        vel.wheel.v_right = z
        rospy.loginfo('x: {} y:{} z:{}'.format(x,y,z))
        vel.movement = Movement.WHEEL
        pub.publish(vel)
        rate.sleep()
move_platform(0.0,-0.5,0.5)





#def callback(data):
    # rospy.loginfo(rospy.get_caller_id,data.data)



#  rospy.loginfo('дальность'.format(data))
#


# #def callback(data):
#     # rospy.loginfo(rospy.get_caller_id,data.data)
#
# def callback(msg):
#     rospy.loginfo("Message = ", msg.link_name)
# #def sharp_1():
#     rospy.init_node('Origin_link', anonymous=True)
#     rospy.Subscriber("/gazebo/link_states", LinkStates,callback)
#     rospy.spin()
#
# #  rospy.loginfo('дальность'.format(data))
# #