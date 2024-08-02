#signature.py
import cv2
from skimage.metrics import structural_similarity as ssim

def match(path1, path2):
    # Load the images from the provided file paths.
    img1 = cv2.imread(path1)
    img2 = cv2.imread(path2)

    # Convert images to grayscale for better similarity comparison.
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    # Resize both images to a consistent size (e.g., 300x300) for comparison.
    img1 = cv2.resize(img1, (300, 300))
    img2 = cv2.resize(img2, (300, 300))

    # Calculate the Structural Similarity Index (SSI) between the two images.
    # Higher SSIM values indicate higher similarity between the images.
    similarity_value = ssim(img1, img2) * 100

    return similarity_value

