from dataStructure.Photo import Photo
from dataStructure.Topo import Topo
from dataStructure.AreaMap import AreaMap
from dataStructure.SubAreaMap import SubAreaMap
from data.GB_Book import book

Topo(name='Bitchin Corners',
     parent=book.formations['Bitchin Corners'],
     paths={
        'topo_o': r'./images/maps/topos/Main/',
        'topo_i': r'./images/maps/topos/Main/'},
     file_name='bitchin.svg',
     size='h',
     loc='e',
     border='rect362',
     routes={
         'path368':book.climbs['Left Corner'],
         'path314':book.climbs['Left Corner'],
         'path1002':book.climbs['Bitchin Corners'],
         'path1029':book.climbs['Bitchin Corners'],
         'path551':book.climbs['Bitchin Arête'],
         'path450':book.climbs['Bitchin Arête'],
         'path1014':book.climbs['Bitchin Corners Sit'],
         'path1031':book.climbs['Bitchin Corners Sit'],
     })
Topo(name='Baldo',
     parent=book.formations['Baldo'],
     paths={
        'topo_o': r'./images/maps/topos/Main/',
        'topo_i': r'./images/maps/topos/Main/'},
     file_name='baldo.svg',
     size='h',
     routes={
         'path600':book.climbs['Frontside Baldo'],
         'path598':book.climbs['Frontside Baldo'],
     })
Topo(name='Berned',
     parent=book.climbs['All Berned Down'],
     paths={
        'topo_o': r'./images/maps/topos/Main/',
        'topo_i': r'./images/maps/topos/Main/'},
     file_name='berned.svg',
     size='h',
     routes={
         'path744':book.climbs['All Berned Up'],
         'path742':book.climbs['All Berned Up'],
         'path740':book.climbs['All Berned Down'],
         'path738':book.climbs['All Berned Down'],
     })
Topo(name='bigSlab',
     parent=book.climbs['Slabarific'],
     paths={
        'topo_o': r'./images/maps/topos/Main/',
        'topo_i': r'./images/maps/topos/Main/'},
     file_name='bigSlab.svg',
     size='h',
     border='rect291',
     routes={
         'path507':book.climbs['Pockets'],
         'path505':book.climbs['Pockets'],
         'path454':book.climbs['Pockets'],
         'path509':book.climbs['Big Slab Right'],
         'path452':book.climbs['Big Slab Right'],
         'path450':book.climbs['Slabarific'],
         'path347':book.climbs['Slabarific'],
     })
Topo(name='hydro',
     parent=book.climbs['Mini Hydrotube'],
     paths={
        'topo_o': r'./images/maps/topos/Main/',
        'topo_i': r'./images/maps/topos/Main/'},
     file_name='hydro.svg',
     size='h',
     border='rect652',
     routes={
         'path656':book.climbs['Mini Hydrotube'],
         'path654':book.climbs['Mini Hydrotube'],
     })
Topo(name='Classique',
     parent=book.formations['Classique'],
     paths={
        'topo_o': r'./images/maps/topos/Main/',
        'topo_i': r'./images/maps/topos/Main/'},
     file_name='classique.svg',
     size='h',
     routes={
         'path445':book.climbs['Classique'],
         'path391':book.climbs['Classique'],
         'path293':book.climbs['Classique'],
     })
Topo(name='Crazy Cool',
     parent=book.formations['Crazy Cool'],
     paths={
        'topo_o': r'./images/maps/topos/Main/',
        'topo_i': r'./images/maps/topos/Main/'},
     file_name='crazyCool.svg',
     size='h',
     routes={
         'path586':book.climbs['Crazy Cool Arête'],
         'path584':book.climbs['Crazy Cool Arête'],
         'path582':book.climbs['Crazy Cool Arête'],
     })
Topo(name='Overhand',
     parent=book.formations['Overhand'],
     paths={
        'topo_o': r'./images/maps/topos/Main/',
        'topo_i': r'./images/maps/topos/Main/'},
     file_name='overhand2.svg',
     size='h',
     border='rect1016',
     routes={
         'path939':book.climbs['Goosebumps'],
         'path937':book.climbs['Goosebumps'],
         'path935':book.climbs['Goosebumps'],
         'path1177':book.climbs['Overhand'],
         'path1175':book.climbs['Overhand'],
         'path470':book.climbs['Goose Egg'],
         'path416':book.climbs['Goose Egg'],
         'path414':book.climbs['Goose Egg'],
     })
Topo(name='Hueco Wabo',
     parent=book.formations['Hueco Wabo'],
     paths={
        'topo_o': r'./images/maps/topos/Main/',
        'topo_i': r'./images/maps/topos/Main/'},
     file_name='hueco.svg',
     size='h',
     routes={
         'path1918':book.climbs['Hueco Wabo'],
         'path1920':book.climbs['Hueco Wabo'],
     })
