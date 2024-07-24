from tkinter import *
from tkinter import ttk
from collections import deque


# Global variables to store recent conversion results
recent_results = deque(maxlen=10)  # Keep the last 10 results

def convert_weight(entry_weight_kg, result_text_gram, result_text_pound, result_text_ounce, error_label_weight):
    try:
        kg_value_str = entry_weight_kg.get().strip()
        assert kg_value_str, "Enter a number to convert."

        kg_value = float(kg_value_str)
        assert kg_value >= 0, "Weight cannot be negative."

        gram = kg_value * 1000
        pound = kg_value * 2.20462
        ounce = kg_value * 35.274

        update_text_widgets(result_text_gram, gram)
        update_text_widgets(result_text_pound, pound)
        update_text_widgets(result_text_ounce, ounce)
        clear_error_message(error_label_weight)

        # Save the result to recent results
        result_str = f"Weight: {kg_value:.2f} kg, {gram:.2f} gram, {pound:.2f} pounds, {ounce:.2f} ounce"
        recent_results.append(result_str)

    except ValueError as error:
        show_error_message(error, error_label_weight)
    except AssertionError as error:
        show_error_message(error, error_label_weight)

def convert_height(entry_height_feet, result_text_cm, result_text_meters, result_text_inches, error_label_height):
    try:
        feet_value_str = entry_height_feet.get().strip()
        assert feet_value_str, "Enter a number to convert."

        feet_value = float(feet_value_str)
        assert feet_value >= 0, "Height cannot be negative."

        cm = feet_value * 30.48
        meters = feet_value * 0.3048
        inches = feet_value * 12

        update_text_widgets(result_text_cm, cm)
        update_text_widgets(result_text_meters, meters)
        update_text_widgets(result_text_inches, inches)
        clear_error_message(error_label_height)

        # Save the result to recent results
        result_str = f"Height: {feet_value:.2f} feet, {cm:.2f} cm, {meters:.2f} meters, {inches:.2f} inches"
        recent_results.append(result_str)

    except ValueError as error:
        show_error_message(error, error_label_height)
    except AssertionError as error:
        show_error_message(error, error_label_height)

def view_recent_results():
    # Create a new window to display recent results
    recent_results_window = Toplevel()
    recent_results_window.title("Recent Conversion Results")

    results_text = Text(recent_results_window, height=10, width=60)
    results_text.pack(padx=10, pady=10)

    # Display recent results in the new window
    for result in reversed(recent_results):
        results_text.insert(END, result + "\n")

def update_text_widgets(widget, value):
    widget.delete("1.0", END)
    widget.insert(END, f"{value:.2f}")

def show_error_message(error, error_label):
    error_label.config(text=f"Error: {error}")

def clear_error_message(error_label):
    error_label.config(text="")

def clear_result_text_widgets(*widgets):
    for widget in widgets:
        widget.delete("1.0", END)

