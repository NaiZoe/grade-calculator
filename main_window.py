import customtkinter as ctk

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
        label = ctk.CTkLabel(main_window, text="Assignment Category", 
            fg_color="PeachPuff",
            font = ctk.CTkFont("Arial", 14),
            text_color="black")
        label.grid(row = 0, column = 1, padx=10, pady=10)

        # Add button to add category
        add_button = ctk.CTkButton(
            main_window,
            text="Add Major Category",
            command=self.add_major_category,
            font=ctk.CTkFont(size=12),
            hover_color="lightgreen",
            text_color="black",
            fg_color="gray")
        add_button.grid(row = 1, column = 1, padx=10, pady=10)
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

        # Create a label for the category
        category_label = ctk.CTkLabel(
            self.main_window,
            text=category_name,
            font=ctk.CTkFont(size=12, weight="bold"),
            text_color="black",
        )
        category_label.grid(row=self.current_row, column=0, pady=5, sticky="w", padx=20)

        # Add button to allow adding sub-items under this category
        add_button = ctk.CTkButton(
            self.main_window,
            text="Add Sub-item",
            command=lambda: self.add_sub_item(category_name),
            font=ctk.CTkFont(size=10),
        )
        add_button.grid(row=self.current_row, column=1, pady=5)

        # Track the category and its first row
        self.categories[category_name] = {"row": self.current_row, "sub_items": []}
        self.current_row += 1  # Increment row for the next category or sub-item

    
    def quit_app(self):
        self.main_window.quit()