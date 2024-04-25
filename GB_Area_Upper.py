from dataStructure import Area, Subarea, Formation, Route, Variation
from GB_Book import book


Area(name='Upper Garden',
     parent=book,
     gps='44.43959094940084, -122.58215256842753',
     description='Located about 3.2 miles down Quatzville Road from Highway 20, park in the gravel pull out where the road bends '
                 'about 0.1 miles before you reach a left hand turnoff to a gated logging road (MS-310). Follow the '
                 'logging road approximately 200 yards up hill until it veers slightly to the right. Look for a '
                 'trail that cuts right through a thin patch of trees to the boulder field (Note: there are a '
                 'couple of trails and its worth getting on the most tread one as the others are unpleasant). This '
                 'area is also known as Armageddon or The Clear Cut.'
                 '\n\n'
                 'Many sections of this area are covered in pioson oak. Climbers are adivised to wear close toed shoes and pants when recrating in this area. If unfamilar with the plant review the section on poison oak in this book\'s introduction.'
                 '\n\n'
                 'Although the Upper Garden appears overgrown, this entire area was clear cut in the early 2000s. Following the clear cut there was almost no vegitation in the area and it was realatively easy to approach and develop the Upper Garden\'s many boulders. This is why the photos in this guide look dramatically different from photos in guides from that era. Even the most isolated and overgrown boulders in this area already have names and routes on them, many of these boulders have been omitted from this guide since they have been swallowed by the poison oak.',)
                 
                 
Subarea(name='Entrance Area',
        item_id = 'entranceUpper',
        gps='44.43961303214984, -122.58215061970166',
        parent=book.areas['Upper Garden'],)
Subarea(name='The Bread Loaves/Scratch and Spliff',
        item_id = 'The Bread Loaves',
        parent=book.areas['Upper Garden'],
        gps='44.43968787057463, -122.58169628966748',
        description='These two boulders are the area\'s main attraction. Historically some groups have called both '
                    'boulders Scratch and Spliff while others called them both the Bread Loaves. The modern compromise '
                    'seems to be that the upper boulder is Scratch and Spliff while the lower boulder is the Bread Loaf.')
Subarea(name='Dr. Strangelove',
        parent=book.areas['Upper Garden'],
        note = 'This sub area is still being rediscovered. Look forward to more information in future revisions of this book or contribute your own knowledge on github.',
        description='More boulders lay under the canopy beyond the tallus NE of the scratch and spliff area. Although there is a lot of poison oak in the way there is one passage which avoids most of it. From the scratch and spliff boulder walk across jumbled tallus towards the cliff band for ~100\' until you pass a large fir tree. From here the distinctive prow of the Dr. Stanglove boulder should be barely visible through the trees. Walk more or less directly towards it bushwhacking along a feint trail once you get into the trees. There is much less poison oak under the canopy but it can still be found in some patches. Alternatively you can follow the approach trail through the Middle Garden and avoid all of the poison oak.')
Subarea(name='Machete Monkey',
        parent=book.areas['Upper Garden'],
        note = 'This sub area is still being rediscovered. Look forward to more information in future revisions of this book or contribute your own knowledge on github.',
        description='About 100\' east of Dr. Strangelove there is a narrow wash of boulders in a clearing. If Approaching from the west follow a faint trail leading from the backside of the Dr. Strangelove boulder to the cliff and walk along the base of the cliff until the trail leads down a steep hill towards the Machete Monkey boulder. If approaching from the East head west from the Jaws boulder ~75\' until you reach the Duck Twirler boulder.')
Subarea(name='Middle Garden',
        parent=book.areas['Upper Garden'],
        note = 'This sub area is still being rediscovered. Look forward to more information in future revisions of this book or contribute your own knowledge on github.',
        description='There are many boulders under the cliffline east of the Machete Monkey area. Rediscovering and restablishing this sector is an ongoing project. In 2024 a new trail was established which allows access to this area directly from the road.')
                    
                    
Formation(name='Pumpkin',
           parent=book.subareas['entranceUpper'],
           description='This is the first boulder that you encounter when approaching the area.')
Formation(name='Baseball',
           parent=book.subareas['entranceUpper'],
           description='This is one of the few boulders that isn\'t covered in poison oak, but there is quite a lot of it '
                       'sounding it. Approach with caution.')