Topo(name='Azain Spire',
     parent=book.formations['Azain Spire'],
     paths={
        'topo_o': r'./images/maps/topos/Main/',
        'topo_i': r'./images/maps/topos/Main/'},
     file_name='azainSpire.svg',
     size='h',
     routes={
         'path724':book.climbs['Snakes and Martyrs'],
         'path726':book.climbs['Snakes and Martyrs'],
     })
Topo(name='Three Star Ledge',
     parent=book.formations['Three Star Ledge'],
     paths={
        'topo_o': r'./images/maps/topos/Main/',
        'topo_i': r'./images/maps/topos/Main/'},
     file_name='threeStar2.svg',
     size='h',
     routes={
         'path2023':book.climbs['Three Star Ledge'],
         'path2017':book.climbs['Three Star Ledge'],
     })
Topo(name='The Good',
     parent=book.routes['The Good'],
     paths={
        'topo_o': r'./images/maps/topos/Main/',
        'topo_i': r'./images/maps/topos/Main/'},
     file_name='good.svg',
     size='f',
     routes={
         'path1453':book.climbs['The Good'],
         'path1459':book.climbs['The Good'],
         'path1451':book.climbs['Another'],
         'path1457':book.climbs['Another'],
         'path1445':book.climbs['Next to the Good'],
         'path1447':book.climbs['Next to the Good'],
         'path1449':book.climbs['Next to the Good'],
         'path1455':book.climbs['The Good Slab'],
         'path1461':book.climbs['The Good Slab'],
     })
Topo(name='Fight Club Right Side',
     parent=book.formations['Fight Club'],
     paths={
        'topo_o': r'./images/maps/topos/Main/',
        'topo_i': r'./images/maps/topos/Main/'},
     file_name='fightClub.svg',
     size='h',
     border='rect789',
     routes={
         'path735':book.climbs['Fight Club 2'],
         'path733':book.climbs['Fight Club 2'],
         'path731':book.climbs['The Ear'],
         'path729':book.climbs['The Ear'],
         'path727':book.climbs['Fight Club'],
         'path725':book.climbs['Fight Club'],
     })
Topo(name='Fight Club Left Side',
     parent=book.routes['Fight Club 2'],
     paths={
        'topo_o': r'./images/maps/topos/Main/',
        'topo_i': r'./images/maps/topos/Main/'},
     file_name='fightClub2.svg',
     size='h',
     routes={
         'path1297':book.climbs['Fight Club 2'],
         'path1303':book.climbs['Fight Club 2'],
         'path1299':book.climbs['Fight Club'],
         'path1301':book.climbs['Fight Club'],
         'path1293':book.climbs['Brewmaster'],
         'path1305':book.climbs['Brewmaster'],
     })
Topo(name='E\'s Dirty B',
     parent=book.formations['E\'s Dirty B'],
     paths={
        'topo_o': r'./images/maps/topos/Main/',
        'topo_i': r'./images/maps/topos/Main/'},
     file_name='eDirty.svg',
     size='h',
     routes={
         'path446':book.climbs['Green Hell'],
         'path290':book.climbs['Green Hell'],
         'path1003':book.climbs['E\'s Dirty B'],
         'path1005':book.climbs['E\'s Dirty B'],
         'path444':book.climbs['Unknown on E\'s Dirty B'],
         'path388':book.climbs['Unknown on E\'s Dirty B'],
     })
Topo(name='Car Alarm Downhill Side',
     parent=book.routes['White Rhino'],
     paths={
        'topo_o': r'./images/maps/topos/Main/',
        'topo_i': r'./images/maps/topos/Main/'},
     file_name='carAlarm.svg',
     size='f',
     routes={
         'path674':book.climbs['Car Alarm Traverse'],
         'path676':book.climbs['Car Alarm Traverse'],
         'path670':book.climbs['White Rhino'],
         'path678':book.climbs['White Rhino'],
         'path668':book.climbs['2 Ton Chevy'],
         'path680':book.climbs['2 Ton Chevy'],
         'path666':book.climbs['Pup Truck'],
         'path682':book.climbs['Pup Truck'],
     })
Topo(name='Car Alarm Uphill Side',
     parent=book.routes['Comp Route'],
     paths={
        'topo_o': r'./images/maps/topos/Main/',
        'topo_i': r'./images/maps/topos/Main/'},
     file_name='carAlarm2.svg',
     size='h',
     routes={
         'path824':book.climbs['Comp Route'],
         'path863':book.climbs['Comp Route'],
         'path851':book.climbs['Panic Button'],
         'path861':book.climbs['Panic Button'],
         'path857':book.climbs['Panic Button Variation'],
         'path859':book.climbs['Panic Button Variation'],
     })
