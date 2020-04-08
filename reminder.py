import tkinter as tkr
import time
import sqlite3

#WIDGET NAMES ARE DECLARED WITH CAPITAL LETTERS

class Reminder:
    def __init__(self):
        #konstruktora setupva neshtata
        self.reminder = tkr.Tk()
        self.read_from_database()
        self.set_up_message_widget()
        self.reminder.wm_attributes("-alpha",self.transparency)
        self.reminder.overrideredirect(1)
        self.center()
        

    #not used useless
    def run(self):
        self.reminder.mainloop()

    #not used useless
    def quit(self):
        self.reminder.quit()
        
    def update(self):
        self.reminder.update()

    def destroy(self):
        self.reminder.destroy()


    def change_transparency(self, new_transparency):
        self.transparency = new_transparency
        self.reminder.wm_attributes("-alpha",self.transparency)

    def change_message(self, msg):
        self.message = msg
        self.MESSAGE.destroy()
        self.set_up_message()

    def change_time_between_reminders(new_time):
        self.time_between_reminders = new_time

    def change_reminder_time_on_screen(new_time):
        self.reminder_time_on_screen = new_time
        
    def center(self):
        self.reminder.update_idletasks()
        width = self.reminder.winfo_width()
        frm_width = self.reminder.winfo_rootx() - self.reminder.winfo_x()
        win_width = width + 2 * frm_width
        height = self.reminder.winfo_height()
        titlebar_height = self.reminder.winfo_rooty() - self.reminder.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = self.reminder.winfo_screenwidth() // 2 - win_width // 2
        y = self.reminder.winfo_screenheight() // 2 - win_height // 2
        self.reminder.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.reminder.deiconify()

    def set_up_message_widget(self):
        self.MESSAGE = tkr.Message(self.reminder, text = self.message)
        self.MESSAGE.config(background = 'white')
        self.MESSAGE.config(font = ('times', 100, 'italic'))
        self.MESSAGE.pack()

    def read_from_database(self):
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
        

while(True):
    reminder = Reminder()
    reminder.update()
    time.sleep(reminder.reminder_time_on_screen)
    time_off = reminder.time_between_reminders
    reminder.destroy()
    time.sleep(time_off)

#safe for later
#root.overrideredirect(1)
#root.lift()

