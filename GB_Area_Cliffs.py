import sys

sys.path.insert(1, '../LocalBoulders')
from dataStructure import Area, Subarea, Formation, Route, Variation
from GB_Book import book

Area(name='Garden Cliffs',
     parent=book,
     gps='44.43998124232581, -122.57539325959186',
     incomplete=True,
     description='PLACEHOLDER', )
     
     
Subarea(name='The Garden Cliff',
        parent=book.areas['Garden Cliffs'], )
Subarea(name='Fairy Tale Wall',
        parent=book.areas['Garden Cliffs'], )
Subarea(name='Cabbage Patch/Thunderdome',
        parent=book.areas['Garden Cliffs'], )
        
        
Formation(name='Garden Cliff Right Side',
          parent=book.subareas['The Garden Cliff'],
          description='')
Formation(name='Garden Cliff Middle',
          parent=book.subareas['The Garden Cliff'],
          description='')
Formation(name='Garden Cliff Left Side',
          parent=book.subareas['The Garden Cliff'],
          description='')
Formation(name='',
          item_id='Fairy Tale Wall',
          parent=book.subareas['Fairy Tale Wall'],
          description='')
Formation(name='Cabbage Patch',
          parent=book.subareas['Cabbage Patch/Thunderdome'],
          description='')
Formation(name='Johny Cash\'s Thunderdome',
          parent=book.subareas['Cabbage Patch/Thunderdome'],
          description='')
          
          
Route(name='Sword and Shield',
      parent=book.formations['Garden Cliff Right Side'],
      grade='5.12a',
      grade_unconfirmed=True,
      )
Route(name='Ladybug',
      parent=book.formations['Garden Cliff Right Side'],
      grade='5.10a',
      )
Route(name='John Henry\'s Hammer',
      parent=book.formations['Garden Cliff Right Side'],
      grade='5.10c/d',
      rating=2,
      )
Route(name='Yggdrasil',
      parent=book.formations['Garden Cliff Right Side'],
      grade='5.11a',
      rating=3,
      )
Route(name='Scorpion Revenge',
      parent=book.formations['Garden Cliff Right Side'],
      grade='5.11b',
      rating=2,
      )
Route(name='Snug as a Snail',
      parent=book.formations['Garden Cliff Right Side'],
      grade='5.11c',
      rating=2,
      )
Route(name='Scorpion Hitchhikers Toilet Bowl Odyssey',
      parent=book.formations['Garden Cliff Right Side'],
      grade='5.11b',
      rating=3,
      )
Route(name='Daring to Fly',
      parent=book.formations['Garden Cliff Right Side'],
      grade='5.11d',
      rating=3,
      )
Route(name='Community',
      parent=book.formations['Garden Cliff Right Side'],
      grade='5.9',
      rating=1,
      )
Route(name='Blackberry Jam',
      parent=book.formations['Garden Cliff Right Side'],
      grade='5.10-',
      grade_unconfirmed=True,
      )
Route(name='Anaphylactic Shock',
      parent=book.formations['Garden Cliff Right Side'],
      grade='5.12a',
      rating=1,
      )
Route(name='Fight Club (Round Two)',
      parent=book.formations['Garden Cliff Right Side'],
      grade='5.12b',
      rating=3,
      )
Route(name='Cutting Crack',
      parent=book.formations['Garden Cliff Right Side'],
      grade='5.9',
      rating=1,
      )
Route(name='Butterfly Effect',
      parent=book.formations['Garden Cliff Right Side'],
      grade='5.13-',
      )
Route(name='Slithering Skink',
      parent=book.formations['Garden Cliff Right Side'],
      grade='5.10d',
      rating=3,
      )
Route(name='Stasis Chamber',
      parent=book.formations['Garden Cliff Right Side'],
      grade='5.12b',
      rating=2,
      )
Route(name='Wildlings',
      parent=book.formations['Garden Cliff Right Side'],
      grade='5.11d',
      rating=2,
      )
Route(name='Rain Shadow',
      parent=book.formations['Garden Cliff Right Side'],
      grade='5.11a/b',
      rating=1,
      )
Route(name='Vine Project',
      parent=book.formations['Garden Cliff Middle'],
      grade='5.?',
      )
Route(name='Hierloom Project',
      parent=book.formations['Garden Cliff Middle'],
      grade='5.?',
      )