Topo(name='Boys in the Woods',
     parent=book.formations['Boys In the Woods'],
     paths={
        'topo_o': r'./images/maps/topos/Main/',
        'topo_i': r'./images/maps/topos/Main/'},
     file_name='BITW.svg',
     size='f',
     routes={
         'path1322':book.climbs['Tabor Tots'],
         'path1320':book.climbs['Tabor Tots'],
         'path300':book.climbs['Boys in the Woods'],
         'path458':book.climbs['Boys in the Woods'],
         'path1485':book.climbs['Cuba Gooding'],
         'path460':book.climbs['Cuba Gooding'],
         'path400':book.climbs['Ice Cubes Shiny Jerry Curl'],
         'path462':book.climbs['Ice Cubes Shiny Jerry Curl'],
         'path404':book.climbs['Tree Slab'],
         'path464':book.climbs['Tree Slab'],
         'path480':book.climbs['EZe'],
         'path426':book.climbs['EZe'],
     })
Topo(name='Turd Party',
     parent=book.formations['Party Boulder'],
     paths={
        'topo_o': r'./images/maps/topos/Main/',
        'topo_i': r'./images/maps/topos/Main/'},
     file_name='turdParty.svg',
     size='h',
     border='rect1578',
     routes={
         'path1524':book.climbs['Turd Party UR Invited'],
         'path1522':book.climbs['Turd Party UR Invited'],
         'path1520':book.climbs['Turd Party UR Invited'],
     })
Topo(name='E7',
     parent=book.routes['E\'s'],
     paths={
        'topo_o': r'./images/maps/topos/Main/',
        'topo_i': r'./images/maps/topos/Main/'},
     file_name='E7.svg',
     size='h',
     border='rect1475',
     routes={
         'path1378':book.climbs['E\'s'],
         'path1376':book.climbs['E\'s'],
         'path1380':book.climbs['Z\'s VB'],
         'path1382':book.climbs['Z\'s VB'],
         'path763':book.climbs['Z\'s VB'],
     })
Topo(name='enchilada',
     parent=book.routes['Enchilada'],
     paths={
        'topo_o': r'./images/maps/topos/Main/',
        'topo_i': r'./images/maps/topos/Main/'},
     file_name='enchilada2.svg',
     size='h',
     routes={
         'path2078':book.climbs['Enchilada'],
         'path2076':book.climbs['Enchilada'],
         'path2086':book.climbs['Enchilada Left Project'],
         'path2084':book.climbs['Enchilada Left Project'],
         'path2082':book.climbs['Enchilada Low Start Project'],
         'path2080':book.climbs['Enchilada Low Start Project'],
     })
Topo(name='little enchilada',
     parent=book.routes['Little Enchilada'],
     paths={
        'topo_o': r'./images/maps/topos/Main/',
        'topo_i': r'./images/maps/topos/Main/'},
     file_name='littleEnchilada.svg',
     size='h',
     border='rect1403',
     routes={
         'path1349':book.climbs['Little Enchilada'],
         'path1347':book.climbs['Little Enchilada'],
     })
Topo(name='Slam dunk',
     parent=book.routes['Slam Dunk'],
     paths={
        'topo_o': r'./images/maps/topos/Main/',
        'topo_i': r'./images/maps/topos/Main/'},
     file_name='eboulder2.svg',
     size='h',
     routes={
         'path623':book.climbs['Layup'],
         'path569':book.climbs['Layup'],
         'path1489':book.climbs['Slam Dunk'],
         'path1487':book.climbs['Slam Dunk'],
         'path474':book.climbs['Baller'],
         'path472':book.climbs['Baller'],
         'path418':book.climbs['Baller'],
         'path416':book.climbs['Baller'],
     })
Topo(name='Gargoyle',
     parent=book.formations['E\'s Boulder'],
     paths={
        'topo_o': r'./images/maps/topos/Main/',
        'topo_i': r'./images/maps/topos/Main/'},
     file_name='eboulder3.svg',
     size='h',
     border='rect292',
     routes={
         'path1625':book.climbs['Gargoyle'],
         'path1627':book.climbs['Gargoyle'],
         'path1631':book.climbs['Gargoyle Direct'],
         'path1629':book.climbs['Gargoyle Direct'],
         'path1635':book.climbs['Slam Dunk'],
         'path1633':book.climbs['Slam Dunk'],
         'path625':book.climbs['Layup'],
         'path627':book.climbs['Layup'],
     })
Topo(name='Bubonic Plague',
     parent=book.formations['Bubonic Plague'],
     paths={
        'topo_o': r'./images/maps/topos/Main/',
        'topo_i': r'./images/maps/topos/Main/'},
     file_name='koan.svg',
     size='h',
     routes={
         'path1777':book.climbs['Bubonic Plague'],
         'path1775':book.climbs['Bubonic Plague'],
     })
