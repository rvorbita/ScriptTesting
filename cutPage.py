#!/usr/bin/python3


import PyPDF2, os

#cut out specific pages from PDFs

#get the path of the pdf file
#check the file extension in the path for .pdf
#loop to the page and save it to a list

pdfFileObj = open('Wing06.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

print(pdfReader.numPages)