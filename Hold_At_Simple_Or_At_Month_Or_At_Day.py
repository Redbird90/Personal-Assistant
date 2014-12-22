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



class Hold_At_Simple_Or_At_Month_Or_At_Day():
    def __init__(self, at_simple=False, at_month=False, at_day=False):
        self.at_simple = at_simple
        self.at_month = at_month
        self.at_day = at_day

    def set_at_simple(self, a_s):
        self.at_simple = a_s

    def set_at_month(self, a_m):
        self.at_month = a_m

    def set_at_day(self, a_d):
        self.at_day = a_d

    def get_at_simple(self):
        return self.at_simple

    def get_at_month(self):
        return self.at_month

    def get_at_day(self):
        return self.at_day