Topo(name='Nightcrawler',
     parent=book.formations['Nightcrawler'],
     paths={
        'topo_o': r'./images/maps/topos/Main/',
        'topo_i': r'./images/maps/topos/Main/'},
     file_name='nightCrawler.svg',
     size='h',
     routes={
         'path1342':book.climbs['Nightcrawler'],
         'path1396':book.climbs['Nightcrawler'],
     })
Topo(name='Azain',
     parent=book.routes['Garden Groove'],
     paths={
        'topo_o': r'./images/maps/topos/Main/',
        'topo_i': r'./images/maps/topos/Main/'},
     file_name='azainCrack.svg',
     size='h',
     routes={
         'path445':book.climbs['Sometimes'],
         'path391':book.climbs['Sometimes'],
         'path447':book.climbs['Garden Groove'],
         'path293':book.climbs['Garden Groove'],
         'path1282':book.climbs['Brontosaurus'],
         'path1280':book.climbs['Brontosaurus'],
     })
Topo(name='Blowie',
     parent=book.formations['Azain'],
     paths={
        'topo_o': r'./images/maps/topos/Main/',
        'topo_i': r'./images/maps/topos/Main/'},
     file_name='blowie.svg',
     size='h',
     routes={
         'path527':book.climbs['Ground up Blowie'],
         'path473':book.climbs['Ground up Blowie'],
         'path1143':book.climbs['Piranesi'],
         'path1045':book.climbs['Piranesi'],
     })
Topo(name='Bubbler',
     parent=book.formations['The Bubbler'],
     paths={
        'topo_o': r'./images/maps/topos/Main/',
        'topo_i': r'./images/maps/topos/Main/'},
     file_name='bubbler.svg',
     size='h',
     border='rect1186',
     routes={
         'path1132':book.climbs['Chillum Sit'],
         'path1081':book.climbs['Chillum Sit'],
         'path1079':book.climbs['Chillum'],
         'path1077':book.climbs['Chillum'],
         'path1075':book.climbs['The Bubbler'],
         'path419':book.climbs['The Bubbler'],
     })
Topo(name='Jesus',
     parent=book.formations['Meth Lab'],
     paths={
        'topo_o': r'./images/maps/topos/Main/',
        'topo_i': r'./images/maps/topos/Main/'},
     file_name='jesus.svg',
     size='f',
     routes={
         'path1908':book.climbs['Don\'t Blow the Jug'],
         'path1910':book.climbs['Don\'t Blow the Jug'],
         'path1906':book.climbs['Trust Issues'],
         'path1912':book.climbs['Trust Issues'],
         'path1902':book.climbs['Leave it to Jesus'],
         'path1916':book.climbs['Leave it to Jesus'],
         'path1904':book.climbs['Leave it to Jesus Sit Start'],
         'path1914':book.climbs['Leave it to Jesus Sit Start'],
         'path736':book.climbs['Leave it to Jesus Left'],
         'path734':book.climbs['Leave it to Jesus Left'],
     })
Topo(name='Methlab Backside',
     parent=book.routes['Octernal'],
     paths={
        'topo_o': r'./images/maps/topos/Main/',
        'topo_i': r'./images/maps/topos/Main/'},
     file_name='Methlab.svg',
     size='pr',
     loc = 'e',
     border='rect306',
     routes={
         'path1874':book.climbs['Smackdown'],
         'path1856':book.climbs['Smackdown'],
         'path1876':book.climbs['Harbor Freight'],
         'path1856-2':book.climbs['Harbor Freight'],
         'path921':book.climbs['Harbor Freight Right Exit'],
         'path919':book.climbs['Harbor Freight Right Exit'],
         'path1878':book.climbs['Heisenburg'],
         'path1858':book.climbs['Heisenburg'],
         'path1880':book.climbs['Learys Lunge'],
         'path1860':book.climbs['Learys Lunge'],
         'path1886':book.climbs['Octernal'],
         'path1864':book.climbs['Octernal'],
         'path1884':book.climbs['Guillotine'],
         'path1866':book.climbs['Guillotine'],
         'path1888':book.climbs['Octernal Center Exit'],
         'path1868':book.climbs['Octernal Center Exit'],
         'path1890':book.climbs['Octernal Direct Exit'],
         'path1862':book.climbs['Octernal Direct Exit'],
         'path1892':book.climbs['E\'s'],
         'path1872':book.climbs['E\'s'],
         'path1042':book.climbs['Z\'s VB'],
         'path1039':book.climbs['Z\'s VB'],
     })
