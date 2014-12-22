#-------------------------------------------------------------------------------
# Name:        Event_Recurring_To_Completion
# Purpose:
#
# Author:      jkougl
#
# Created:     05/09/2014
# Copyright:   (c) jkougl 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------



class Event_Recurring_To_Completion():

    def __init__(self, name, date_due, date_created, reminder_days,\
    recurrence_data, days_before_to_remind=0, \
    location = None, note = None):
        self.name = name
        self.dates_of_events = dates_of_events
        self.date_created = date_created
        self.reminder_days = reminder_days
        self.recurrence_data = recurrence_data
        self.days_before_to_remind = days_before_to_remind
        self.location = location
        self.note = note