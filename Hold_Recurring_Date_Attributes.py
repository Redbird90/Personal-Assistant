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



class Hold_Recurring_Date_Attributes():
    def __init__(self, simple_scale_num=1, simple_radio_value='', \
    month_first_thru_last_value='', month_monday_thru_day_value='', \
    month_scale_num='', day_checkbutton_value_tsil=[], day_scale_num=1, \
    holding_completion_date=False, completion_date = '', \
    holding_recurring_date=False, holding_simple=False, \
    holding_month=False, holding_day=False):
        self.simple_scale_num = simple_scale_num
        self.simple_radio_value = simple_radio_value
        self.month_first_thru_last_value = month_first_thru_last_value
        self.month_monday_thru_day_value = month_monday_thru_day_value
        self.month_scale_num = month_scale_num
        self.day_checkbutton_value_tsil = day_checkbutton_value_tsil
        self.day_scale_num = day_scale_num
        self.holding_completion_date = holding_completion_date
        self.completion_date = completion_date
        self.holding_recurring_date = holding_recurring_date
        self.holding_simple = holding_simple
        self.holding_month = holding_month
        self.holding_day = holding_day

    def reinitialize(self):
        self.simple_scale_num = 1
        self.simple_radio_value = ''
        self.month_first_thru_last_value = ''
        self.month_monday_thru_day_value = ''
        self.month_scale_num = 1
        self.day_checkbutton_value = []
        self.day_scale_num = 1
        self.holding_simple = False
        self.holding_month = False
        self.holding_day = False
        self.holding_completion_date = False