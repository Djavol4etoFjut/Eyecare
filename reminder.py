import tkinter as tkr
import time

class Reminder:
    def __init__(self):
        print('intitalizaing object')
        self.reminder = tkr.Tk()
        self.transparency = 1.0
        self.message = 'Reminder'
        self.LABEL = tkr.Label(self.reminder, text = self.message)

        self.reminder.wm_attributes("-alpha",self.transparency)
        self.LABEL.pack()
        self.reminder.overrideredirect(1)
        

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
        #useless

    def stop(self):
        print('destroying reminder')
        self.reminder.destroy()


    def change_transparency(self, new_transparency):
        print('changing transparency to',new_transparency)
        self.transparency = new_transparency
        self.reminder.wm_attributes("-alpha",self.transparency)

    def change_message(self, msg):
        print('çhanging message')
        self.message = msg
        self.LABEL.destroy()
        self.LABEL = tkr.Label(self.reminder, text = self.message)
        self.LABEL.pack()

reminder = Reminder()
reminder.update()
time.sleep(2)
reminder.change_transparency(0.5)
reminder.change_message('BKLALBALBALBLAAL')
reminder.update()
time.sleep(2)
reminder.stop()

#safe for later
#root.overrideredirect(1)
#root.lift()

