import tkinter as tk
from main_window import MainWindow

class WelcomeWindow:

    def __init__(self, window):
        self.window = window
        self.window.title("Grade Calculator")
        self.window.geometry("400x300")

         # Welcome message
        label = tk.Label(window, text="Welcome to the Grade Calculator!", font=("Arial", 16), pady=20)
        label.pack(expand=True, anchor="center")

        # Button to proceed to the main application
        start_button = tk.Button(window, text="Start", font=("Arial", 14), command=self.open_main_window)
        start_button.pack(pady=(0, 50))

        #add footer
        footer_label = tk.Label(window, text="Designed and Developed by Qitao Yang", font=("Arial", 10), fg="gray")
        footer_label.pack(side="bottom", pady=10)

    def open_main_window(self):
        """Closes the welcome window and opens the main application."""
        # Close the welcome window
        self.window.destroy() 
        
        # Open the main application window
        main_window = tk.Tk()
        MainWindow(main_window)
        main_window.mainloop()

# Run the Welcome Window
if __name__ == "__main__":
    window = tk.Tk()
    WelcomeWindow(window)
    window.mainloop()