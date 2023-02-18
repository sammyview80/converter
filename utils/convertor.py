import aspose.slides as slides
import aspose.words as words

def convert_ppt_to_pdf(ppt_file_path, pdf_file_path):
    """Converts PPT to PDF"""
    # Load presentation
    pres = slides.Presentation(ppt_file_path)

    # Convert PPTX to PDF
    pres.save(pdf_file_path, slides.export.SaveFormat.PDF)

def convert_docx_to_pdf(docx_file_path, pdf_file_path):
    """Converts DOCX to PDF"""
    # Load word document
    doc = words.Document(docx_file_path)

    # Create save options and set compliance
    saveOptions = words.saving.PdfSaveOptions()
    saveOptions.compliance = words.saving.PdfCompliance.PDF17 

    # Save as PDF
    doc.save(pdf_file_path, saveOptions)