from dataStructure import *


book = Book(
    name='The Garden',
    collaborators=['Andrew Child'],
    repo='https://github.com/AndrewChild/The-Garden-Guidebook',
    dl='https://github.com/AndrewChild/The-Garden-Guidebook/raw/main/guideBook.pdf',
    paths={
        'LaTeXTemplates': '../LocalBoulders/templates/',
        'LaTeXOut': './sections/',
        'pdf': './',
        'ghost_script': r'C:\Program Files\gs\gs10.00.0\bin\gswin64.exe',
    }
)



if __name__ == '__main__':
    sys.exit()
