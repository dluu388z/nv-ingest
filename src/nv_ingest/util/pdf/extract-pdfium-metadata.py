'''
Sample code to extract important document-level metadata
  using PDFium 

'''
import sys
import pypdfium2.raw as pdfium
from pypdfium2 import PdfDocument
import ctypes

if __name__ == '__main__':
    source_name = sys.argv[1]
    document_json = {}

    pdf = PdfDocument(source_name, autoclose=True)

    pdf_version = ctypes.c_int()  # C integer, init to zero
    ok = pdfium.FPDF_GetFileVersion(pdf, pdf_version)
    document_json['PDF version'] = pdf_version.value if ok else None
    document_json['num_pages'] = len(pdf)
    # Important Document-level Metadata: title, subject, author, keywords
    document_json['metadata'] = pdf.get_metadata_dict()

    # print(document_json)

