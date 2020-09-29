#!/usr/bin/python3
#combinepdfs.py - combines all the PDFs in the current working dirct into
#into a single PDF

import PyPDF2,os

#get all the pdf filenames.
pdfFiles = []

for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)

pdfFiles.sort(key = str.lower)
pdfWriter = PyPDF2.PdfFileWriter()

#loop through all the PDF files.
for filename in pdfFiles:
    pdfObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfObj)

#Loop through all the pages (except the first) and add them.
    for pageNum in range(1, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

#Save the resulting PDF to a file.
outputPDF = open('allminutes.pdf', 'wb')
pdfWriter.write(outputPDF)
pdfObj.close()
outputPDF.close()