Topo(name='octernal2',
     parent=book.routes['Two Blows One Stroke'],
     paths={
        'topo_o': r'./images/maps/topos/Main/',
        'topo_i': r'./images/maps/topos/Main/'},
     file_name='octurnal2.svg',
     size='h',
     routes={
         'path3604':book.climbs['Two Blows One Stroke'],
         'path3553':book.climbs['Octernal Direct Exit'],
         'path3608':book.climbs['Two Blows One Stroke'],
         'path3606':book.climbs['Octernal Direct Exit'],
     })
Topo(name='Locksmith',
     parent=book.formations['Locksmith'],
     paths={
        'topo_o': r'./images/maps/topos/Main/',
        'topo_i': r'./images/maps/topos/Main/'},
     file_name='hula.svg',
     size='h',
     routes={
         'path888':book.climbs['Philanthropy'],
         'path886':book.climbs['Philanthropy'],
         'path883':book.climbs['Brain Hemorrhage'],
         'path879':book.climbs['Brain Hemorrhage'],
         'path881':book.climbs['Locksmith'],
         'path877':book.climbs['Locksmith'],
     })
Topo(name='Philanthropy',
     parent=book.routes['Philanthropy'],
     paths={
        'topo_o': r'./images/maps/topos/Main/',
        'topo_i': r'./images/maps/topos/Main/'},
     file_name='philanthropy.svg',
     size='h',
     routes={
         'path1321':book.climbs['Brain Hemorrhage'],
         'path1319':book.climbs['Brain Hemorrhage'],
         'path1317':book.climbs['Philanthropy'],
         'path1315':book.climbs['Philanthropy'],
         'path1313':book.climbs['Philanthropy']
     })
Topo(name='arboretum2',
     parent=book.routes['Garden Variety'],
     paths={
        'topo_o': r'./images/maps/topos/Main/',
        'topo_i': r'./images/maps/topos/Main/'},
     file_name='childOfGod.svg',
     size='pr',
     border='rect1172',
     routes={
         'path1920':book.climbs['Sebulba'],
         'path1915':book.climbs['Sebulba'],
         'path1917':book.climbs['Eurovision'],
         'path1913':book.climbs['Eurovision'],
         'path1492':book.climbs['Gumby Arête'],
         'path1490':book.climbs['Gumby Arête'],
         'path1488':book.climbs['Bag of Tricks'],
         'path1486':book.climbs['Bag of Tricks'],
         'path1484':book.climbs['The Siren'],
         'path1482':book.climbs['The Siren'],
         'path1480':book.climbs['Somewhere In-Between'],
         'path1478':book.climbs['Somewhere In-Between'],
         'path1476':book.climbs['Somewhere In-Between'],
         'path1474':book.climbs['The Other Berned'],
         'path1472':book.climbs['The Other Berned'],
         'path1470':book.climbs['The Arboretum'],
         'path1468':book.climbs['The Arboretum'],
         'path1466':book.climbs['The Arboretum'],
         'path1464':book.climbs['Garden Project'],
         'path1462':book.climbs['Garden Project'],
         'path1460':book.climbs['Garden Variety'],
         'path903':book.climbs['Garden Variety'],
     })
Topo(name='Chock Stone',
     parent=book.formations['Chock Stone Highball'],
     paths={
        'topo_o': r'./images/maps/topos/Main/',
        'topo_i': r'./images/maps/topos/Main/'},
     file_name='chockstone.svg',
     size='h',
     routes={
         'path1669':book.climbs['Chock Stone Highball'],
         'path1667':book.climbs['Chock Stone Highball'],
     })
Topo(name='All Sorts of Ease',
     parent=book.formations['All Sorts of Ease'],
     paths={
        'topo_o': r'./images/maps/topos/Main/',
        'topo_i': r'./images/maps/topos/Main/'},
     file_name='ease.svg',
     size='h',
     routes={
         'path1938':book.climbs['In the Shadow of Giants'],
         'path1936':book.climbs['In the Shadow of Giants'],
         'path1934':book.climbs['All Sorts of Ease'],
         'path1932':book.climbs['All Sorts of Ease'],
     })
Topo(name='scaryGrandma',
     parent=book.routes['Scary Grandma'],
     paths={
        'topo_o': r'./images/maps/topos/Main/',
        'topo_i': r'./images/maps/topos/Main/'},
     file_name='scaryGrandma.svg',
     size='h',
     routes={
         'path609':book.climbs['Scary Grandma'],
         'path603':book.climbs['Scary Grandma'],
         'path611':book.climbs['Angry Mom'],
         'path605':book.climbs['Angry Mom'],
         'path613':book.climbs['Easy Grandma'],
         'path607':book.climbs['Easy Grandma'],
     })
