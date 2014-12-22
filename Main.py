#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Juli
#
# Created:     06/09/2014
# Copyright:   (c) Juli 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------


# Tkinter imports
import Tkinter
import ImageTk, Image, tkFont
from Tkinter import IntVar, StringVar, Toplevel

# My obj imports
from Hold_Creating_Task_Or_Date import Hold_Creating_Task_Or_Date
from Hold_At_Simple_Or_At_Month_Or_At_Day import \
Hold_At_Simple_Or_At_Month_Or_At_Day
from Hold_Recurring_Date_Attributes import Hold_Recurring_Date_Attributes
from Calendar_Window import Calendar_Window
from Reminder_Window import Reminder_Window

# Other imports
from ttkcalendar_updated import *
from create_task import create_task




"""For image load"""
img_path = 'C:\Genome Work\Sec_revised.gif'

# Hold current and prior messages.  Both will be updated as actions are taken
# by the user.
current_msg = 'You can limit the number of characters in each line by setting \
this option to the desired number. The default value, 0, means that lines will \
be broken only at newlines.'
previous_msg = 'You can limit the number of characters in each line by setting \
this option to the desired number. The default value, 0, means that lines will \
be broken only at newlines.'

# Coordinate locations for ALL items blitted to the screen.

# For items on main_screen:
""" None """

# For items on new_task/new_event screen: (likely to be individualized later)
x_label_location = 300
y_name_label_location = 40
y_date_label_location = 80
y_time_label_location = 130
y_location_label_location = 170
y_note_label_location = 210
x_ok_confirmation_location = 460
x_back_confirmation_location = 530
y_confirmation_location = 280
x_advanced_date_location = 510
y_advanced_date_location = 102
x_completion_advanced_date_button_location = 560
y_completion_advanced_date_button_location = 260
x_remindme_button_location = 560
y_remindme_button_location = y_advanced_date_location

# For items always on advanced_date_screen:
x_simple_location = 100
x_month_location = 300
x_day_location = 500
x_back_advanced_date_location = 200
y_back_or_confirm_advanced_date_location = 300
x_confirm_advanced_date_location = 400

# For items on simple_advanced_date_screen:
y_simple_month_day_location = 40
x_simple_scale_location = 240
y_simple_scale_location = 135
x_simple_day_week_month_year_radio_location = 400
y_simple_day_radio_location = 130
y_simple_week_radio_location = 160
y_simple_month_radio_location = 190
y_simple_year_radio_location = 220
x_simple_text_advanced_date_location = 140
y_simple_text_advanced_date_location = 180

# For items on month_advanced_date_screen:
x_first_thru_last_menubutton_location = 120
y_advanced_month_both_menubuttons = 180
x_monday_thru_day_menubutton_location = 270
x_weekday_day_checkbutton_location = 160
y_monday_day_checkbutton_location = 100
x_weekend_day_checkbutton_location = x_weekday_day_checkbutton_location + 110
x_month_advanced_scale_location = 470
y_month_advanced_scale_location = 140
y_saturday_checkbutton_location = 145
x_month_text_1_advanced_date_location = 390
x_month_text_2_advanced_date_location = 540
y_month_text_advanced_date_location = y_simple_text_advanced_date_location

# For items on day_advanced_date_screen:
x_day_scale_location = 470
y_day_scale_location = 140
x_day_text_1_advanced_date_location = 390
x_day_text_2_advanced_date_location = 540
y_day_text_advanced_date_location = y_simple_text_advanced_date_location

# Set up main_window.
main_window = Tkinter.Tk()
main_window.title('P_A')
main_window.geometry('700x350')
main_window.configure(background='GREY')

