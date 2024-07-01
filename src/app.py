import os
import sys
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import pytesseract

# Set the path to the Tesseract executable if it's not in your PATH
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Ensure the src directory is in the sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from extractor import extract_passport_details

app = FastAPI()

@app.post("/upload-passport/")
async def upload_passport(file: UploadFile = File(...)):
    try:
        # Save the uploaded file to a temporary location
        temp_file_path = f"temp_{file.filename}"
        with open(temp_file_path, "wb") as temp_file:
            temp_file.write(file.file.read())

        # Extract passport details
        result = extract_passport_details(temp_file_path)

        # Remove the temporary file
        os.remove(temp_file_path)

        if result["success"]:
            return JSONResponse(content={"details": result["data"]})
        else:
            raise HTTPException(status_code=400, detail=result["error"])

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))