Formation(name='Bread Loaf',
           parent=book.subareas['The Bread Loaves'],
           description='')
Formation(name='Scratch and Spliff',
           parent=book.subareas['The Bread Loaves'],
           description='')
Formation(name='Dr. Strangelove',
           parent=book.subareas['Dr. Strangelove'],
           description='')
Formation(name='Kick It',
           parent=book.subareas['Dr. Strangelove'],
           description='')
Formation(name='Mega Good Boulder',
           parent=book.subareas['Dr. Strangelove'],
           description='')
Formation(name='Algebra',
           parent=book.subareas['Dr. Strangelove'],
           description='This small chossy block would be easy to overlook, but the sole line on it is acutally much more fun than you might think.')
Formation(name='Crack Boulder',
           parent=book.subareas['Machete Monkey'],
           description='')
Formation(name='Machete Monkey',
           parent=book.subareas['Machete Monkey'],
           description='This huge pancke shaped boulder is propped upright and mostly hanging wedged between smaller blocks. So far only the routes on the back side are documented, though there is some evidence in prior guidebooks that the main face may have been climbed before.')
Formation(name='June 24th',
           parent=book.subareas['Machete Monkey'],
           description='')
Formation(name='Young Ju¢y',
           parent=book.subareas['Machete Monkey'],
           description='Just down from June 24 there\'s a sloping halfmoon boulder.')
Formation(name='Duck Twirler',
           parent=book.subareas['Machete Monkey'],
           description='')
Formation(name='Deep Sea Diver',
           parent=book.subareas['Middle Garden'], 
           description='This cool mini cliff band is roughly 25\' tall and features a hand crack on the left side. The entire wall seaps and the crack in particular is almost always wet. A variety of lines have been climbed and forgotten on this formation over the years, those currently listed below are just guesses.')
Formation(name='Jaws',
           parent=book.subareas['Middle Garden'],
           description='Just down hill from the Deep Sea Diver wall is a boulder with some fun compression on its down hill face.')
Formation(name='Prince Albert',
           parent=book.subareas['Middle Garden'],
           description='This cool spire is surprisingly hard to see from the road. Several lines have been established and frogotten on all aspects of the pillar. Note that getting off of this rod can be a challenge; your best options are (in no particular order): use the highly suspicious bolt on top to rapell, down climb "Easy up, Easy Down" (name is subjective), or down climb the top of "Prince Albert" and drop. Also watch out for poison oak on the road facing side.')
           
           
Route(name='Pumpkin Spice',
      parent=book.formations['Pumpkin'],
      grade='6',
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
Route(name='Bread Heel',
      parent=book.formations['Bread Loaf'],
      grade=3,
      rating=1,
      description='Stand start in narrow compression on two big sidepulls. Make your way to a big undercling flake and follow it up and left onto the slab.')
Route(name='Bread Loaf Left',
      parent=book.formations['Bread Loaf'],
      grade=4,
      rating=3,
      description='Stand start on two horizontal edges. Navigate your way to some good lumpy jugs midway up the ' 
                  'route and either mantle or side pull your way to the top..')
Route(name='Breadwinner',
      parent=book.formations['Bread Loaf'],
      grade='9/10',
      FA='Kalel Chester',
      grade_unconfirmed=True,
      description='Start as for Bread Loaf Traverse, climb straight up..')
Route(name='Bread Loaf Traverse',
      parent=book.formations['Bread Loaf'],
      grade=5,
      rating=2,
      description='stand start with hands matched in the left of two good pods in the lowest diagonal crack. Follow '
                  'the crack system right with the help of a good hold under the roof. top along the arête. Dabby.')
Route(name='Worf',
      parent=book.formations['Bread Loaf'],
      grade=5,
      rating=2,
      description='Starting from the low horizontal seams crank a few powerful moves to gain a blunt corner. Both sides of the corner are worthwhile and valid top out options, each challenging in its own way.')
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
      description='Squat start on a low ramp on the NW corner of the boulder using a left hand low on the arête and '
                  'a right hand side pull. Bump up the arête then dyno to the lip. Dab potential creates a lot of '
                  'the difficulty.')
