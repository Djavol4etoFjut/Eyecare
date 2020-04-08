import tkinter as tkr
import time
import subprocess
import os
import signal
import sqlite3

#WIDGET NAMES ARE DECLARED WITH CAPITAL LETTERS
#a

class Interface:
    def __init__(self):
        self.interface = tkr.Tk()
        self.update_from_database()
        self.set_up_widgets()
        self.interface.mainloop()


    def update_all(self):
        self.write_settings_to_database()
        self.destroy_widgets()
        self.set_up_widgets()
        self.interface.update()
        
    def on_click_message(self, new_msg):
        self.change_message(new_msg)
        self.update_all()
        
    def on_click_time_between_reminders(self, new_time_between_reminders):
        self.change_time_between_reminders(int(new_time_between_reminders))
        self.update_all()
            
    def on_click_reminder_time_on_screen(self, new_reminder_time_on_screen):
        self.change_reminder_time_on_screen(int(new_reminder_time_on_screen))
        self.update_all()
            
    def on_click_transparency(self, new_transparency):
        self.change_transparency(float(new_transparency))
        self.update_all()
        
    def on_click_process_status(self):
        if(self.process_status == False):
            self.PID = subprocess.Popen('reminderexe.exe')
            self.process_id_in_string = str(self.PID.pid)
            self.process_status = True
        elif(self.process_status == True):
            #self.PID.terminate()
            #self.PID.kill()
            subprocess.Popen("TASKKILL /F /PID {pid} /T".format(pid=int(self.process_id_in_string)))
            self.process_status = False
            self.process_id_in_string = 'NULL'
        self.update_all()
        
    def set_up_widgets(self):
        self.CLOSE_BUTTON = tkr.Button(text = 'close', command = self.exit_main_loop)

        self.MESSAGE_CURRENT = tkr.Label(self.interface, text = 'current message is: ' + self.message)
        self.TIME_BETWEEN_REMINDERS_CURRENT = tkr.Label(self.interface, text = 'current time between reminders is: ' + str(self.time_between_reminders))
        self.REMINDER_TIME_ON_SCREEN_CURRENT = tkr.Label(self.interface, text = 'current time of reminder on screen is: ' + str(self.reminder_time_on_screen))
        self.TRANSPARENCY_CURRENT = tkr.Label(self.interface, text = 'current transparency is: ' + str(self.transparency))

        self.MESSAGE_ENTRY = tkr.Entry(self.interface)
        self.TIME_BETWEEN_REMINDERS_ENTRY = tkr.Entry(self.interface)
        self.REMINDER_TIME_ON_SCREEN_ENTRY = tkr.Entry(self.interface)
        self.TRANSPARENCY_ENTRY = tkr.Entry(self.interface)

        self.MESSAGE_BUTTON = tkr.Button(self.interface, text='Change', command=lambda: self.on_click_message(self.MESSAGE_ENTRY.get()))
        self.TIME_BETWEEN_REMINDERS_BUTTON = tkr.Button(self.interface, text='Change', command=lambda: self.on_click_time_between_reminders(self.TIME_BETWEEN_REMINDERS_ENTRY.get()))
        self.REMINDER_TIME_ON_SCREEN_BUTTON = tkr.Button(self.interface, text='Change', command=lambda: self.on_click_reminder_time_on_screen(self.REMINDER_TIME_ON_SCREEN_ENTRY.get()))
        self.TRANSPARENCY_BUTTON = tkr.Button(self.interface, text='Change', command=lambda: self.on_click_transparency(self.TRANSPARENCY_ENTRY.get()))

        self.STATUS_CURRENT = tkr.Label(self.interface, text = 'current status of process: ' + self.process_status_to_string())
        self.STATUS_BUTTON = tkr.Button(self.interface, text = 'ON/OFF', command = self.on_click_process_status)
    
        
        self.MESSAGE_CURRENT.grid(row=1, column=0)
        self.TIME_BETWEEN_REMINDERS_CURRENT.grid(row=2, column=0)
        self.REMINDER_TIME_ON_SCREEN_CURRENT.grid(row=3, column=0)
        self.TRANSPARENCY_CURRENT.grid(row=4, column=0)
        
        self.MESSAGE_ENTRY.grid(row=1, column=1)
        self.TIME_BETWEEN_REMINDERS_ENTRY.grid(row=2, column=1)
        self.REMINDER_TIME_ON_SCREEN_ENTRY.grid(row=3, column=1)
        self.TRANSPARENCY_ENTRY.grid(row=4, column=1)

        self.MESSAGE_BUTTON.grid(row=1, column=2)
        self.TIME_BETWEEN_REMINDERS_BUTTON.grid(row=2, column=2)
        self.REMINDER_TIME_ON_SCREEN_BUTTON.grid(row=3, column=2)
        self.TRANSPARENCY_BUTTON.grid(row=4, column=2)

        self.STATUS_CURRENT.grid(row=5, column=0)
        self.STATUS_BUTTON.grid(row=5, column=1)

        self.CLOSE_BUTTON.grid(row=6,column=0)

    def destroy_widgets(self):
        self.CLOSE_BUTTON.grid_remove()
        
        self.MESSAGE_CURRENT.grid_remove()
        self.TIME_BETWEEN_REMINDERS_CURRENT.grid_remove()
        self.REMINDER_TIME_ON_SCREEN_CURRENT.grid_remove()
        self.TRANSPARENCY_CURRENT.grid_remove()

        self.MESSAGE_ENTRY.grid_remove()
        self.TIME_BETWEEN_REMINDERS_ENTRY.grid_remove()
        self.REMINDER_TIME_ON_SCREEN_ENTRY.grid_remove()
        self.TRANSPARENCY_ENTRY.grid_remove()

        self.MESSAGE_BUTTON.grid_remove()
        self.TIME_BETWEEN_REMINDERS_BUTTON.grid_remove()
        self.REMINDER_TIME_ON_SCREEN_BUTTON.grid_remove()
        self.TRANSPARENCY_BUTTON.grid_remove()

        self.STATUS_CURRENT.grid_remove()
        self.STATUS_BUTTON.grid_remove()

    def process_status_to_string(self):
        if(self.process_status == False):
            return 'OFF'
        elif(self.process_status == True):
            return 'ON'
        
    def exit_main_loop(self):
        self.interface.quit()

    def destroy(self):
        self.interface.destroy()

    def change_transparency(self, new_transparency):
        self.transparency = new_transparency

    def change_time_between_reminders(self, new_time_between_reminders):
        self.time_between_reminders = new_time_between_reminders

    def change_reminder_time_on_screen(self, new_reminder_time_on_screen):
        self.reminder_time_on_screen = new_reminder_time_on_screen

    def change_message(self, new_message):
        self.message = new_message


    def update_from_database(self):
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()
        
        cur.execute("SELECT message FROM settings")
        temp = cur.fetchall()
        self.message = temp[0][0]

        cur.execute("SELECT transparency FROM settings")
        temp = cur.fetchall()
        self.transparency = temp[0][0]

        cur.execute("SELECT time_between_reminders FROM settings")
        temp = cur.fetchall()
        self.time_between_reminders = temp[0][0]

        cur.execute("SELECT time_of_reminder_on_screen FROM settings")
        temp = cur.fetchall()
        self.reminder_time_on_screen = temp[0][0]

        cur.execute("SELECT process_status FROM settings")
        temp = cur.fetchall()
        if(temp[0][0] == 1):
            self.process_status = True
        else:
            self.process_status = False

        cur.execute("SELECT PID_STR FROM settings")
        temp = cur.fetchall()
        self.process_id_in_string = temp[0][0]
        
    def write_settings_to_database(self):
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()

        str1 = ''' UPDATE settings 
                    SET message = ?,
                    transparency = ?,
                    time_between_reminders = ?,
                    time_of_reminder_on_screen = ?,
                    process_status = ?,
                    PID_STR = ?'''
        if(self.process_status == False):
            help1 = 0
        elif(self.process_status == True):
            help1 = 1
        help2 = (self.message, self.transparency,
                 self.time_between_reminders, self.reminder_time_on_screen,
                 help1, self.process_id_in_string)
        cur.execute(str1, help2)
        
        conn.commit()
        
    

interface = Interface()
interface.destroy()
interface.update_from_database()
