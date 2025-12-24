# This file is used to build the user interface of the application

import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk
from modules.ui_elements import SecureSendUI



# SecureSendGUI is a sub class of Gtk.Application.
class SecureSendGUI(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="com.aswin.securesend")


#do_activate() is a special method of Gtk.Application. GTK calls it automatically when you run the application with app.run().


# Note: why we are adding 'self'
# 1. Python automatically passes the instance (app) as the first argument to methods.
# 2. By convention, we name this first argument self.
# 3. You always need it in instance methods if you want to access attributes or other methods of the same object.



    def do_activate(self):

        # Set the Application Window properties

        # we are setting the property window to the object
        self.window = Gtk.ApplicationWindow(application=self)

        # we are setting the property 'window.set_title' to the object
        self.window.set_title("SecureSend")

        # we are setting the property 'window.set_default_size' to the object
        self.window.set_default_size(1000, 700)

        # Prevents the user from resizing the window. Its optional. I like to have a fixed window size.
        self.window.set_resizable(False)


        #SecureSendUI: This is a method created in another file: check modules/ui.py
        #You are creating an instance of that class and passing self.window to it. This tells SecureSendUI which window to attach its widgets to.
        self.ui = SecureSendUI(self.window)  
        self.ui.build_layout() 

        # Shows the rendered window on the screen
        self.window.present()



# Creates an instance of your app.
app = SecureSendGUI()
#Run the app
app.run()



# Our main entry file : app.py ended.

'''
1. The next implementation is in : ui_elements.py 
2. There we created a class called SecureSendUI and a method called def build_layout(self): 
3. def build_layout(self): This method will create all the UI elements such as buttons, labels boxed etc.

'''