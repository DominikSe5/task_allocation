#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
from task_allocation.msg import poruka

class agent1(object):
    def __init__(self):
        self.M = ['funkcija1', 'funkcija2']
        self.gamma = [0.1, -0.1]
        self.ready_check = []
        self.pub = rospy.Publisher("/varijabla_funkciji", poruka, queue_size = 1)
        self.sub = rospy.Subscriber("/varijabla1/funkcija_varijabli", poruka, self.callback, queue_size = 10)
        self.Rs = {'funkcija1': 0, 'funkcija2': 0}
        rospy.spin()

    def callback(self, data):
        self.ready_check.append(data.posiljatelj)
        self.Rs[data.posiljatelj] = data.data
        check = set(self.M) <= set(self.ready_check)
        if check == True:
            for funkcija_kojim_saljemo in self.M:
                poruka_funkciji = poruka()
                poruka_funkciji.posiljatelj = 'varijabla1'
                poruka_funkciji.primatelj = funkcija_kojim_saljemo
                poruka_funkciji.data = self.Poruka_v_f(funkcija_kojim_saljemo)
                self.pub.publish(poruka_funkciji)
            self.ready_check.clear()

    def Poruka_v_f(self, f):
        if f in self.M:
            out = [0, 0]
            for primatelj, vrijednost in self.Rs.items():
                if primatelj != f:
                    out[0] += vrijednost[0]
                    out[1] += vrijednost[1]
        return out

if __name__ == "__main__":
    rospy.init_node("agent1")
    try:
        node = agent1()
    except rospy.ROSInterruptException:
        pass