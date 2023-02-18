# converter
Convert ppt or doc or oocx to pdf using aspose. 

## Application stetup

- Install python version3.8 on your device.
- Create a folder and pull the repo with command : `git clone https://github.com/sammyview80/converter`
- cd directory
- Create a python environment with command: `python3.8 -m venv name-env`.
- Install all dependency with command: `pip install -r requirements.txt`
- Run python3.8 setup.py install
- Run Python3.8 main.py

~Note: All the pdf should me in the director eg: Attachments to be converted.~

##Things that I have encounter creating this projects:

1. Conversion of PPT to PDF: I have really hard time on conversion of PPT to PDF. I want a python module that can convert PPT to PDF without any windows or ubuntu OS. But I have found a package name aspose.slide. `pip install Aspose.Slide`. This package don't use any ms powerpoind or anything. Besides I have came to know its module is written on cpython which is in format `slides.cpython-37m-x86_64-linux-gnu.so` which needs `libpython<version>.so.1.o`. So better note it if you face any problems installing this application. And another ubuntu dependency `libgdiplus` which can be installed by command `sudo apt-get install -y libgdiplus`.
