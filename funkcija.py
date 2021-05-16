#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
from testing.msg import poruka_funkciji
from testing.msg import poruka_varijabli

class funkcija(object):
    def __init__(self):
        varijable = ['varijabla1', 'varijabla2', 'varijabla3']
        self.pubs = {
            'varijabla1': rospy.Publisher("varijabla1/poruka_varijabli", poruka_varijabli, queue_size = 10),
            'varijabla2': rospy.Publisher("varijabla2/poruka_varijabli", poruka_varijabli, queue_size = 10),
            'varijabla3': rospy.Publisher("varijabla3/poruka_varijabli", poruka_varijabli, queue_size = 10)
            }
        self.sub = rospy.Subscriber("/poruka_funkciji", poruka_funkciji, self.callback, queue_size=10)
        self.Qs = {'varijabla1': 0, 'varijabla2': 0, 'varijabla3': 0}
        self.recived = ['varijabla1', 'varijabla2', 'varijabla3']
        while not rospy.is_shutdown():
            print(self.recived, varijable)
            if set(self.recived) >= set(varijable):
                self.recived.clear()
                for i in self.pubs:
                    poruka = poruka_varijabli()
                    poruka.primatelj = i
                    poruka.value = self.Qs[i] + varijable.index(i) + 1
                    self.pubs[i].publish(poruka)
            rospy.sleep(5)
                    
    def callback(self, data):
        print("Q recived")
        self.Qs[data.posiljatelj] = data.value
        if data.posiljatelj not in self.recived:
            self.recived.append(data.posiljatelj)


if __name__ == "__main__":
    rospy.init_node("funkcija")
    try:
        node = funkcija()
    except rospy.ROSInterruptException:
        pass