# styles.py
# ----- Imports ----- #
import tkinter as tk
from tkinter import ttk

# ----- AppStyles Class ----- #
class AppStyles(ttk.Style):
    """
    Configures custom styles for the application's Tkinter widgets.

    This class inherits from ttk.Style and sets the visual appearance for labels, 
    buttons, and tree views used throughout the application. It applies colors, 
    fonts, padding, and other visual properties.
    """
    def __init__(self):
        """
        Initializes the AppStyles class and applies custom styling.

        Configures the following widget styles:
        - 'TLabel': A label with a dark blue background and orange text, centered, with padding and raised relief.
        - 'Treeview': A table-style widget with orange background and dark blue text, using a 'groove' relief.
        - 'Treeview.Heading': A bold heading with dark blue background and orange text.
        - 'AppButton.TButton': A button style with specific foreground, background, and font changes on hover.
        """
        super().__init__()

        self.theme_use('clam')

        # Configuring label style
        self.configure(
            'TLabel', 
            background='dark blue', 
            foreground='orange', 
            font=('Roman', 16), 
            relief='raised', 
            padding=5, 
            border=5, 
            justify='center'
        )

        # Configuring treeview style
        self.configure('Treeview', bd=5, background='orange', foreground='dark blue', font=('Arial', 12), relief='groove')
        self.configure('Treeview.Heading', font=('Times', 15, 'bold'), background='dark blue', foreground='orange')

        # Configuring button style with hover effects
        self.configure('AppButton.TButton', relief='raised')
        self.map('AppButton.TButton', 
                 background=[('active', 'dark blue'), 
                             ('!disabled', 'orange')], 
                 foreground=[('active', 'orange'), 
                             ('!disabled', '#002060')], 
                 bordercolor=[('active', 'orange'), 
                              ['!disabled', '#002060']], 
                 font=[('active', 'courier 14 italic'), 
                       ('!disabled', 'courier 14 bold')])
