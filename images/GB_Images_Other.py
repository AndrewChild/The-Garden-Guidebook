from dataStructure.Photo import Photo
from dataStructure.Topo import Topo
from dataStructure.AreaMap import AreaMap
from dataStructure.SubAreaMap import SubAreaMap
from data.GB_Book import book

Topo(name='Big Iron',
     parent=book.formations['Big Iron'],
     paths={
        'topo_o': r'./images/maps/topos/Other/',
        'topo_i': r'./images/maps/topos/Other/'},
     file_name='bigIron.svg',
     size='h',
     loc='b',
     border='rect522',
     routes={
         'path456': book.climbs['No Stone Unturned'],
         'path454': book.climbs['No Stone Unturned'],
         'path452': book.climbs['Big Iron Direct'],
         'path450': book.climbs['Big Iron Direct'],
         'path445': book.climbs['Big Iron'],
         'path447': book.climbs['Big Iron'],
         'path293': book.climbs['Big Iron'],
     })
Topo(name='Wild Roses',
     parent=book.climbs['Wild Roses'],
     paths={
        'topo_o': r'./images/maps/topos/Other/',
        'topo_i': r'./images/maps/topos/Other/'},
     file_name='wildRoses.svg',
     size='h',
     routes={
         'path666': book.climbs['Wild Roses'],
         'path664': book.climbs['Wild Roses'],
     })
           
if __name__ == '__main__':
    sys.exit()