# Set up ALL variables, IntVar() and StringVar() are Tkinter objects, look
# up related attributes and methods and place here.
day_week_month_year_radio_var = IntVar()
first_thru_last_menu_var = IntVar()
mon_thru_day_menu_var = IntVar()
num_simple_from_scale = IntVar()
num_day_from_scale = IntVar()
monday_checkbutton_value = StringVar()
tuesday_checkbutton_value = StringVar()
wednesday_checkbutton_value = StringVar()
thursday_checkbutton_value = StringVar()
friday_checkbutton_value = StringVar()
saturday_checkbutton_value = StringVar()
sunday_checkbutton_value = StringVar()
checkbutton_value_tsil = [monday_checkbutton_value, tuesday_checkbutton_value,\
wednesday_checkbutton_value, thursday_checkbutton_value, \
friday_checkbutton_value, saturday_checkbutton_value, sunday_checkbutton_value]
poss_checkbutton_value_tsil = ['monday', 'tuesday', 'wednesday', 'thursday', \
'friday', 'saturday', 'sunday']
holding_advanced_date = False
completion_date = ''

# Set up variables to point to my custom objects.
curr_task_or_event_obj = Hold_Creating_Task_Or_Date()
curr_advanced_date_state = Hold_At_Simple_Or_At_Month_Or_At_Day()
curr_recurring_date_info = Hold_Recurring_Date_Attributes()
calendar_for_completion = Calendar_Window()
calendar_for_non_adv_date = Calendar_Window()
reminder_window_handler = Reminder_Window()

# Set up fonts of varying size to be used by Tkinter objects on screen.
smaller_font = tkFont.Font(size=6)
bigger_font = tkFont.Font(size=12)
small_font = tkFont.Font(size=8)
big_font = tkFont.Font(size=10)

# Load image for main_window
actual_image = Image.open(img_path)
img_to_blit = ImageTk.PhotoImage(actual_image)

# start_program() blits messagebox and starting buttons to main_window loaded
# above.
def start_program():
    add_msgbox()
    add_starting_buttons()

# Both move_to_create_new_event and move_to_create_new_task methods get rid of
# items on main screen and call methods to add appropriate items for creation
# screen.  In addition, whether a task or event is being created is handled
# by an attribute in the object curr_task_or_event_obj.

# This method is called by the Create Event button on the main_screen.
def move_to_create_new_event():
    remove_starting_buttons()
    add_new_event_values()
    add_confirmation_buttons()
    curr_task_or_event_obj.set_creating_event(True)

# This method is called by the Create Task button on the main_screen.
def move_to_create_new_task():
    remove_starting_buttons()
    add_new_task_values()
    add_confirmation_buttons()
    curr_task_or_event_obj.set_creating_task(True)

# The ok_to_create_new_event_or_task method determines whether an event or
# task should be made, then calls the appropriate creation method while
# passing the appropriate args from input objects on creation screen. A
# method to publish the appropriate data is also called. Then the
# move_to_main_screen_method is called to handle reverting to main_screen.
# This method is called by the OK button on the event/task creation screen.
def ok_to_create_new_event_or_task():

    if curr_task_or_event_obj.get_creating_task == True:
        obj_to_publish = create_task(name_label_input.get(), \
        date_label_input.get(), time_label_input.get(), \
         location_label_input.get(), note_label_input.get(), \
        curr_recurring_date_info)
    elif curr_task_or_event_obj.get_creating_event == True:
        obj_to_publish = create_event()

    """ create publish method """
    #publish_to_events_and_task_database(obj_to_publish)

    move_to_main_screen()

# The move_to_main_screen method removes appropriate items based on whether in
# the process of creating an event or task. In addition, an attribute is
# changed in the curr_recurring_date_info object.
# This method is called by the Back button on the creation screen or
# ok_to_create_new_event_or_task().
def move_to_main_screen():
    if curr_task_or_event_obj.get_creating_task() == True:
        remove_new_task_values()
        remove_confirmation_buttons()
        add_msgbox()
        add_starting_buttons()
        curr_task_or_event_obj.set_creating_task(False)
    elif curr_task_or_event_obj.get_creating_event() == True:
        remove_new_event_values()
        remove_confirmation_buttons()
        add_msgbox()
        add_starting_buttons()
        curr_task_or_event_obj.set_creating_event(False)

    setattr(curr_recurring_date_info, 'holding_recurring_date', False)



