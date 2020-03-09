import tkinter as tkr
import time

#WIDGET NAMES ARE DECLARED WITH CAPITAL LETTERS

class Interface:
    def __init__(self):
        print('initializing interface object')
        self.interface = tkr.Tk()
        self.time_between_reminders = 60*60
        self.reminder_time_on_screen = 5
        self.transparency = 0.5
        self.message = 'Give you eyes some rest'
        self.set_up_widgets()
        self.interface.mainloop()


    def on_click_message(self, new_msg):
        self.change_message(new_msg)
        #zapishi v baza danni
        self.destroy_widgets()
        self.set_up_widgets()
        self.interface.update()
        
    def on_click_time_between_reminders(self, new_time_between_reminders):
        self.change_time_between_reminders(int(new_time_between_reminders))
        #zapishi v baza danni
        self.destroy_widgets()
        self.set_up_widgets()
        self.interface.update()
            
    def on_click_reminder_time_on_screen(self, new_reminder_time_on_screen):
        self.change_reminder_time_on_screen(int(new_reminder_time_on_screen))
        #zapishi v baza danni
        self.destroy_widgets()
        self.set_up_widgets()
        self.interface.update()
            
    def on_click_transparency(self, new_transparency):
        self.change_transparency(float(new_transparency))
        #zapishi v baza danni
        self.destroy_widgets()
        self.set_up_widgets()
        self.interface.update()
        
    
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

        
        self.CLOSE_BUTTON.grid(row=5,column=0)

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


    def exit_main_loop(self):
        print('exiting main loop')
        self.interface.quit()

    def destroy(self):
        print('destroying interface object')
        self.interface.destroy()

    def change_transparency(self, new_transparency):
        self.transparency = new_transparency

    def change_time_between_reminders(self, new_time_between_reminders):
        self.time_between_reminders = new_time_between_reminders

    def change_reminder_time_on_screen(self, new_reminder_time_on_screen):
        self.reminder_time_on_screen = new_reminder_time_on_screen

    def change_message(self, new_message):
        self.message = new_message


    def write_settings_to_database():
        #she se zapisva v database vsichki nastroiki v taq funkciq
        pass

interface = Interface()
interface.destroy()

