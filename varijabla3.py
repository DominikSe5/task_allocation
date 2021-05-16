#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
from testing.msg import poruka_funkciji
from testing.msg import poruka_varijabli

class varijabla3(object):
    def __init__(self):
        self.sub = rospy.Subscriber("/varijabla3/poruka_varijabli", poruka_varijabli, self.callback, queue_size = 1)
        self.pub = rospy.Publisher("/poruka_funkciji", poruka_funkciji, queue_size=1)
        rospy.spin()

    def callback(self, data):
        print("R recived")
        poruka = poruka_funkciji()
        poruka.value = data.value - 10
        poruka.posiljatelj = 'varijabla3'
        self.pub.publish(poruka)

if __name__ == "__main__":
    rospy.init_node("varijabla3")
    try:
        node = varijabla3()
    except rospy.ROSInterruptException:
        pass