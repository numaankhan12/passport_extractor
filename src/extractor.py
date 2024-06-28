import pytesseract
from passporteye import read_mrz

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

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
