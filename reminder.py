import tkinter as tkr
import time

#WIDGET NAMES ARE DECLARED WITH CAPITAL LETTERS

class Reminder:
    def __init__(self):
        print('intitalizaing reminder object')
        self.reminder = tkr.Tk()
        self.transparency = 0.5
        self.message = 'nik e gei'
        self.time_between_reminders = 2
        self.reminder_time_on_screen = 2
        
        self.set_up_message()

        self.reminder.wm_attributes("-alpha",self.transparency)
        self.reminder.overrideredirect(1)
        self.center()
        

    def run(self):
        print('running mainloop reminder')
        self.reminder.mainloop()
        #useless ne moe go barame blokira vsichkiq kod dolu
        #do spirane na tkinera

    def quit(self):
        print('closing mainloop reminder')
        self.reminder.quit()
        #useless
        
    def update(self):
        print('updating reminder')
        self.reminder.update()

    def destroy(self):
        print('destroying reminder')
        self.reminder.destroy()


    def change_transparency(self, new_transparency):
        print('changing transparency to',new_transparency)
        self.transparency = new_transparency
        self.reminder.wm_attributes("-alpha",self.transparency)

    def change_message(self, msg):
        print('çhanging message')
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

    def set_up_message(self):
        self.MESSAGE = tkr.Message(self.reminder, text = self.message)
        self.MESSAGE.config(background = 'white')
        self.MESSAGE.config(font = ('times', 100, 'italic'))
        self.MESSAGE.pack()

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
