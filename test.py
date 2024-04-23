import pytesseract
from PIL import Image
from reportlab.lib.pagesizes import landscape, A3
from reportlab.pdfgen import canvas

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Aretex-Gerome\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

image_path = 'test3.png'

with Image.open(image_path) as img:

    data = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT)


pdf_path = 'extracted_text2.pdf'


c = canvas.Canvas(pdf_path, pagesize=landscape(A3))


for i in range(len(data['text'])):

    word = data['text'][i]
    left = int(data['left'][i])
    top = int(data['top'][i])
    width = int(data['width'][i])
    height = int(data['height'][i])
    

    c.drawString(left, img.height - top, word)
    

c.save()


print("Extracted text with exact layout has been saved to 'extracted_text2.pdf'")