def create_gui():
    window = Tk()
    window.title("W&HC-GROUP6")

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window_width = 645
    window_height = 850
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2
    window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    style = ttk.Style()
    style.configure("TLabel", font=("Arial", 10))
    style.configure("TButton", font=("Arial", 10), padding=(10, 5))
    style.configure("TFrame", background="#f0f0f0")

    # Header
    header_label = ttk.Label(
        window, 
        text="Weight and Height Converter - GROUP 6", 
        style="TLabel",
        font=("Helvetica", 16, "bold"),
        background="#3498db",
        foreground="white"
    )
    header_label.grid(row=0, column=0, columnspan=3, pady=10, sticky="ew")

    # Add a section for app information and instructions
    info_frame = ttk.Frame(window, padding="10", relief="groove", style="TFrame")
    info_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

    app_info_label = ttk.Label(
        info_frame,
        text="Weight and Height Converter\n\n"
             "This app allows you to convert weights and heights between different units.\n\n"
             "Follow the steps below to use the converter:\n"
             "1. Enter the weight in kilograms and feet for height.\n"
             "2. Click the 'Convert' button to see the conversion results.\n"
             "3. Click the 'Clear' button to remove the current results.\n"
             "4. Recent converstion results can also be seen by clicking \n the 'View Recent Conversion Results' button.\n\n"
             "Accepted inputs:\n"
             "- Positive numeric values\n\n"
             "Not accepted inputs:\n"
             "- Negative values\n"
             "- Non-numeric values\n",
        style="TLabel",
        justify=LEFT
    )
    app_info_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

    # Weight Converter UI Elements
    weight_frame = ttk.Frame(window, padding="10", relief="groove", style="TFrame")
    weight_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

    label_weight_prompt = ttk.Label(weight_frame, text="Enter the weight in kilograms (kg):", style="TLabel")
    entry_weight_kg = ttk.Entry(weight_frame)
    button_convert_weight = ttk.Button(weight_frame, text="Convert", command=lambda: convert_weight(entry_weight_kg, result_text_gram, result_text_pound, result_text_ounce, error_label_weight), style="TButton")
    button_clear_weight = ttk.Button(weight_frame, text="Clear", command=lambda: clear_result_text_widgets(result_text_gram, result_text_pound, result_text_ounce), style="TButton")
    error_label_weight = ttk.Label(weight_frame, text="", foreground="red", style="TLabel")

    # Labels for result units
    label_gram = ttk.Label(weight_frame, text='Gram', style="TLabel")
    label_pound = ttk.Label(weight_frame, text='Pounds', style="TLabel")
    label_ounce = ttk.Label(weight_frame, text='Ounce', style="TLabel")

    # Result Text widgets
    result_text_gram = Text(weight_frame, height=1, width=20)
    result_text_pound = Text(weight_frame, height=1, width=20)
    result_text_ounce = Text(weight_frame, height=1, width=20)

    # Grid layout for Weight Converter
    label_weight_prompt.grid(row=0, column=0, columnspan=2, pady=5, sticky="w")
    entry_weight_kg.grid(row=0, column=2, padx=5, pady=5)
    button_convert_weight.grid(row=0, column=3, padx=5, pady=5)
    button_clear_weight.grid(row=1, column=3, padx=5, pady=5)
    error_label_weight.grid(row=3, column=0, columnspan=4, pady=5, sticky="w")

    # Units labels and result text widgets
    label_gram.grid(row=2, column=0)
    label_pound.grid(row=2, column=1)
    label_ounce.grid(row=2, column=2)
    result_text_gram.grid(row=1, column=0)
    result_text_pound.grid(row=1, column=1)
    result_text_ounce.grid(row=1, column=2)

    # Height Converter UI Elements
    height_frame = ttk.Frame(window, padding="10", relief="groove", style="TFrame")
    height_frame.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

    label_height_prompt = ttk.Label(height_frame, text="Enter the height in feet (ft):", style="TLabel")
    entry_height_feet = ttk.Entry(height_frame)
    button_convert_height = ttk.Button(height_frame, text="Convert", command=lambda: convert_height(entry_height_feet, result_text_cm, result_text_meters, result_text_inches, error_label_height), style="TButton")
    button_clear_height = ttk.Button(height_frame, text="Clear", command=lambda: clear_result_text_widgets(result_text_cm, result_text_meters, result_text_inches), style="TButton")
    error_label_height = ttk.Label(height_frame, text="", foreground="red", style="TLabel")

    # Labels for result units
    label_cm = ttk.Label(height_frame, text='Centimeters', style="TLabel")
    label_meters = ttk.Label(height_frame, text='Meters', style="TLabel")
    label_inches = ttk.Label(height_frame, text='Inches', style="TLabel")

    # Result Text widgets
    result_text_cm = Text(height_frame, height=1, width=20)
    result_text_meters = Text(height_frame, height=1, width=20)
    result_text_inches = Text(height_frame, height=1, width=20)

    # Grid layout for Height Converter
    label_height_prompt.grid(row=0, column=0, columnspan=2, pady=5, sticky="w")
    entry_height_feet.grid(row=0, column=2, padx=5, pady=5)
    button_convert_height.grid(row=0, column=3, padx=5, pady=5)
    button_clear_height.grid(row=1, column=3, padx=5, pady=5)
    error_label_height.grid(row=3, column=0, columnspan=4, pady=5, sticky="w")

    # Units labels and result text widgets
    label_cm.grid(row=2, column=0)
    label_meters.grid(row=2, column=1)
    label_inches.grid(row=2, column=2)
    result_text_cm.grid(row=1, column=0)
    result_text_meters.grid(row=1, column=1)
    result_text_inches.grid(row=1, column=2)

    # Add a footer label
    footer_label = ttk.Label(window, text="© 2023 W&HC-GROUP6.", style="TLabel", background="#f0f0f0", font=("Arial", 8))
    footer_label.grid(row=5, column=0, columnspan=3, pady=(10, 5), sticky="ew")

    # Add a button to view recent conversion results
    button_view_results = ttk.Button(window, text="View Recent Conversion Results", command=view_recent_results, style="TButton")
    button_view_results.grid(row=4, column=0, columnspan=3, pady=10)

    # Improve window resizable behavior
    window.resizable(False, False)

    return window, entry_weight_kg, entry_height_feet

if __name__ == "__main__":
    main_window, entry_weight_kg, entry_height_feet = create_gui()
    main_window.mainloop()
