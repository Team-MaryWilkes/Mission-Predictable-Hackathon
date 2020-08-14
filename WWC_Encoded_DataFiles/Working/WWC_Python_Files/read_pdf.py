import PyPDF2

def read_forida_dept_health_pdf(input_pdfName, output_filename):
  """Opens pdf file from Florida Department of Health website saved on local disk.  Reads pdf file line by line and prints to a text file."""

  read_pdf = PyPDF2.PdfFileReader(input_pdfName)
 
  with open(output_filename, 'a') as f:
    for i in range(read_pdf.getNumPages()):
        page = read_pdf.getPage(i)
        f.write(f'Page No -   {str(1+read_pdf.getPageNumber(page))}')
        page_content = page.extractText()
        f.write(page_content)
       
      