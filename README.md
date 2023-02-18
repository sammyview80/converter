# converter
Convert ppt or doc or oocx to pdf using aspose. 

## Application stetup

- Install python version3.8 on your device.
- Create a folder and pull the repo with command : `git clone https://github.com/sammyview80/converter`
- cd directory
- Create a python environment with command: `python3.8 -m venv name-env`.
- Install all dependency with command: `pip install -r requirements.txt`
- Run python3.8 setup.py install.
- Run Python3.8 main.py

> Note: All the pdf should be in the director (eg: Attachments) to be converted.

#### Packages Used and code explanation: 
1. aspose-words: Contains classes for work with Microsoft PowerPoint presentations without utilizing Microsoft PowerPoint.
> Installation: pip install aspose.words

> Documentation: https://reference.aspose.com/slides/python-net/aspose.slides/. 
```
 import aspose.words as words
 
 def convert_docx_to_pdf(docx_file_path, pdf_file_path):
    """Converts DOCX to PDF"""
    # Load word document
    doc = words.Document(docx_file_path)

    # Create save options and set compliance
    saveOptions = words.saving.PdfSaveOptions()
    saveOptions.compliance = words.saving.PdfCompliance.PDF17 

    # Save as PDF
    doc.save(pdf_file_path, saveOptions)
 
```
2. Aspose-Slides: Aspose.Words library is written in Python and C#, and contains only safe managed code. Microsoft Word is not required in order to use Aspose.Words. https://reference.aspose.com/words/python-net/aspose.words/.
```
import aspose.slides as slides

def convert_ppt_to_pdf(ppt_file_path, pdf_file_path):
    """Converts PPT to PDF"""
    # Load presentation
    pres = slides.Presentation(ppt_file_path)

    # Convert PPTX to PDF
    pres.save(pdf_file_path, slides.export.SaveFormat.PDF)

```
3. python-magic: python-magic is a Python interface to the libmagic file type identification library. libmagic identifies file types by checking their headers according to a predefined list of file types. This functionality is exposed to the command line by the Unix command file. 
> Installation: pip install python-magic

> Documentation: https://magic.readthedocs.io/_/downloads/en/stable/pdf/
```
import magic

def is_pdf(file_path):
    mime = magic.Magic(mime=True) # Initialize instance of Magic with type
    file_mime_type = mime.from_file(file_path) # Load the file 
    return file_mime_type == 'application/pdf' # return tru of file is pdf.

def is_ppt(file_path):
    mime = magic.Magic(mime=True)
    file_mime_type = mime.from_file(file_path)
    return file_mime_type == 'application/vnd.ms-powerpoint'

def is_docx(file_path):
    mime = magic.Magic(mime=True)
    file_mime_type = mime.from_file(file_path)
    return file_mime_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document" or file_mime_type == "application/msword"
```
- file_mime_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document" for `.docx`
- file_mime_type == "application/msword" for `.doc`
- file_mime_type == 'application/vnd.ms-powerpoint' for `.ppt`
- file_mime_type == 'application/pdf' for `.pdf`


## Things that I have encounter creating this projects:

1. Conversion of PPT to PDF: I have really hard time on conversion of PPT to PDF. I want a python module that can convert PPT to PDF without any windows or ubuntu OS. But I have found a package name aspose.slide. `pip install Aspose.Slide`. This package don't use any ms powerpoind or anything. Besides I have came to know its module is written on cpython which is in format `slides.cpython-37m-x86_64-linux-gnu.so` which needs `libpython<version>.so.1.o`. So better note it if you face any problems installing this application. And another ubuntu dependency `libgdiplus` which can be installed by command `sudo apt-get install -y libgdiplus`.
