import os
import sys
import json
import argparse

# Set the path to the Tesseract executable if it's not in your PATH
import pytesseract
#pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Add the parent directory of src to the sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from extractor import extract_passport_details

def main(image_path):
    # Debug prints to verify the image path
    print(f"Received image path: {image_path}")
    abs_image_path = os.path.abspath(image_path)
    print(f"Absolute image path: {abs_image_path}")

    if not os.path.exists(abs_image_path):
        print(f"Image file not found: {abs_image_path}")
        return

    # Extract passport details
    result = extract_passport_details(abs_image_path)

    if result["success"]:
        print("Extracted Passport Details:")
        print(json.dumps(result["data"], indent=4))
    else:
        print(f"Error: {result['error']}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract details from a passport image")
    parser.add_argument("image_path", help="Path to the passport image")
    args = parser.parse_args()

    main(args.image_path)


