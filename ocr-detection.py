try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
content = pytesseract.image_to_string(Image.open(image-path))
