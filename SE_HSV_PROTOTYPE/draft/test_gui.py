import os
import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim
from sklearn.svm import SVC
from skimage.feature import hog, local_binary_pattern
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report, accuracy_score
import tkinter as tk
from tkinter import filedialog

# Function to extract HOG and LBP features from an image
def extract_features(image):
    # Extract HOG features
    hog_features, hog_image = hog(image, pixels_per_cell=(8, 8), cells_per_block=(2, 2), block_norm='L2-Hys', visualize=True)

    # Extract LBP features
    lbp_radius = 1
    lbp_n_points = 8 * lbp_radius
    lbp_image = local_binary_pattern(image, lbp_n_points, lbp_radius, method='uniform')
    lbp_histogram, _ = np.histogram(lbp_image.ravel(), bins=np.arange(0, lbp_n_points + 3), range=(0, lbp_n_points + 2))

    # Combine HOG and LBP features
    features = np.concatenate((hog_features, lbp_histogram))

    return features, hog_image, lbp_image

# Function to visualize the verification result
def visualize_verification(original_image, tested_image, hog_original, hog_tested, lbp_original, lbp_tested, similarity_percentage, result):
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))

    axes[0, 0].imshow(original_image, cmap='gray')
    axes[0, 0].set_title('Original Signature')

    axes[0, 1].imshow(tested_image, cmap='gray')
    axes[0, 1].set_title('Tested Signature - ' + ('Genuine' if result == 0 else 'Forged'))

    axes[0, 2].imshow(hog_original, cmap='gray')
    axes[0, 2].set_title('HOG - Original')

    axes[1, 0].imshow(hog_tested, cmap='gray')
    axes[1, 0].set_title('HOG - Tested')

    axes[1, 1].imshow(lbp_original, cmap='gray')
    axes[1, 1].set_title('LBP - Original')

    axes[1, 2].imshow(lbp_tested, cmap='gray')
    axes[1, 2].set_title('LBP - Tested')

    plt.suptitle(f'Similarity Percentage: {similarity_percentage:.2%}', fontsize=16)

    for ax in axes.flatten():
        ax.axis('off')

    plt.show()

# Function to verify the signature using SVM
def verify_signature_svm(svm, original_image_path, tested_image_path):
    # Load and preprocess the original image
    original_image = cv2.imread(original_image_path, cv2.IMREAD_GRAYSCALE)
    original_image = cv2.resize(original_image, (300, 300))
    original_features, hog_original, lbp_original = extract_features(original_image)

    # Load and preprocess the tested image
    test_image = cv2.imread(tested_image_path, cv2.IMREAD_GRAYSCALE)
    test_image = cv2.resize(test_image, (300, 300))
    test_features, hog_tested, lbp_tested = extract_features(test_image)

    # Compute Structural Similarity Index (SSI)
    ssi_hog, _ = ssim(hog_original, hog_tested, full=True, data_range=hog_tested.max() - hog_tested.min())
    ssi_lbp, _ = ssim(lbp_original, lbp_tested, full=True, data_range=lbp_tested.max() - lbp_tested.min())

    # Average the SSI scores from HOG and LBP
    similarity_percentage = (ssi_hog + ssi_lbp) #/ 2

    # Predict the label using the trained SVM model
    prediction = svm.predict([test_features])

    # Display the SVM prediction
    if prediction[0] == 0:
        print("The signature is genuine.")
    else:
        print("The signature is forged.")

    # Visualize the verification result
    visualize_verification(original_image, test_image, hog_original, hog_tested, lbp_original, lbp_tested, similarity_percentage, prediction[0])

# Load and preprocess the genuine image (the original signature)
genuine_image_path = 'signature_data/genuine/genuine-01.png'
genuine_image = cv2.imread(genuine_image_path, cv2.IMREAD_GRAYSCALE)
genuine_image = cv2.resize(genuine_image, (300, 300))
genuine_features, hog_original, lbp_original = extract_features(genuine_image)

