from PIL import Image
import pytesseract

def scan_receipt(image_path):
    try:
        text = pytesseract.image_to_string(Image.open(image_path))
        return text
    except Exception as e:
        return f"Error reading image: {str(e)}"
