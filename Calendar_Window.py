#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Juli
#
# Created:     14/09/2014
# Copyright:   (c) Juli 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import Tkinter
from ttkcalendar_updated import *
from Tkinter import *
import tkMessageBox

class Calendar_Window():
    def __init__(self, window_name='Calendar', date_to_get=False):
        self.window_name = window_name
        self.date_to_get = date_to_get


    def start_window(self, master_window):
        self.root_window = Toplevel()
        self.root_window.grab_set()
        self.root_window.title(self.window_name)
        self.ok_button = Tkinter.Button(self.root_window, text='OK', \
        command=self.on_ok_button_press)
        self.back_button = Tkinter.Button(self.root_window, text='Back', \
        command=self.on_back_button_press)
        self.calendar_obj = Calendar(self.root_window)

        self.calendar_obj.pack(side='top')
        self.ok_button.pack(side='left', padx=50)
        self.back_button.pack(side='right', padx=50)
        #self.root_window.focus_force()
        #self.root_window.mainloop()


    def on_ok_button_press(self):
        self.date_to_get = self.calendar_obj.selection
        if self.date_to_get == None:
            tkMessageBox.showinfo("Error", \
            'Please select a date then press OK.')
            self.root_window.grab_set()
            self.root_window.lift()
        else:
            self.root_window.destroy()

    def on_back_button_press(self):
        self.date_to_get = False
        self.root_window.destroy()

    def get_date(self):
        return self.date_to_get


'''
any_window = Tkinter.Tk()


c = Calendar_Window()
c.start_window(any_window)

any_window.mainloop()
'''