import magic

def is_pdf(file_path):
    mime = magic.Magic(mime=True)
    file_mime_type = mime.from_file(file_path)
    return file_mime_type == 'application/pdf'

def is_ppt(file_path):
    mime = magic.Magic(mime=True)
    file_mime_type = mime.from_file(file_path)
    return file_mime_type == 'application/vnd.ms-powerpoint'

def is_docx(file_path):
    mime = magic.Magic(mime=True)
    file_mime_type = mime.from_file(file_path)
    return file_mime_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document" or file_mime_type == "application/msword"