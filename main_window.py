import customtkinter as ctk

class MainWindow:

    def __init__(self, main_window):
        #create main application window
        self.main_window = main_window
        self.main_window.title("Grade Calculator")

        #window size
        window_width = 600
        window_height = 1000
        self.main_window.geometry(f"{window_width}x{window_height}")

        #Variables
        self.current_row = 1 #use to track current row
        self.category_count = 0
        self.max_category = 10

        #Track main cateogories
        self.categories = {}  # Dictionary to track main categories and their subcategories

        # Assignment category column
        label = ctk.CTkLabel(
            main_window, 
            text="Assignment Category", 
            fg_color="PeachPuff",
            font = ctk.CTkFont("Arial", 14),
            text_color="black")
        label.grid(row = 0, column = 0, padx=10, pady=10)

        # Add button to add category
        self.add_button = ctk.CTkButton(
            main_window,
            text="Add Major Category",
            command=self.add_major_category,
            font=ctk.CTkFont(size=12),
            hover_color="lightgreen",
            text_color="black",
            fg_color="gray")
        self.add_button.grid(row = 1, column = 0, padx=10, pady=10)

        # Warning label
        self.warning_label = ctk.CTkLabel(
            main_window,
            text="", 
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color="red",
        )

        """
        # Grade column
        label = ctk.CTkLabel(main_window, text="Grade", fg_color="PeachPuff", font = ctk.CTkFont("Arial", 14), text_color="black")
        label.grid(row = 0, column = 2, padx=50, pady=10)

        # Grade weight column
        label = ctk.CTkLabel(main_window, text="Weight", fg_color="PeachPuff", font = ctk.CTkFont("Arial", 14), text_color="black")
        label.grid(row = 0, column = 3, padx=50, pady=10)

        # Create user input box
        rows = 5 #default number of row

        #next step here: add entry to the list for category, grade, and weight
        assignment_category_entry_list = []
        grade_entry_list = []
        weight_entry_list = []


        for i in range(rows):
            # Assignment category input
            assignment_category_entry = ctk.CTkEntry(main_window, width=100)
            assignment_category_entry.grid(row=i + 1, column=1, padx=10, pady=5)
            #append to the list here

            # Assignment grade input
            grade_entry = ctk.CTkEntry(main_window, width = 50)
            grade_entry.grid(row = i + 1, column=2, padx=10, pady=5)
            #append to the list here

            # Assignment weight input
            weight_entry = ctk.CTkEntry(main_window, width = 50)
            weight_entry.grid(row = i + 1, column=3, padx=10, pady=5)
            #append to the list here
        """
    def add_major_category(self):
        """Adds a new major assignment category."""

        if self.category_count >= self.max_category: #check if the number of categry is below the limit 10
            self.show_error_popup("Max categories (10) reached!")
            return
        
         # Store the current row as the parent category row
        parent_row = self.current_row  # Save the current row before incrementing

        # Create a label for the category
        main_category_entry = ctk.CTkEntry(
            self.main_window,
            font=ctk.CTkFont(size=12, weight="bold"),
            text_color="black",
        )
        main_category_entry.grid(row=self.current_row, column=0, pady=5, padx=20)

        # Add button to allow adding subcategories
        add_sub_button = ctk.CTkButton(
            self.main_window,
            text="Add Subcategory",
            font=ctk.CTkFont(size=10),
            command=lambda row=parent_row: self.add_subcategory(row),
            fg_color="lightgray",
            text_color="black",
            hover_color="gray",
        )
        add_sub_button.grid(row=self.current_row, column=1, pady=5, padx=10)

        # Track this main category and update values
        self.categories[self.current_row] = {"entry": main_category_entry, "sub_row": parent_row + 1}
        # Increment row and category count
        self.current_row += 1
        self.category_count += 1

        # Move the "Add Major Category" button down
        self.add_button.grid(row=self.current_row, column=0, padx=10, pady=10)

    def add_subcategory(self, parent_category):
        """Adds a subcategory under the specified main category."""
        sub_row = self.categories[parent_category]["sub_row"]

        # Create subcategory entry
        sub_category_entry = ctk.CTkEntry(
            self.main_window,
            font=ctk.CTkFont(size=14),
            placeholder_text="Enter Subcategory",
        )
        sub_category_entry.grid(row=sub_row, column=0, pady=2, padx=0, sticky="E")

        # Update the next available row for this main category
        self.categories[parent_category]["sub_row"] += 1
        self.current_row = max(self.current_row, sub_row + 1)  # Adjust the row for other main categories

        # Move "Add Major Category" button down
        self.add_button.grid(row=self.current_row, column=0, padx=10, pady=10)

    def show_error_popup(self, message):
        """Show an error message in a popup window centered on the main window."""
        # Create the popup window
        popup = ctk.CTkToplevel(self.main_window)
        popup.title("Error")

        # Dimensions of the popup
        popup_width = 300
        popup_height = 150

        # Get the position of the main window
        main_window_x = self.main_window.winfo_x()
        main_window_y = self.main_window.winfo_y()
        main_window_width = self.main_window.winfo_width()
        main_window_height = self.main_window.winfo_height()

        # Calculate the center position for the popup
        popup_x = main_window_x + (main_window_width // 2) - (popup_width // 2)
        popup_y = main_window_y + (main_window_height // 2) - (popup_height // 2)

        # Set the popup geometry
        popup.geometry(f"{popup_width}x{popup_height}+{popup_x}+{popup_y}")

        # Add a label with the error message
        label = ctk.CTkLabel(
            popup,
            text=message,
            font=ctk.CTkFont(size=12),
            text_color="red",
            wraplength=250,  # Wrap text if it exceeds the width
        )
        label.pack(pady=20)

        # Add a button to close the popup
        close_button = ctk.CTkButton(
            popup,
            text="Close",
            command=popup.destroy,  # Close the popup when clicked
            font=ctk.CTkFont(size=12),
        )
        close_button.pack(pady=10)

        # Disable interaction with the main window until the popup is closed
        popup.grab_set()


    def quit_app(self):
        self.main_window.quit()