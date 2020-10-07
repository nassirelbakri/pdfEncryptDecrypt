#! python3
# this program walk through a folder and encrypt all PDF files 
# and save them with _encrypted suffix

import sys, os, PyPDF2
from pathlib import Path

folder= 'C:/users/nassi/encryptedPDF' #sys.argv[1]
password= 'swordfish'#sys.argv[2]

folder=Path(folder)

for foldername, subfolders, filenames in os.walk(folder):
    foldername=Path(foldername)
    for filename in filenames:
        if filename.endswith('.pdf'):
            filePath=foldername/filename
            pdfObj=open(filePath,'rb')
            pdfReader=PyPDF2.PdfFileReader(pdfObj)
            if pdfReader.decrypt(str(password))==0:
                print(f'incorrect password for file %s'%filePath)
                continue
            else:
                pdfReader.decrypt(str(password))
                pdfWriter=PyPDF2.PdfFileWriter()
                for pageNum in range(pdfReader.numPages):
                    pdfWriter.addPage(pdfReader.getPage(pageNum))
            
            resultPDF=open(f'%s_decrypted.pdf'%filePath.stem[:-10],'wb')
            pdfWriter.write(resultPDF)
            resultPDF.close()    
