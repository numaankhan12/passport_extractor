import numpy as np
from passporteye import read_mrz
import cv2
import pytesseract

# Set the path to the Tesseract executable if needed
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

def extract_passport_details(image_path):
    # Read the MRZ from the image
    mrz = read_mrz(image_path)

    # Check if the MRZ was successfully read
    if mrz is None:
        return {"success": False, "error": "MRZ could not be read"}

    # Print the MRZ object for debugging purposes
    print("MRZ object:", mrz)

    # Print the attributes of the MRZ object for debugging
    print("MRZ attributes:", dir(mrz))

    # Extract details safely
    details = {
        "Surname": getattr(mrz, 'surname', None),
        "GivenNames": getattr(mrz, 'names', None),
        "PassportNumber": getattr(mrz, 'number', None),
        "Nationality": getattr(mrz, 'nationality', None),
        "DateOfBirth": getattr(mrz, 'date_of_birth', None),
        "Sex": getattr(mrz, 'sex', None),
        "DateOfExpiry": getattr(mrz, 'expiration_date', None),
        "IssuingCountry": getattr(mrz, 'country', None)
    }

    return {"success": True, "data": details}

class RotatedBox:
    def __init__(self, center, size, angle, rotation_center=None):
        self.center = np.asarray(center, dtype=float)
        self.size = size
        self.angle = angle
        if rotation_center is not None:
            self.rotation_center = np.asarray(rotation_center, dtype=float)
        else:
            self.rotation_center = self.center

    @staticmethod
    def from_points(points, box_type='h'):
        points = np.asarray(points, dtype=float)
        if box_type == 'h':
            center = np.mean(points, axis=0)
            size = np.max(points, axis=0) - np.min(points, axis=0)
            angle = 0.0
        elif box_type == 'r':
            # Assuming points are given as [top-left, top-right, bottom-right, bottom-left]
            (cx, cy), (w, h), angle = cv2.minAreaRect(points)
            center = (cx, cy)
            size = (w, h)
        else:
            raise ValueError("Unknown box type")

        return RotatedBox(center, size, angle)

    # Other methods can be added here as needed
