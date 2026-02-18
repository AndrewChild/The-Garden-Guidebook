from dataStructure.Photo import Photo
from dataStructure.Topo import Topo
from dataStructure.AreaMap import AreaMap
from dataStructure.SubAreaMap import SubAreaMap
from data.GB_Book import book

Topo(name='Story of O',
     parent=book.formations['The Story of O Boulder'],
     paths={
        'topo_o': r'./images/maps/topos/Upper/',
        'topo_i': r'./images/maps/topos/Upper/'},
     file_name='storyO.svg',
     size='f',
     loc='e',
     border='rect878',
     routes={
         'path820':book.climbs['wikiFeet'],
         'path818':book.climbs['wikiFeet'],
         'path824':book.climbs['Arnold Palmer'],
         'path822':book.climbs['Arnold Palmer'],
         'path762':book.climbs['Santa Cruz Ski Trip'],
         'path760':book.climbs['Santa Cruz Ski Trip'],
         'path758':book.climbs['The Story of O'],
         'path707':book.climbs['The Story of O'],
     })
Topo(name='Hoggin Dogs',
     parent=book.formations['Titanium Boulder'],
     paths={
        'topo_o': r'./images/maps/topos/Upper/',
        'topo_i': r'./images/maps/topos/Upper/'},
     file_name='hogginDogs.svg',
     size='f',
     loc='e',
     border='rect1047',
     routes={
         'path1033':book.climbs['Bilbo Baggins'],
         'path1031':book.climbs['Bilbo Baggins'],
         'path1029':book.climbs['Loggin Bogs'],
         'path1027':book.climbs['Loggin Bogs'],
         'path1025':book.climbs['Häagen Dogs'],
         'path1023':book.climbs['Häagen Dogs'],
         'path1021':book.climbs['Häagen Dogs'],
     })
Topo(name='Titanium',
     parent=book.climbs['Titanium'],
     paths={
        'topo_o': r'./images/maps/topos/Upper/',
        'topo_i': r'./images/maps/topos/Upper/'},
     file_name='titanium.svg',
     size='h',
     border='rect1180',
     routes={
         'path1178':book.climbs['Titanium'],
         'path1176':book.climbs['Titanium'],
     })
Topo(name='Foxglove',
     parent=book.formations['Foxglove Boulder'],
     paths={
        'topo_o': r'./images/maps/topos/Upper/',
        'topo_i': r'./images/maps/topos/Upper/'},
     file_name='foxglove.svg',
     size='h',
     loc='e',
     border='rect1328',
     routes={
         'path1319':book.climbs['Foxglove'],
         'path1317':book.climbs['Foxglove'],
     })
Topo(name='Pumpkin',
     parent=book.formations['Pumpkin'],
     paths={
        'topo_o': r'./images/maps/topos/Upper/',
        'topo_i': r'./images/maps/topos/Upper/'},
     file_name='pSpice.svg',
     size='h',
     border='rect1616',
     routes={
         'path887':book.climbs['Pumpkin Spice'],
         'path885':book.climbs['Pumpkin Spice'],
         'path883':book.climbs['Pumpkin Spice'],
         'path695':book.climbs['Ice Spice'],
         'path749':book.climbs['Ice Spice'],
         'path693':book.climbs['Ice Spice'],
     })
Topo(name='Baseball',
     parent=book.formations['Baseball'],
     paths={
        'topo_o': r'./images/maps/topos/Upper/',
        'topo_i': r'./images/maps/topos/Upper/'},
     file_name='baseball.svg',
     size='h',
     routes={
         'path349':book.climbs['Baseball'],
         'path293':book.climbs['Baseball'],
         'path351':book.climbs['Bunt'],
         'path295':book.climbs['Bunt'],
     })
