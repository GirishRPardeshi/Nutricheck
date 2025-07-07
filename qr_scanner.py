# qr_scanner.py

import cv2
from pyzbar.pyzbar import decode
import numpy as np
from PIL import Image

def scan_qr_code(image_file):
    """
    Takes an uploaded image (from Streamlit) and returns the decoded QR/barcode content.
    """
    try:
        image = Image.open(image_file).convert("RGB")
        open_cv_image = np.array(image)
        codes = decode(open_cv_image)

        if codes:
            return codes[0].data.decode("utf-8")
        else:
            return None
    except Exception as e:
        return None
