from passporteye import read_mrz

def extract_passport_details(image_path):
    # Read the MRZ from the image
    mrz = read_mrz(image_path)

    # Check if the MRZ was successfully read
    if mrz is None:
        return {"success": False, "error": "Invalid Document: Please upload a valid passport"}

    # Extract details
    details = {
        "Surname": mrz.surname,
        "GivenNames": mrz.names,  # Correct attribute might be 'names'
        "PassportNumber": mrz.number,
        "Nationality": mrz.nationality,
        "DateOfBirth": mrz.date_of_birth,
        "Sex": mrz.sex,
        "DateOfExpiry": mrz.expiration_date,
        "IssuingCountry": mrz.country
    }

    return {"success": True, "data": details}