# Load and preprocess the dataset
data_dir = 'signature_data'
image_paths = [os.path.join(data_dir, 'genuine', filename) for filename in os.listdir(os.path.join(data_dir, 'genuine'))]
image_paths += [os.path.join(data_dir, 'forged', filename) for filename in os.listdir(os.path.join(data_dir, 'forged'))]

X = []
y = []

for image_path in image_paths:
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    image = cv2.resize(image, (300, 300))
    features, _, _ = extract_features(image)
    X.append(features)
    if 'forged' in image_path:
        y.append(1)  # Class 1 represents forged signatures
    else:
        y.append(0)  # Class 0 represents genuine signatures

X = np.array(X)
y = np.array(y)

# Train an SVM classifier
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

svm = SVC(kernel='linear', C=1)
svm.fit(X_train, y_train)

# Evaluate the model on the testing set
y_pred = svm.predict(X_test)
# Print classification report and accuracy
print("Classification Report:\n", classification_report(y_test, y_pred))
print("Accuracy: ", accuracy_score(y_test, y_pred))

# Create the main window
root = tk.Tk()
root.title("Handwritten Signature Verification")

# Set a fixed window size
window_width = 800
window_height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Add a header
header_label = tk.Label(root, text="Handwritten Signature Verification", font=("Helvetica", 16, "bold"))
header_label.grid(row=0, column=0, columnspan=4, pady=(20, 10))

# Create and place widgets with improved styling
style = {'padx': 10, 'pady': 10, 'sticky': 'e'}


# Function to handle the original signature browse button click
def on_original_browse_button_click():
    file_path = filedialog.askopenfilename(title="Select Original Signature", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    entry_original_image.delete(0, tk.END)
    entry_original_image.insert(0, file_path)

# Function to handle the test image browse button click
def on_test_browse_button_click():
    file_path = filedialog.askopenfilename(title="Select Test Image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    entry_tested_image.delete(0, tk.END)
    entry_tested_image.insert(0, file_path)

# Function to handle the verify button click
def on_verify_button_click():
    original_image_path = entry_original_image.get()
    tested_image_path = entry_tested_image.get()
    
    if original_image_path and tested_image_path:
        verify_signature_svm(svm, original_image_path, tested_image_path)
    else:
        result_label.config(text="Please select both original and test images.")

# Function to handle the original signature clear button click
def on_original_clear_button_click():
    entry_original_image.delete(0, tk.END)

# Function to handle the test image clear button click
def on_test_clear_button_click():
    entry_tested_image.delete(0, tk.END)

# Widgets for the GUI layout
label_original_image = tk.Label(root, text="Original Signature:")
entry_original_image = tk.Entry(root, width=40)
original_browse_button = tk.Button(root, text="Browse", command=on_original_browse_button_click)
original_clear_button = tk.Button(root, text="Clear", command=on_original_clear_button_click)

label_tested_image = tk.Label(root, text="Test Signature:")
entry_tested_image = tk.Entry(root, width=40)
tested_browse_button = tk.Button(root, text="Browse", command=on_test_browse_button_click)
tested_clear_button = tk.Button(root, text="Clear", command=on_test_clear_button_click)

verify_button = tk.Button(root, text="Verify Signature", command=on_verify_button_click)
result_label = tk.Label(root, text="")

# Grid placement for the widgets
label_original_image.grid(row=1, column=0, **style)
entry_original_image.grid(row=1, column=1, **style)
original_browse_button.grid(row=1, column=2, **style)
original_clear_button.grid(row=1, column=3, **style)

label_tested_image.grid(row=2, column=0, **style)
entry_tested_image.grid(row=2, column=1, **style)
tested_browse_button.grid(row=2, column=2, **style)
tested_clear_button.grid(row=2, column=3, **style)

verify_button.grid(row=3, column=1, pady=20)
result_label.grid(row=4, column=1, pady=10)

# Add a footer
footer_label = tk.Label(root, text="@GROUP14_BSCS3A", font=("Helvetica", 10), fg="gray")
footer_label.grid(row=5, column=0, columnspan=4, pady=(10, 20))

# Run the Tkinter event loop
root.mainloop()