# The move_to_advanced_date_screen method calls all methods necessary to
# remove items on the create event/task screen and place items on the
# simple_advanced_date_screen. Both curr_advanced_date_state and
# curr_recurring_date_info objects are updated appropriately.
# This method is called by the Advanced... button on the creation screen.
def move_to_advanced_date_screen():
    remove_new_event_values()
    add_simple_advanced_date_values()
    add_simple_month_day_buttons()
    remove_confirmation_buttons()
    add_advanced_date_confirmation_buttons()
    simple_button.configure(relief='sunken')
    curr_advanced_date_state.set_at_simple(True)
    curr_recurring_date_info.reinitialize()
    add_completion_advanced_date_button()

# The remove_whichever_advanced_date_values first determines which advanced
# date state the user is at, then removes the items on the screen specific
# to that date state.
def remove_whichever_advanced_date_values():
    if curr_advanced_date_state.get_at_simple() == True:
        remove_simple_advanced_date_values()
        simple_button.configure(relief='raised')
    elif curr_advanced_date_state.get_at_month() == True:
        remove_month_advanced_date_values()
        month_button.configure(relief='raised')
    elif curr_advanced_date_state.get_at_day() == True:
        remove_day_advanced_date_values()
        day_button.configure(relief='raised')

# The move_to_create_new_event_or_task_from_advanced_date method handles
# deletion of items on the advanced_date_screen and addition of items for
# the appropriate creation screen.
# This method is called by the Never Mind button on the advanced_date_screen
# or store_recurring_date_and_move().
def move_to_create_new_event_or_task_from_advanced_date():
    if curr_task_or_event_obj.get_creating_task() == True:
        remove_whichever_advanced_date_values()
        remove_simple_month_day_buttons()
        remove_advanced_date_confirmation_buttons()
        remove_completion_advanced_date_button()
        add_new_task_values()
        add_confirmation_buttons()
    elif curr_task_or_event_obj.get_creating_event() == True:
        remove_whichever_advanced_date_values()
        remove_simple_month_day_buttons()
        remove_advanced_date_confirmation_buttons()
        remove_completion_advanced_date_button()
        add_new_event_values()
        add_confirmation_buttons()

    """ testing """
    print curr_recurring_date_info.day_checkbutton_value_tsil, curr_recurring_date_info.day_scale_num.get()

# The store_recurring_date_and_move method determines the state of
# advanced_date_screen the user is at then stores the appropriate
# information in the curr_recurring_date_info object. If completion date
# was chosen, the appropriate object is updated as well. The method to
# move to creation screen is then called.
# This method is called by the Confirm button on the advanced_date_screen.
def store_recurring_date_and_move():
    """ Code to store recurring date in variable """
    if curr_advanced_date_state.get_at_simple() == True:
        """ code for simple vars """
        setattr(curr_recurring_date_info, \
        'simple_scale_num', num_simple_from_scale.get())
        setattr(curr_recurring_date_info, \
        'simple_radio_value', day_week_month_year_radio_var.get())
        setattr(curr_recurring_date_info, \
        'holding_simple', True)
    elif curr_advanced_date_state.get_at_month() == True:
        """ month """
        setattr(curr_recurring_date_info, \
        'month_first_thru_last_value', first_thru_last_menu_var)
        setattr(curr_recurring_date_info, \
        'month_monday_thru_day_value', mon_thru_day_menu_var)
        setattr(curr_recurring_date_info, \
        'month_scale_num', month_advanced_scale.get())
        setattr(curr_recurring_date_info, \
        'holding_month', True)
    elif curr_advanced_date_state.get_at_day() == True:
        """ day """
        setattr(curr_recurring_date_info, \
        'day_scale_num', num_day_from_scale)
        checkbutton_values_tsil_to_attr = append_checkbutton_values()
        setattr(curr_recurring_date_info, \
        'day_checkbutton_value_tsil', checkbutton_values_tsil_to_attr)
        setattr(curr_recurring_date_info, \
        'holding_day', True)

    """ update appropriate object to indicate recurring date present """
    setattr(curr_recurring_date_info, 'holding_recurring_date', True)

    """ determine if completion date present, and update appropriate object
    if so """
    if calendar_for_completion.get_date() != False:
        completion_date = calendar_for_completion.get_date()
        setattr(curr_advanced_date_state, 'completion_date', \
        calendar_for_completion.get_date())
        setattr(curr_advanced_date_state, 'holding_completion_date', True)

    """ move part """
    move_to_create_new_event_or_task_from_advanced_date()

