from PyPDF2 import PdfReader
from tkinter import Tk  
from tkinter.filedialog import askopenfilename

Tk().withdraw()
filename = askopenfilename() 

reader = PdfReader(filename)
number_of_pages = len(reader.pages)
yourId = input('Enter your Id: ')

for i in range(number_of_pages):
    text = reader.pages[i].extract_text().split('\n')
    out = list(filter(lambda i: i.__contains__(yourId),text))
    if(out != []):
        print(out[0])