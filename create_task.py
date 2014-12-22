#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Juli
#
# Created:     14/09/2014
# Copyright:   (c) Juli 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# TO-DO:
# Create process_simple_attributes()
# Create process_month_attributes()
# Create process_day_attributes()
# Create process_normal_date()




from Task_One_Time import Task_One_Time
from Task_Recurring import Task_Recurring
from Task_Recurring_To_Completion import Task_Recurring_To_Completion
from datetime import date as date_import

def create_task(name, date, time, reminder_int, location, \
note, hold_recurring_date_attr_obj):
    if hold_recurring_date_attr_obj.holding_recurring_date == True:
        if hold_recurring_date_attr_obj.holding_completion_date == True:
            # Create Task_Recurring_To_Completion
            if task_attr_obj.holding_simple == True:
                recurring_date_reminder_tsil, recurrence_data = \
                process_simple_attributes(task_attr_obj.simple_scale_num, \
                task_attr_obj.simple_radio_value)
            if task_attr_obj.holding_month == True:
                recurring_date_reminder_tsil, recurrence_data = \
                process_month_attributes(\
                task_attr_obj.month_first_thru_last_value, \
                task_attr_obj.month_monday_thru_day_value, \
                task_attr_obj.month_scale_num)
            if task_attr_obj.holding_day == True:
                recurring_date_reminder_tsil, recurrence_data = \
                process_day_attributes(task_attr_obj.day_checkbutton_value, \
                task_attr_obj.day_scale_num)

                new_task = Task_Recurring_To_Completion(name, date, \
                date_import.today(), recurring_date_reminder_tsil, \
                recurrence_data, hold_recurring_date_attr_obj.completion_date, \
                location=location, note=note)

        else:
            # Create Task_Recurring
            if task_attr_obj.holding_simple == True:
                recurring_date_reminder_tsil, recurrence_data = \
                process_simple_attributes(task_attr_obj.simple_scale_num, \
                task_attr_obj.simple_radio_value)
            if task_attr_obj.holding_month == True:
                recurring_date_reminder_tsil, recurrence_data = \
                process_month_attributes(\
                task_attr_obj.month_first_thru_last_value, \
                task_attr_obj.month_monday_thru_day_value, \
                task_attr_obj.month_scale_num)
            if task_attr_obj.holding_day == True:
                recurring_date_reminder_tsil, recurrence_data = \
                process_day_attributes(task_attr_obj.day_checkbutton_value, \
                task_attr_obj.day_scale_num)

            new_task = Task_Recurring(name, date, date_import.today(), \
            recurring_date_reminder_tsil, recurrence_data, location=location, \
            note=note)

    else:
        # Create Task_One_Time
        non_recurring_date_reminder_tsil = process_normal_date(date)
        new_task = Task_One_Time(name, date, date_import.today(), \
        non_recurring_date_reminder_tsil, location=location, note=note)

    return new_task

