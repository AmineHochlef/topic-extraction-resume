import re
from pdfminer.high_level import extract_pages, extract_text
# tabula library for extracting data from tables in a pdf 
import tabula
# fitz from PyMuPDF - PIL.Image from Pillow
# libraries for extracting images data
import fitz
import PIL.Image
import io # for working with image data 


# extracting simple text from the pdf
text = extract_text("aminehochlef-sample-pdf-file.pdf")
print("----all the text within the file-----: \n",text)

# extracting text that contains the pattern
pattern = re.compile(r"[a-zA-Z]+,{1}\s{1}")
matches = pattern.findall(text)
print("----text that matches the pattern-----: \n",matches)

# reading text from a table in the pdf
tables = tabula.read_pdf("aminehochlef-sample-pdf-file.pdf",pages="all")
# df of type pandas DataFrame
df = tables[0]
print(df.head(2))


# extracting images from pdf file
pdf = fitz.open("aminehochlef-sample-pdf-file.pdf")
counter = 1
for i in range(len(pdf)): # len(pdf) -> number of pages
    page = pdf[i]
    images = page.get_images()
    for image in images:
        base_img = pdf.extract_image(image[0])
        image_data = base_img["image"]
        img = PIL.Image.open(io.BytesIO(image_data))
        extention = base_img["ext"]
        img.save(open(f"image{counter}.{extention}", "wb"))
        counter += 1
# The first image from the pdf gets saved in the same directory 
# as the py file with the name image<number of image in the pdf>.jpeg
