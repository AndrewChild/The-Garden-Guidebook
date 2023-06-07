import sys
from GB_Book import book
from GB_Area_Main import *
from GB_Area_PinkTag import *
from GB_Area_Cliffs import *
from GB_Area_Upper import *
from GB_Area_Quartz import *
from GB_Area_Other import *
from GB_Images import *

if __name__ == '__main__':
    book.paths['LaTeXTemplates'] = '../LocalBoulders/templates/'
    book.paths['LaTeXOut'] = './sections/'
    book.paths['pdf'] = './'
    book.filename = 'guideBook_print'
    book.gen()
    book.format_options.append('skip_action_photos')
    book.filename = 'guideBook'
    book.gen()