#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Juli
#
# Created:     12/09/2014
# Copyright:   (c) Juli 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------



class Hold_Creating_Task_Or_Date():
    def __init__(self, creating_task=False, creating_event=False):
        self.creating_task = creating_task
        self.creating_event = creating_event

    def set_creating_task(self, c_t):
        self.creating_task = c_t

    def set_creating_event(self, c_e):
        self.creating_event = c_e

    def get_creating_task(self):
        return self.creating_task

    def get_creating_event(self):
        return self.creating_event

