from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QInputDialog,
    QFileDialog,
    QDialog,
)

from PySide6.QtGui import QImage, QPixmap, QIcon
from PySide6.QtCore import Qt, QTimer, QFile, QSize
from PySide6.QtUiTools import QUiLoader

import numpy as np
import sys
import nibabel as nib

from mainwindow_slider_4 import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):

        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("title here")

        self.original_pixmap = None

        self.ui.display_scan_button.clicked.connect(self.on_display_button_clicked)
        self.ui.slice_slider.valueChanged.connect(self.display_scan) # Added this

    def on_display_button_clicked(self):
        # Display the scan when the button is clicked
        self.display_scan()
        print("Scan was displayed!")


    def display_scan(self): # Edited this
        # Load the NIfTI image
        img = nib.load("../Scans/s0011/ct.nii.gz")
        data = img.get_fdata()
        # # Take the middle slice along the z-axis
        # slice_idx = data.shape[2] // 2
        # slice_2d = data[:, :, slice_idx]

        num_slices = data.shape[2] # Added this
        # Set slider range if not already set
        self.ui.slice_slider.setMinimum(0)
        self.ui.slice_slider.setMaximum(num_slices - 1)

        # Set slider to centre if not already set
        if not hasattr(self, "_slider_initialized"):
            self.ui.slice_slider.setValue(num_slices // 2)
            self._slider_initialized = True

        # Get current slice from slider
        slice_idx = self.ui.slice_slider.value()
        slice_2d = data[:, :, slice_idx]

        self.ui.slice_label.setText(f"Slice {slice_idx + 1} of {num_slices}")  # Added this

        # Rotate the image by 90 degrees anti-clockwise
        slice_2d = np.rot90(slice_2d, k=1)

        # Normalize to 0-255 and convert to uint8
        slice_norm = 255 * (slice_2d - np.min(slice_2d)) / (np.ptp(slice_2d))
        slice_uint8 = slice_norm.astype(np.uint8)
        slice_uint8 = np.ascontiguousarray(slice_uint8)  # Ensure C-contiguous

        # Convert to QImage
        h, w = slice_uint8.shape
        qimg = QImage(slice_uint8.data, w, h, w, QImage.Format_Grayscale8)
        pixmap = QPixmap.fromImage(qimg)

        self.original_pixmap = pixmap
        self.update_image()

    def update_image(self):
        if self.original_pixmap:
            scaled = self.original_pixmap.scaled(
                self.ui.scan_view.size(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation,
            )
            self.ui.scan_view.setPixmap(scaled)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        QTimer.singleShot(0, self.update_image)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())