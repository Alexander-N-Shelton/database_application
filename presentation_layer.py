#!/usr/bin/env python
# presentation_layer.py
"""
Author          :   Alexander Shelton
Date            :   October 2024
Name            :   Database Application
Description     :   An application for users to view data from a database based on their permissions.    
"""
# ----- Imports ----- # 
import tkinter as tk
from tkinter import ttk, messagebox
from business_layer import BusinessLayer
from styles import AppStyles
# ----- Login Screen ----- #
class LoginScreen:
    """
    Represents the login screen for the application. Manages user login and transitions
    to the main application upon successful login.

    Attributes:
        root : (tk.Tk)
            The root Tkinter window for the login screen.
        username_entry : (ttk.Entry)
            Entry widget for entering the username.
        password_entry : (ttk.Entry)
            Entry widget for entering the password.
        business_layer : (BusinessLayer)
            An instance of the BusinessLayer class for database interaction.
    """
    def __init__(self, root):
        """
        Initializes the LoginScreen class, setting up the GUI layout for the login screen.

        Parameters:
            root : (tk.Tk)
                The root Tkinter window.
        """
        self.root = root

        # Set the title for login page
        self.root.title('Login')

        # Set the window Geometry
        self.root.geometry('500x500')

        # Set the background color
        self.root.configure(bg='dark blue')
        
        # Bring the configured styles
        self.style = AppStyles()

        # Padding 
        padding = {'padx': 10, 'pady': 10}
        
        # Entry Fonts
        entry_font = {'font': ('Courier', 14), 'foreground': 'maroon'}
        

        ttk.Label(root, text="Username:", style='TLabel').pack(**padding)
        self.username_entry = ttk.Entry(root, **entry_font)
        self.username_entry.pack(**padding)

        ttk.Label(root, text="Password:", style='TLabel').pack(**padding)
        self.password_entry = ttk.Entry(root, **entry_font, show="*")
        self.password_entry.pack(**padding)

        ttk.Button(root, text="Login", style='AppButton.TButton', command=self.login).pack(side='bottom', anchor='s', **padding)

    def login(self):
        """
        Authenticates the user by checking credentials entered in the login form.
        Opens the main application if login is successful, else displays an error.
        """
        user = self.username_entry.get()        # Get username entered by user
        password = self.password_entry.get()    # Get Password entered by user

        if not user and password:               # Gives an error message if both aren't filled out
            messagebox.showerror('Error', 'All fields are required.')

        try:
            self.business_layer = BusinessLayer(user=user, password=password)   # connect to db using BusinessLayer

            messagebox.showinfo('Success', f'You are logged in as {user}.')
            self.open_main_app()

        except Exception as e:
            messagebox.showerror("Login Failed", f"Login failed: {e}")

    def open_main_app(self):
        """
        Opens the main application window after a successful login and closes the
        current login window.
        """
        self.root.destroy()                                 # Destroy the current window 

        root = tk.Tk()                                      # Initiate a new one 
        main_app = Application(root, self.business_layer)
        root.mainloop()                                     # Let her rip