Topo(name='Bread Loaf',
     parent=book.routes['Worf'],
     paths={
        'topo_o': r'./images/maps/topos/Upper/',
        'topo_i': r'./images/maps/topos/Upper/'},
     file_name='breadLoaf.svg',
     size='f',
     border='rect1397',
     routes={
         'path2171':book.climbs['Bread Heel'],
         'path2169':book.climbs['Bread Heel'],
         'path543':book.climbs['Bread Loaf Left'],
         'path1100':book.climbs['Bread Loaf Left'],
         'path1104':book.climbs['Bread Loaf Traverse'],
         'path1153':book.climbs['Bread Loaf Traverse'],
         'path390':book.climbs['Breadwinner'],
         'path444':book.climbs['Breadwinner'],
         'path1155':book.climbs['Baker\'s Dozen'],
         'path1157':book.climbs['Baker\'s Dozen'],
     })
Topo(name='Bread Loaf2',
     parent=book.routes['Worf'],
     paths={
        'topo_o': r'./images/maps/topos/Upper/',
        'topo_i': r'./images/maps/topos/Upper/'},
     file_name='breadLoaf2.svg',
     size='h',
     loc='e',
     routes={
         'path1350':book.climbs['Worf'],
         'path1346':book.climbs['Worf'],
     })
Topo(name='Scratch and Spliff',
      parent=book.subareas['The Bread Loaves'],
      paths={
         'topo_o': r'./images/maps/topos/Upper/',
         'topo_i': r'./images/maps/topos/Upper/'},
      file_name='scratchSpliff4.svg',
      size='p',
      loc='e',
      routes={
          'path2067':book.climbs['Scratch and Spliff Traverse'],
          'path2065':book.climbs['Scratch and Spliff Traverse'],
          'path2080':book.climbs['Spliff'],
          'path2075':book.climbs['Spliff'],
          'path2077':book.climbs['Scratch'],
          'path2073':book.climbs['Scratch'],
          'path2071':book.climbs['Late Start'],
          'path2069':book.climbs['Late Start'],
          'path1921':book.climbs['Spliff'],
          'path1919':book.climbs['Spliff'],
          'path1925':book.climbs['Scratch and Spliff Traverse'],
          'path1923':book.climbs['Scratch and Spliff Traverse'],
          'path1917':book.climbs['Roach'],
          'path1915':book.climbs['Roach'],
          'path2515':book.climbs['For What it\'s Worth'],
          'path2513':book.climbs['For What it\'s Worth'],
      })
# Topo(name='Scratch and Spliff',
#      parent=book.formations['Scratch and Spliff'],
#      paths={
#         'topo_o': r'./images/maps/topos/Upper/',
#         'topo_i': r'./images/maps/topos/Upper/'},
#      file_name='scratchSpliff.svg',
#      size='f',
#      loc='e',
#      routes={
#          'path1921':book.climbs['Spliff'],
#          'path1919':book.climbs['Spliff'],
#          'path1925':book.climbs['Scratch and Spliff Traverse'],
#          'path1923':book.climbs['Scratch and Spliff Traverse'],
#          'path1917':book.climbs['Roach'],
#          'path1915':book.climbs['Roach'],
#          'path2515':book.climbs['For What it\'s Worth'],
#          'path2513':book.climbs['For What it\'s Worth'],
#      })
# Topo(name='Scratch and Spliff 2',
#      parent=book.routes['Spliff'],
#      paths={
#         'topo_o': r'./images/maps/topos/Upper/',
#         'topo_i': r'./images/maps/topos/Upper/'},
#      file_name='scratchSpliff2.svg',
#      size='f',
#      loc='e',
#      routes={
#          'path2067':book.climbs['Scratch and Spliff Traverse'],
#          'path2065':book.climbs['Scratch and Spliff Traverse'],
#          'path2080':book.climbs['Spliff'],
#          'path2075':book.climbs['Spliff'],
#          'path2077':book.climbs['Scratch'],
#          'path2073':book.climbs['Scratch'],
#          'path2071':book.climbs['Late Start'],
#          'path2069':book.climbs['Late Start'],
#      })
Topo(name='Scratch and Spliff 3',
     parent=book.routes['Caliban\'s War'],
     paths={
        'topo_o': r'./images/maps/topos/Upper/',
        'topo_i': r'./images/maps/topos/Upper/'},
     file_name='scratchSpliff3.svg',
     size='h',
     routes={
         'path2226':book.climbs['Caliban\'s War'],
         'path2224':book.climbs['Caliban\'s War'],
         'path2222':book.climbs['Caliban\'s War'],
         'path2228':book.climbs['Stoned Age'],
         'path2230':book.climbs['Stoned Age'],
     })
