#-------------------------------------------------------------------------------
# Name:        Task_One_Time
# Purpose:
#
# Author:      jkougl
#
# Created:     05/09/2014
# Copyright:   (c) jkougl 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------



class Task_One_Time():

    def __init__(self, name, date_due, date_created, reminder_days,\
    days_before_to_remind=0, location = None, note = None):
        self.name = name
        self.date_due = date_due
        self.date_created = date_created
        self.reminder_days = reminder_days
        self.days_before_to_remind = days_before_to_remind
        self.location = location
        self.note = note