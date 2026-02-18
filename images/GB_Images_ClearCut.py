from dataStructure.Photo import Photo
from dataStructure.Topo import Topo
from dataStructure.AreaMap import AreaMap
from dataStructure.SubAreaMap import SubAreaMap
from data.GB_Book import book

Topo(name='Star Gazer',
     parent=book.formations['Star Gazer'],
     paths={
        'topo_o': r'./images/maps/topos/ClearCut/',
        'topo_i': r'./images/maps/topos/ClearCut/'},
     file_name='StarGazer.svg',
     size='h',
     loc='b',
     border='rect463',
     routes={
         'path293':book.climbs['Galileo'],
         'path347':book.climbs['Galileo'],
         'path349':book.climbs['Fleming'],
         'path351':book.climbs['Fleming'],
         'path353':book.climbs['Huygens'],
         'path355':book.climbs['Huygens'],
     })
Topo(name='Dig Dug',
     parent=book.formations['Dig Dug'],
     paths={
        'topo_o': r'./images/maps/topos/ClearCut/',
        'topo_i': r'./images/maps/topos/ClearCut/'},
     file_name='DigDug.svg',
     size='f',
     loc='b',
     border='rect728',
     routes={
         'path726':book.climbs['Tear Duct Finish'],
         'path724':book.climbs['Tear Duct Finish'],
         'path722':book.climbs['Tear Duct Direct'],
         'path718':book.climbs['Tear Duct Direct'],
         'path720':book.climbs['Tear Duct'],
         'path716':book.climbs['Tear Duct'],
         'path714':book.climbs['Fly Guy SDS'],
         'path712':book.climbs['Fly Guy SDS'],
         'path710':book.climbs['Fly Guy'],
         'path708':book.climbs['Fly Guy'],
         'path706':book.climbs['Mud Flaps'],
         'path608':book.climbs['Mud Flaps'],
         'path606':book.climbs['Skrunch'],
         'path604':book.climbs['Skrunch'],
     })
Topo(name='Grizzly Face',
     parent=book.formations['Grizzly Face'],
     paths={
        'topo_o': r'./images/maps/topos/ClearCut/',
        'topo_i': r'./images/maps/topos/ClearCut/'},
     file_name='GrizzlyFace.svg',
     size='h',
     format_options=['fill_to_bottom'],
     loc='b',
     border='rect889',
     routes={
         'path887':book.climbs['Baloo'],
         'path885':book.climbs['Baloo'],
         'path883':book.climbs['Br\'er Bear'],
         'path877':book.climbs['Br\'er Bear'],
     })
Topo(name='Bear Back',
     parent=book.formations['Bear Back'],
     paths={
        'topo_o': r'./images/maps/topos/ClearCut/',
        'topo_i': r'./images/maps/topos/ClearCut/'},
     file_name='BearBack.svg',
     size='f',
     loc='b',
     border='rect1044',
     routes={
         'path1042':book.climbs['Chet Ripley'],
         'path1040':book.climbs['Chet Ripley'],
         'path1038':book.climbs['Roman Craig'],
         'path1036':book.climbs['Roman Craig'],
         'path1034':book.climbs['Wally'],
         'path1032':book.climbs['Wally'],
         'path1030':book.climbs['Bald Bear'],
         'path1028':book.climbs['Bald Bear'],
     })
Topo(name='Double Stump',
     parent=book.formations['Double Stump'],
     paths={
        'topo_o': r'./images/maps/topos/ClearCut/',
        'topo_i': r'./images/maps/topos/ClearCut/'},
     file_name='DoubleStump.svg',
     size='h',
     format_options=['fill_to_bottom'],
     loc='b',
     border='rect1199',
     routes={
         'path1197':book.climbs['Double Stump Project Right'],
         'path1195':book.climbs['Double Stump Project Right'],
         'path1193':book.climbs['Double Stump Project'],
         'path1191':book.climbs['Double Stump Project'],
         'path1189':book.climbs['Ballistics Dummy'],
         'path1187':book.climbs['Ballistics Dummy'],
     })
Topo(name='Double Stump 2',
     parent=book.climbs['Chump Mantle'],
     paths={
        'topo_o': r'./images/maps/topos/ClearCut/',
        'topo_i': r'./images/maps/topos/ClearCut/'},
     file_name='DoubleStump2.svg',
     size='h',
     format_options=['fill_to_bottom'],
     loc='b',
     border='rect1344',
     routes={
         'path1342':book.climbs['Chump Mantle'],
         'path1340':book.climbs['Chump Mantle'],
     })
Topo(name='Cuneiform',
     parent=book.formations['Cuneiform'],
     paths={
        'topo_o': r'./images/maps/topos/ClearCut/',
        'topo_i': r'./images/maps/topos/ClearCut/'},
     file_name='Cuneiform.svg',
     size='f',
     format_options=['fill_to_bottom'],
     loc='b',
     border='rect1497',
     routes={
         'path1495':book.climbs['Eridu'],
         'path1493':book.climbs['Eridu'],
         'path1491':book.climbs['Cuneiform Project'],
         'path1489':book.climbs['Cuneiform Project'],
         'path1487':book.climbs['Walk the Line'],
         'path1485':book.climbs['Walk the Line'],
         'path1483':book.climbs['Cuneiform1'],
         'path1481':book.climbs['Cuneiform1'],
     })
           
if __name__ == '__main__':
    sys.exit()