# Utility function to gather checkbutton values on the day state of the
# advanced_date_screen. Called by store_recurring_date_and_move().
def append_checkbutton_values():
    tsil_to_return = []
    for x in checkbutton_value_tsil:
        for y in poss_checkbutton_value_tsil:
            if x.get() == y:
                tsil_to_return.append(x.get())
    return tsil_to_return

# The completion_open_calendar method opens a new window with the arg
# master_window as its root window, used to select a date for an event
# to occur or a task to be due.
def completion_open_calendar(master_window):
    calendar_for_completion.start_window(master_window)

# The move_to_reminder_screen method opens a new window for the user to input
# the number of days before an event's occurrence to display a reminder.
def move_to_reminder_screen():
    reminder_window_handler.start_window()

# These methods are responsible for switching between simple, month, and day
# states on advanced_date_screen.
def move_to_simple_advanced_date_screen():
    if curr_advanced_date_state.get_at_month() == True:
        remove_month_advanced_date_values()
        month_button.configure(relief='raised')
        curr_advanced_date_state.set_at_month(False)
    elif curr_advanced_date_state.get_at_day() == True:
        remove_day_advanced_date_values()
        day_button.configure(relief='raised')
        curr_advanced_date_state.set_at_day(False)

    add_simple_advanced_date_values()
    simple_button.configure(relief='sunken')
    curr_advanced_date_state.set_at_simple(True)

def move_to_month_advanced_date_screen():
    if curr_advanced_date_state.get_at_simple() == True:
        remove_simple_advanced_date_values()
        simple_button.configure(relief='raised')
        curr_advanced_date_state.set_at_simple(False)
    elif curr_advanced_date_state.get_at_day() == True:

        remove_day_advanced_date_values()
        day_button.configure(relief='raised')
        curr_advanced_date_state.set_at_day(False)

    add_month_advanced_date_values()
    month_button.configure(relief='sunken')
    curr_advanced_date_state.set_at_month(True)

def move_to_day_advanced_date_screen():
    if curr_advanced_date_state.get_at_simple() == True:
        remove_simple_advanced_date_values()
        simple_button.configure(relief='raised')
        curr_advanced_date_state.set_at_simple(False)
    elif curr_advanced_date_state.get_at_month() == True:
        remove_month_advanced_date_values()
        month_button.configure(relief='raised')
        curr_advanced_date_state.set_at_month(False)

    for each_checkbutton in monday_thru_sunday_day_checkbutton_tsil:
        each_checkbutton.deselect()

    add_day_advanced_date_values()
    day_button.configure(relief='sunken')
    curr_advanced_date_state.set_at_day(True)

# These methods are responsible for the placement and removal of items on
# the main_screen:

# The add_msgbox blits the msgbox Text/Label object to the screen with
# current_msg inside.
def add_msgbox():
    msgbox.delete('1.0', 'end')
    msgbox.insert('1.0', current_msg)
    msgbox.place(height=160, width=380, x=300, y=30)

def remove_msgbox():
    msgbox.place_forget()


def add_starting_buttons():
    new_event_button.place(x=340, y=240, height=40, width=80)
    new_task_button.place(x=540, y=240, height=40, width=80)
    reminder_button.place(x=440, y=240, height=40,width=80)

def remove_starting_buttons():
    new_event_button.place_forget()
    new_task_button.place_forget()
    reminder_button.place_forget()
    msgbox.place_forget()

