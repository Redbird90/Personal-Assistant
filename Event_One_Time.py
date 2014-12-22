#-------------------------------------------------------------------------------
# Name:        Event_One_Time
# Purpose:
#
# Author:      jkougl
#
# Created:     05/09/2014
# Copyright:   (c) jkougl 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------



class Event_One_Time():

    def __init__(self, name, date_of_event, date_created, reminder_days,\
    location = None, note = None):
        self.name = name
        self.date_of_event = date_of_event
        self.date_created = date_created
        self.reminder_days = reminder_days
        self.location = location
        self.note = note