Route(name='Caliban\'s War',
      parent=book.formations['Scratch and Spliff'],
      grade=6,
      grade_unconfirmed=True,
      description='Stand start with hand holds in a horizontal crack. Crank one move to the lip. Extremely morpho. ')
Route(name='Stoned Age',
      parent=book.formations['Scratch and Spliff'],
      grade=2,
      grade_unconfirmed=True,
      description='It looks like you could easily climb from the horizontal crack to a diagonal crack on the upper '
                  'right, but the landing is very poor. Older guidebooks indicate that this has been done.')
Route(name='Dr. Strangelove',
      parent=book.formations['Dr. Strangelove'],
      grade=6,
      rating=3,
      serious=1,
      description='Climb the aesthetic arête from the left (right hand on arête) side. The natural landing is heinous, but can be improved by laying logs over the chasm. Also known as "The Hook"')
Route(name='War Room',
      parent=book.formations['Dr. Strangelove'],
      grade=9,
      rating=2,
      grade_unconfirmed=True,
      description='Start with left hand on your choice of holds on a sloper rail, and right hand on a vertical edge. Make a hardish move to a decent left hand sidepull, then bravely launch for the jug lip over a mediocre landing. A couple holds broke here during a 2019 cleaning, but this route (or something similar) was once known as "Andrew\'s Line" (no, some other Andrew).')
Route(name='Kick It',
      parent=book.formations['Kick It'],
      grade=2,
      rating=2,
      description='Start standing with left hand on a small edge or on the left arête and right hand undercling a big slopey rib. Climb the clean face using both arêtes. Worth doing if you are making the trek out to strange love. Also known as Dishing.')
Route(name='Mega Good Boulder',
      parent=book.formations['Mega Good Boulder'],
      item_id='MGB',
      grade=4,
      rating=1,
      description='Sit start the MGB using single pad edges below the blobby sloper. Harder and weirder than it looks.')
Route(name='Algebra',
      parent=book.formations['Algebra'],
      grade=5,
      rating=1,
      description='Sit start using the detatched block. Climb the left arête.')
Route(name='Jugs',
      parent=book.formations['Crack Boulder'],
      grade=0,
      grade_unconfirmed=True,
      description='Sit start and climb the short line of jugs.')
Route(name='Jenga Crack',
      parent=book.formations['Crack Boulder'],
      item_id='Crack 2',
      grade=2,
      grade_unconfirmed=True,
      name_unconfirmed=True,
      description='Climb the short vertical crack from a sit start. Eliminating holds will make this more difficult.')
Route(name='Machete Monkey',
      parent=book.formations['Machete Monkey'],
      grade=3,
      rating=1,
      grade_unconfirmed=True,
      description='Climb the left arête of the higher-tiered area to the left of the obvious roof. Fun liebacking from an obvious jug at break')
Route(name='Little Hesitator',
      parent=book.formations['June 24th'],
      item_id='June 1',
      grade=2,
      rating=2,
      name_unconfirmed=True,
      description='Use thin flakes to pearch on a large protuding foot hold. Technical edging, some small crimps, and maybe a dyno will bring you to the top of this mostly blank slab. This route is much more challenging (and therefore more rewarding) if you are short.')
Route(name='June 24th',
      parent=book.formations['June 24th'],
      grade=7,
      rating=3,
      description='Stand start matched at the bottom of a left facing diagonal rail. A sequence of difficult laybacks gives way to small crimps. This is one of the best lines that the Garden has to offfer.')
Route(name='Young Ju¢y',
      parent=book.formations['Young Ju¢y'],
      grade=8,
      rating=1,
      grade_unconfirmed=True,
      description='Climb an arching line left across the lip starting from two right-facing sidepulls at/below the lip for on the right side of the boulder. Technical and close to impossible without a solid brushing')
Route(name='Duck Hole',
      parent=book.formations['Duck Twirler'],
      item_id='DT 1',
      grade=4,
      rating=1,
      name_unconfirmed=True,
      description='Stand start in a pit using a left hand jug and good right hand sidepull pinch. Use techy feet to grab whatever you can on a weirdly smooth bludge and crank to better holds higher up. Harder than you\'d think.')