Topo(name='Kick It',
     parent=book.formations['Kick It'],
     paths={
        'topo_o': r'./images/maps/topos/Upper/',
        'topo_i': r'./images/maps/topos/Upper/'},
     file_name='kickIt.svg',
     size='h',
     border='rect653',
     routes={
         'path599':book.climbs['Kick It'],
         'path595':book.climbs['Kick It'],
         'path597':book.climbs['Kick It'],
     })
Topo(name='Algebra',
     parent=book.formations['Algebra'],
     paths={
        'topo_o': r'./images/maps/topos/Upper/',
        'topo_i': r'./images/maps/topos/Upper/'},
     file_name='algebra.svg',
     size='h',
     border='rect650',
     routes={
         'path648':book.climbs['Algebra'],
         'path646':book.climbs['Algebra'],
         'path644':book.climbs['Algebra'],
     })
Topo(name='MGB',
     parent=book.formations['Mega Good Boulder'],
     paths={
        'topo_o': r'./images/maps/topos/Upper/',
        'topo_i': r'./images/maps/topos/Upper/'},
     file_name='MGB.svg',
     size='h',
     border='rect401',
     routes={
         'path347':book.climbs['MGB'],
         'path293':book.climbs['MGB'],
     })
Topo(name='Dr. Strangelove',
     parent=book.formations['Dr. Strangelove'],
     paths={
        'topo_o': r'./images/maps/topos/Upper/',
        'topo_i': r'./images/maps/topos/Upper/'},
     file_name='strangeLove.svg',
     size='h',
     border='rect808',
     routes={
         'path797':book.climbs['War Room'],
         'path795':book.climbs['War Room'],
         'path793':book.climbs['Dr. Strangelove'],
         'path791':book.climbs['Dr. Strangelove'],
     })
Topo(name='Crack',
     parent=book.formations['Crack Boulder'],
     paths={
        'topo_o': r'./images/maps/topos/Upper/',
        'topo_i': r'./images/maps/topos/Upper/'},
     file_name='crack.svg',
     size='h',
     border='rect505',
     routes={
         'path451':book.climbs['Crack 2'],
         'path449':book.climbs['Crack 2'],
         'path445':book.climbs['Jugs'],
         'path391':book.climbs['Jugs'],
     })
Topo(name='Machete Monkey',
     parent=book.formations['Machete Monkey'],
     paths={
        'topo_o': r'./images/maps/topos/Upper/',
        'topo_i': r'./images/maps/topos/Upper/'},
     file_name='machete.svg',
     size='h',
     border='rect796',
     routes={
         'path588':book.climbs['Machete Monkey Left'],
         'path586':book.climbs['Machete Monkey Left'],
         'path794':book.climbs['Machete Man'],
         'path790':book.climbs['Machete Man'],
         'path792':book.climbs['Machete Monkey'],
         'path788':book.climbs['Machete Monkey'],
     })
Topo(name='June 24th',
     parent=book.formations['June 24th'],
     paths={
        'topo_o': r'./images/maps/topos/Upper/',
        'topo_i': r'./images/maps/topos/Upper/'},
     file_name='June24.svg',
     size='h',
     border='rect943',
     routes={
         'path941':book.climbs['June 24th'],
         'path939':book.climbs['June 24th'],
         'path937':book.climbs['June 1'],
         'path935':book.climbs['June 1'],
         'path1016':book.climbs['June 69th High Start'],
         'path1018':book.climbs['June 69th High Start'],
         'path1020':book.climbs['June 69th'],
         'path1022':book.climbs['June 69th'],
     })
Topo(name='Young Ju¢y',
     parent=book.formations['Young Ju¢y'],
     paths={
        'topo_o': r'./images/maps/topos/Upper/',
        'topo_i': r'./images/maps/topos/Upper/'},
     file_name='young.svg',
     size='f',
     loc='b',
     routes={
         'path572':book.climbs['Loosey Ju¢y'],
         'path570':book.climbs['Loosey Ju¢y'],
         'path568':book.climbs['Juice WRLD'],
         'path418':book.climbs['Juice WRLD'],
         'path1086':book.climbs['Young Ju¢y'],
         'path1084':book.climbs['Young Ju¢y'],
         'path1082':book.climbs['Young Ju¢y'],
     })
