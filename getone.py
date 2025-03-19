import os
import shutil
from PyPDF2 import PdfReader, PdfWriter
import re

def extract_first_page(pdf_path, output_path):
    with open(pdf_path, 'rb') as pdf_file:
        reader = PdfReader(pdf_file)
        writer = PdfWriter()
        writer.add_page(reader.pages[0])
        
        with open(output_path, 'wb') as output_pdf:
            writer.write(output_pdf)

def main():
    input_folder = r'c:\Users\daiyn\OneDrive\桌面\202525\新建文件夹'
    output_folder = os.path.join(input_folder, 'extracted_pages')
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(input_folder):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(input_folder, filename)
            # 提取文件名中的第一个数字
            match = re.match(r'(\d+)', filename)
            if match:
                output_filename = match.group(1) + '.pdf'
                output_path = os.path.join(output_folder, output_filename)
                extract_first_page(pdf_path, output_path)
                print(f'Extracted first page of {filename} to {output_filename}')

if __name__ == '__main__':
    main()