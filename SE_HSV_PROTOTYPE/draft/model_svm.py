import os
import cv2
import numpy as np
from sklearn.svm import SVC
from skimage.feature import hog, local_binary_pattern
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score

# Function to extract HOG and LBP features from an image
def extract_features(image):
    # Extract HOG features
    hog_features = hog(image, pixels_per_cell=(8, 8), cells_per_block=(2, 2), block_norm='L2-Hys', visualize=False)

    # Extract LBP features
    lbp_radius = 1
    lbp_n_points = 8 * lbp_radius
    lbp_image = local_binary_pattern(image, lbp_n_points, lbp_radius, method='uniform')
    lbp_histogram, _ = np.histogram(lbp_image.ravel(), bins=np.arange(0, lbp_n_points + 3), range=(0, lbp_n_points + 2))

    # Combine HOG and LBP features
    features = np.concatenate((hog_features, lbp_histogram))

    return features

# Load and preprocess the dataset
data_dir = 'signature_data'
image_paths = [os.path.join(data_dir, 'genuine', filename) for filename in os.listdir(os.path.join(data_dir, 'genuine'))]
image_paths += [os.path.join(data_dir, 'forged', filename) for filename in os.listdir(os.path.join(data_dir, 'forged'))]

X = []
y = []

for image_path in image_paths:
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    image = cv2.resize(image, (300, 300))
    features = extract_features(image)
    X.append(features)
    if 'forged' in image_path:
        y.append(1)  # Class 1 represents forged signatures
    else:
        y.append(0)  # Class 0 represents genuine signatures

X = np.array(X)
y = np.array(y)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train an SVM classifier
svm = SVC(kernel='linear', C=1)
svm.fit(X_train, y_train)

# Evaluate the model on the testing set
y_pred = svm.predict(X_test)

# Print classification report and accuracy
print("Classification Report:\n", classification_report(y_test, y_pred))
print("Accuracy: ", accuracy_score(y_test, y_pred))

# Use the trained model to make predictions on new signature images
new_image_path = 'signature_data/new/signature1.png'
new_image = cv2.imread(new_image_path, cv2.IMREAD_GRAYSCALE)
new_image = cv2.resize(new_image, (300, 300))
new_features = extract_features(new_image)
prediction = svm.predict([new_features])

if prediction[0] == 0:
    print("The signature is genuine.")
else:
    print("The signature is forged.")
