from dataStructure.Book import Book


book = Book(
    name='The Garden',
    collaborators=['Andrew Child'],
    repo='https://andrewchild.github.io/The-Garden-Guidebook/',
    dl='https://github.com/AndrewChild/The-Garden-Guidebook/raw/main/guideBook.pdf',
    paths={
        'LaTeXTemplates': '../LocalBoulders/templates/',
        'LaTeXOut': './sections/',
        'pdf': './',
        'photos': './images/photos/',
        'graphics': './images/maps',
        'histogram_o': './images/maps/plots/',
        'qr_o': './images/maps/qr/',
        'topo_i': './images/maps/topos/',
        'topo_o': './images/maps/topos/',
        'subarea_i': './images/maps/area/',
        'subarea_o': './images/maps/area/out/',
        'area_i': './images/maps/area/',
        'area_o': './images/maps/area/out/',
    },
)



if __name__ == '__main__':
    sys.exit()
