import tkinter as tk

class MainWindow:

    def __init__(self, main_window):
        #create main application window
        self.main_window = main_window
        self.main_window.title("Grade Calculator")
        #window size
        window_width = 550
        window_height = 550
        self.main_window.geometry(f"{window_width}x{window_height}")

        # Assignment category column
        label = tk.Label(main_window, text="Assignment category", bg="PeachPuff", font=("Arial", 14))
        label.grid(row = 0, column = 1, padx=10, pady=10)

        # Grade column
        label = tk.Label(main_window, text="Grade", bg="PeachPuff", font=("Arial", 14))
        label.grid(row = 0, column = 2, padx=50, pady=10)

        # Grade weight column
        label = tk.Label(main_window, text="Weight", bg="PeachPuff", font=("Arial", 14))
        label.grid(row = 0, column = 3, padx=50, pady=10)

        # Create user input box
        rows = 5 #default number of row

        #next step here: add entry to the list for category, grade, and weight
        assignment_category_entry_list = []
        grade_entry_list = []
        weight_entry_list = []


        for i in range(rows):
            # Assignment category input
            assignment_category_entry = tk.Entry(main_window, width=15)
            assignment_category_entry.grid(row=i + 1, column=1, padx=10, pady=5)
            #append to the list here

            # Assignment grade input
            grade_entry = tk.Entry(main_window, width = 15)
            grade_entry.grid(row = i + 1, column=2, padx=10, pady=5)
            #append to the list here

            # Assignment weight input
            weight_entry = tk.Entry(main_window, width = 15)
            weight_entry.grid(row = i + 1, column=3, padx=10, pady=5)
            #append to the list here
        