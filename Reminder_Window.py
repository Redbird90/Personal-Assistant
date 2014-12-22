#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      jkougl
#
# Created:     16/09/2014
# Copyright:   (c) jkougl 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------


import tkMessageBox
from Tkinter import Toplevel
import Tkinter
import tkFont

x_reminder_text_1_location = 120
x_reminder_text_2_location = 230
y_reminder_texts_location = 75
x_reminder_entry_location = 200
y_reminder_entry_location = y_reminder_texts_location
x_ok_reminder_button_location = 250
x_back_reminder_button_location = 150
y_ok_back_reminder_button_locations = 140



class Reminder_Window():



    def start_window(self):
        self.reminder_window = Toplevel()
        self.reminder_window.grab_set()
        self.reminder_window.title('Reminder')
        self.reminder_window.geometry('400x200')
        big_font = tkFont.Font(size=10)
        self.reminder_text_1 = Tkinter.Label(self.reminder_window,
        text='Remind me', font=big_font)
        self.reminder_text_2 = Tkinter.Label(self.reminder_window, \
        text='day(s) before.', font=big_font)
        self.reminder_entry = Tkinter.Entry(self.reminder_window, width=3)
        self.ok_reminder_button = Tkinter.Button(self.reminder_window,
        text='OK', command=self.on_ok_button_press)
        self.back_reminder_button = Tkinter.Button(self.reminder_window, \
        text='Back', command=self.on_back_button_press)


        self.reminder_text_1.place(x=x_reminder_text_1_location, \
        y=y_reminder_texts_location)
        self.reminder_text_2.place(x=x_reminder_text_2_location, \
        y=y_reminder_texts_location)
        self.reminder_entry.place(x=x_reminder_entry_location, \
        y=y_reminder_entry_location)
        self.ok_reminder_button.place(x=x_ok_reminder_button_location, \
        y=y_ok_back_reminder_button_locations)
        self.back_reminder_button.place(x=x_back_reminder_button_location, \
        y=y_ok_back_reminder_button_locations)
        self.reminder_window.mainloop()

    def on_ok_button_press(self):
        entry_reminder_value = self.reminder_entry.get()
        try:
            int_entry_reminder_value = int(entry_reminder_value)
            #print 0 > int_entry_reminder_value, int_entry_reminder_value < 50
            if 0 > int_entry_reminder_value or int_entry_reminder_value > 50:
                print 'hi'
                tkMessageBox.showinfo("Error", \
                'Invalid Entry.  Please enter a number from 0-50')
                self.reminder_window.grab_set()
                self.reminder_window.lift()

            else:
                self.num_of_days_before_to_remind_int = int_entry_reminder_value
                self.reminder_window.destroy()

        except ValueError:
            tkMessageBox.showinfo("Error", \
            'Invalid Entry.  Please enter a number from 0-50')
            self.reminder_window.grab_set()
            self.reminder_window.lift()


    def on_back_button_press(self):
        self.num_of_days_before_to_remind_int = 0
        self.reminder_window.destroy()



'''
now = Reminder_Window()
now.start_window()
'''