# ---- Application ----- #
class Application:
    """
    Represents the main application interface after login. Allows users to view
    and interact with data from the database.

    Attributes:
        root : (tk.Tk)
            The root Tkinter window for the main application.
        business_layer : (BusinessLayer)
            An instance of the BusinessLayer class for database interaction.
        tree : (ttk.Treeview)
            A tree view widget for displaying data in table format.
        paddings : (dict)
            Padding configuration for widgets.
    """
    def __init__(self, root, business_layer):
        """
        Initializes the Application class, setting up the GUI layout and data display.

        Parameters:
            root : (tk.Tk)
                The root Tkinter window.
            business_layer : (BusinessLayer)
                An instance of the BusinessLayer class for database interaction.
        """
        self.root = root

        # Set Title
        self.root.title('Main Application')

        # Set background
        self.root.configure(bg='dark blue')
        
        # Set size 
        self.root.geometry('1200x900')
        
        # Call business layer
        self.business_layer = business_layer
        
        # Bring in the configured styles
        AppStyles()

        # Paddings
        self.paddings = {'padx': 5, 'pady': 5}


        # Create the different buttons based on what each user has the permissions to do
        if 'in450a' in self.business_layer.user:      # in450a has permission to view all three tables, so all options are shown
            ttk.Button(root, text="Show IN450a Row Count", style='AppButton.TButton', command=self.show_in450a_row_count).pack(**self.paddings)
            ttk.Button(root, text="Show IN450b Names", style='AppButton.TButton', command=self.show_in450b_names).pack(**self.paddings)
            ttk.Button(root, text='Show IN450c Count', style='AppButton.TButton', command=self.show_in450c_row_count).pack(**self.paddings)

            ttk.Button(root, text='Show All Data for in450a', style='AppButton.TButton', command=self.show_in450a_data).pack(**self.paddings)
            ttk.Button(root, text='Show All Data for in450b', style='AppButton.TButton', command=self.show_in450b_data).pack(**self.paddings)
            ttk.Button(root, text='Show All Data for in450c', style='AppButton.TButton', command=self.show_in450c_data).pack(**self.paddings)
        
        # in450b only has permission to see the in450b table, so that is the only option shown.
        elif 'in450b' in self.business_layer.user: 
            ttk.Button(root, text='Show IN450b Names', style='AppButton.TButton', command=self.show_in450b_names).pack(**self.paddings)
            ttk.Button(root, text='Show All Data for in450b', style='AppButton.TButton', command=self.show_in450b_data).pack(**self.paddings)
        
        # in450c only has permission to see the in450c table, so that is the only option shown.
        elif 'in450c' in self.business_layer.user:
            ttk.Button(root, text='Show IN450c Count', style='AppButton.TButton', command=self.show_in450c_row_count).pack(**self.paddings)
            ttk.Button(root, text='Show All Data for in450c', style='AppButton.TButton', command=self.show_in450c_data).pack(**self.paddings)


        # Create a tkinter Treeview object for viewing the data in a table format.
        self.tree = ttk.Treeview(root, selectmode='browse')
        self.tree['show'] = 'headings'                              # Get rid of the annoying empty column 
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Create a scrollbar for the Treeview even though one isn't necessary
        self.tree_scrollbar = ttk.Scrollbar(self.tree, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.config(yscrollcommand=self.tree_scrollbar.set)
        self.tree_scrollbar.pack(side='right', anchor='e')

        self.tree.bind('<<TreeviewSelect>>', self.action)

    def show_in450a_row_count(self):
        """
        Fetches and displays the row count from the 'in450a' table in a message box.
        """
        try:
            row_count = self.business_layer.get_in450a_row_count()
            messagebox.showinfo("IN450a Row Count", f"Row count: {row_count}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to get row count: {e}")
    
    def show_in450b_names(self):
        """
        Fetches and displays the names (first and last) from the 'in450b' table in the Treeview.
        """
        try:
            names = self.business_layer.get_in450b_names()
            self.display_data(names, ['First Name', 'Last Name'])

        except Exception as e:
            messagebox.showerror("Error", f"Failed to get names: {e}")
            
    def show_in450c_row_count(self):
        """
        Fetches and displays the row count from the 'in450c' table in a message box.
        """
        try:
            row_count = self.business_layer.get_in450c_row_count()
            messagebox.showinfo('IN450c Row Count', f'Row count: {row_count}')
        except Exception as ex:
            messagebox.showerror('Error', f'Failed to get namees: {ex}')
            
    def show_in450a_data(self):
        """
        Fetches and displays all data from the 'in450a' table in the Treeview.
        """
        data = self.business_layer.get_in450a_data()
        self.display_data(data, ['Time', 'Source', 'Destination', 'Protocol', 'Length', 'Info']) 

    def show_in450b_data(self):
        """
        Fetches and displays all data from the 'in450b' table in the Treeview.
        """
        data = self.business_layer.get_in450b_data()
        self.display_data(data, ['First Name', 'Last Name', 'Email', 'Source IP', 'Destination IP'])

    def show_in450c_data(self):
        """
        Fetches and displays all data from the 'in450c' table in the Treeview.
        """
        data = self.business_layer.get_in450c_data()
        self.display_data(data, ['App ID', 'App Name', 'App Version', 'Source IP', 'Destination IP', 'DigSig'])

    def display_data(self, data, columns):
        """
        Configures the Treeview to display the specified columns and populates it with data.

        Parameters:
            data : (list of tuple)
                The data to display in the Treeview.
            columns : (list of str)
                The column names to display as headers.
        """
        # Clear the Treeview
        self.tree.delete(*self.tree.get_children())

        # Set up columns and headers
        self.tree["columns"] = columns
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor=tk.W)

        # Insert data into Treeview
        for row in data:
            self.tree.insert('', tk.END, values=row)
            
    def action(self, event):
        """
        Displays information about the selected row in the Treeview when a row is clicked.

        Parameters:
        ----------
        event : tk.Event
            The event object from the Treeview row click.
        """
        focus = self.tree.focus()
        x = self.tree.item(focus).get('values')
        messagebox.showinfo('Info', message='\n'.join(x))

    def on_closing(self):
        """
        Closes the database connection and the main application window.
        """
        if self.business_layer:
            self.business_layer.close_connection()
        self.destroy()