# These methods are responsible for the placement and removal of items on
# the create_event screen:
def add_new_event_values():
    name_label.place(x=x_label_location, y=y_name_label_location, width=80)
    date_label.place(x=x_label_location, y=y_date_label_location, width=80)
    time_label.place(x=x_label_location, y=y_time_label_location, width=80)
    location_label.place(x=x_label_location, y=\
    y_location_label_location, width=80)
    note_label.place(x=x_label_location, y=y_note_label_location, width=80)
    name_label_input.place(x=x_label_location+100, y=y_name_label_location)
    date_label_input.place(x=x_label_location+100, y=y_date_label_location)
    time_label_input.place(x=x_label_location+100, y=y_time_label_location)
    location_label_input.place(x=x_label_location+100, y=y_location_label_location)
    note_label_input.place(x=x_label_location+100, y=y_note_label_location)
    advanced_date_button.place(x=x_advanced_date_location,\
    y=y_advanced_date_location)
    reminder_screen_button.place(x=x_remindme_button_location, \
    y=y_remindme_button_location)

def remove_new_event_values():
    name_label.place_forget()
    date_label.place_forget()
    time_label.place_forget()
    location_label.place_forget()
    note_label.place_forget()
    name_label_input.place_forget()
    date_label_input.place_forget()
    time_label_input.place_forget()
    location_label_input.place_forget()
    note_label_input.place_forget()
    advanced_date_button.place_forget()
    reminder_screen_button.place_forget()

# These methods are responsible for the placement and removal of items on the
# create_task screen:
def add_new_task_values():
    name_label.place(x=x_label_location, y=y_name_label_location, width=80)
    date_label.place(x=x_label_location, y=y_date_label_location, width=80)
    time_label.place(x=x_label_location, y=y_time_label_location, width=80)
    location_label.place(x=x_label_location, y=\
    y_location_label_location, width=80)
    note_label.place(x=x_label_location, y=y_note_label_location, width=80)
    name_label_input.place(x=x_label_location+100, y=y_name_label_location)
    date_label_input.place(x=x_label_location+100, y=y_date_label_location)
    time_label_input.place(x=x_label_location+100, y=y_time_label_location)
    location_label_input.place(x=x_label_location+100, y=y_location_label_location)
    note_label_input.place(x=x_label_location+100, y=y_note_label_location)
    advanced_date_button.place(x=x_advanced_date_location,\
    y=y_advanced_date_location)
    reminder_screen_button.place(x=x_remindme_button_location, \
    y=y_remindme_button_location)

def remove_new_task_values():
    name_label.place_forget()
    date_label.place_forget()
    time_label.place_forget()
    location_label.place_forget()
    note_label.place_forget()
    name_label_input.place_forget()
    date_label_input.place_forget()
    time_label_input.place_forget()
    location_label_input.place_forget()
    note_label_input.place_forget()
    advanced_date_button.place_forget()
    reminder_screen_button.place_forget()

# These methods are responsible for the placement and removal of items on
# both the create_event and create_task screens:
def add_confirmation_buttons():
    ok_confirmation.place(x=x_ok_confirmation_location,\
     y=y_confirmation_location)
    back_confirmation.place(x=x_back_confirmation_location,\
     y=y_confirmation_location)

def remove_confirmation_buttons():
    ok_confirmation.place_forget()
    back_confirmation.place_forget()

# These methods are responsible for the placement and removal of items on the
# advanced_date_screen.
def add_simple_month_day_buttons():
    simple_button.place(x=x_simple_location, y=y_simple_month_day_location)
    month_button.place(x=x_month_location, y=y_simple_month_day_location)
    day_button.place(x=x_day_location, y=y_simple_month_day_location)

def remove_simple_month_day_buttons():
    simple_button.place_forget()
    month_button.place_forget()
    day_button.place_forget()

def add_advanced_date_confirmation_buttons():
    back_advanced_date_button.place(x=x_back_advanced_date_location, \
    y=y_back_or_confirm_advanced_date_location)
    confirm_advanced_date_button.place(x=x_confirm_advanced_date_location, \
    y=y_back_or_confirm_advanced_date_location)

def remove_advanced_date_confirmation_buttons():
    back_advanced_date_button.place_forget()
    confirm_advanced_date_button.place_forget()

