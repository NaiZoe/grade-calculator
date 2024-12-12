import customtkinter as ctk
from main_window import MainWindow
from welcome_window import WelcomeWindow

# Run the Welcome Window
if __name__ == "__main__":

    app = ctk.CTk()
    WelcomeWindow(app)
    app.mainloop()