import os
import cv2
import numpy as np
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLabel
from sklearn.svm import SVC
from svm import extract_features, verify_signature_svm

class SignatureVerificationApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.svm = None  # Initialize SVM model

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Handwritten Signature Verification (Prototype)")
        self.setWindowIcon(QIcon('hsv.png'))
        self.setGeometry(100, 100, 800, 600)

        self.setStyle(QtWidgets.QStyleFactory.create("Fusion"))
        self.setPalette(QtGui.QPalette(QtGui.QColor("#1b2838")))

        layout = QtWidgets.QGridLayout(self)

         # Set the application icon
        app_icon = QtGui.QIcon("HSV_MEDYO_FINAL\hsv.png")  # Replace with the actual path to your icon file
        self.setWindowIcon(app_icon)

        # Header
        header_label = QtWidgets.QLabel("Handwritten Signature Verification")
        header_label.setAlignment(QtCore.Qt.AlignCenter)
        header_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #66c0f4; margin-bottom: 20px;")
        layout.addWidget(header_label, 0, 0, 1, 2)

        # Load and preprocess the dataset here (same code as in svm.py)
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
        self.svm = SVC(kernel='linear', C=1)
        self.svm.fit(X, y)

        # Create image boxes
        original_box = self.create_image_box("Original Signature:")
        test_box = self.create_image_box("Test Signature:")

        # Widgets for the GUI layout
        self.label_original_image = original_box["label"]
        self.entry_original_image = original_box["entry"]
        self.original_browse_button = original_box["browse_button"]
        self.original_clear_button = original_box["clear_button"]
        self.original_image_display = original_box["image_display"]

        self.label_tested_image = test_box["label"]
        self.entry_tested_image = test_box["entry"]
        self.tested_browse_button = test_box["browse_button"]
        self.tested_clear_button = test_box["clear_button"]
        self.tested_image_display = test_box["image_display"]

        self.verify_button = QtWidgets.QPushButton("Verify Signature", self)
        self.verify_button.setStyleSheet("background-color: #2a475e; color: white; border: 1px solid #66c0f4; border-radius: 5px; padding: 5px 10px; font-size: 14px;")
        self.result_label = QtWidgets.QLabel(self)
        self.result_label.setStyleSheet("color: #66c0f4; font-size: 14px;")

        # Styles for labels
        label_style = "font-size: 16px; color: #66c0f4;"

        self.label_original_image.setStyleSheet(label_style)
        self.label_tested_image.setStyleSheet(label_style)

        # Connect signals to slots
        self.original_browse_button.clicked.connect(self.on_original_browse_button_click)
        self.tested_browse_button.clicked.connect(self.on_test_browse_button_click)
        self.verify_button.clicked.connect(self.on_verify_button_click)
        self.original_clear_button.clicked.connect(self.on_original_clear_button_click)
        self.tested_clear_button.clicked.connect(self.on_test_clear_button_click)

        # Add boxes to the layout
        layout.addWidget(original_box["box"], 1, 0)
        layout.addWidget(test_box["box"], 1, 1)

        # Add a footer
        footer_label = QtWidgets.QLabel("@GROUP14_BSCS3A", self)
        footer_label.setStyleSheet("font-size: 12px; color: #c7d5e0;")
        footer_label.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(footer_label, 4, 0, 1, 2)

        # Add a info button
        info_button = QtWidgets.QPushButton("Info", self)
        info_button.setStyleSheet("background-color: #2a475e; color: white; border: 1px solid #66c0f4; border-radius: 5px; padding: 5px 10px; font-size: 14px;")
        info_button.clicked.connect(self.show_info_dialog)
        layout.addWidget(info_button, 5, 0, 1, 2)

        # Add boxes to the layout
        layout.addWidget(original_box["box"], 1, 0)
        layout.addWidget(test_box["box"], 1, 1)

        # Add a footer
        layout.addWidget(self.verify_button, 2, 0, 1, 2)
        layout.addWidget(self.result_label, 3, 0, 1, 2)

        self.setLayout(layout)

    def show_info_dialog(self):
        info_dialog = QtWidgets.QDialog(self)
        info_dialog.setWindowTitle("Instructions - Handwritten Signature Verification")
        info_dialog.setFixedSize(600, 400)

        # Create a QTextBrowser to display instructions
        instructions_text = """
        <html>
            <body>
                <h2>Handwritten Signature Verification (Prototype)</h2>

                <p><strong>Introduction:</strong><br>
                Welcome to the Handwritten Signature Verification application! This tool allows you to verify if a test signature matches a given original signature using a Support Vector Machine (SVM) model.</p>

                <h3>Instructions:</h3>

                <ol>
                    <li><strong>Launch the Application:</strong><br>
                        - Double-click on the application icon to launch it.
                    </li>

                    <li><strong>Load Signature Data:</strong><br>
                        - The application automatically loads handwritten signature data for training the SVM model.<br>
                        - To test other signature, go to the file location of the prototype and find the signature_data folder,<br>
                          replace the content of the forged and genuine signature with the images of signature you want to verify.
                    </li>

                    <li><strong>Select Original Signature:</strong><br>
                        - Click the "Browse" button next to "Original Signature."<br>
                        - Choose an original signature image file (in PNG, JPG, or JPEG format) from your computer.<br>
                        - Click "Open" in the file dialog to load the original signature.
                    </li>

                    <li><strong>Select Test Signature:</strong><br>
                        - Click the "Browse" button next to "Test Signature."<br>
                        - Choose a test signature image file (in PNG, JPG, or JPEG format) from your computer.<br>
                        - Click "Open" in the file dialog to load the test signature.
                    </li>

                    <li><strong>Verify Signatures:</strong><br>
                        - After selecting both original and test signatures, click the "Verify Signature" button.<br>
                        - The application will analyze the signatures and display the result.
                    </li>

                    <li><strong>Review Result:</strong><br>
                        - The result will be displayed below the "Verify Signature" button.<br>
                        - If the test signature matches the original, you'll see a success message. Otherwise, an error message will be shown.
                    </li>

                    <li><strong>Clear Signature Selection:</strong><br>
                        - To clear the selected original signature, click the "Clear" button next to the original signature entry.<br>
                        - To clear the selected test signature, click the "Clear" button next to the test signature entry.
                    </li>

                    <li><strong>Exit the Application:</strong><br>
                        - You can close the application by clicking the close button (X) on the top right corner of the window.
                    </li>
                </ol>

                <h3>Additional Information:</h3>

                <ul>
                    <li><strong>Note:</strong><br>
                        - Make sure to select valid image files for both the original and test signatures.<br>
                        - For optimal results, use clear and well-scanned signature images.<br>
                    </li>

                    <li><strong>Support:</strong><br>
                        - If you encounter any issues or have questions, please contact the developer GROUP14_BSCS3A or refer to the documentation provided.<br>
                </li>
                </ul>

                <footer>
                    Thank you for using the Handwritten Signature Verification application!
                </footer>
            </body>
        </html>
        """

        text_browser = QtWidgets.QTextBrowser()
        text_browser.setHtml(instructions_text)

        # Add the QTextBrowser to the layout
        layout = QtWidgets.QVBoxLayout(info_dialog)
        layout.addWidget(text_browser)

        # Show the dialog
        info_dialog.exec_()

    def create_image_box(self, label_text):
        box = QtWidgets.QFrame(self)
        box.setFrameShape(QtWidgets.QFrame.Panel)
        box.setFrameShadow(QtWidgets.QFrame.Raised)
        box_layout = QtWidgets.QVBoxLayout(box)

        label = QtWidgets.QLabel(label_text)
        label.setStyleSheet("font-size: 16px; color: #333; font-weight: bold;")

        image_frame = QtWidgets.QFrame()
        image_frame_layout = QtWidgets.QHBoxLayout(image_frame)

        entry = QtWidgets.QLineEdit(box)
        entry.setStyleSheet("border: 1px solid #66c0f4; border-radius: 5px;")
        browse_button = QtWidgets.QPushButton("Browse", box)
        browse_button.setStyleSheet("background-color: #2a475e; color: white; border: 1px solid #66c0f4; border-radius: 5px; padding: 5px 10px; font-size: 14px;")
        clear_button = QtWidgets.QPushButton("Clear", box)
        clear_button.setStyleSheet("background-color: #2a475e; color: white; border: 1px solid #66c0f4; border-radius: 5px; padding: 5px 10px; font-size: 14px;")
        image_display = QLabel(self)
        image_display.setAlignment(QtCore.Qt.AlignCenter)
        image_display.setFixedSize(300, 300)
        image_display.setStyleSheet("border: 2px solid #66c0f4; border-radius: 5px; background-color: #FFF;")

        image_frame_layout.addWidget(image_display)

        box_layout.addWidget(label)
        box_layout.addWidget(entry)
        box_layout.addWidget(browse_button)
        box_layout.addWidget(clear_button)
        box_layout.addWidget(image_frame)

        return {
            "box": box,
            "label": label,
            "entry": entry,
            "browse_button": browse_button,
            "clear_button": clear_button,
            "image_display": image_display
        }

    def on_original_browse_button_click(self):
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select Original Signature", "", "Image files (*.png;*.jpg;*.jpeg)")
        self.entry_original_image.setText(file_path)
        self.display_image(file_path, self.original_image_display)

    def on_test_browse_button_click(self):
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select Test Image", "", "Image files (*.png;*.jpg;*.jpeg)")
        self.entry_tested_image.setText(file_path)
        self.display_image(file_path, self.tested_image_display)

    def on_verify_button_click(self):
        original_image_path = self.entry_original_image.text()
        tested_image_path = self.entry_tested_image.text()

        if original_image_path and tested_image_path:
            verify_signature_svm(self.svm, original_image_path, tested_image_path)
        else:
            self.result_label.setText("Please select both original and test signatures.")

    def on_original_clear_button_click(self):
        self.entry_original_image.clear()
        self.original_image_display.clear()

    def on_test_clear_button_click(self):
        self.entry_tested_image.clear()
        self.tested_image_display.clear()

    def display_image(self, file_path, image_display):
        pixmap = QtGui.QPixmap(file_path)
        pixmap = pixmap.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
        image_display.setPixmap(pixmap)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = SignatureVerificationApp()
    window.show()
    app.exec_()