Topo(name='Duck Twirler',
     parent=book.formations['Duck Twirler'],
     paths={
        'topo_o': r'./images/maps/topos/Upper/',
        'topo_i': r'./images/maps/topos/Upper/'},
     file_name='duckTwirl.svg',
     size='f',
     loc='b',
     width='0.8',
     routes={
         'path758':book.climbs['Screaming at a Wall'],
         'path704':book.climbs['Screaming at a Wall'],
         'path702':book.climbs['Screaming at a Wall'],
         'path1223':book.climbs['Anti-Tiff'],
         'path1225':book.climbs['Anti-Tiff'],
         'path1227':book.climbs['Duck Twirler'],
         'path1229':book.climbs['Duck Twirler'],
         'path1231':book.climbs['Duck Twirler'],
         'path1233':book.climbs['Deforestation'],
         'path1235':book.climbs['Deforestation'],
         'path1237':book.climbs['Deforestation'],
     })
Topo(name='Duck Twirler 2',
     parent=book.formations['Duck Twirler'],
     paths={
        'topo_o': r'./images/maps/topos/Upper/',
        'topo_i': r'./images/maps/topos/Upper/'},
     file_name='duckTwirl2.svg',
     size='h',
     format_options=['fill_to_bottom'],
     loc='e',
     routes={
         'path1379':book.climbs['DT 1'],
         'path1381':book.climbs['DT 1'],
         'path1383':book.climbs['DT 1'],
         'path1385':book.climbs['Anti-Tiff'],
         'path1387':book.climbs['Anti-Tiff'],
     })
Topo(name='Deep Sea Diver',
     parent=book.formations['Deep Sea Diver'],
     paths={
        'topo_o': r'./images/maps/topos/Upper/',
        'topo_i': r'./images/maps/topos/Upper/'},
     file_name='deepSea.svg',
     size='f',
     loc='b',
     border='rect513',
     routes={
         'path459':book.climbs['DSD 4'],
         'path457':book.climbs['DSD 4'],
         'path453':book.climbs['DSD 3'],
         'path451':book.climbs['DSD 3'],
         'path449':book.climbs['Ya Ya Crack'],
         'path447':book.climbs['Ya Ya Crack'],
         'path443':book.climbs['Deep Sea Diver'],
         'path293':book.climbs['Deep Sea Diver'],
     })
Topo(name='Back Seat Driver',
     parent=book.formations['Back Seat Driver'],
     paths={
        'topo_o': r'./images/maps/topos/Upper/',
        'topo_i': r'./images/maps/topos/Upper/'},
     file_name='back_seat_driver.svg',
     size='h',
     border='rect1318',
     routes={
         'path1316':book.climbs['Back Seat Driver'],
         'path1314':book.climbs['Back Seat Driver'],
     })
Topo(name='Jaws',
     parent=book.formations['Jaws'],
     paths={
        'topo_o': r'./images/maps/topos/Upper/',
        'topo_i': r'./images/maps/topos/Upper/'},
     file_name='Jaws.svg',
     size='h',
     loc='b',
     border='rect559',
     routes={
         'path451':book.climbs['Remora'],
         'path449':book.climbs['Remora'],
         'path351':book.climbs['Remora'],
         'path349':book.climbs['Jaws'],
         'path295':book.climbs['Jaws'],
         'path293':book.climbs['Jaws'],
     })
Topo(name='Prince Albert',
     parent=book.formations['Prince Albert'],
     paths={
        'topo_o': r'./images/maps/topos/Upper/',
        'topo_i': r'./images/maps/topos/Upper/'},
     file_name='princeAlbert.svg',
     size='h',
     loc='e',
     border='rect1003',
     routes={
         'path449':book.climbs['PA 2'],
         'path447':book.climbs['PA 2'],
         'path445':book.climbs['Prince Albert'],
         'path391':book.climbs['Prince Albert'],
         'path293':book.climbs['Prince Albert'],
     })
     

if __name__ == '__main__':
    sys.exit()