def add_simple_advanced_date_values():
    day_radiobutton.place(x=x_simple_day_week_month_year_radio_location, \
    y=y_simple_day_radio_location)
    week_radiobutton.place(x=x_simple_day_week_month_year_radio_location, \
    y=y_simple_week_radio_location)
    month_radiobutton.place(x=x_simple_day_week_month_year_radio_location, \
    y=y_simple_month_radio_location)
    year_radiobutton.place(x=x_simple_day_week_month_year_radio_location, \
    y=y_simple_year_radio_location)
    num_simple_scale.place(x=x_simple_scale_location, \
    y=y_simple_scale_location)
    simple_text_advanced_date.place(x=x_simple_text_advanced_date_location, \
    y=y_simple_text_advanced_date_location)

def remove_simple_advanced_date_values():
    num_simple_scale.place_forget()
    day_radiobutton.place_forget()
    week_radiobutton.place_forget()
    month_radiobutton.place_forget()
    year_radiobutton.place_forget()
    simple_text_advanced_date.place_forget()

def add_month_advanced_date_values():
    first_thru_last_month_menubutton.place(\
    x=x_first_thru_last_menubutton_location, \
    y=y_advanced_month_both_menubuttons)
    monday_thru_day_month_menubutton.place(\
    x=x_monday_thru_day_menubutton_location, \
    y=y_advanced_month_both_menubuttons)
    month_advanced_scale.place(x=x_month_advanced_scale_location, \
    y=y_month_advanced_scale_location)
    month_text_advanced_date_1.place(x=x_month_text_1_advanced_date_location, \
    y=y_month_text_advanced_date_location)
    month_text_advanced_date_2.place(x=x_month_text_2_advanced_date_location, \
    y=y_month_text_advanced_date_location)

def remove_month_advanced_date_values():
    first_thru_last_month_menubutton.place_forget()
    monday_thru_day_month_menubutton.place_forget()
    month_advanced_scale.place_forget()
    month_text_advanced_date_1.place_forget()
    month_text_advanced_date_2.place_forget()

def add_day_advanced_date_values():
    monday_day_checkbutton.place(x=x_weekday_day_checkbutton_location, \
    y=y_monday_day_checkbutton_location)
    tuesday_day_checkbutton.place(x=x_weekday_day_checkbutton_location, \
    y=y_monday_day_checkbutton_location+35)
    wednesday_day_checkbutton.place(x=x_weekday_day_checkbutton_location, \
    y=y_monday_day_checkbutton_location+70)
    thursday_day_checkbutton.place(x=x_weekday_day_checkbutton_location, \
    y=y_monday_day_checkbutton_location+105)
    friday_day_checkbutton.place(x=x_weekday_day_checkbutton_location, \
    y=y_monday_day_checkbutton_location+140)
    saturday_day_checkbutton.place(x=x_weekend_day_checkbutton_location, \
    y=y_saturday_checkbutton_location)
    sunday_day_checkbutton.place(x=x_weekend_day_checkbutton_location, \
    y=y_saturday_checkbutton_location+60)
    one_to_52_day_scale.place(x=x_day_scale_location, y=y_day_scale_location)
    day_text_advanced_date_1.place(x=x_day_text_1_advanced_date_location, \
    y=y_day_text_advanced_date_location)
    day_text_advanced_date_2.place(x=x_day_text_2_advanced_date_location, \
    y=y_day_text_advanced_date_location)

def remove_day_advanced_date_values():
    monday_day_checkbutton.place_forget()
    tuesday_day_checkbutton.place_forget()
    wednesday_day_checkbutton.place_forget()
    thursday_day_checkbutton.place_forget()
    friday_day_checkbutton.place_forget()
    saturday_day_checkbutton.place_forget()
    sunday_day_checkbutton.place_forget()
    one_to_52_day_scale.place_forget()
    day_text_advanced_date_1.place_forget()
    day_text_advanced_date_2.place_forget()

def add_completion_advanced_date_button():
    completion_advanced_date_button.place(\
    x=x_completion_advanced_date_button_location, \
    y=y_completion_advanced_date_button_location)

def remove_completion_advanced_date_button():
    completion_advanced_date_button.place_forget()

# Create objects to be blitted onto the screen by the methods above.

