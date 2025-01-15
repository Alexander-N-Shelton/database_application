#!/usr/bin/env python
# main.py
"""
Author          :   Alexander Shelton
Date            :   October 2024
Name            :   Database Application
Description     :   An application for users to view data from a database based on their permissions.    
"""
import tkinter as tk
from presentation_layer import LoginScreen

def main():
    """
    The main function to initialize and run the login screen for the application.
    """
    root = tk.Tk()
    app = LoginScreen(root)
    root.mainloop()

if __name__ == "__main__":
    main()