Topo(name='scaryGrandma2',
     parent=book.formations['Scary Grandma'],
     paths={
        'topo_o': r'./images/maps/topos/Main/',
        'topo_i': r'./images/maps/topos/Main/'},
     file_name='angryMom.svg',
     size='h',
     routes={
         'path447':book.climbs['Easy Grandma'],
         'path391':book.climbs['Easy Grandma'],
         'path445':book.climbs['Angry Mom'],
         'path293':book.climbs['Angry Mom'],
     })
Topo(name='Mini Me',
     parent=book.formations['Mini Me'],
     paths={
        'topo_o': r'./images/maps/topos/Main/',
        'topo_i': r'./images/maps/topos/Main/'},
     file_name='miniMe.svg',
     size='h',
     border='rect505',
     routes={
         'path451':book.climbs['Austin Powers'],
         'path449':book.climbs['Austin Powers'],
         'path447':book.climbs['Austin Powers'],
         'path445':book.climbs['Mini Me'],
         'path391':book.climbs['Mini Me'],
         'path293':book.climbs['Mini Me'],
     })
Topo(name='Mini Me 2',
     parent=book.routes['Dr. Evil'],
     paths={
        'topo_o': r'./images/maps/topos/Main/',
        'topo_i': r'./images/maps/topos/Main/'},
     file_name='drEvil.svg',
     size='h',
     border='rect561',
     routes={
         'path453':book.climbs['Austin Powers'],
         'path451':book.climbs['Austin Powers'],
         'path449':book.climbs['Mr. Bigglesworth'],
         'path351':book.climbs['Mr. Bigglesworth'],
         'path349':book.climbs['Dr. Evil'],
         'path295':book.climbs['Dr. Evil'],
         'path293':book.climbs['Dr. Evil'],
     })
Topo(name='Office',
     parent=book.formations['Crash Test Dummies'],
     paths={
        'topo_o': r'./images/maps/topos/Main/',
        'topo_i': r'./images/maps/topos/Main/'},
     file_name='office.svg',
     size='f',
     border='rect568',
     routes={
         'path460':book.climbs['Dwight Schrute'],
         'path458':book.climbs['Dwight Schrute'],
         'path456':book.climbs['Jim Halpert'],
         'path454':book.climbs['Jim Halpert'],
         'path452':book.climbs['Michael Scott'],
         'path351':book.climbs['Michael Scott'],
         'path449':book.climbs['Daryl Philbin'],
         'path349':book.climbs['Daryl Philbin'],
         'path347':book.climbs['Vince'],
         'path293':book.climbs['Vince'],
     })
Topo(name='Swollen Member',
     parent=book.formations['Swollen Member'],
     paths={
        'topo_o': r'./images/maps/topos/Main/',
        'topo_i': r'./images/maps/topos/Main/'},
     file_name='swollen2.svg',
     size='h',
     routes={
         'path1813':book.climbs['Meth Lab Highball'],
         'path2042':book.climbs['Meth Lab Highball'],
         'path1830':book.climbs['Meth Lab Highball Sit Start'],
         'path2040':book.climbs['Meth Lab Highball Sit Start'],
         'path1832':book.climbs['Meth Lab Highball Right'],
         'path2044':book.climbs['Meth Lab Highball Right'],
         'path1760':book.climbs['Swollen Member'],
         'path1811':book.climbs['Swollen Member'],
         'path2046':book.climbs['Swollen Member'],
     })
Topo(name='Fern Sully',
     parent=book.formations['Fern Sully'],
     paths={
        'topo_o': r'./images/maps/topos/Main/',
        'topo_i': r'./images/maps/topos/Main/'},
     file_name='fern.svg',
     size='h',
     routes={
         'path445':book.climbs['Fern Sully'],
         'path391':book.climbs['Fern Sully'],
         'path293':book.climbs['Fern Sully'],
     })
Topo(name='Southern Discomfort',
     parent=book.formations['Meth Lab'],
     paths={
        'topo_o': r'./images/maps/topos/Main/',
        'topo_i': r'./images/maps/topos/Main/'},
     file_name='soDisco.svg',
     size='h',
     loc='e',
     border='rect646',
     routes={
         'path592':book.climbs['West Arête'],
         'path590':book.climbs['West Arête'],
         'path588':book.climbs['Southern Discomfort'],
         'path586':book.climbs['Southern Discomfort'],
         'path584':book.climbs['Southern Discomfort Direct'],
         'path582':book.climbs['Southern Discomfort Direct'],
     })
