from dataStructure.Photo import Photo
from dataStructure.Topo import Topo
from dataStructure.AreaMap import AreaMap
from dataStructure.SubAreaMap import SubAreaMap
from data.GB_Book import book
"""
Low Priority Images get loaded after everything else and will there for always be placed after other images
"""


Photo(name='WACC',
      file_name='WACC.png',
      parent=book,
      size = 'p',
      loc = 'a',
      format_options=['force_include'],
      )
Photo(name='Overview',
      file_name='areaOverview.png',
      parent=book,
      size = 'pr',
      loc = 'a',
      format_options=['force_include'],
      description='Garden areas overview. Parking areas marked in dark blue.'
      )
Photo(name='Riptide',
      file_name='Riptide.jpg',
      parent=book.formations['Undertow'],
      size = 'h',
      loc = 'e',
      route=book.routes['Riptide'],
      credit='Andrew Child',
      description='Rob on Riptide.')
Photo(name='Fight Club',
      file_name='FightClub2.jpg',
      parent=book.subareas['Fight Club'],
      size='h',
      loc='e',
      route=book.routes['Fight Club'],
      credit='Andrew Child',
      description='Michael near the top of Fight Club.')
Photo(name='Octernal',
      file_name='Octurnal.jpg',
      parent=book.subareas['Undertow'],
      size='s',
      loc='e',
      route=book.routes['Octernal'],
      credit='Andrew Child',
      description='Carson landing the big throw on Octernal. Classic!')
Photo(name='Smackdown',
      file_name='Smackdown.jpg',
      parent=book.subareas['François'],
      route=book.routes['Smackdown'],
      size='f',
      loc='e',
      credit='Carson Dension',
      description='Andrew posting up at the start of Smackdown.')
Photo(name='Ground up Blowie',
      file_name='blowie.jpg',
      parent=book.formations['Toilet Bowl'],
      size='p',
      loc='e',
      route=book.routes['Ground up Blowie'],
      credit='Michael Gardener Brown',
      description='Andrew struggling to find a finger lock on Ground up Blowie.')
Photo(name='Butterfly',
      file_name='butterfly.jpg',
      parent=book.subareas['The Garden Cliff'],
      size='f',
      loc='e',
      route=book.routes['Butterfly Effect'],
      credit='Andrew Child',
      description='Griffin on Butterfly Effect.')
Photo(name='2blows',
      file_name='2blows.jpg',
      parent=book.subareas['Azain'],
      size='h',
      loc='e',
      route=book.routes['Two Blows One Stroke'],
      credit='Andrew Child',
      description='Griffin on Two Blows One Stroke.')      
Photo(name='gargoyle',
      file_name='gargoyle.jpg',
      parent=book.subareas['Child of God'],
      size='h',
      loc='e',
      route=book.climbs['Gargoyle Direct'],
      credit='Andrew Child',
      description='Michael Gardener-Brown on Gargoyle Direct.')     
Photo(name='pinkTag',
      file_name='pinkTagSign.jpg',
      parent=book.subareas['Pink Tag'],
      size='h',
      format_options=['force_include'],
      description='All but one of the climbs in this area are downhill of this sign.')      
Photo(name='strangelove',
      file_name='strangelove.jpg',
      parent=book.areas['Upper Garden'],
      size='h',
      loc='a',
      route=book.routes['Dr. Strangelove'],
      credit='Andrew Child',
      description='Cyrus biffs the top on Dr. Strangelove.')       
Photo(name='beard',
      file_name='beard.jpg',
      parent=book.areas['Quartzville Creek'],
      size='h',
      loc='a',
      route=book.climbs['Step on my Beard'],
      credit='Andrew Child',
      description='Jacob on Step on my Beard.')      
Photo(name='Mondorail',
      file_name='mondorail.jpg',
      parent=book.subareas['Redneck Riviera'],
      size='f',
      loc='e',
      route=book.climbs['Monorail Extension Project'],
      credit='Andrew Child',
      description='Noah on Mondorail.')
Photo(name='needles',
      file_name='needles.jpg',
      parent=book.subareas['The Needles'],
      size='f',
      format_options=['force_include'],
      description='The Needles as seen from NF-1133.')      
Photo(name='pinnacle',
      file_name='pinnacle.jpg',
      parent=book.subareas['Santiam Pinnacle'],
      size='h',
      format_options=['force_include'],
      description='Santiam Pinnacle as seen from the road.')      
Photo(name='Cascadia',
      file_name='CascadiaCave2.jpg',
      parent=book.subareas['Cascadia Cave'],
      size='h',
      format_options=['force_include'],
      description='This is a cultural site. Do not climb here.')                
           
if __name__ == '__main__':
    sys.exit()
