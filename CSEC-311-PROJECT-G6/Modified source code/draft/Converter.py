#Weight and Height Converter by Group 6

from tkinter import *
from tkinter import ttk
from collections import deque

class ConverterApp:
    def __init__(self, master):
        # OOP: Initialize the ConverterApp class
        self.master = master
        master.title("W&HC-GROUP6")
        self.recent_results = deque(maxlen=10)  # Keep track of the last 10 conversion results

        # Set up the GUI
        self.setup_gui()

    def setup_gui(self):
        # OOP: Window setup
        self.master.geometry("645x850")
        style = ttk.Style()
        style.configure("TLabel", font=("Arial", 10))
        style.configure("TButton", font=("Arial", 10), padding=(10, 5))
        style.configure("TFrame", background="#f0f0f0")

        # Create different sections of the GUI
        self.create_header()
        self.create_info_section()
        # OOP: Method for creating the converter section
        self.create_converter_section("Weight in kilogram(kg)", self.convert_weight, ["Gram(g)", "Pounds(lb)", "Ounce(oz)"])
        self.create_converter_section("Height in feet (ft)", self.convert_height, ["Centimeters(cm)", "Meters(m)", "Inches(in)"])
        self.create_footer()
        self.create_recent_results_button()

    def create_header(self):
        # OOP: Method for creating header label
        header_label = ttk.Label(
            self.master,
            text="Weight and Height Converter - GROUP 6",
            style="TLabel",
            font=("Helvetica", 16, "bold"),
            background="#3498db",
            foreground="white"
        )
        header_label.grid(row=0, column=0, columnspan=3, pady=10, sticky="ew")

    def create_info_section(self):   
        # OOP: Method for creating info section
        info_frame = ttk.Frame(padding="10", relief="groove", style="TFrame")
        info_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        app_info_label = ttk.Label(
            info_frame,
            text="Weight and Height Converter\n\n"
                "This app allows you to convert weights and heights between different units.\n\n"
                "Follow the steps below to use the converter:\n"
                "1. Enter the weight in kilograms and feet for height.\n"
                "2. Click the 'Convert' button to see the conversion results.\n"
                "3. Click the 'Clear' button to remove the current results.\n"
                "4. Recent conversion results can also be seen by clicking \n the 'View Recent Conversion Results' button.\n\n"
                "Accepted inputs:\n"
                "- Positive numeric values\n\n"
                "Not accepted inputs:\n"
                "- Negative values\n"
                "- Non-numeric values\n",
            style="TLabel",
            justify=LEFT
        )
        app_info_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

    def create_converter_section(self, label_text, convert_func, unit_labels):
        # OOP: Method for creating converter section for weight or height
        frame = ttk.Frame(self.master, padding="10", relief="groove", style="TFrame")
        frame.grid(row=self.master.grid_size()[1], column=0, padx=10, pady=10, sticky="nsew")

        label_prompt = ttk.Label(frame, text=f"Enter the {label_text.lower()}:", style="TLabel")
        entry_value = ttk.Entry(frame)
        button_convert = ttk.Button(frame, text="Convert", command=lambda: convert_func(entry_value, result_widgets, error_label), style="TButton")
        button_clear = ttk.Button(frame, text="Clear", command=lambda: self.clear_result_widgets(result_widgets), style="TButton")
        error_label = ttk.Label(frame, text="", foreground="red", style="TLabel")

        # Result Text widgets
        result_widgets = [Text(frame, height=1, width=20) for _ in unit_labels]

        # Grid layout for Converter Section
        label_prompt.grid(row=0, column=0, columnspan=2, pady=5, sticky="w")
        entry_value.grid(row=0, column=2, padx=5, pady=5)
        button_convert.grid(row=0, column=3, padx=5, pady=5)
        button_clear.grid(row=1, column=3, padx=5, pady=5)
        error_label.grid(row=3, column=0, columnspan=4, pady=5, sticky="w")

        # Units labels and result text widgets
        for i, unit_label in enumerate(unit_labels):
            ttk.Label(frame, text=unit_label, style="TLabel").grid(row=2, column=i)
            result_widgets[i].grid(row=1, column=i)

    def create_footer(self):
        # OOP: Method for creating footer label
        footer_label = ttk.Label(self.master, text="© 2023 W&HC-GROUP6.", style="TLabel", background="#f0f0f0", font=("Arial", 8))
        footer_label.grid(row=5, column=0, columnspan=3, pady=(10, 5), sticky="ew")

    def create_recent_results_button(self):
        # OOP: Method for creating button to view recent results
        button_view_results = ttk.Button(self.master, text="View Recent Conversion Results", command=self.view_recent_results, style="TButton")
        button_view_results.grid(row=4, column=0, columnspan=3, pady=10)

    def convert_weight(self, entry_value, result_widgets, error_label):
        # Input Validation: Check for non-negative numeric value
        self.convert(entry_value, result_widgets, error_label, "Weight(kg)", [1000, 2.20462, 35.274])

    def convert_height(self, entry_value, result_widgets, error_label):
        # Input Validation: Check for non-negative numeric value
        self.convert(entry_value, result_widgets, error_label, "Height(ft)", [30.48, 0.3048, 12])

    def convert(self, entry_value, result_widgets, error_label, label_text, conversion_factors):
        # Input validation, error handling, and actual conversion logic
        try:
            value_str = entry_value.get().strip()
            assert value_str, "Enter a number to convert."

            value = float(value_str)
            assert value >= 0, f"{label_text} cannot be negative."

            results = [value * factor for factor in conversion_factors]

            for widget, val in zip(result_widgets, results):
                self.update_result_widgets(widget, val)

            result_str = f"{label_text}: {value:.2f}\n"

            # Define units for each type of conversion
            unit_labels = ["", "Centimeters(cm)", "Meters(m)", "Inches(in)"] if "Height" in label_text else ["", "Gram(g)", "Pounds(lb)", "Ounce(oz)"]

            # Create a list of formatted strings for each unit and result
            formatted_results = [f"{unit:<15}: {res:.2f}" for res, unit in zip(results, unit_labels[1:])]
            # Modify the format of the result_str concatenation
            result_str += "\n".join(formatted_results)
            result_str += "\n" + "=" * 30  # Line separator
            self.recent_results.append(result_str)

        except ValueError as error:
            # Error Exception: Handle ValueError during conversion
            self.show_error_message(error, error_label)
        except AssertionError as error:
            # Assert: Handle AssertionError for input validation
            self.show_error_message(error, error_label)

    def update_result_widgets(self, result_widget, value):
        # Output Encoding: Update the result widgets with the calculated values
        result_widget.delete("1.0", END)
        result_widget.insert(END, f"{value:.2f}")

    def clear_error_message(self, error_label):
        # Clear the error message label
        error_label.config(text="")

    def clear_result_widgets(self, result_widgets):
        # Clear the result widgets
        for widget in result_widgets:
            widget.delete("1.0", END)

    def show_error_message(self, error, error_label):
        # Error Handling: Display error message
        error_label.config(text=f"Error: {error}")

    def view_recent_results(self):
        # Decorators: Display the recent conversion results in a new window
        recent_results_window = Toplevel(self.master)
        recent_results_window.title("Recent Conversion Results")

        results_text = Text(recent_results_window, height=30, width=30)
        results_text.pack(padx=10, pady=10)

        for result in reversed(self.recent_results):
            results_text.insert(END, result + "\n")

if __name__ == "__main__":
    # OOP: Create the Tkinter root window and run the application
    root = Tk()
    app = ConverterApp(root)
    root.mainloop()