Topo(name='Toilet Bowl',
     parent=book.formations['Toilet Bowl'],
     paths={
        'topo_o': r'./images/maps/topos/Main/',
        'topo_i': r'./images/maps/topos/Main/'},
     file_name='toilet.svg',
     size='h',
     routes={
         'path1036':book.climbs['Toilet Bowl Traverse'],
         'path1034':book.climbs['Toilet Bowl Traverse'],
         'path1026':book.climbs['Toilet Bowl'],
         'path1024':book.climbs['Toilet Bowl'],
     })
Topo(name='Tonsil',
     parent=book.routes['Tonsil'],
     paths={
        'topo_o': r'./images/maps/topos/Main/',
        'topo_i': r'./images/maps/topos/Main/'},
     file_name='tonsil2.svg',
     size='h',
     routes={
         'path2317':book.climbs['Gingiva'],
         'path2315':book.climbs['Gingiva'],
         'path2313':book.climbs['Prowed'],
         'path2311':book.climbs['Prowed'],
         'path2309':book.climbs['Tonsil'],
         'path2307':book.climbs['Tonsil'],
         'path2305':book.climbs['Tonsil'],
     })
Topo(name='Geodesic Wiener',
     parent=book.formations['François'],
     paths={
        'topo_o': r'./images/maps/topos/Main/',
        'topo_i': r'./images/maps/topos/Main/'},
     file_name='weiner.svg',
     size='h',
     routes={
         'path2460':book.climbs['Geodesic Wiener'],
         'path2458':book.climbs['Geodesic Wiener'],
         'path995':book.climbs['Geodong'],
         'path290':book.climbs['Geodong'],
         'path999':book.climbs['Pseudorapidity'],
         'path997':book.climbs['Pseudorapidity'],
     })
Topo(name='Trust',
     parent=book.formations['Trust'],
     paths={
        'topo_o': r'./images/maps/topos/Main/',
        'topo_i': r'./images/maps/topos/Main/'},
     file_name='trust.svg',
     size='f',
     border='rect1523',
     routes={
         'path678':book.climbs['Trust'],
         'path830':book.climbs['Trust'],
         'path776':book.climbs['Iron Cross'],
         'path832':book.climbs['Iron Cross'],
         'path834':book.climbs['Project Mayhem'],
         'path836':book.climbs['Project Mayhem'],
         'path838':book.climbs['Tyler Durten Dyno'],
         'path840':book.climbs['Tyler Durten Dyno'],
         'path298':book.climbs['Angel Face'],
         'path410':book.climbs['Angel Face'],
         'path302':book.climbs['Durten Layback'],
         'path412':book.climbs['Durten Layback'],
     })
Topo(name='Turtle',
     parent=book.formations['Turtle Shell Boulder'],
     paths={
        'topo_o': r'./images/maps/topos/Main/',
        'topo_i': r'./images/maps/topos/Main/'},
     file_name='turtle.svg',
     size='h',
     routes={
         'path855':book.climbs['Raphael Crack'],
         'path861':book.climbs['Raphael Crack'],
         'path857':book.climbs['Donatello'],
         'path863':book.climbs['Donatello'],
         'path859':book.climbs['Leonardo'],
         'path919':book.climbs['Leonardo'],
         'path294':book.climbs['Turtle Traverse'],
         'path1065':book.climbs['Turtle Traverse'],
     })
Topo(name='Undertow',
     parent=book.routes['Undertow'],
     paths={
        'topo_o': r'./images/maps/topos/Main/',
        'topo_i': r'./images/maps/topos/Main/'},
     file_name='undertow.svg',
     size='h',
     routes={
         'path1199':book.climbs['Spray Skirt'],
         'path1201':book.climbs['Spray Skirt'],
         'path1097':book.climbs['Undertow'],
         'path1111':book.climbs['Undertow'],
         'path1099':book.climbs['Spray Against the Undertow'],
         'path1105':book.climbs['Spray Against the Undertow'],
         'path1101':book.climbs['Undertow Sit Start'],
         'path1107':book.climbs['Undertow Sit Start'],
         'path1103':book.climbs['Riptide'],
         'path1109':book.climbs['Riptide'],
     })
Topo(name='Undertow2',
     parent=book.formations['Undertow'],
     paths={
        'topo_o': r'./images/maps/topos/Main/',
        'topo_i': r'./images/maps/topos/Main/'},
     file_name='undertow2.svg',
     size='f',
     routes={
         'path932':book.climbs['Silly Steep Mantle'],
         'path942':book.climbs['Silly Steep Mantle'],
         'path938':book.climbs['Undertow'],
         'path946':book.climbs['Undertow'],
         'path934':book.climbs['Spray Against the Undertow'],
         'path944':book.climbs['Spray Against the Undertow'],
         'path936':book.climbs['Undertow Sit Start'],
         'path950':book.climbs['Undertow Sit Start'],
         'path1134':book.climbs['Riptide'],
         'path948':book.climbs['Riptide'],
         'path940':book.climbs['Tidepool'],
         'path952':book.climbs['Tidepool'],
         'path1309':book.climbs['Simple Math'],
         'path1305':book.climbs['Simple Math'],
         'path1307':book.climbs['Shake it Out'],
         'path748':book.climbs['Shake it Out'],
     })
