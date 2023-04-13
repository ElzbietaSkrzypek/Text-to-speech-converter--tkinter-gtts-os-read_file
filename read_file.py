from PyPDF2 import PdfReader
import docx2txt


class Read_File:
    def __init__(self, to_convert):
        self.to_convert = to_convert

    # reading word file
    def read_word_files(self):
        to_convert = self.to_convert.split('\n')[0]
        return docx2txt.process(to_convert)

    # reading pdf file
    def read_pdf_files(self):
        to_convert = self.to_convert.split('\n')[0]
        path = open(to_convert, 'rb')  # path of the PDF file
        pdfReader = PdfReader(path)  # creating a PdfFileReader object
        text = ""
        for page in pdfReader.pages:
            text += page.extract_text() + "\n"  # extracting the text from the PDF
        return text

    # reading simple text file
    def read_text_files(self):
        to_convert = self.to_convert.split('\n')[0]
        with open(to_convert) as file:
            return file.read()
