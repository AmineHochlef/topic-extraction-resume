import re
from pdfminer.high_level import extract_pages, extract_text
# tabula library for extracting data from tables in a pdf 
import tabula

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


