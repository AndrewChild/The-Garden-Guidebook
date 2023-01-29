import sys
sys.path.insert(1, '../LocalBoulders')
from dataStructure import *


book = Book(
    name='The Garden Boulders',
    collaborators=['Andrew Child'],
    repo='https://github.com/AndrewChild/The-Garden-Guidebook',
    dl='https://github.com/AndrewChild/The-Garden-Guidebook/raw/main/guideBook.pdf',
    options={'topos_attached_to_routes': True},
)



if __name__ == '__main__':
    sys.exit()




if __name__ == '__main__':
    book.paths['LaTeXTemplates'] = '../LocalBoulders/templates/'
    book.paths['LaTeXOut'] = './sections/'
    book.paths['pdf'] = './'
    book.gen()