Route(name='Chimeras',
      parent=book.formations['Garden Cliff Middle'],
      grade='5.13a',
      )
Route(name='Littlest Birds',
      parent=book.formations['Garden Cliff Middle'],
      grade='5.11b',
      rating=2,
      )
Route(name='Castle Black',
      parent=book.formations['Garden Cliff Middle'],
      grade='5.11-',
      rating=1,
      )
Route(name='Seraphim Nachash',
      parent=book.formations['Garden Cliff Middle'],
      grade='5.11b/c',
      rating=3,
      )
Route(name='My Empire of Dirt',
      parent=book.formations['Garden Cliff Middle'],
      grade='5.12b',
      rating=3,
      )
Route(name='Honeycomb Project',
      parent=book.formations['Garden Cliff Left Side'],
      grade='5.?',
      )
Route(name='Criss Cross Applesauce',
      parent=book.formations['Garden Cliff Left Side'],
      grade='5.11c',
      rating=2,
      )
Route(name='Vandals in the Graveyard',
      parent=book.formations['Garden Cliff Left Side'],
      grade='5.12a',
      rating=1,
      )
Route(name='Ovulation Send-sation',
      parent=book.formations['Garden Cliff Left Side'],
      grade='5.12a',
      rating=2,
      )
Route(name='Fertile Crescent',
      parent=book.formations['Garden Cliff Left Side'],
      grade='5.12a',
      rating=3,
      )
Route(name='My Secret Garden',
      parent=book.formations['Garden Cliff Left Side'],
      grade='5.11a',
      rating=2,
      )
Route(name='Nest',
      parent=book.formations['Garden Cliff Left Side'],
      grade='5.10c',
      rating=2,
      )
Route(name='A Garden Called Peace',
      parent=book.formations['Garden Cliff Left Side'],
      grade='5.10a',
      rating=3,
      )
Route(name='Hive',
      parent=book.formations['Garden Cliff Left Side'],
      grade='5.10c',
      rating=1,
      )
Route(name='Baba Yaga',
      parent=book.formations['Fairy Tale Wall'],
      grade='5.9',
      rating=1,
      )
Route(name='Death of Koschei the Deathless',
      parent=book.formations['Fairy Tale Wall'],
      grade='5.11a',
      rating=1,
      )
Route(name='Feather of the Finst Falcon',
      parent=book.formations['Fairy Tale Wall'],
      grade='5.8',
      rating=1,
      )
Route(name='Fee-Fi-Fo-Fum',
      parent=book.formations['Fairy Tale Wall'],
      grade='5.10c',
      rating=2,
      )
Route(name='Don\'t Forget the Nooch',
      parent=book.formations['Cabbage Patch'],
      grade='5.4',
      grade_unconfirmed=True,
      )
Route(name='Tabouli',
      parent=book.formations['Cabbage Patch'],
      grade='5.7',
      grade_unconfirmed=True,
      )
Route(name='Babaganoush',
      parent=book.formations['Cabbage Patch'],
      grade='5.10b',
      grade_unconfirmed=True,
      )
Route(name='Kim Chi Corner',
      parent=book.formations['Cabbage Patch'],
      grade='5.11a',
      grade_unconfirmed=True,
      )
Route(name='I Fell for You Like a Child',
      parent=book.formations['Johny Cash\'s Thunderdome'],
      grade='5.8',
      rating=3,
      )
Route(name='I Will Let You Down',
      parent=book.formations['Johny Cash\'s Thunderdome'],
      grade='5.6',
      rating=2,
      )
Route(name='A Million Dollars of Good',
      parent=book.formations['Johny Cash\'s Thunderdome'],
      grade='5.8',
      rating=2,
      )
Route(name='Stop Once to Wipe the Sweat Away',
      parent=book.formations['Johny Cash\'s Thunderdome'],
      grade='5.10a',
      rating=1,
      )
      
      
Variation(name='John to Snug Linkup',
          parent=book.routes['John Henry\'s Hammer'],
          grade='5.10c/d',
          rating=2,)
Variation(name='Lazarus',
          parent=book.routes['Stasis Chamber'],
          grade='5.12c',
          rating=2,
          )
Variation(name='Honeycomb Traverse',
          parent=book.routes['Honeycomb Project'],
          grade='5.12a',
          rating=2,)


if __name__ == '__main__':
    sys.exit()
