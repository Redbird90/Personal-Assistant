#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      jkougl
#
# Created:     17/09/2014
# Copyright:   (c) jkougl 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------




# For num_on_scale, type=int, values=1-45
# For days_weeks_months...., type=int, values=0-4 (1-4=days,weeks,months,years)
def process_simple_attributes(num_on_scale, days_weeks_months_or_years, \
at_creation=False):
    pass

# For first_thru_last, type=int, values=0-5 (1-5=first,second,third,fourth,
# last).
# For monday_thru_day, type=int, values=0-8 (1-8=monday,tuesday,wednesday,
# thrusday,friday,saturday,sunday,day)
# For scale_num, type=int, values=1-24
def process_month_attributes(first_thru_last, monday_thru_day, scale_num, \
at_creation=False):
    pass

# For day_checkbutton_value, type=tsil, possible_values='monday','tuesday',
# 'wednesday','thursday','friday','saturday','sunday', all of type string
# For day_scale_num, type=int, values=1-52
def process_day_attributes(day_checkbutton_value, day_scale_num, \
at_creation=False):
    pass




