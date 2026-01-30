from dataStructure.Photo import Photo
from dataStructure.Topo import Topo
from dataStructure.AreaMap import AreaMap
from dataStructure.SubAreaMap import SubAreaMap
from data.GB_Book import book

Topo(name='Monorail',
     parent=book.formations['Monorail'],
     paths={
        'topo_o': r'./images/maps/topos/Quartz/',
        'topo_i': r'./images/maps/topos/Quartz/'},
     file_name='Monorail.svg',
     size='f',
     routes={
         'path973':book.climbs['Deliverance'],
         'path975':book.climbs['Deliverance'],
         'path446':book.climbs['Deliverance'],
         'path448':book.climbs['Deliverance Low'],
         'path502':book.climbs['Deliverance Low'],
         'path971':book.climbs['Monorail Extension Project'],
         'path969':book.climbs['Monorail Extension Project'],
         'path967':book.climbs['Monorail'],
         'path763':book.climbs['Monorail'],
         'path634':book.climbs['Trivial Solution'],
         'path632':book.climbs['Trivial Solution'],
     })
Topo(name='Yo Mamma',
     parent=book.formations['Yo Mamma Boulder'],
     paths={
        'topo_o': r'./images/maps/topos/Quartz/',
        'topo_i': r'./images/maps/topos/Quartz/'},
     file_name='YoMamma.svg',
     size='h',
     border='rect966',
     routes={
         'path955':book.climbs['Ugly Face'],
         'path953':book.climbs['Ugly Face'],
         'path951':book.climbs['Binding of Isaac'],
         'path947':book.climbs['Binding of Isaac'],
     })
Topo(name='4.5',
     parent=book.formations['The 4.5'],
     paths={
        'topo_o': r'./images/maps/topos/Quartz/',
        'topo_i': r'./images/maps/topos/Quartz/'},
     file_name='45.svg',
     size='f',
     border='rect1383',
     routes={
         'path1329':book.climbs['Falcon\'s Reach'],
         'path1323':book.climbs['Falcon\'s Reach'],
         'path1327':book.climbs['Teenage Libertarians'],
         'path1321':book.climbs['Teenage Libertarians'],
         'path499':book.climbs['Step on my Beard'],
         'path445':book.climbs['Step on my Beard'],
         'path1325':book.climbs['Chicken Tendies'],
         'path764': book.climbs['Chicken Tendies'],
     })
Topo(name='Dab Rig',
     parent=book.formations['The Dab Rig'],
     paths={
        'topo_o': r'./images/maps/topos/Quartz/',
        'topo_i': r'./images/maps/topos/Quartz/'},
     file_name='DabRig.svg',
     size='f',
     routes={
         'path456':book.climbs['Dank Commander'],
         'path454':book.climbs['Dank Commander'],
         'path452':book.climbs['Unsalted Almonds'],
         'path398':book.climbs['Unsalted Almonds'],
         'path300':book.climbs['Unsalted Almonds'],
     })
           
if __name__ == '__main__':
    sys.exit()