# For items on the main_screen:
msgbox = Tkinter.Text(main_window, fg='BLUE', bg='WHITE', wrap='word')
new_event_button = Tkinter.Button(text='New Event', \
command=lambda: move_to_create_new_event())
new_task_button = Tkinter.Button(text='New Task', \
command=lambda: move_to_create_new_task())
reminder_button = Tkinter.Button(text="What\'s up?")

# For items on the creation screen:
name_label = Tkinter.Label(text='Name', relief='flat')
date_label = Tkinter.Label(text='Date', relief='flat')
time_label = Tkinter.Label(text='Time', relief='flat')
location_label = Tkinter.Label(text='Location', relief='flat')
note_label = Tkinter.Label(text='Notes', relief='flat')
name_label_input = Tkinter.Entry(width=40)
date_label_input = Tkinter.Entry(width=40)
time_label_input = Tkinter.Entry(width=40)
location_label_input = Tkinter.Entry(width=40)
note_label_input = Tkinter.Text(width=30, height=3)

ok_confirmation = Tkinter.Button(text='OK',\
command=lambda: ok_to_create_new_event_or_task())
back_confirmation = Tkinter.Button(text='Back', \
command=lambda: move_to_main_screen())

advanced_date_button = Tkinter.Button(text='Advanced...', font=smaller_font, \
command=move_to_advanced_date_screen)
reminder_screen_button = Tkinter.Button(text='Remind me...', \
font=smaller_font, command=move_to_reminder_screen)

# For items always on the advanced_date_screen:
simple_button = Tkinter.Button(text='Simple...', font=bigger_font, \
command=move_to_simple_advanced_date_screen)
month_button = Tkinter.Button(text='Month...', font=bigger_font, \
command=move_to_month_advanced_date_screen)
day_button = Tkinter.Button(text='Day...', font=bigger_font, \
command=move_to_day_advanced_date_screen)
back_advanced_date_button = Tkinter.Button(text='Never mind', \
command=move_to_create_new_event_or_task_from_advanced_date)
confirm_advanced_date_button = Tkinter.Button(text='Confirm', \
command=store_recurring_date_and_move)
completion_advanced_date_button = Tkinter.Button(text='Until...?', \
command=lambda: completion_open_calendar(main_window))

# For items on simple_advanced_date_screen:
num_simple_scale = Tkinter.Scale(main_window, variable=num_simple_from_scale, \
from_=1, to=45)
day_simple, week_simple, month_simple, year_simple = 0, 0, 0, 0

day_radiobutton = Tkinter.Radiobutton(main_window, text='Days', \
var=day_week_month_year_radio_var, value=1, font=big_font, bg='GREY', \
activebackground='GREY')
week_radiobutton = Tkinter.Radiobutton(main_window, text='Weeks', \
var=day_week_month_year_radio_var, value=2, font=big_font, bg='GREY', \
activebackground='GREY')
month_radiobutton = Tkinter.Radiobutton(main_window, text='Months', \
var=day_week_month_year_radio_var, value=3, font=big_font, bg='GREY', \
activebackground='GREY')
year_radiobutton = Tkinter.Radiobutton(main_window, text='Years', \
var=day_week_month_year_radio_var, value=4, font=big_font, bg='GREY', \
activebackground='GREY')

simple_text_advanced_date = Tkinter.Label(main_window, \
text='Every', font=bigger_font, bg='GREY')

# For items on month_advanced_date_screen:
first_thru_last_month_menubutton = Tkinter.Menubutton(main_window, \
text='Choose...', relief='raised', font=big_font)
first_thru_last_month_menubutton.menu = \
Tkinter.Menu(first_thru_last_month_menubutton)
first_thru_last_month_menubutton["menu"]=first_thru_last_month_menubutton.menu
first_thru_last_month_menubutton.menu.add_radiobutton(label='First', \
variable=first_thru_last_menu_var, value=1)
first_thru_last_month_menubutton.menu.add_radiobutton(label='Second', \
variable=first_thru_last_menu_var, value=2)
first_thru_last_month_menubutton.menu.add_radiobutton(label='Third', \
variable=first_thru_last_menu_var, value=3)
first_thru_last_month_menubutton.menu.add_radiobutton(label='Fourth', \
variable=first_thru_last_menu_var, value=4)
first_thru_last_month_menubutton.menu.add_radiobutton(label='Last', \
variable=first_thru_last_menu_var, value=5)

