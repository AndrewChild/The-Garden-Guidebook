from dataStructure import Area, Subarea, Formation, Route, Variation
from GB_Book import book


Area(name='Quartzville Creek',
     parent=book,
     description='About an hour further down the road from the main area there are a few interesting boulders '
                 'in a creek. Generally lower temperatures, free camping, and pleasant swimming holes make this '
                 'a nice mid summer spot.')
                 
                 
Subarea(name='Redneck Riviera',
        parent=book.areas['Quartzville Creek'],
        gps='44.570410945356336, -122.4060701729652',
        description='Redneck rivierra is located on Quartzville road apporximately 20.6 miles from highway 20 park in '
                    'the gravel pull out on the creek side of the road. This '
                    'is a nice spot with good swimming access and a few established routes on both sides of the river. '
                    'The locals like to use this spot to pan for gold. Often they are friendly and willing '
                    'to share the space.')
Subarea(name='Old Miner\'s Camp',
        parent=book.areas['Quartzville Creek'],
        gps='44.58651338802075, -122.35033857932665',
        description='Located on Quartzville approximately 24.8 miles from highway 20, the old miner\'s camp is a '
                    'popular group campsite there are a few good sized boulders in the river. Only one boulder has '
                    'established lines on it. Park either at the camp day use area or on the side of the road '
                    'immediately above the Dab Rig boulder. Note: the dab rig boulder is typically underwater in the '
                    'rainy season.')
Formation(name='Pony Boy',
           parent=book.subareas['Redneck Riviera'],
           description='A small boulder sits on the far bank of the river upriver from the parking.')
Formation(name='Monorail',
           parent=book.subareas['Redneck Riviera'],
           description='Low boulder just below the parking area with an obvious sharp lip that spans the entire downhill face.',)
Formation(name='Yo Mamma Boulder',
           parent=book.subareas['Redneck Riviera'],
           description='Yo Mamma is bigger than any of the other boulders in this area. Look for it across the river and downstream from the parking.')
Formation(name='Moss Boss',
           parent=book.subareas['Redneck Riviera'],
           description='A large mossy boulder on the roadside of the river and downstream of the parking area.')
Formation(name='The 4.5',
           parent=book.subareas['Redneck Riviera'],
           description='Located on the river downstream and across the river from the parking. look for a clean "4.5° overhanging" face pointing downhill.')
Formation(name='The Dab Rig',
           parent=book.subareas['Old Miner\'s Camp'],
           description='')
           
           
Route(name='Pony Boy',
      parent=book.formations['Pony Boy'],
      grade=2, 
      rating=0,
      description='Sit start with hands matched in a juggy pocket on the overhanging face of the boulder. Climbing '
                  'this thing is probably not worth getting your pads wet.')
Route(name='Monorail',
      parent=book.formations['Monorail'],
      grade='8+', 
      rating=3,
      FA='Zachary Radke',
      description='Start on the far right and traverse left along the lip. Topping in a shallow divot on the center left of the boulder.') 
Route(name='Megarail Project',
      parent=book.formations['Monorail'],
      description='Sit start and climb the steep roof using right facing rib. Top as for Monorail or travers out left.') 
Route(name='Ugly Face',
      parent=book.formations['Yo Mamma Boulder'],
      grade=0, 
      serious=1,
      rating=1,
      description='Stand start on the left side of the west face of the boulder. This is also the down climb.')
Route(name='Binding of Isaac',
      parent=book.formations['Yo Mamma Boulder'],
      grade=2, 
      serious=1,
      rating=2,
      description='Stand start with a left hand sidepull about 5\' left of Ugly face.')
Route(name='Moss Boss',
      parent=book.formations['Moss Boss'],
      grade=3, 
      FA='Nick Koch',
      rating=1,
      description='Believe it or not a route has been established and climbed on this dirty choss pile. Stand start on big holds on the river face and trend up and right finishing half way up the upstream face of the boulder. A direct finish is certainly possible too.') 
Route(name='Chicken Tendies',
      parent=book.formations['The 4.5'],
      grade=1, 
      rating=1,
      description='Stand start with hands matched on a good crimp rail on the left side of the boulder. Climb straight up.')
Route(name='Teenage Libertarians',
      parent=book.formations['The 4.5'],
      grade=4, 
      rating=3,
      FA='Nick Koch',
      description='Start as for chicken tendies but traverse right and ascend the tallest part of the boulder.')
Route(name='Falcon\'s Reach',
      parent=book.formations['The 4.5'],
      grade=3, 
      rating=1,
      description='Squat start on a juggy edge. Climb straight up.')
Route(name='Unsalted Almonds',
      parent=book.formations['The Dab Rig'],
      grade=8,
      FA='Griffin Thoms',
      grade_unconfirmed=True,
      description='Sit start stradling the right arête with left hand on a diagonal edge and right hand on a sloper. Climb up and left across the well featured face.')
Route(name='Dank Commander',
      parent=book.formations['The Dab Rig'],
      grade=4,
      FA='Griffin Thoms',
      grade_unconfirmed=True,
      description='Start as for Unsalted Almonds, but go straight up.')
Variation(name='Monorail Extention Project',
          parent=book.routes['Monorail'],
          description='Climb Monorail and ride the lip the whole way across the boulder.') 
      

if __name__ == '__main__':
    sys.exit()