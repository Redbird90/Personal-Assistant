#-------------------------------------------------------------------------------
# Name:        Event_Recurring
# Purpose:
#
# Author:      jkougl
#
# Created:     05/09/2014
# Copyright:   (c) jkougl 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------



class Event_Recurring():

    def __init__(self, name, dates_of_events, date_created, reminder_days,\
    recurrence_data, days_before_to_remind=0, location = None, note = None):
        self.name = name
        self.dates_of_events = dates_of_events
        self.date_created = date_created
        self.reminder_days = reminder_days
        self.days_before_to_remind = days_before_to_remind
        self.recurrence_data = recurrence_data
        self.location = location
        self.note = note