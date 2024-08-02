import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import os
from PIL import Image, ImageTk
from signature import match

# Match Threshold
THRESHOLD = 70

def browse_image(ent, img_label):
    filename = askopenfilename(filetypes=[("Image Files", "*.jpeg *.jpg *.png")])
    if filename:
        ent.delete(0, tk.END)
        ent.insert(tk.END, filename)
        display_image(filename, img_label)

def remove_image(ent, img_label):
    ent.delete(0, tk.END)
    img_label.config(image=None)
    img_label.image = None

def display_image(filename, img_label):
    image = Image.open(filename)
    image = image.resize((300, 200), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    img_label.config(image=photo)
    img_label.image = photo

def verify_signatures(ent1, ent2, result_label):
    path1 = ent1.get()
    path2 = ent2.get()
    if not path1 or not path2:
        messagebox.showerror("Error", "Please select both images.")
        return
    
    result = match(path1=path1, path2=path2)
    
    if result <= THRESHOLD:
        result_label.config(text=f"Similarity: {result:.2f}%\nStatus: Forged", foreground="red")
    else:
        result_label.config(text=f"Similarity: {result:.2f}%\nStatus: Authentic", foreground="green")

def remove_directory(path):
    if os.path.exists(path):
        if os.path.isdir(path):
            for root, dirs, files in os.walk(path, topdown=False):
                for name in files:
                    os.remove(os.path.join(root, name))
                for name in dirs:
                    os.rmdir(os.path.join(root, name))
            os.rmdir(path)

def clear_result(result_label):
    result_label.config(text="")

# Create the main window
root = tk.Tk()
root.title("Handwritten Signature Verification")


# Header Frame
header_frame = tk.Frame(root, bg="#35477D")
header_frame.pack(fill="x")

# Title Label
title_label = tk.Label(header_frame, text="Signature Verification", font=("Helvetica", 24, "bold"), foreground="white", bg="#35477D")
title_label.pack(pady=20)

# Create a content frame
content_frame = tk.Frame(root, bg="#F2F2F2")
content_frame.pack(fill="both", expand=True)

# Center the "Original Signature" and "Test Signature" sections
content_frame.grid_columnconfigure(0, weight=1)
content_frame.grid_columnconfigure(3, weight=1)

# Original Signature Frame
original_frame = tk.LabelFrame(content_frame, text="Original Signature")
original_frame.grid(row=0, column=1, padx=10, pady=20, sticky="nsew")

original_image_path_entry = tk.Entry(original_frame, font=("Helvetica", 12))
original_image_path_entry.grid(row=0, column=0, pady=10, padx=10, sticky="ew")

original_browse_button = tk.Button(original_frame, text="Browse", command=lambda: browse_image(original_image_path_entry, original_image_display))
original_browse_button.grid(row=1, column=0, pady=10, padx=10, sticky="ew")

original_remove_button = tk.Button(original_frame, text="Remove", command=lambda: remove_image(original_image_path_entry, original_image_display))
original_remove_button.grid(row=2, column=0, pady=10, padx=10, sticky="ew")

original_image_display = tk.Label(original_frame)
original_image_display.grid(row=3, column=0, pady=10)

# Test Signature Frame
test_frame = tk.LabelFrame(content_frame, text="Test Signature")
test_frame.grid(row=0, column=2, padx=10, pady=20, sticky="nsew")

test_image_path_entry = tk.Entry(test_frame, font=("Helvetica", 12))
test_image_path_entry.grid(row=0, column=0, pady=10, padx=10, sticky="ew")

test_browse_button = tk.Button(test_frame, text="Browse", command=lambda: browse_image(test_image_path_entry, test_image_display))
test_browse_button.grid(row=1, column=0, pady=10, padx=10, sticky="ew")

test_remove_button = tk.Button(test_frame, text="Remove", command=lambda: remove_image(test_image_path_entry, test_image_display))
test_remove_button.grid(row=2, column=0, pady=10, padx=10, sticky="ew")

test_image_display = tk.Label(test_frame)
test_image_display.grid(row=3, column=0, pady=10)

# Verify Button Frame
verify_frame = tk.Frame(content_frame)
verify_frame.grid(row=1, column=1, columnspan=2, pady=20, padx=10, sticky="ew")

# Center the "Verify Signatures" button and the result label
verify_frame.grid_columnconfigure(0, weight=1)

# Verify Button
verify_button = tk.Button(verify_frame, text="Verify Signatures", command=lambda: verify_signatures(original_image_path_entry, test_image_path_entry, result_label))
verify_button.pack(side="top", padx=10, pady=10)

# Result Label
result_frame = tk.LabelFrame(content_frame, text="Result", labelanchor="n")
result_frame.grid(row=2, column=1, columnspan=2, pady=20, padx=10, sticky="nsew")

result_label = tk.Label(result_frame, font=("Helvetica", 16))
result_label.pack(side="top", padx=10, pady=10)

# Clear Result Button (Below Result Frame)
clear_result_button = tk.Button(content_frame, text="Clear Result", command=lambda: clear_result(result_label))
clear_result_button.grid(row=3, column=1, columnspan=2, pady=(0, 10), padx=10)

# Configure row and column weights for responsiveness
for i in range(4):
    content_frame.grid_rowconfigure(i, weight=1)

root.mainloop()
