import sys
sys.path.insert(1, '../LocalBoulders')
from dataStructure import Area, Subarea, Formation, Route, Variation
from GB_Book import book


Area(name='Upper Garden',
     parent=book,
     gps='44.43959094940084, -122.58215256842753',
     incomplete=True,
     description='Located about 3.2 miles down quatzville road from highway 20, park in the Gravel pull out where the road bends '
                 'about 0.1 miles before you reach a left hand turnoff to a gated logging road (MS-310). Follow the '
                 'logging road approximately 200 yards up hill until it veers slightly to the right. Look for a '
                 'trail that cuts right through a thin patch of trees to the boulder field (Note: there are a '
                 'couple of trails and its worth getting on the most tread one as the others are unpleasant). There '
                 'are a lot of small boulders in this area which have been climbed historically, but are not '
                 'included in this guide because they are covered in poison oak. This '
                 'area is also known as Armageddon.',)
                 
                 
Subarea(name='Entrance Area',
        item_id = 'entranceUpper',
        parent=book.areas['Upper Garden'],)
Subarea(name='The Bread Loaves/Scratch and Spliff',
        parent=book.areas['Upper Garden'],
        description='These two boulders are the area\'s main attraction. Historically some groups have called both '
                    'boulders Scratch and Spliff while others called them both the Bread Loaves. The modern compromise '
                    'seems to be that the upper boulder is Scratch and Spliff while the lower boulder is the Bread Loaf.')
Subarea(name='Middle Garden',
        parent=book.areas['Upper Garden'],)
                    
                    
Formation(name='Pumpkin',
           parent=book.subareas['entranceUpper'],
           description='This is the first boulder that you encounter when approaching the area.')
Formation(name='Baseball',
           parent=book.subareas['entranceUpper'],
           description='This is one of the few boulders that isn\'t covered in poison oak, but there is quite a lot of it '
                       'sounding it. Approach with caution.')
Formation(name='Bread Loaf',
           parent=book.subareas['The Bread Loaves/Scratch and Spliff'],
           description='')
Formation(name='Scratch and Spliff',
           parent=book.subareas['The Bread Loaves/Scratch and Spliff'],
           description='')
Formation(name='Dr. Strangelove',
           parent=book.subareas['Middle Garden'],
           description='')
Formation(name='Young Juicy',
           parent=book.subareas['Middle Garden'],
           description='')
           
           
Route(name='Pumpkin Spice',
      parent=book.formations['Pumpkin'],
      grade=7,
      rating=2,
      name_unconfirmed=True,
      description='Sit start on the left side of the overhang with left hand on a sharp side pull and right hand on the lower of two side pull rails. Trend right along the roof to an easy topout over a sussy landing.')
Route(name='Baseball',
      parent=book.formations['Baseball'],
      grade='3-',
      rating=1,
      description='Sit start with a high left hand on a good dish around the blunt corner and a low right hand '
                  'pinch. Pull a powerful move to good edges and continue straight up.')
Route(name='Bunt',
      parent=book.formations['Baseball'],
      grade=1,
      rating=1,
      description='Sit start with both hands in a low bubbly pod. Climb straight up.')
Route(name='Bread Loaf Left',
      parent=book.formations['Bread Loaf'],
      grade=4,
      rating=2,
      description='Stand start on two horizontal edges. Navigate your way to some good lumpy jugs midway up the ' 
                  'route and either mantle or side pull your way to the top. Also called Buddha\'s Belly.')
Route(name='Bread Loaf Traverse',
      parent=book.formations['Bread Loaf'],
      grade=5,
      rating=2,
      description='stand start with hands matched in the left of two good pods in the lowest diagonal crack. Follow '
                  'the crack system right with the help of a good hold under the roof. top along the arete. Dabby.')
Route(name='Worf',
      parent=book.formations['Bread Loaf'],
      grade=5,
      rating=2,
      description='Starting from two horizontal cracks a bizarre sequence leads you first left then right as you '
                  'climb the rounded corner. Some but not all of the difficulty comes from the dab potential.')
Route(name='Scratch and Spliff Traverse',
      parent=book.formations['Scratch and Spliff'],
      grade=3,
      rating=3,
      description='Start at the far right of the major horizontal crack (as for Roach) and traverse all the way left '
                  'topping out along a juggy vertical crack system.')
Route(name='Scratch',
      parent=book.formations['Scratch and Spliff'],
      grade=4,
      rating=2,
      description='Stand start with right hand on a good hold in the horizontal crack and left hand wrapping around '
                  'a juggy corner. Jump to a bubbly rail and tick tack your way to the top. Originally this route '
                  'started as for Scratch and Spliff Traverse.')
Route(name='Spliff',
      parent=book.formations['Scratch and Spliff'],
      grade=3,
      rating=3,
      serious=1,
      description='Start on a large hanging flake. Climb straight up. Sit start seems possible but wouldn\'t add '
                  'much to the experience.')
Route(name='Roach',
      parent=book.formations['Scratch and Spliff'],
      grade=0,
      rating=2,
      description='Stand start with a good edge in the horizantal crack..')
Route(name='For What it\'s Worth',
      parent=book.formations['Scratch and Spliff'],
      grade=2,
      rating=2,
      name_unconfirmed=True,
      description='Squat start on a low ramp on the NW corner of the boulder using a left hand low on the arete and '
                  'a right hand side pull. Bump up the arete then Dyno to the lip. Dab potential creates a lot of '
                  'the difficulty.')
Route(name='Caliban\'s War',
      parent=book.formations['Scratch and Spliff'],
      grade=6,
      grade_unconfirmed=True,
      description='Stand start with hand holds in a horizontal crack. Crank one move to the lip.')
Route(name='Stoned Age',
      parent=book.formations['Scratch and Spliff'],
      grade=2,
      grade_unconfirmed=True,
      description='It looks like you could easily climb from the horizontal crack to a diagonal crack on the upper '
                  'right, but the landing is very poor. Older guidebooks indicate that this has been done.')



Variation(name='Baker\'s Dozen',
          parent=book.routes['Bread Loaf Traverse'],
          grade=8,
          grade_unconfirmed=True,
          description='Start as for Bread Loaf Left, traverse into the bread loaf traverse.')
Variation(name='Late Start',
          parent=book.routes['Scratch and Spliff Traverse'],
          grade=2,
          rating=2,
          name_unconfirmed=True,
          description='Sit start with juggy holds at the top of a low ramp. Climb straight up into the top of Scratch '
                      'and Spliff Traverse.')
                      
                      
if __name__ == '__main__':
    sys.exit()