from subprocess import Popen, PIPE
from docx import opendocx, getdocumenttext
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO
import os
path1='/home/mahesh/Desktop/pdfresumelist'
txtpath='/home/mahesh/Desktop/txtresumelist'
list1=os.listdir(path1)
def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = file(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()
    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)
    fp.close()
    device.close()
    str = retstr.getvalue()
    retstr.close()
    return str
def create_text_file():
      for file1 in list1:
        file2=path1+'/'+file1
        content=convert_pdf_to_txt(file2)
        file3=file1[:-4]
        file4='/home/mahesh/Desktop/txtresumelist/'+file3
        print(file4)
        f=open(file4,'w')
        f.write(content)
        f.close()

create_text_file()

