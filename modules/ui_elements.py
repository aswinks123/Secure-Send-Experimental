import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk



# Here we are creating a new class

# Why this class: ?
'''
1. We are passing the window property that we createdin app.py's SecureSendGUI class.
2. So that out UI the the window property can be accessed in the UI_elements.py's build_layout  method.
3. build_layout method created the controls/elemets and attach it to the self.window.
4. Without creating a new class, the window property we created in app.py's SecureSendGUI class's build_layout  method cannot be accesses in ui_elements file

'''
class SecureSendUI:

    #This is the constructor. It runs automatically when you create an object of this class.
    # window is the paramenter we pass from app.py, It is the main application window where all UI elements will appear.
    def __init__(self, window):
        self.window = window  #This stores the window inside the object so other parts of the class can access it.
        self.files = [] #This creates an empty list to store files that the user will select later.


    def build_layout(self):  # function that created the UI elements


        # Creates a horizontal box (hbox) that will hold all UI elements. We attach all elemets in this box.
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=20)
        hbox.set_margin_top(15)
        hbox.set_margin_bottom(15)
        hbox.set_margin_start(15)
        hbox.set_margin_end(15)
        #puts this box inside the main window. (self.window)
        self.window.set_child(hbox)

    # Now the box is created on the window - Perfect!



    #----------Left Side Controls----------------

    # Inside the box that we created, we are now going to create a grid. This grid hold left side controls
    # On left side of the box (left grid), we are planning to place some controls such as labels, buttons etc.

    #1. create the left grid
        left_grid = Gtk.Grid(column_spacing=10, row_spacing=20)
    #2. Attach this grid to our already created box.
        hbox.append(left_grid) 
    
    #3. Now add elements one by one.

        #Add label for server-IP
        left_grid.attach(Gtk.Label(label="Server IP:"), 0, 0, 1, 1) #iputs label in column 0, row 0, spanning 1 column and 1 row.
        #Add entry box to type the user input
        self.ip_entry = Gtk.Entry() #create a text input box for the user to type the server IP."self.ip_entry " stores as an object feature so that we can read its value later.
        left_grid.attach(self.ip_entry, 1, 0, 1, 1) #attach to grids column 1, row 0 ; ie, straight to serverIP label.

    # Similarly add all required controls:

        #Add username field
        left_grid.attach(Gtk.Label(label="Username:"), 0, 1, 1, 1)
        self.user_entry = Gtk.Entry()
        left_grid.attach(self.user_entry, 1, 1, 1, 1)

        # Authentication Type to choose password or passwordless
        left_grid.attach(Gtk.Label(label="Auth Type:"), 0, 2, 1, 1)
        self.auth_type_combo = Gtk.ComboBoxText()
        self.auth_type_combo.append_text("Password")
        self.auth_type_combo.append_text("Private Key")
        self.auth_type_combo.set_active(0)  # default: Password
        left_grid.attach(self.auth_type_combo, 1, 2, 1, 1)

        #Add password field   
        left_grid.attach(Gtk.Label(label="Password:"), 0, 3, 1, 1)
        self.pass_entry = Gtk.Entry()
        self.pass_entry.set_visibility(False) #hides the text while typing
        left_grid.attach(self.pass_entry, 1, 3, 1, 1)


        # To input the destination path to sent files
        left_grid.attach(Gtk.Label(label="Destination Path:"), 0, 4, 1, 1)
        self.destination_entry = Gtk.Entry()
        self.destination_entry.set_text("/tmp/")  # Set default path
        left_grid.attach(self.destination_entry, 1, 4, 1, 1)

        #Add Send button
        self.send_btn = Gtk.Button(label="Send") #Creates a button labeled “Send".
        left_grid.attach(self.send_btn, 0, 5, 2, 1)# Placed in row 3, spanning 2 columns, so it’s centered under the entries.

        #Adding Clear button
        self.clear_btn = Gtk.Button(label="Clear") #Creates a button labeled “Clear”.
        left_grid.attach(self.clear_btn, 0, 6, 2, 1)# Placed in row 3, spanning 2 columns, so it’s centered under the entries.