Route(name='Anti-Tiff',
      parent=book.formations['Duck Twirler'],
      grade=2,
      rating=2,
      description='Stand start and climb the center face however you see fit. This has also been climbed from a low sit start.')
Route(name='Screaming at a Wall',
      parent=book.formations['Duck Twirler'],
      grade=2,
      rating=2,
      description='Stand start with low sidepulls in wide compression, a few long moves bring you to a technical mantle at the top. Starting a little higher is also a valid and potentially more enjoyable interpretation.')
Route(name='Duck Twirler',
      parent=book.formations['Duck Twirler'],
      grade=2,
      rating=2,
      description='Sit start in wide compression with right hand on a large vertical rail and left hand on a low sidepull. Climb up and right finishing through a cool pinch near the top of the boulder')
Route(name='Deforestation',
      parent=book.formations['Duck Twirler'],
      grade=3,
      rating=3,
      description='Squat start on a pair of sloping rails. A few tensiony moves on good holds get you to the top.')
Route(name='Deep Sea Diver',
      parent=book.formations['Deep Sea Diver'],
      grade='?',
      description='Climb the base of the cliff as a left to right traverse.')
Route(name='Ya Ya Crack',
      parent=book.formations['Deep Sea Diver'],
      grade='?',
      description='Climb the hand crack on the left side of the cliff. Maybe better as a TR as the top is a dirty slab.')
Route(name='Deep Sea Diver Crack',
      parent=book.formations['Deep Sea Diver'],
      item_id='DSD 3',
      grade='?',
      name_unconfirmed=True,
      description='Climb a system of thin cracks on the right side of the cliff from an obvious low jug. Be aware that the upper portion of this line is chossy and dirty.')
Route(name='Deep Sea Diver Right',
      parent=book.formations['Deep Sea Diver'],
      item_id='DSD 4',
      grade='?',
      name_unconfirmed=True,
      description='Climb the ledges on the far right of the cliff.')
Route(name='Jaws',
      parent=book.formations['Jaws'],
      grade=5,
      rating=2,
      description='Stand start using the best parts of the two opposed compression arêtes. A few squeezy moves leads to a dabby yoink to a jug followed by a hard to read top out.')
Route(name='Remora',
      parent=book.formations['Jaws'],
      grade=6,
      rating=2,
      name_unconfirmed=True,
      description='Lay down start in compression with your right hand at the bottom of the left hand sloping rib of Jaws and your left hand on a low sloper at the rim of a little alcove. A far away toe hook helps you pull off the ground. Pull a few moves to join the top of Jaws.')           
Route(name='Prince Albert',
      parent=book.formations['Prince Albert'],
      grade=4,
      rating=2,
      serious=1,
      description='A sequence of balancy moves lead you up the aesthetic trail faicing side of the boulder to a mercifully juggy top out. Stand start with left hand on the arête and right hand on a dishy sidepull. See boulder description for descent beta.') 
Route(name='Prince Albert, Cliff Face',
      parent=book.formations['Prince Albert'],
      name_unconfirmed=True,
      item_id='PA 2',
      grade='?',
      description='The cliff facing side of Prince Albert has apparently been climbed a number of different ways.')
Route(name='Easy up, easy down',
      parent=book.formations['Prince Albert'],
      grade=0,
      rating=1,
      serious=2,
      description='Climb the chossy slab.')
Variation(name='Baker\'s Dozen',
          parent=book.routes['Bread Loaf Traverse'],
          grade='7/8',
          rating=2,
          description='Start as for Bread Loaf Left, traverse into the bread loaf traverse.')
Variation(name='Late Start',
          parent=book.routes['Scratch and Spliff Traverse'],
          grade=2,
          rating=2,
          name_unconfirmed=True,
          description='Sit start with juggy holds at the top of a low ramp. Climb straight up into the top of Scratch '
                      'and Spliff Traverse.')
Variation(name='Machete Man',
          parent=book.routes['Machete Monkey'],
          grade=5,
          rating=1,
          grade_unconfirmed=True,
         description='A mediocre sit start joins Machete Monkey from the hole underneath. Begin with your right hand on the obvious edge and left hand on a low edge around the corner')       
                      
if __name__ == '__main__':
    sys.exit()