monday_thru_day_month_menubutton = Tkinter.Menubutton(main_window, \
text='Choose...', relief='raised', font=big_font)
monday_thru_day_month_menubutton.menu = \
Tkinter.Menu(monday_thru_day_month_menubutton)
monday_thru_day_month_menubutton["menu"]=monday_thru_day_month_menubutton.menu
monday_thru_day_month_menubutton.menu.add_radiobutton(label='Monday', \
variable=mon_thru_day_menu_var, value=1)
monday_thru_day_month_menubutton.menu.add_radiobutton(label='Tuesday', \
variable=mon_thru_day_menu_var, value=2)
monday_thru_day_month_menubutton.menu.add_radiobutton(label='Wednesday', \
variable=mon_thru_day_menu_var, value=3)
monday_thru_day_month_menubutton.menu.add_radiobutton(label='Thursday', \
variable=mon_thru_day_menu_var, value=4)
monday_thru_day_month_menubutton.menu.add_radiobutton(label='Friday', \
variable=mon_thru_day_menu_var, value=5)
monday_thru_day_month_menubutton.menu.add_radiobutton(label='Saturday', \
variable=mon_thru_day_menu_var, value=6)
monday_thru_day_month_menubutton.menu.add_radiobutton(label='Sunday', \
variable=mon_thru_day_menu_var, value=7)
monday_thru_day_month_menubutton.menu.add_radiobutton(label='Day', \
variable=mon_thru_day_menu_var, value=8)

month_advanced_scale = Tkinter.Scale(main_window, from_=1, to=24)

month_text_advanced_date_1 = Tkinter.Label(main_window, \
text='of every', font=bigger_font, bg='GREY')
month_text_advanced_date_2 = Tkinter.Label(main_window, \
text='months.', font=bigger_font, bg='GREY')

# For items on day_advanced_date_screen:
monday_day_checkbutton = Tkinter.Checkbutton(text='Monday', \
variable=monday_checkbutton_value, onvalue=poss_checkbutton_value_tsil[0])
tuesday_day_checkbutton = Tkinter.Checkbutton(text='Tuesday', \
variable=tuesday_checkbutton_value, onvalue=poss_checkbutton_value_tsil[1])
wednesday_day_checkbutton = Tkinter.Checkbutton(text='Wednesday', \
variable=wednesday_checkbutton_value, onvalue=poss_checkbutton_value_tsil[2])
thursday_day_checkbutton = Tkinter.Checkbutton(text='Thursday', \
variable=thursday_checkbutton_value, onvalue=poss_checkbutton_value_tsil[3])
friday_day_checkbutton = Tkinter.Checkbutton(text='Friday', \
variable=friday_checkbutton_value, onvalue=poss_checkbutton_value_tsil[4])
saturday_day_checkbutton = Tkinter.Checkbutton(text='Saturday', \
variable=saturday_checkbutton_value, onvalue=poss_checkbutton_value_tsil[5])
sunday_day_checkbutton = Tkinter.Checkbutton(text='Sunday', \
variable=sunday_checkbutton_value, onvalue=poss_checkbutton_value_tsil[6])

one_to_52_day_scale = Tkinter.Scale(main_window, variable=num_day_from_scale, \
from_=1, to=52)

monday_thru_sunday_day_checkbutton_tsil = [monday_day_checkbutton, \
tuesday_day_checkbutton, wednesday_day_checkbutton, thursday_day_checkbutton, \
friday_day_checkbutton, saturday_day_checkbutton, sunday_day_checkbutton]

day_text_advanced_date_1 = Tkinter.Label(main_window, \
text='of every', font=bigger_font, bg='GREY')
day_text_advanced_date_2 = Tkinter.Label(main_window, \
text='weeks.', font=bigger_font, bg='GREY')




start_program()
main_window.mainloop()


