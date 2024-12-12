import customtkinter as ctk
from main_window import MainWindow

class WelcomeWindow:

    def __init__(self, window):

        # Options: "light", "dark", "system"
        ctk.set_appearance_mode("light") 
        # Options: "blue", "green", "dark-blue"
        ctk.set_default_color_theme("green")

        self.window = window
        self.window.title("Grade Calculator")
        self.window.geometry("400x300")

         # Welcome message
        label = ctk.CTkLabel(window, text="Welcome to the Grade Calculator!", font = ctk.CTkFont("Arial", 16), pady=20)
        label.pack(expand=True, anchor="center")

        # Button to proceed to the main application
        start_button = ctk.CTkButton(window, text="Start", font = ctk.CTkFont("Arial", 14), command=self.open_main_window)
        start_button.pack(pady=(0, 50))

        #add footer
        footer_label = ctk.CTkLabel(window, text="Designed and Developed by Qitao Yang", font = ctk.CTkFont("Arial", 10), text_color="gray")
        footer_label.pack(side="bottom", pady=10)

    def open_main_window(self):
        """Closes the welcome window and opens the main application."""
        # Close the welcome window
        self.window.withdraw() 
        
        # Open the main application window
        main_window = ctk.CTk()
        MainWindow(main_window)
        main_window.mainloop()

