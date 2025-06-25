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

from mainwindow_scan_2 import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):

        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("title here")

        self.ui.display_scan_button.clicked.connect(self.on_display_button_clicked)

    def on_display_button_clicked(self):
        # Display the scan when the button is clicked
        self.display_scan()
        print("Scan was displayed!")

    def display_scan(self):
        # Load the NIfTI image
        img = nib.load("../Scans/s0011/ct.nii.gz")
        data = img.get_fdata()
        # Take the middle slice along the z-axis
        slice_idx = data.shape[2] // 2
        slice_2d = data[:, :, slice_idx]

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

        # Display in QLabel (assumes you have self.ui.image_label)
        self.ui.scan_view.setPixmap(pixmap)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())