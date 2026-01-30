from dataStructure.Photo import Photo
from dataStructure.Topo import Topo
from dataStructure.AreaMap import AreaMap
from dataStructure.SubAreaMap import SubAreaMap
from data.GB_Book import book 

Topo(name='Farley',
     parent=book.routes['Belushi'],
     paths={
        'topo_o': r'./images/maps/topos/PinkTag/',
        'topo_i': r'./images/maps/topos/PinkTag/'},
     file_name='farley.svg',
     size='f',
     routes={
         'path2245':book.climbs['Farley Prep'],
         'path2243':book.climbs['Farley Prep'],
         'path2241':book.climbs['Farley Prep'],
         'path2239':book.climbs['Le Lemét'],
         'path2237':book.climbs['Le Lemét'],
         'path2232':book.climbs['Lippity Split'],
         'path2228':book.climbs['Lippity Split'],
         'path2230':book.climbs['Belushi'],
         'path2226':book.climbs['Belushi'],
     })
Topo(name='Frat House',
     parent=book.formations['Frat House'],
     paths={
        'topo_o': r'./images/maps/topos/PinkTag/',
        'topo_i': r'./images/maps/topos/PinkTag/'},
     file_name='fratHouse.svg',
     size='h',
     border='rect1761',
     routes={
         'path1063':book.climbs['Frat Mouse'],
         'path1061':book.climbs['Frat Mouse'],
         'path1059':book.climbs['Frat House'],
         'path1057':book.climbs['Frat House'],
     })
Topo(name='Jonah\'s Dab Rig',
     parent=book.formations['Jonah\'s Dab Rig'],
     paths={
        'topo_o': r'./images/maps/topos/PinkTag/',
        'topo_i': r'./images/maps/topos/PinkTag/'},
     file_name='jonah.svg',
     size='h',
     routes={
         'path1028':book.climbs['Jonah\'s Dab Rig'],
         'path1030':book.climbs['Jonah\'s Dab Rig'],
         'path1032':book.climbs['Jonah\'s Dab Rig'],
         'path1034':book.climbs['Workshop 68'],
         'path1036':book.climbs['Workshop 68'],
     })
Topo(name='Aquamarine',
     parent=book.formations['Aquamarine'],
     paths={
        'topo_o': r'./images/maps/topos/PinkTag/',
        'topo_i': r'./images/maps/topos/PinkTag/'},
     file_name='aquamarine.svg',
     border='rect1173',
     size='h',
     routes={
         'path1165':book.climbs['Aquamarine'],
         'path1161':book.climbs['Aquamarine'],
         'path1163':book.climbs['Aquamarine'],
         'path1171':book.climbs['Stone Ocean'],
         'path1167':book.climbs['Stone Ocean'],
         'path1169':book.climbs['Stone Ocean'],
     })
Topo(name='Territorial Pissings',
     parent=book.formations['Pissing Boulder'],
     paths={
        'topo_o': r'./images/maps/topos/PinkTag/',
        'topo_i': r'./images/maps/topos/PinkTag/'},
     file_name='pissings.svg',
     size='h',
     routes={
         'path1462':book.climbs['Territorial Pissings'],
         'path1460':book.climbs['Territorial Pissings'],
     })
           
if __name__ == '__main__':
    sys.exit()
