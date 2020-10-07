#! python3
# this program walk through a folder and encrypt all PDF files 
# and save them with _encrypted suffix

import sys, os, PyPDF2
from pathlib import Path

folder= sys.argv[1]
password= sys.argv[2]

folder=Path(folder)

for foldername, subfolders, filenames in os.walk(folder):
    foldername=Path(foldername)
    for filename in filenames:
        if filename.endswith('.pdf'):
            filePath=foldername/filename
            pdfObj=open(filePath,'rb')
            pdfReader=PyPDF2.PdfFileReader(pdfObj)
            pdfWriter=PyPDF2.PdfFileWriter()
            for pageNum in range(pdfReader.numPages):
                pdfWriter.addPage(pdfReader.getPage(pageNum))
            pdfWriter.encrypt(str(password))
            resultPDF=open(f'%s_encrypted.pdf'%filePath.stem,'wb')
            pdfWriter.write(resultPDF)
            resultPDF.close()    
