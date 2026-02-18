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
    special_thanks=[
    'The Willamette Valley Climbers Coalition',
    'The Valley Rock Gym Climbing Community',
    'Austin Alexander',
    'Eric Brown',
    'Mitchel Brown',
    'Kerstin Cullen',
    'Frankie D',
    'Carson Denison',
    'Jonah Koilpillai',
    'Jonah Krietzburg',
    'Ed Friesen',
    'Michael Gardener-Brown',
    'Rose Holdorf',
    'Craig Malik',
    'Cyrus McDowell',
    'Jayson Nissen',
    'Catrina Nowakowski',
    'Zach Radke',
    'Matt Slayton',
    'Griffin Thoms',
    'Silas Thoms',
    'Paul Waters',
    'Cameron Watson',
    'Andrew Young',
    ],
    format_options = ['skip_acknowledgments']
)



if __name__ == '__main__':
    sys.exit()
