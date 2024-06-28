import unittest
import os
from src.extractor import extract_passport_details

class TestPassportExtractor(unittest.TestCase):

    def test_valid_passport(self):
        image_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images', 'sample_passport.jpg')
        result = extract_passport_details(image_path)
        self.assertTrue(result["success"])
        self.assertIn("Surname", result["data"])
        self.assertIn("GivenNames", result["data"])
        self.assertIn("PassportNumber", result["data"])
        self.assertIn("Nationality", result["data"])
        self.assertIn("DateOfBirth", result["data"])
        self.assertIn("Sex", result["data"])
        self.assertIn("DateOfExpiry", result["data"])
        self.assertIn("IssuingCountry", result["data"])

    def test_invalid_passport(self):
        image_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images', 'invalid_passport.jpg')
        result = extract_passport_details(image_path)
        self.assertFalse(result["success"])

if __name__ == '__main__':
    unittest.main()