Topo(name='François',
     parent=book.routes['François'],
     paths={
        'topo_o': r'./images/maps/topos/Main/',
        'topo_i': r'./images/maps/topos/Main/'},
     file_name='frank.svg',
     size='h',
     loc='e',
     routes={
         'path2390':book.climbs['François'],
         'path2388':book.climbs['François'],
         'path1192':book.climbs['Schrödinger Project'],
         'path1190':book.climbs['Schrödinger Project'],
     })
Topo(name='Oregon Arête',
     parent=book.formations['Garden Roof'],
     paths={
        'topo_o': r'./images/maps/topos/Main/',
        'topo_i': r'./images/maps/topos/Main/'},
     file_name='oregonArete.svg',
     size='h',
     routes={
         'path742':book.climbs['Full Stroke'],
         'path737':book.climbs['Full Stroke'],
         'path739':book.climbs['Dream Weaver'],
         'path735':book.climbs['Dream Weaver'],
         'path733':book.climbs['Oregon Arête'],
         'path731':book.climbs['Oregon Arête'],
         'path729':book.climbs['Oregon Arête'],
     })
Topo(name='Full Stroke',
     parent=book.routes['Full Stroke'],
     paths={
        'topo_o': r'./images/maps/topos/Main/',
        'topo_i': r'./images/maps/topos/Main/'},
     file_name='fullStroke.svg',
     size='h',
     border='rect444',
     routes={
         'path1215':book.climbs['Sebulba'],
         'path1207':book.climbs['Sebulba'],
         'path1212':book.climbs['Eurovision'],
         'path1205':book.climbs['Eurovision'],
         'path1217':book.climbs['Dream Weaver'],
         'path1203':book.climbs['Dream Weaver'],
         'path1209':book.climbs['Full Stroke'],
         'path1201':book.climbs['Full Stroke'],
     })
Topo(name='The Good Warm Up',
     parent=book.formations['The Good Warm Up'],
     paths={
        'topo_o': r'./images/maps/topos/Main/',
        'topo_i': r'./images/maps/topos/Main/'},
     file_name='goodWarmUp.svg',
     size='h',
     routes={
         'path579':book.climbs['The Good Warm Up'],
         'path581':book.climbs['The Good Warm Up'],
     })
Topo(name='Gumby Wall',
     parent=book.formations['Gumby Wall'],
     paths={
        'topo_o': r'./images/maps/topos/Main/',
        'topo_i': r'./images/maps/topos/Main/'},
     file_name='gumby.svg',
     size='f',
     routes={
         'path643':book.climbs['Bag of Tricks'],
         'path594':book.climbs['Bag of Tricks'],
         'path434':book.climbs['Bag of Tricks'],
         'path432':book.climbs['Gumby Arête'],
         'path430':book.climbs['Gumby Arête'],
         'path428':book.climbs['Gumby Slab'],
         'path426':book.climbs['Gumby Slab'],
         'path424':book.climbs['Gumby Crack'],
         'path370':book.climbs['Gumby Crack'],
     })
Topo(name='Hanging Prow Project',
     parent=book.formations['Hanging Prow'],
     paths={
        'topo_o': r'./images/maps/topos/Main/',
        'topo_i': r'./images/maps/topos/Main/'},
     file_name='prowProj.svg',
     size='h',
     border='rect1075',
     routes={
         'path1600':book.climbs['Hanging Prow Project'],
         'path1598':book.climbs['Hanging Prow Project'],
         'path859':book.climbs['Hanging Prow Project'],
     })
Topo(name='Small',
     parent=book.formations['Small'],
     paths={
        'topo_o': r'./images/maps/topos/Main/',
        'topo_i': r'./images/maps/topos/Main/'},
     file_name='small.svg',
     size='h',
     routes={
         'path1740':book.climbs['Smol'],
         'path1738':book.climbs['Smol'],
         'path1736':book.climbs['Smol'],
         'path1276':book.climbs['Tip Toe'],
         'path1121':book.climbs['Tip Toe'],
     })
Topo(name='Spider Bumps',
     parent=book.routes['Spider Bumps'],
     paths={
        'topo_o': r'./images/maps/topos/Main/',
        'topo_i': r'./images/maps/topos/Main/'},
     file_name='spiderBumps.svg',
     size='h',
     routes={
         'path1879':book.climbs['Spider Bumps'],
         'path1877':book.climbs['Spider Bumps'],
     })


if __name__ == '__main__':
    sys.exit()
