import sys
sys.path.insert(1, '../LocalBoulders')
from dataStructure import *


book = Book(
    name='The Garden Boulders',
    collaborators=['Andrew Child'],
    repo='https://github.com/AndrewChild/The-Garden-Guidebook',
    dl='https://github.com/AndrewChild/The-Garden-Guidebook/raw/main/guideBook.pdf',
    options={'topos_attached_to_routes': True},
)


Area(name='The Garden Main',
     parent=book,
     gps='44.44076010641458, -122.5752659013521',
     description='Located about 3.5 miles down quatzville road from highway 20, park in the gravel pull out where the road bends '
     'left just before you reach the boulders. The Garden Main bouldering area is true to its name. '
     'A lush green space features moss covered boulders situated under a dense canopy.',)
Area(name='Pink Tag Boulders',
     parent=book,
     gps='44.43998124232581, -122.57539325959186',
     incomplete=True,
     description='Just across the road from the main area lay a few boulders on the banks of the River. Beware the '
                 'water level can rise quickly blocking off access to some of the boulders in this area. Consult '
                 'the USGS flow charts for below green peter damn to know when the river will be low. See driving '
                 'directions for the Garden Main area.',)
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
Area(name='Quartzville Creek',
     parent=book,
     incomplete=True,
     description='About an hour further down the road from the main area there are a few interesting boulders '
                 'in a creek. Generally lower temperatures, free camping, and pleasant swimming holes make this '
                 'a nice mid summer spot.')


Subarea(name='Entrance Area',
        parent=book.areas['The Garden Main'],
        description='A cluster of boulders situated inbetween the two main trails.'
    )
Subarea(name='Fight Club',
        parent=book.areas['The Garden Main'],
        description='Located in the southwest corner of the Garden main, The Fight Club zone is home to the '
                    'namesake V8 test piece as well as several other quality lines. Flat landings and easy access '
                    'make this a nice spot to spend some time')
Subarea(name='Undertow',
        parent=book.areas['The Garden Main'],
        description='Directly uphill from Fightclub are a few quality boulders separated by overgrown trails.')
Subarea(name='Meth Lab',
        parent=book.areas['The Garden Main'],
        description='Easily the most recognizable feature at the Garden, the Meth Lab boulder towers over all other stones in the '
                    'main area. Most climbs for this zone are located in a secluded natural amphitheater on the '
                    'uphill side of the boulder.')
Subarea(name='Big',
        parent=book.areas['The Garden Main'],
        description='Inspite of this area\'s close proximety to both the main trail and the road the most of the climbs here are '
                    'very obscure. Several other lines around here have been documented over the years but they have yet '
                    'to be rediscovered.')
Subarea(name='Azain',
        parent=book.areas['The Garden Main'],
        description='Azain is a jumbled collection of rocks which forms the highest point of the Garden main.',
        )
Subarea(name='Big Fred',
        parent=book.areas['The Garden Main'],)
Subarea(name='',
        parent=book.areas['Pink Tag Boulders'],)
Subarea(name='Entrance Area',
        item_id = 'entranceUpper',
        parent=book.areas['Upper Garden'],)
Subarea(name='The Bread Loaves/Scratch and Spliff',
        parent=book.areas['Upper Garden'],
        description='These two boulders are the area\'s main attraction. Historically some groups have called both '
                    'boulders Scratch and Spliff while others called them both the Bread Loaves. The modern compromise '
                    'seems to be that the upper boulder is Scratch and Spliff while the lower boulder is the Bread Loaf.')
Subarea(name='Redneck Riviera',
        parent=book.areas['Quartzville Creek'],
        gps='44.570410945356336, -122.4060701729652',
        description='Redneck rivierra is located on Quartzville road apporximately 20.6 miles from highway 20 park in '
                    'the gravel pull out on the creek side of the road. This '
                    'is a nice spot with good swimming access and a few established routes on both sides of the river. '
                    'The locals like to use this spot to pan for gold. In my experience they are friendly and willing '
                    'to share the space.')
Subarea(name='Old Miner\'s Camp',
        parent=book.areas['Quartzville Creek'],
        gps='44.58651338802075, -122.35033857932665',
        description='Located on Quartzville approximately 24.8 miles from highway 20, the old miner\'s camp is a '
                    'popular group campsite there are a few good sized boulders in the river only one boulder has '
                    'established lines on it. Park either at the camp day use area or on the side of the road '
                    'immediately above the Dab Rig boulder. Note: the dab rig boulder is typically underwater in the '
                    'rainy season.')


Formation(name='Toilet Bowl',
           parent=book.subareas['Entrance Area'],
           description='If approaching via the main trail this is the first boulder you will encounter just of the road.')
Formation(name='Boys In the Woods',
           parent=book.subareas['Entrance Area'],
           description='A low boulder with an identifiable scoop on the downhill side is located on the main trail '
                       'roughly 150ft uphill from the road.')
Formation(name='The Good Warmup',
           parent=book.subareas['Entrance Area'],
           description='A tiny finshaped boulder on the main trail.')
Formation(name='Tree Slab',
           parent=book.subareas['Entrance Area'],
           description='A narrow slab just uphill and to the right of the Boys in the Woods boulder.')
Formation(name='Tonsil',
           parent=book.subareas['Entrance Area'],
           description='A small hanging prow wedged under a larger hanging prow, which is itself wedged under the Meth Lab prow (a very big hanging prow).')
Formation(name='All Sorts of Ease',
           parent=book.subareas['Entrance Area'],
           description='A low angle slab under the Meth Lab prow')
Formation(name='Three Star Ledge',
           parent=book.subareas['Entrance Area'],
           description='Angular boulder in the rocky landscape between the two entrance trails.')
Formation(name='Overhand',
           parent=book.subareas['Entrance Area'],
           description='a short prow in the rocky landscape between the two entrance trails.')
Formation(name='Turtle Shell Boulder',
           parent=book.subareas['Entrance Area'],
           description='A short boulder with a low angle offwidth crack. If approaching on the fight club trail this is '
                       'the first boulder that you will encounter')
Formation(name='The Office',
           parent=book.subareas['Fight Club'],
           description='A tall not quite vertical boulder is immediately on your right as you enter the Fight Club Area')
Formation(name='Crash Test Dummies',
           parent=book.subareas['Fight Club'],
           description='A small boulder in between The Office and Fight Club.')
Formation(name='Fight Club',
           parent=book.subareas['Fight Club'],
           description='The obvious overhanging boulder with an interesting bubbly texture.')
Formation(name='Tyler Durten',
           parent=book.subareas['Fight Club'],
           description='Just to the left of the fight club boulder is a tall wall with few features other than a '
                       'distinctive crimp rail at eye level.')
Formation(name='Trust',
           parent=book.subareas['Fight Club'],
           description='The Trust boulder sits on an terrace behind Mini Me and to the Left of Tyler Durten')
Formation(name='Mini Me',
           parent=book.subareas['Fight Club'],
           description='A short pointy boulder with a flat landing is nearly freestanding on the downhill side of the '
                       'Fight Club zone',)
Formation(name='E\'s Dirty B',
           parent=book.subareas['Fight Club'],
           description='Following a faint trail west traveling past the trust boulder brings you to a Large boulder '
                       'which almost immediately gives way to low angle slab.')
Formation(name='Silly Steep',
           parent=book.subareas['Undertow'],
           description='Thin overhanging block left of the Undertow boulder.')
Formation(name='Undertow',
           parent=book.subareas['Undertow'],
           description='Realatively off the beaten path as far as classic garden boulders goes. Follow a faint trail '
                       'upill past the trust boulder.')
Formation(name='Car Alarm',
           parent=book.subareas['Undertow'],
           description='This secluded block has a variety of worthwhile beginner climbs. Most of the rock is covered with holds so its also a good spot to play around and make up your own linkups.')
Formation(name='Chockstone Highball',
           parent=book.subareas['Undertow'],
           description='')
Formation(name='Zen Koan',
           parent=book.subareas['Undertow'],
           description='A short boulder on the hillside inbetween Chockstone Highball and the Meth Lab.')
Formation(name='Meth Lab Front Side',
           parent=book.subareas['Meth Lab'],)
Formation(name='Meth Lab Back Side',
           parent=book.subareas['Meth Lab'],)
Formation(name='Swollen Member',
           parent=book.subareas['Meth Lab'],
           description='A small prow just out of the hill side above the Meth Lab boulder protrudes at a provocative angle.')
Formation(name='Meth Lab Highball',
           parent=book.subareas['Meth Lab'],
           description='Slabby boulder located to the left of Swollen Member. Not to be confused with the highballs on the actual Meth Lab boulder.')
Formation(name='E\'s Boulder',
           parent=book.subareas['Meth Lab'],
           description='A large boulder directly to the right of Octernal holds a few notable routes.')
Formation(name='The Bubbler',
           parent=book.subareas['Meth Lab'],
           description='A small unassuming block sits just downhill of E\'s boulder.')
Formation(name='Bitchin Corners',
           parent=book.subareas['Big'],
           description='A neet angular face sits on the downhill of an otherwise unremarkable boulder.')
Formation(name='Hueco Wabo',
           parent=book.subareas['Big'],
           description='An aesthetic boulder sits well off the beaten path')
Formation(name='Baldo',
           parent=book.subareas['Big'],)
Formation(name='Big',
           parent=book.subareas['Big'],
           description='The "Big" boulder is a large moss covered boulder on the eastern boundary of the Garden Main '
                       'area, in other guides this has also been called "roadside", and "North Block"')
Formation(name='Small',
           parent=book.subareas['Big'],)
Formation(name='The Good',
           parent=book.subareas['Azain'],
           description='Continuing up the main trail from Boys in the Woods leads to a good boulder with two routes on '
                       'the downhill face.')
Formation(name='Next to the Good',
           parent=book.subareas['Azain'],
           description='A slender boulder hangs off the ground to the left of the Good.')
Formation(name='Night Crawler',
           parent=book.subareas['Azain'],
           description='This iconic double arete boulder hangs like a throne near the top of the Azain formation.')
Formation(name='Azain Spire',
           parent=book.subareas['Azain'],
           description='A thin triangular flake stands on end behind swollen member and in front of Azain')
Formation(name='Light Cave',
           parent=book.subareas['Azain'],
           description='A cave directly behind Azain Spire is mostly full of bats and trash. Tread carefully if you '
                       'decide to venture down here.')
Formation(name='Azain',
           parent=book.subareas['Azain'],
           description='The huge walls of the Azain formation are located just off the main trail behind The Good.')
Formation(name='Locksmith',
           parent=book.subareas['Azain'],
           description='A tall narrow boulder that leans up against the backside of Azain.')
Formation(name='Garden Roof',
           parent=book.subareas['Azain'],
           description='Just past the locksmith is a wide short overhang which sits opposite a field of blackberries on '
                       'the main trail.')
Formation(name='Gumby Wall',
           parent=book.subareas['Azain'],
           description='Continuing past the Garden Roof leads to the Gumby Wall. Look for the obvious overhanging prow of '
                       'the siren.')
Formation(name='Gumby Crack',
           parent=book.subareas['Azain'],
           description='Immediately to the right of the Gumby Wall is another slab thats broken by a juggy horizontal crack.')
Formation(name='Big Fred',
           parent=book.subareas['Big Fred'],
           description='The main trail veers left into a narrow corridor inbetween this large boulder and Azain.')
Formation(name='Angry Grandma',
           parent=book.subareas['Big Fred'],
           description='A secluded boulder can be approached by staying right at the fork when the main trail turns left around Big Fred.')
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
Formation(name='Pony Boy',
           parent=book.subareas['Redneck Riviera'],
           description='A small boulder sits on the far bank of the river upriver from the parking.')
Formation(name='Mono Rail',
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
           description='A clean overhanging face points downhill the river downstream and across the river from the parking.')
Formation(name='The Dab Rig',
           parent=book.subareas['Old Miner\'s Camp'],
           description='')


Route(name='Raphael Crack',
      parent=book.formations['Turtle Shell Boulder'],
      grade=0,
      rating=1,
      description='Climb the wide crack from a stand start.')
Route(name='Donatello',
      parent=book.formations['Turtle Shell Boulder'],
      grade=1,
      rating=1,
      description='start on a flat ledge where the rock angle changes. Slap a low angle arete until you can hike your feet up. Only somewhat distinct from Leonardo.')
Route(name='Leonardo',
      parent=book.formations['Turtle Shell Boulder'],
      grade=3,
      rating=1,
      description='Lay down start with hands lon a low broken flake. With difficulty pull off the ground and slap a slopey ledge traverse up and left until you can rock over onto the downhill face. Sort of like a worse version of boys in the woods.')
Route(name='Toilet Bowl',
      parent=book.formations['Toilet Bowl'],
      grade=1,
      rating=1,
      description='Stand start on a protruding block with left hand on an undercling and right hand on a knob. Pull a few moves to gain the lip of the boulder.')
Route(name='Toilet Bowl Traverse',
      parent=book.formations['Toilet Bowl'],
      grade=0,
      rating=2,
      description='Starting on a good rail at the lower left of the boulder. Travers the lip topping out at the highest point or continue all the way until the boulder recedes into the hill',)
Route(name='Boys in the Woods',
      parent=book.formations['Boys In the Woods'],
      grade=4,
      rating=2,
      description='Start on a low jug just before the scoop at the lowest part of the boulder. Climb up the left '
                  'arete of the scoop until you can flop in. Some may consider this an eliminate since, with '
                  'difficulty, you could also just mantle directly into the scoop.',)
Route(name='Cuba Gooding',
      parent=book.formations['Boys In the Woods'],
      grade=6,
      rating=2,
      description='Start as for Boys in the Woods but climb right along the lip of the scoop into the top of Ice '
                  'Cubes Shiny Jerry Curl. Contrived.')
Route(name='Ice Cubes Shiny Jerry Curl',
      parent=book.formations['Boys In the Woods'],
      grade=6,
      rating=2,
      description='Sit start on a low sloping edge and make a huge reach to gain sharp crimps in thin horizontal '
                  'seams at eye level.')
Route(name='Tree Slab',
      parent=book.formations['Tree Slab'],
      grade="1+",
      rating=2,
      description='Climb the center of the slab from a stand start.')
Route(name='The Good Warm Up',
      parent=book.formations['The Good Warmup'],
      grade=0,
      rating=1,
      description='Whether or not this is a good warmup is debatable. Sit start with hands matched on good rail. Climb the short face using both aretes. Also known as Shark Fin.')
Route(name='Three Star Ledge',
      parent=book.formations['Three Star Ledge'],
      grade=2,
      rating=2,
      description='Stand start with hands matched on the ledge. Chuck out to the left arete and follow it to the apex of the boulder. The small boulders at the base are off.')
Route(name='Overhand',
      parent=book.formations['Overhand'],
      grade=7,
      grade_unconfirmed=True,
      description='Climbs a short overhang starting at the bottom of the left arete.')
Route(name='All Sorts of Ease',
      parent=book.formations['All Sorts of Ease'],
      grade='B',
      rating=2,
      description='Climb the left side of the face on good holds. Fun.')
Route(name='In the Shadow of Giants',
      parent=book.formations['All Sorts of Ease'],
      grade=2,
      rating=1,
      description='Stand start with wide hands. Left hand on thin pinch at head height and right hang on a slightly '
                  'higher small lumpy edge with a thumb catch. Pull a few delicate moves to gain the lip. A sit '
                  'start looks doable, but unpleasant.')
Route(name='Tonsil',
      parent=book.formations['Tonsil'],
      grade=4,
      rating=2,
      description='Step off the boulder below to gain high starting holds. Begin in compression with right hand on a '
                  'vertical side pull sloper on the blunt right corner and left hand on a juggy undercling.  Shorter '
                  'climbers will have difficulty reaching the starting holds. After establishing the rock below is '
                  'off.')
Route(name='Gingiva',
      name_unconfirmed=True,
      parent=book.formations['Tonsil'],
      grade=2,
      rating=1,
      description='Climbs the boulder below Tonsil. Sit start with low holds on the right arete. Pull a few awkward '
                  'moves into a cramped top out.')
Route(name='Trust',
      parent=book.formations['Trust'],
      grade=2,
      rating=3,
      description='Sit start in compression on a hanging refrigerator block. Climb straight up through a slopeing '
                  'ledge to the top. Look for the juggy crack ~1ft inset from the lip.')
Route(name='Mini Me',
      parent=book.formations['Mini Me'],
      grade=3,
      rating=0,
      description='start on blunt corner. Make tricky moves to a blocky jug to the lip and traverse left to an easy '
                  'top over a rocky landing')
Route(name='Austin Powers',
      parent=book.formations['Mini Me'],
      grade=5,
      rating=2,
      description='Start as for Mini Me but move right into top of Dr. Evil')
Route(name='Dr. Evil',
      parent=book.formations['Mini Me'],
      rating=2,
      grade=4,
      description='sit start in compression with left hand on a low sloper sidepull and right hand on the arete. '
                  'Pull some tricky moves to gain better holds either rolling onto the right hand slab early or '
                  'staying on the arete the whole way.')
Route(name='Project Mayhem',
      parent=book.formations['Tyler Durten'],
      rating=1,
      grade="1+",
      description='Start on a henious crimp rail and punch out left to much better holds.')
Route(name='Angel Face',
      parent=book.formations['Tyler Durten'],
      grade=6,
      grade_unconfirmed=True,
      description='Start as for Tyler Durten but climb more or less straight up using the sloping rib on the upper '
                  'right side of the boulder')
Route(name='Durten Layback',
      parent=book.formations['Tyler Durten'],
      grade=1,
      grade_unconfirmed=True,
      description='Stand start and climb the right corner using the Fight Club boulder for feet.')
Route(name='Jim Halpert',
      parent=book.formations['The Office'],
      rating=0,
      grade=1,
      serious=2,
      description='Starting on the right edge of the block climb climb the right corner over a rocky landing. Either '
                  'pull some harder moves to stay on the downhill face or round the corner to the right and pull '
                  'some easier moves over a worse landing. Grade and rating unconfirmed.',
      grade_unconfirmed=True)
Route(name='Daryl Philbin',
      parent=book.formations['The Office'],
      rating=3,
      grade="1/2",
      serious=2,
      description='Starting at the Center of the block climb left on good holds to the arete. Climb up the arete '
                  'until you can reach good face holds up right and continue through a, thankfully, juggy top out. '
                  'Mind the rock at the base of the climb. Left and right alternative starts add a little variety but do '
                  'not change the grade.')
Route(name='Vince',
      parent=book.formations['Crash Test Dummies'],
      rating=2,
      grade=2,
      description='Squat start on good edges. Navigate a crescent shaped sidpull rail to a delicate top out. Make '
                  'sure to clean the top out before attempting.')
Route(name='The Ear',
      parent=book.formations['Fight Club'],
      rating=3,
      grade="2+",
      description='Start on the arete at the far right end of the boulder. Climb straight up through tricky holds '
                  'to a heady top out. Veering onto the face instead of using the good holds on the right arete '
                  'bumps the grade up to around V4.')
Route(name='Fight Club',
      parent=book.formations['Fight Club'],
      rating=3,
      grade=8,
      description='Area classic, this rig is a feather in any would be crushers cap. Start on the far right arete as for Ear. '
                  'Traverse across the angle change and top out above a bubbly crimp rail on the overhanging face.')
Route(name='Fight Club 2',
      parent=book.formations['Fight Club'],
      grade=10,
      rating=2,
      description='Sit start with hands matched low on the left arete of the overhanging boulder. Climb across the overhang topping as for Fight Club.')
Route(name='Brewmaster',
      parent=book.formations['Fight Club'],
      grade=5,
      rating=2,
      description='Often mistaken for Fight Club 2. Sit start in the same spot but climb up the arete. Starting a '
                  'move or two in brings the grade down a bit. This is also known as tool shed direct.')
Route(name='E\'s Dirty B',
      parent=book.formations['E\'s Dirty B'],
      rating=2,
      grade=5,
      description='Start with hands matched on a lumpy flake in the back of a small cave. Using slopeing edges out right and a '
                  'difficult undercling navigate out of the cave trending right at the lip to a jug. The final '
                  'slab quest is an enjoyable and easy top out.',)
Route(name='Silly Steep Mantle',
      parent=book.formations['Silly Steep'],
      grade=4,
      rating=2,
      description='Stand start with good compression holds in the roof. Make a hard pull to the juggy edge below the '
                  'lip and figure out how to get your body over the top. Starting from the juggy edge knocks the '
                  'grade down to V2/3.')
Route(name='Undertow',
      parent=book.formations['Undertow'],
      grade=3,
      rating=3,
      description='Start on two boob shaped slopers at head height. Climb straight up using face holds and the right '
                  'arete.')
Route(name='Riptide',
      name_unconfirmed=True,
      parent=book.formations['Undertow'],
      grade=3,
      rating=2,
      description='Start as for undertow but trend right around the corner to a juggy hueco top out.')
Route(name='Simple Math',
      parent=book.formations['Undertow'],
      grade=3,
      grade_unconfirmed=True,
      description='Stand start with knobby holds at head height. Follow the diagonal seam up and right.')
Route(name='Tidepool',
      parent=book.formations['Undertow'],
      grade=3,
      grade_unconfirmed=True)
Route(name='Car Alarm Traverse',
      parent=book.formations['Car Alarm'],
      grade=2,
      rating=2,
      description='Stand start with hands on an incut rail at the far left end of the wall. Traverse right to pup truck staying below the lip the whole time. The reverse goes at the same grade.')
Route(name='White Rhino',
      name_unconfirmed=True,
      parent=book.formations['Car Alarm'],
      grade=1,
      rating=1,
      description='Stand start just left of 2 ton Chevy with left hand in a baseball size dish and right hand on the juggy part of a protruding rib. Climb up and left.')
Route(name='2 Ton Chevey',
      parent=book.formations['Car Alarm'],
      grade=1,
      rating=2,
      description='Squat start on a diagonal left hand edge and a shallow 3 finger pocket on your lower right. Climb up two flat ledges to the top.')
Route(name='Pup Truck',
      parent=book.formations['Car Alarm'],
      grade=0,
      rating=2,
      description='squat start on a blunt corner with right hand on a diagonal crimp and left hand in a shallow pocket.')
Route(name='Comp Route',
      name_unconfirmed=True,
      parent=book.formations['Car Alarm'],
      grade=0,
      rating=1,
      description='stand start with hands on an undercling at knee height. Using some tricky holds and a good left foot lunge out and left to a jug rail at the lip.')
Route(name='Panic Button',
      name_unconfirmed=True,
      parent=book.formations['Car Alarm'],
      grade=0,
      rating=1,
      description='Stand start just to the left of a rounded corner with feet on a blocky protrusion and not much for hands. Climb up and along the rounded corner.')
Route(name='Meth Lab Project',
      parent=book.formations['Meth Lab Front Side'],
      serious=3,
      description='The obvious prow on the front of the Meth Lab boulder has a bolted top rope anchor and maybe '
                  'someone has top roped it, but who knows. It\'s likely that the never been climbed by any other '
                  'means. The ethics of climbing this behemoth are contentious but in my opinion it is fair game to '
                  'bolt as a sport route. If you have the desire to do so consider '
                  'working it out on TR first before placing new equipment.')
Route(name='Don\'t Blow the Jug',
      parent=book.formations['Meth Lab Front Side'],
      grade='2+',
      rating=2,
      serious=1,
      description='Start at the base of the wide crack. Climb inverted in the offwidth until you can make use of a jug to '
                  'squeeze into the crack. Walk through the crack to the far side of the boulder.')
Route(name='Trust Issues',
      parent=book.formations['Meth Lab Front Side'],
      serious=2,
      grade='8',
      description='Sit start at the base of a diagonal crack. Proceed up and left over a subpar landing.')
Route(name='Leave it to Jesus',
      parent=book.formations['Meth Lab Front Side'],
      rating=3,
      grade=1,
      description='Also known as Showboat. Start with hands on sloping edges. Use one or two intermediate holds to reposition yourself and make a long pull to the lip. Short but brilliant.')
Route(name='Smackdown',
      parent=book.formations['Meth Lab Back Side'],
      rating=2,
      grade=6,
      description='Start standing with left hand gaston and right hand jug sidepull. Crank some powerful moves on bad feet '
                  'and follow the line of crimps to a top out left')
Route(name='Heisenburg',
      parent=book.formations['Meth Lab Back Side'],
      grade=9,
      grade_unconfirmed=True,
      description='Sit start with opposing sidepulls on a low flake. follow a slopey rib possibly making use of small'
                  ' holds further left.')
Route(name='Guillotine',
      name_unconfirmed=True,
      parent=book.formations['Meth Lab Back Side'],
      rating=2,
      grade=4,
      description='Start underclinging on the hanging \"Guillotine blade\" flake left of Octernal. Climb straight up.')
Route(name='Octernal',
      parent=book.formations['Meth Lab Back Side'],
      rating=3,
      grade=7,
      description='For many this is THE local test piece. Start sitting '
                  'with left hand on a sloping triangular rib and right hand on a slopey cripm at the arete. Crank a few hard '
                  'moves to gain the lip then traverse left through the lightning bolt hold to a pumpy top out. Originally known as \"Tom\'s phsychadelic trip\".')
Route(name='Two Blows One Stroke',
      parent=book.formations['Meth Lab Back Side'],
      grade=6,
      description='Sit start on two single pad edges just to the left of a right facing rib. Pop a left foot onto a '
                  'third  slightly wider edge and crank a few moves to gain a good edge roughly 7ft off the ground. '
                  'From here trend right into a flake.')
Route(name='Swollen Member',
      parent=book.formations['Swollen Member'],
      grade=3,
      rating=2,
      description='A classic hazing route. Start hugging the underside of the block underside with good hand holds '
                  'on each side of the stubby prow. Manuver youself into a less scandelous orientation using toe '
                  'hooks, heel hooks and  all manner of dirty tricks.')
Route(name='Meth Lab Highball',
      parent=book.formations['Meth Lab Highball'],
      rating=2,
      grade=1,
      serious=1,
      description='Stand start with left hand on a slopey ledge and right hand on a diagonal incut seam. Pull yourself onto the ledge and climb a tenuous slab using a blunt corner for your right hand.')
Route(name='Meth Lab Highball Right',
      parent=book.formations['Meth Lab Highball'],
      rating=1,
      grade=1,
      description='Start as for Meth Lab Highball but pull yourself around the blunt corner into a mossy scoop. Continue right to an easy top out.')
Route(name='Gargoyle',
      name_unconfirmed=True,
      parent=book.formations['E\'s Boulder'],
      rating=2,
      grade=3,
      description='Starts with a low right hand incut and traverses left across the boulder before circling back '
                  'along the lip before topping out. Sit start on the ramp for style points.')
Route(name='Slam Dunk',
      parent=book.formations['E\'s Boulder'],
      grade=7,
      description='Sit start with hands matching on a crimp rail on the lower right hand side of a small overhang. '
                  'Pull a few moves into the namesake slam dunk maneuver followed by an easy top out.')
Route(name='E\'s',
      parent=book.formations['E\'s Boulder'],
      grade=7,
      grade_unconfirmed=True,
      description='Stand start with hands matched on a chest high crimp rail. Pull a few enormous moves to a '
                  'big ledge.')
Route(name='Enchilada',
      rating=2,
      parent=book.formations['E\'s Boulder'],
      grade='8/9',
      description='Low ball. Sit start with hands matched on a crimp at the lower right of a crescent shaped rail. '
                  'Thrutch your way through a few hard moves to a good jug followed by a \"still on\" top out.')
Route(name='The Bubbler',
      parent=book.formations['The Bubbler'],
      grade=5,
      grade_unconfirmed=True,
      description='This short boulder reportedly goes at V5, no idea how.')
Route(name='Bitchin Corners',
      grade=2,
      rating=1,
      parent=book.formations['Bitchin Corners'],
      description='Stand start with left hand on a high diagonal crimp and right hand on an arete pinch.'
  )
Route(name='Frontside Baldo',
      parent=book.formations['Baldo'],
      grade=2,
      rating=2,
      description='Sit start with left hand on a juggy side pull and right hand at the bottom of the diagonal crack. Climb the triangular face using the crack and holds on both aretes.'
      )
Route(name='Hueco Wabo',
      grade=3,
      grade_unconfirmed=True,
      parent=book.formations['Hueco Wabo'],
      description='Stand start on good side pull underclings pull some rad moves to an insecure, scary top out. '
                  'It\'s possible to bail right at almost any point on this route, but that\'s no fun. A sit start '
                  'might also exist but looks unfun. Grade unconfirmed.')
Route(name='Mini Hydro Tube',
      grade=1,
      serious=1,
      grade_unconfirmed=True,
      parent=book.formations['Big'],
      description='Climbs a dirty water groove on the downhill face of the boulder. Scope out a down climb before '
                  'getting on this one')
Route(name='All Bernd Up',
      grade=10,
      grade_unconfirmed=True,
      parent=book.formations['Big'],
      description='Follows a hanging knife flake. Apparently there were multiple holds along both sides of the flake, but '
                  'they all broke off. It\'s unclear if this line has been climbed in it\'s current state.')
Route(name='Smol',
      name_unconfirmed=True,
      parent=book.formations['Small'],
      grade=2,
      rating=1,
      description='Sit start with left hand on good side pull pod. Right hand on crimp just below the angle chang. '
                  'Pull a few bear huggy moves to get on to. Better than it looks.')
Route(name='The Good Slab',
      parent=book.formations['The Good'],
      grade=1,
      rating=2,
      description='Squat start on an incut flake at knee height. Climb the slab around the corner from The Good.')
Route(name='The Good',
      parent=book.formations['The Good'],
      grade=3,
      rating=2,
      description='Start matched on a juggy flake on the right side of the boulder\'s downhill face.')
Route(name='Another',
      parent=book.formations['The Good'],
      grade=3,
      rating=1,
      serious=1,
      description='start with opposing sidepulls on the center of the boulder\'s downhill face. Traverse to the left '
                  'arete and ascend using delecate feet and unideal hands. Mind the uneven landing. Aggresive cleaning has reveiled that the dirty ledge to the left of the rock is infact part of the rock so stepping of here is still on route I guess, but its cooler if you don\'t.')
Route(name='Next to the Good',
      parent=book.formations['Next to the Good'],
      grade=3,
      rating=1,
      serious=1,
      description='Stand start with right hand on a crimp rail under the overhang and left on a high diagonal side pull. A few burly moves give way to a low angle slab. Bailing into the gully instead of climbing the upper slab doesn\'t change the grade, but it is cheating.'
      )
Route(name='Snakes and Martyrs',
      parent=book.formations['Azain Spire'],
      grade=0,
      rating=3,
      description=' Stand start in a juggy seam. Could be scary if you are uncomfortable climbing outside.'
  )
Route(name='Ground up Blowie',
      parent=book.formations['Azain'],
      rating=2,
      grade=5,
      description='Start at the base of a diagonal finger crack. Follow the crack around a dabby tree and onto an easy '
                  'slab. This route was named as an omage to the first ascent when the top out was cleaned via '
                  'leafblower from a stance mid route.')
Route(name='Into the Light',
      parent=book.formations['Light Cave'],
      grade=6,
      grade_unconfirmed=True, )
Route(name='Azain Crack',
      parent=book.formations['Azain'],
      grade='5.?',
      description='This isn\'t really a boulder but it is in the main area so it is included here. Climb the crack '
                  'to easier terrain. There are bolts on the route after the crack as well as at the top.')
Route(name='Night Crawler',
      parent=book.formations['Night Crawler'],
      grade=10,
      rating=2,
      description='Sit start at a juggy undercling on the right arete. Believe it or not this is a completely '
                  'different boulder than Hula.')
Route(name='Locksmith',
      parent=book.formations['Locksmith'],
      grade=4,
      rating=3,
      serious=2,
      description='Also known as Hula. Sit start with a juggy left hand sidebpull and right hand on an undercling edge. Pull a few '
                  'crimpy moves until you can reach a good hold on the arete. Rock over onto the slab and quest to '
                  'the top. Be sure to clean the upper section before attempting this rig.')
Route(name='Philanthropy',
      parent=book.formations['Locksmith'],
      grade=4,
      rating=1,
      serious=2,
      description='Stand start with wide hands, left on a crimp sloper and right on a crimp sidepull. Pull a few '
                  'techy moves to gain good jugs and rock over onto the slab. follow the path of least resistance or '
                  'least moss to the top.')
Route(name='Full Stroke',
      parent=book.formations['Garden Roof'],
      grade=2,
      rating=2,
      serious=1,
      description='Stand start on a jug flake. Trend left to a high top in a shallow chimney.'
  )
Route(name='Garden Project',
      parent=book.formations['Garden Roof'],
      description='Project. Sit start at the base of the low roof and climb into garden variety or Full Stroke. Once '
                  'climbed this will be one of the hardes routes in Oregon.')
Route(name='Garden Variety',
      parent=book.formations['Garden Roof'],
      grade=4,
      grade_unconfirmed=True,
      description='Reportedly there is a way to start the center of the overhanging face if you are tall or using a '
                  'pad stack. Does this even count as a distinct route or is it just a lame way to tick a line when '
                  'you can\'t pull the harder moves down low?')
Route(name='The Arboretum',
      parent=book.formations['Garden Roof'],
      grade=11,
      rating=3,
      description='Stand start with left hand on a big under cling and right in a small dish. Climb up and left.')
Route(name='The Other Bernd',
      parent=book.formations['Garden Roof'],
      rating=0,
      grade=10,
      grade_unconfirmed=True,
      description='Sit start on small opposing crimps at the far right of the block, climb more or less straight up '
                  'on exfoliating rock. Due to the crumbly nature of the rock its hard to tell what, if anything, '
                  'this ever was. It\'s uncear if this has been climbed in its current state.')
Route(name='The Siren',
      parent=book.formations['Gumby Wall'],
      grade=5,
      rating=3,
      description='Sit start at the base of the prow with one hand on an incut ledge and the other on the slopey rib below. Climb the prow using a few different beta options. This route is also refered to as "Witch Hunt".')
Route(name='Gumby Arete',
      parent=book.formations['Gumby Wall'],
      grade=2,
      rating=2,
      description='Stand start on underclings at the left side of the face. Challenge yourself by staying on the '
                  'Arete the whole way up or bail onto the ledge out right and top as for Gumby Slab.',)
Route(name='Gumby Slab',
      parent=book.formations['Gumby Wall'],
      grade=1,
      rating=3,
      description='Stand start in the center of the face. This can be scary if not used to climbing outdoors.',)
Route(name='Gumby Crack',
      parent=book.formations['Gumby Crack'],
      grade=0,
      rating=2,
      description='Climb the well featured wall to the right of Gumby slab from a stand start.',)
Route(name='Chockstone Highball',
      parent=book.formations['Chockstone Highball'],
      grade=4,
      grade_unconfirmed=True,)
Route(name='Zen Koan',
      parent=book.formations['Zen Koan'],
      grade=2,
      rating=2,
      name_unconfirmed=True,
      description='Stand start with a blocky hold near the top of a short overhang. Meander your way to the top.',)
Route(name='Big Fred',
      parent=book.formations['Big Fred'],
      grade=3,
      grade_unconfirmed=True,
      description='This highball has a storied legacy. It seems that at one point it was a well traveled classic but '
                  'it has since faded into mossy obscurity. One (very controversial) bolt exists on the face so you '
                  'could climb it as a sport route I guess.')
Route(name='Easy Grandma',
      name_unconfirmed=True,
      parent=book.formations['Angry Grandma'],
      grade=0,
      rating=1,
      description='Squat start on a juggy flake and climb using face holds the arete to a pyramid hold 12ft off the ground.')
Route(name='Angry Mom',
      parent=book.formations['Angry Grandma'],
      grade=2,
      rating=2,
      serious=1,
      description='Stand start over a ledge foot climb left around a flake then veer hard right towards the arete. '
                  'Exciting. Starting on sharp crimps to the right adds variety but doesn\'t feel like a distinct '
                  'route')
Route(name='Angry Grandma',
      parent=book.formations['Angry Grandma'],
      grade=7,
      grade_unconfirmed=True,
      description='Reportedly the intimidating overhanging face on the angry grandma boulder goes at V7. Looks hard and scary.')
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
Route(name='Buddha\'s Belly',
      parent=book.formations['Bread Loaf'],
      grade=4,
      rating=2,
      description='Stand start on two horizontal edges. Navigate your way to some good lumpy jugs midway up the ' 
                  'route and either mantle or side pull your way to the top. Also called bread loaf left.')
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
Route(name='Pony Boy',
      parent=book.formations['Pony Boy'],
      grade=2, 
      rating=0,
      description='Sit start with hands matched in a juggy pocket on the overhanging face of the boulder. Climbing '
                  'this thing is probably not worth getting your pads wet.')
Route(name='Monorail Project',
      parent=book.formations['Mono Rail'],
      description='Project. Start on the far right and traverse left along the lip.') 
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
      description='Stand start with a left hand sidepull about 5ft left of Ugly face.')
Route(name='Moss Boss',
      parent=book.formations['Moss Boss'],
      grade=3, 
      rating=1,) 
Route(name='Chicken Tendies',
      parent=book.formations['The 4.5'],
      grade=1, 
      rating=1,
      description='Stand start with hands matched on a good crimp rail on the left side of the boulder. Climb straight up.')
Route(name='Teenage Libertarians',
      parent=book.formations['The 4.5'],
      grade=4, 
      rating=3,
      description='Start as for chicken tendies but traverse right and ascend the tallest part of the boulder.')
Route(name='Falcon\'s Reach',
      parent=book.formations['The 4.5'],
      grade=3, 
      rating=1,
      description='Squat start on a juggy edge. Climb straight up.')
Route(name='Unsalted Almonds',
      parent=book.formations['The Dab Rig'],
      grade=7,
      grade_unconfirmed=True,)
Route(name='Dank Commander',
      parent=book.formations['The Dab Rig'],
      grade=4,
      grade_unconfirmed=True,)


Variation(name='Three Star Ledge Variation',
          parent=book.routes['Three Star Ledge'],
          grade=2,
          rating=2,
          description='Squat start with feet on the small boulder below 3 star (it\'s on this time!) and hands on opposing underclings.')
Variation(name='Tonsil Low Start',
          parent=book.routes['Tonsil'],
          description='Climb tonsil from the obvious lower holds without using the boulder below it as a foot. Seems '
                      'like it might go, but at a much harder grade.')
Variation(name='Prowed',
          parent=book.routes['Tonsil'],
          serious=2,
          description='Climb tonsil but instead of doing the normal top out, countinue climbing the steep prow above it. '
                'Reportedly this was an old school classic.')
Variation(name='Panic Button Variation',
          name_unconfirmed=True,
          parent=book.routes['Panic Button'],
          grade=2,
          rating=2,
          description='Sit start and pull into the start of Panic Button instead of topping right head left over the techy slab.')
Variation(name='Iron Cross',
          parent=book.routes['Trust'],
          grade=2,
          rating=1,
          description='Avoid the committing moves at the lip by traversing left early.')
Variation(name='Mr. Bigglesworth',
          parent=book.routes['Dr. Evil'],
          grade=1,
          rating=2,
          description='Start on your choice of waist high holds, climb straight up the right face or '
                'stay left on the arete. Authors note: other guides identify several other variations on '
                'this route, this book intentionally omits other variations in preference of encouraging '
                'climbers to find their own beta.')
Variation(name='Tyler Durten Dyno',
          parent=book.routes['Project Mayhem'],
          grade='?',
          description='It has been speculated that the dyno from the starting hold straight to the lip will go.')
Variation(name='Spray Against the Undertow',
          parent=book.routes['Undertow'],
          grade=6,
          description='Sit start with left hand in a slopey dish and right hand on a low sidepull. Pull some bizzare '
                      'moves to join into Undertow.')
Variation(name='Undertow Sit Start',
          parent=book.routes['Undertow'],
          grade=7,
          rating=3,
          description='Sit start left hand on a borken sidepull and right '
                      'hand on a low undercling, climb into undertow. At one point this line was simply refered to as '
                      'Undertow, for this book modern naming standards have been conserved.')
Variation(name='Shake it Out',
          parent=book.routes['Simple Math'],
          grade=3,
          rating=1,
          description='Stand start as for Simple Math and climb straight up into riptide.')
Variation(name='Cuba Gooding Variation',
          parent=book.routes['Cuba Gooding'],
          grade=3,
          rating=1,
          name_unconfirmed=True,
          description='Climb Cuba Gooding but use good holds to pull into the scoop and exit early.')
Variation(name='Leave it to Jesus Sit Start',
          parent=book.routes['Leave it to Jesus'],
          grade=7,
          grade_unconfirmed=True,
          description='Sit start on razor crimps to the lower left of the stand start.')
Variation(name='Leave it to Jesus Left',
          parent=book.routes['Leave it to Jesus'],
          grade=10,
          grade_unconfirmed=True,
          description='Sit start as for Trust Issues and traverse right all the way into Leave it to Jesus.')
Variation(name='Learys Lunge',
          parent=book.routes['Heisenburg'],
          grade=9,
          rating=3,
          description='Start as for Heiserburg and dyno up and right to juggy holds at the lip.')
Variation(name='Octernal Direct Exit',
          parent=book.routes['Octernal'],
          grade=7,
          rating=3,
          description='Of all the Octernal exits this one has the most interesting moves. Climb Octernal to the ledge '
                      'then pull some tricky moves to round the right arete. Continue on through a heads up top out.')
Variation(name='Octernal Center Exit',
          parent=book.routes['Octernal'],
          grade='6/7',
          rating=2,
          description='The easiest top option for this boulder involves pulling through a suprisingly good side pull '
                      'above the left end of the ledge. For years this variation livided in moss covered obscurity. '
                      'Climbing it will make you wonder why the awkward pumpfest traverse exit is the default line')
Variation(name='Sweethome Traverse',
          parent=book.routes['Octernal'],
          grade='3/4',
          rating=2,
          description='Climb Octernal from the ledge. Starting one move lower (on the undercling) adds a grade.')
Variation(name='Harbor Freight',
          parent=book.routes['Smackdown'],
          grade=8,
          rating=3,
          description='Sit down start with hands matched on a blocky undercling, climb into Smackdown. This variation was literally '
                      'unearthed when a local climber yarded a large rock out from the landing of Smackdown using a '
                      'chain and come along. The device broke in the process inspiring the name of the route.')
Variation(name='Meth Lab Highball Sit Start',
          name_unconfirmed=True,
          parent=book.routes['Meth Lab Highball'],
          grade=3,
          rating=1,
          description='Sit start with left hand on a diagonal undercling rail and right hand on a low diagonal side pull edge. Doesn\'t add much to the stand start.')
Variation(name='Into the Light Assis',
          parent=book.routes['Into the Light'],
          grade=9,
          grade_unconfirmed=True,)
Variation(name='Gargoyle Direct',
          name_unconfirmed=True,
          parent=book.routes['Gargoyle'],
          rating=2,
          grade=5,
          description='Starts as for Gargoyle but climbs straight up. Harder than it looks')
Variation(name='Bitchin Corners Sit',
          parent=book.routes['Bitchin Corners'],
          rating=2,
          grade=6,
          description='Sit start with hands matched on a sharp corner at the bottom of the right arete.')
Variation(name='Brain Haemorrhage',
          parent=book.routes['Locksmith'],
          grade=7,
          description='Start as for locksmith and traverse right into philanthropy',
          grade_unconfirmed=True,)
Variation(name='The Siren Stand Start',
          parent=book.routes['The Siren'],
          grade=3,
          rating=2,
          description='Start with your left hand on the left arete and right hand on a good sidepull just above the sit '
                      'start holds.',)
Variation(name='Bag of Tricks',
          parent=book.routes['Gumby Slab'],
          grade=3,
          rating=1,
          description='Start as for Siren and traverse right topping on either Gumby Arete or Gumby Slab.')
Variation(name='Baker\'s Dozen',
          parent=book.routes['Bread Loaf Traverse'],
          grade=8,
          grade_unconfirmed=True,
          description='Start as for Buddha\'s Belly, traverse into the bread loaf traverse.')
Variation(name='Late Start',
          parent=book.routes['Scratch and Spliff Traverse'],
          grade=2,
          rating=2,
          name_unconfirmed=True,
          description='Sit start with juggy holds at the top of a low ramp. Climb straight up into the top of Scratch '
                      'and Spliff Traverse.')


# Photo(name='Austin Powers',
#       fileName='AustinPowers.jpg',
#       parent=book.formations['Mini Me'],
#       route=book.routes['austinPowers'],
#       credit='Andrew Child',
#       description='Carson cranking across the face on Austin Powers.'),
Photo(name='Riptide',
      fileName='Riptide.jpg',
      parent=book.formations['Undertow'],
      route=book.routes['Riptide'],
      credit='Andrew Child',
      description='Rob on Riptide')
Photo(name='Fight Club',
      fileName='FightClub2.jpg',
      parent=book.formations['Fight Club'],
      route=book.routes['Fight Club'],
      credit='Andrew Child',
      description='Michael near the top of Fight Club.')
Photo(name='Octernal',
      fileName='Octurnal.jpg',
      parent=book.formations['Meth Lab Back Side'],
      route=book.routes['Octernal'],
      credit='Andrew Child',
      description='Carson landing the big throw on Octernal. Classic!')
# Photo(name='Smackdown',
      # fileName='Smackdown.jpg',
      # parent=book.formations['Meth Lab Back Side'],
      # route=book.routes['smackdown'],
      # credit='Carson Dension',
      # description='Andrew posting up at the start of Smackdown')
Photo(name='Ground up Blowie',
      fileName='blowie.jpg',
      parent=book.formations['Azain'],
      route=book.routes['Ground up Blowie'],
      credit='Michael Gardener Brown',
      description='Andrew strugling to finde a finger lock on Ground up Blowie')
Topo(name='Bitchin Corners',
     parent=book.formations['Bitchin Corners'],
     fileName='bitchin.svg',
     size='h',
     description='Bitchin Corners',
     routes={
         'path1002': book.routes['Bitchin Corners'],
         'path1029': book.routes['Bitchin Corners'],
         'path1014': book.variations['Bitchin Corners Sit'],
         'path1031': book.variations['Bitchin Corners Sit'],
     })
Topo(name='Baldo',
     parent=book.formations['Baldo'],
     fileName='baldo.svg',
     size='h',
     description='Baldo',
     routes={
         'path862': book.routes['Frontside Baldo'],
         'path864': book.routes['Frontside Baldo'],
     })
Topo(name='Overhand',
     parent=book.formations['Overhand'],
     fileName='overhand.svg',
     size='h',
     description='Overhand',
     routes={
         'path293': book.routes['Overhand'],
         'path443': book.routes['Overhand'],
     })
Topo(name='Hueco Wabo',
     parent=book.formations['Hueco Wabo'],
     fileName='hueco.svg',
     size='h',
     description='Hueco Wabo',
     routes={
         'path1918': book.routes['Hueco Wabo'],
         'path1920': book.routes['Hueco Wabo'],
     })
Topo(name='Azain Spire',
     parent=book.formations['Azain Spire'],
     fileName='azainSpire.svg',
     size='h',
     description='Azain Spire',
     routes={
         'path724': book.routes['Snakes and Martyrs'],
         'path726': book.routes['Snakes and Martyrs'],
     })
Topo(name='Three Star Ledge',
     parent=book.formations['Three Star Ledge'],
     fileName='3star.svg',
     size='h',
     description='Three Star Ledge',
     routes={
         'path300': book.routes['Three Star Ledge'],
         'path583': book.routes['Three Star Ledge'],
         'path514': book.variations['Three Star Ledge Variation'],
         'path529': book.variations['Three Star Ledge Variation'],
         'path585': book.variations['Three Star Ledge Variation'],
     })
Topo(name='The Good',
     parent=book.formations['The Good'],
     fileName='good.svg',
     size='f',
     description='The Good',
     routes={
         'path1453': book.routes['The Good'],
         'path1459': book.routes['The Good'],
         'path1451': book.routes['Another'],
         'path1457': book.routes['Another'],
         'path1445': book.routes['Next to the Good'],
         'path1447': book.routes['Next to the Good'],
         'path1449': book.routes['Next to the Good'],
         'path1455': book.routes['The Good Slab'],
         'path1461': book.routes['The Good Slab'],
     })
Topo(name='Fight Club Right Side',
     parent=book.formations['Fight Club'],
     fileName='fightClub.svg',
     size='h',
     description='Fight Club Right Side',
     routes={
         'path1145': book.routes['The Ear'],
         'path1151': book.routes['The Ear'],
         'path1143': book.routes['Fight Club'],
         'path1153': book.routes['Fight Club'],
         'path1147': book.routes['Vince'],
         'path1149': book.routes['Vince'],
     })
Topo(name='Fight Club Left Side',
     parent=book.formations['Fight Club'],
     fileName='fightClub2.svg',
     size='h',
     description='Fight Club Left Side',
     routes={
         'path1297': book.routes['Fight Club 2'],
         'path1303': book.routes['Fight Club 2'],
         'path1299': book.routes['Fight Club'],
         'path1301': book.routes['Fight Club'],
         'path1293': book.routes['Brewmaster'],
         'path1305': book.routes['Brewmaster'],
     })
Topo(name='E\'s Dirty B',
     parent=book.formations['E\'s Dirty B'],
     fileName='eDirty.svg',
     size='h',
     description='E\'s Dirty B',
     routes={
         'path1003': book.routes['E\'s Dirty B'],
         'path1005': book.routes['E\'s Dirty B'],
     })
Topo(name='Car Alarm Downhill Side',
     parent=book.formations['Car Alarm'],
     fileName='carAlarm.svg',
     size='f',
     description='Car Alarm Downhill Side',
     routes={
         'path674': book.routes['Car Alarm Traverse'],
         'path676': book.routes['Car Alarm Traverse'],
         'path670': book.routes['White Rhino'],
         'path678': book.routes['White Rhino'],
         'path668': book.routes['2 Ton Chevey'],
         'path680': book.routes['2 Ton Chevey'],
         'path666': book.routes['Pup Truck'],
         'path682': book.routes['Pup Truck'],
     })
Topo(name='Car Alarm Uphill Side',
     parent=book.formations['Car Alarm'],
     fileName='carAlarm2.svg',
     size='h',
     description='Car Alarm Uphill Side',
     routes={
         'path824': book.routes['Comp Route'],
         'path863': book.routes['Comp Route'],
         'path851': book.routes['Panic Button'],
         'path861': book.routes['Panic Button'],
         'path857': book.variations['Panic Button Variation'],
         'path859': book.variations['Panic Button Variation'],
     })
Topo(name='Boys in the Woods',
     parent=book.formations['Boys In the Woods'],
     fileName='BITW.svg',
     size='f',
     description='Boys in the Woods and Tree Slab',
     routes={
         'path300': book.routes['Boys in the Woods'],
         'path458': book.routes['Boys in the Woods'],
         'path1485': book.routes['Cuba Gooding'],
         'path460': book.routes['Cuba Gooding'],
         'path400': book.routes['Ice Cubes Shiny Jerry Curl'],
         'path462': book.routes['Ice Cubes Shiny Jerry Curl'],
         'path404': book.routes['Tree Slab'],
         'path464': book.routes['Tree Slab'],
         'path480': book.variations['Cuba Gooding Variation'],
         'path426': book.variations['Cuba Gooding Variation'],
     })
Topo(name='enchilada',
     parent=book.formations['E\'s Boulder'],
     fileName='enchilada.svg',
     size='h',
     description='Enchilada',
     routes={
         'path848': book.routes['Enchilada'],
         'path902': book.routes['Enchilada'],
     })
Topo(name='Slam dunk',
     parent=book.formations['E\'s Boulder'],
     fileName='eboulder2.svg',
     size='h',
     description='Slam dunk',
     routes={
         'path1489': book.routes['Slam Dunk'],
         'path1487': book.routes['Slam Dunk'],
     })
Topo(name='Gargoyle',
     parent=book.formations['E\'s Boulder'],
     fileName='eboulder3.svg',
     size='h',
     description='Gargoyle',
     routes={
         'path1625': book.routes['Gargoyle'],
         'path1627': book.routes['Gargoyle'],
         'path1631': book.variations['Gargoyle Direct'],
         'path1629': book.variations['Gargoyle Direct'],
         'path1635': book.routes['Slam Dunk'],
         'path1633': book.routes['Slam Dunk'],
     })
Topo(name='Zen Koan',
     parent=book.formations['Zen Koan'],
     fileName='koan.svg',
     size='h',
     description='Zen Koan',
     routes={
         'path1777': book.routes['Zen Koan'],
         'path1775': book.routes['Zen Koan'],
     })
Topo(name='Night Crawler',
     parent=book.formations['Night Crawler'],
     fileName='nightCrawler.svg',
     size='h',
     description='Night Crawler',
     routes={
         'path1342': book.routes['Night Crawler'],
         'path1396': book.routes['Night Crawler'],
     })
Topo(name='Jesus',
     parent=book.formations['Meth Lab Front Side'],
     fileName='jesus.svg',
     size='f',
     description='Methlab East Face',
     routes={
         'path1908': book.routes['Don\'t Blow the Jug'],
         'path1910': book.routes['Don\'t Blow the Jug'],
         'path1906': book.routes['Trust Issues'],
         'path1912': book.routes['Trust Issues'],
         'path1902': book.routes['Leave it to Jesus'],
         'path1916': book.routes['Leave it to Jesus'],
         'path1904': book.variations['Leave it to Jesus Sit Start'],
         'path1914': book.variations['Leave it to Jesus Sit Start'],
         'path736': book.variations['Leave it to Jesus Left'],
         'path734': book.variations['Leave it to Jesus Left'],
     })
Topo(name='Methlab Backside',
     parent=book.formations['Meth Lab Back Side'],
     fileName='Methlab.svg',
     size='f',
     description='Meth Lab backside',
     routes={
         'path1874': book.routes['Smackdown'],
         'path1856': book.routes['Smackdown'],
         'path1876': book.variations['Harbor Freight'],
         'path1856-2': book.variations['Harbor Freight'],
         'path1878': book.routes['Heisenburg'],
         'path1858': book.routes['Heisenburg'],
         'path1880': book.variations['Learys Lunge'],
         'path1860': book.variations['Learys Lunge'],
         'path1886': book.routes['Octernal'],
         'path1864': book.routes['Octernal'],
         'path1884': book.routes['Guillotine'],
         'path1866': book.routes['Guillotine'],
         'path1888': book.variations['Octernal Center Exit'],
         'path1868': book.variations['Octernal Center Exit'],
         'path1890': book.variations['Octernal Direct Exit'],
         'path1862': book.variations['Octernal Direct Exit'],
         'path1892': book.routes['E\'s'],
         'path1872': book.routes['E\'s'],
     })
Topo(name='octernal2',
     parent=book.formations['Meth Lab Back Side'],
     fileName='octurnal2.svg',
     size='h',
     description='Meth Lab across from E\'s',
     routes={
         'path3604': book.routes['Two Blows One Stroke'],
         'path3553': book.variations['Octernal Direct Exit'],
         'path3608': book.routes['Two Blows One Stroke'],
         'path3606': book.variations['Octernal Direct Exit'],
     })
Topo(name='Locksmith',
     parent=book.formations['Locksmith'],
     fileName='locksmith.svg',
     size='h',
     description='The Locksmith',
     routes={
         'path1894': book.routes['Locksmith'],
         'path1898': book.routes['Locksmith'],
         'path1896': book.variations['Brain Haemorrhage'],
         'path1900': book.variations['Brain Haemorrhage'],
     })
Topo(name='arboretum',
     parent=book.formations['Garden Roof'],
     fileName='arboretum.svg',
     size='h',
     description='Routes on the Garden Roof',
     routes={
         'path501': book.routes['Garden Variety'],
         'path505': book.routes['Garden Project'],
         'path293': book.routes['The Arboretum'],
         'path349': book.routes['The Other Bernd'],
         'path512': book.routes['Garden Variety'],
         'path510': book.routes['Garden Project'],
         'path508': book.routes['The Arboretum'],
         'path508-1': book.routes['The Other Bernd'],
     })
Topo(name='siren',
     parent=book.formations['Gumby Wall'],
     fileName='siren.svg',
     size='h',
     description='The Siren',
     routes={
         'path5162': book.variations['The Siren Stand Start'],
         'path4111': book.routes['The Siren'],
         'path4117': book.routes['Gumby Arete'],
         'path4212': book.routes['The Other Bernd'],
         'path4115': book.variations['Bag of Tricks'],
         'path4175': book.routes['The Siren'],
         'path4175-8': book.routes['Gumby Arete'],
         'path4175-8-6': book.routes['The Other Bernd'],
         'path4175-2': book.variations['Bag of Tricks'],
         'path4175-8-6-6': book.variations['The Siren Stand Start'],
     })
Topo(name='Gumby',
     parent=book.formations['Gumby Wall'],
     fileName='gumby.svg',
     size='h',
     description='Gumby Slab',
     routes={
         'path1571': book.variations['Bag of Tricks'],
         'path1573': book.variations['Bag of Tricks'],
         'path1678': book.variations['Bag of Tricks'],
         'path1569': book.routes['Gumby Arete'],
         'path1676': book.routes['Gumby Arete'],
         'path1563': book.routes['Gumby Slab'],
         'path1674': book.routes['Gumby Slab'],
     })
Topo(name='Mini Me 3',
     parent=book.formations['Mini Me'],
     fileName='miniMe3.svg',
     size='h',
     description='Mini Me',
     routes={
         'path1844': book.routes['Dr. Evil'],
         'path1842': book.routes['Dr. Evil'],
         'path1850': book.routes['Dr. Evil'],
         'path1846': book.routes['Austin Powers'],
         'path1852': book.routes['Austin Powers'],
         'path1848': book.routes['Mini Me'],
         'path1854': book.routes['Mini Me'],
     })
Topo(name='Office',
     parent=book.formations['The Office'],
     fileName='office.svg',
     size='h',
     description='The Office',
     routes={
         'path1834': book.routes['Daryl Philbin'],
         'path1838': book.routes['Daryl Philbin'],
         'path1836': book.routes['Jim Halpert'],
         'path1840': book.routes['Jim Halpert'],
     })
Topo(name='Swollen Member',
     parent=book.formations['Swollen Member'],
     fileName='swollen2.svg',
     size='h',
     description='Swollen Member and Meth Lab High Ball',
     routes={
         'path1813': book.routes['Meth Lab Highball'],
         'path2042': book.routes['Meth Lab Highball'],
         'path1830': book.variations['Meth Lab Highball Sit Start'],
         'path2040': book.variations['Meth Lab Highball Sit Start'],
         'path1832': book.routes['Meth Lab Highball Right'],
         'path2044': book.routes['Meth Lab Highball Right'],
         'path1760': book.routes['Swollen Member'],
         'path1811': book.routes['Swollen Member'],
         'path2046': book.routes['Swollen Member'],
     })
Topo(name='Toilet Bowl',
     parent=book.formations['Toilet Bowl'],
     fileName='toiletBowl.svg',
     size='h',
     description='Toilet Bowl',
     routes={
         'path1752': book.routes['Toilet Bowl'],
         'path1756': book.routes['Toilet Bowl'],
         'path1754': book.routes['Toilet Bowl Traverse'],
         'path1758': book.routes['Toilet Bowl Traverse'],
     })
Topo(name='Tonsil',
     parent=book.formations['Tonsil'],
     fileName='tonsil.svg',
     size='h',
     description='Tonsil',
     routes={
         'path1686': book.routes['Tonsil'],
         'path1688': book.routes['Tonsil'],
         'path1696': book.routes['Tonsil'],
         'path1680': book.routes['All Sorts of Ease'],
         'path1690': book.routes['All Sorts of Ease'],
         'path1682': book.routes['In the Shadow of Giants'],
         'path1692': book.routes['In the Shadow of Giants'],
         'path1684': book.routes['Gingiva'],
         'path1694': book.routes['Gingiva'],
         'path716': book.variations['Prowed'],
         'path566': book.variations['Prowed'],
     })
Topo(name='Trust',
     parent=book.formations['Tyler Durten'],
     fileName='trust.svg',
     size='h',
     description='Trust and Tyler Durten',
     routes={
         'path678': book.routes['Trust'],
         'path830': book.routes['Trust'],
         'path776': book.variations['Iron Cross'],
         'path832': book.variations['Iron Cross'],
         'path834': book.routes['Project Mayhem'],
         'path836': book.routes['Project Mayhem'],
         'path838': book.variations['Tyler Durten Dyno'],
         'path840': book.variations['Tyler Durten Dyno'],
         'path298': book.routes['Angel Face'],
         'path410': book.routes['Angel Face'],
         'path302': book.routes['Durten Layback'],
         'path412': book.routes['Durten Layback'],
     })
Topo(name='Turtle',
     parent=book.formations['Turtle Shell Boulder'],
     fileName='turtle.svg',
     size='h',
     description='Turtle Shell',
     routes={
         'path855': book.routes['Raphael Crack'],
         'path861': book.routes['Raphael Crack'],
         'path857': book.routes['Donatello'],
         'path863': book.routes['Donatello'],
         'path859': book.routes['Leonardo'],
         'path919': book.routes['Leonardo'],
     })
Topo(name='Undertow',
     parent=book.formations['Undertow'],
     fileName='undertow.svg',
     size='h',
     description='Undertow downhill face',
     routes={
         'path1097': book.routes['Undertow'],
         'path1111': book.routes['Undertow'],
         'path1099': book.variations['Spray Against the Undertow'],
         'path1105': book.variations['Spray Against the Undertow'],
         'path1101': book.variations['Undertow Sit Start'],
         'path1107': book.variations['Undertow Sit Start'],
         'path1103': book.routes['Riptide'],
         'path1109': book.routes['Riptide'],
     })
Topo(name='Undertow2',
     parent=book.formations['Undertow'],
     fileName='undertow2.svg',
     size='f',
     description='Undertow East face',
     routes={
         'path932': book.routes['Silly Steep Mantle'],
         'path942': book.routes['Silly Steep Mantle'],
         'path938': book.routes['Undertow'],
         'path946': book.routes['Undertow'],
         'path934': book.variations['Spray Against the Undertow'],
         'path944': book.variations['Spray Against the Undertow'],
         'path936': book.variations['Undertow Sit Start'],
         'path950': book.variations['Undertow Sit Start'],
         'path1134': book.routes['Riptide'],
         'path948': book.routes['Riptide'],
         'path940': book.routes['Tidepool'],
         'path952': book.routes['Tidepool'],
         'path1309': book.routes['Simple Math'],
         'path1305': book.routes['Simple Math'],
         'path1307': book.variations['Shake it Out'],
         'path748': book.variations['Shake it Out'],
     })
Topo(name='Baseball',
     parent=book.formations['Baseball'],
     fileName='baseball.svg',
     size='h',
     description='Baseball',
     routes={
         'path349': book.routes['Baseball'],
         'path293': book.routes['Baseball'],
         'path351': book.routes['Bunt'],
         'path295': book.routes['Bunt'],
     })
Topo(name='Bread Loaf',
     parent=book.formations['Bread Loaf'],
     fileName='breadLoaf.svg',
     size='h',
     description='Bread Loaf',
     routes={
         'path543': book.routes['Buddha\'s Belly'],
         'path1100': book.routes['Buddha\'s Belly'],
         'path1104': book.routes['Bread Loaf Traverse'],
         'path1153': book.routes['Bread Loaf Traverse'],
         'path1155': book.variations['Baker\'s Dozen'],
         'path1157': book.variations['Baker\'s Dozen'],
     })
Topo(name='Bread Loaf2',
     parent=book.formations['Bread Loaf'],
     fileName='breadLoaf2.svg',
     size='h',
     description='Bread Loaf 2',
     routes={
         'path1350': book.routes['Worf'],
         'path1348': book.routes['Worf'],
         'path1346': book.routes['Worf'],
     })
Topo(name='Scratch and Spliff',
     parent=book.formations['Scratch and Spliff'],
     fileName='scratchSpliff.svg',
     size='h',
     description='Scratch and Spliff',
     routes={
         'path1921': book.routes['Spliff'],
         'path1919': book.routes['Spliff'],
         'path1925': book.routes['Scratch and Spliff Traverse'],
         'path1923': book.routes['Scratch and Spliff Traverse'],
         'path1917': book.routes['Roach'],
         'path1915': book.routes['Roach'],
         'path2515': book.routes['For What it\'s Worth'],
         'path2513': book.routes['For What it\'s Worth'],
     })
Topo(name='Scratch and Spliff 2',
     parent=book.formations['Scratch and Spliff'],
     fileName='scratchSpliff2.svg',
     size='f',
     description='Scratch and Spliff 2',
     routes={
         'path2067': book.routes['Scratch and Spliff Traverse'],
         'path2065': book.routes['Scratch and Spliff Traverse'],
         'path2080': book.routes['Spliff'],
         'path2075': book.routes['Spliff'],
         'path2077': book.routes['Scratch'],
         'path2073': book.routes['Scratch'],
         'path2071': book.variations['Late Start'],
         'path2069': book.variations['Late Start'],
     })
Topo(name='Scratch and Spliff 3',
     parent=book.formations['Scratch and Spliff'],
     fileName='scratchSpliff3.svg',
     size='h',
     description='Scratch and Spliff 3',
     routes={
         'path2226': book.routes['Caliban\'s War'],
         'path2224': book.routes['Caliban\'s War'],
         'path2222': book.routes['Caliban\'s War'],
         'path2228': book.routes['Stoned Age'],
         'path2230': book.routes['Stoned Age'],
     })
AreaMap(name='The Garden Main Area Overview',
        parent=book.areas['The Garden Main'],
        fileName='Garden.svg',
        sub_areas={
            'rect2027': book.subareas['Big'],
            'rect1376': book.subareas['Azain'],
            'rect2313': book.subareas['Entrance Area'],
            'rect2908': book.subareas['Big Fred'],
            'rect3027': book.subareas['Fight Club'],
            'rect3200': book.subareas['Meth Lab'],
            'rect3386': book.subareas['Undertow'],
        },
        layers=['Base'],
        size='f',
        description='The Garden Main Area Overview',)
AreaMap(name='Armageddon Area Overview',
        parent=book.areas['Upper Garden'],
        fileName='upperGarden.svg',
        sub_areas={
            'rect27128': book.subareas['The Bread Loaves/Scratch and Spliff'],
            'rect27051': book.subareas['entranceUpper'],
        },
        layers=['Base', 'border'],
        border='rect27048',
        size='f',
        description='The Garden Main Area Overview',)
SubAreaMap(name='Entrance Area map',
           parent=book.subareas['Entrance Area'],
           outFileName='entrance.png',
           fileName='Garden.svg',
           path_i='./maps/area/',
           path_o='./maps/area/',
           layers=['Entrance', 'Base'],
           border='rect2313',
           description='Entrance Area map',
           routes={
           'path1767': book.routes['Toilet Bowl Traverse'],
           'path1769': book.routes['Toilet Bowl'],
           'path1771': book.routes['Donatello'],
           'path1773': book.routes['Leonardo'],
           'path1775': book.routes['Raphael Crack'],
           'path1777': book.routes['Overhand'],
           'path1779': book.routes['Three Star Ledge'],
           'path1781': book.routes['All Sorts of Ease'],
           'path1783': book.routes['In the Shadow of Giants'],
           'path1785': book.routes['Tonsil'],
           'path1787': book.routes['Boys in the Woods'],
           'path1789': book.routes['Ice Cubes Shiny Jerry Curl'],
           'path1791': book.routes['Tree Slab'],
           })
SubAreaMap(name='Fight Club Area map',
           parent=book.subareas['Fight Club'],
           outFileName='fightClub.png',
           fileName='Garden.svg',
           path_i='./maps/area/',
           path_o='./maps/area/',
           layers=['Fight Club', 'Base'],
           border='rect3027',
           description='Fight Club Area map',
           size='f',
           routes={
           'path4077': book.routes['E\'s Dirty B'],
           'path1519': book.routes['Jim Halpert'],
           'path1517': book.routes['Daryl Philbin'],
           'path1515': book.routes['Vince'],
           'path1513': book.routes['The Ear'],
           'path1511': book.routes['Fight Club 2'],
           'path1509': book.routes['Project Mayhem'],
           'path1507': book.routes['Trust'],
           'path1505': book.routes['Austin Powers'],
           'path1503': book.routes['Dr. Evil'],
           })
SubAreaMap(name='Undertow area map',
           parent=book.subareas['Undertow'],
           outFileName='undertow.png',
           fileName='Garden.svg',
           path_i='./maps/area/',
           path_o='./maps/area/',
           layers=['Undertow', 'Base'],
           border='rect3386',
           description='Undertow area map',
           routes={
               'path1244': book.routes['Silly Steep Mantle'],
               'path1246': book.routes['Undertow'],
               'path1248': book.routes['Tidepool'],
               'path1250': book.routes['Chockstone Highball'],
               'path1252': book.routes['Car Alarm Traverse'],
               'path1254': book.routes['2 Ton Chevey'],
               'path1256': book.routes['Pup Truck'],
               'path1258': book.routes['Comp Route'],
               'path1260': book.routes['Panic Button'],
               'path3384': book.routes['Zen Koan'],
           })
SubAreaMap(name='Meth Lab area map',
           parent=book.subareas['Meth Lab'],
           outFileName='methLab.png',
           fileName='Garden.svg',
           path_i='./maps/area/',
           path_o='./maps/area/',
           layers=['Meth Lab', 'Base'],
           border='rect3200',
           description='Meth Lab area map',
           routes={
               'path760': book.routes['Don\'t Blow the Jug'],
               'path762': book.routes['Trust Issues'],
               'path764': book.routes['Leave it to Jesus'],
               'path766': book.routes['Smackdown'],
               'path768': book.routes['Heisenburg'],
               'path770': book.routes['Guillotine'],
               'path772': book.routes['Octernal'],
               'path774': book.routes['Two Blows One Stroke'],
               'path776': book.routes['E\'s'],
               'path778': book.routes['Enchilada'],
               'path780': book.routes['Swollen Member'],
               'path782': book.routes['Meth Lab Highball'],
               'path784': book.routes['The Bubbler'],
               'path4341': book.routes['Meth Lab Project'],
               'path426': book.routes['Slam Dunk'],
               'path428': book.routes['Gargoyle'],
           })
SubAreaMap(name='Big area map',
           parent=book.subareas['Big'],
           outFileName='big.png',
           fileName='Garden.svg',
           path_i='./maps/area/',
           path_o='./maps/area/',
           description='Big area map',
           routes={
               'path5664': book.routes['Frontside Baldo'],
               'path5662': book.routes['Hueco Wabo'],
               'path5660': book.routes['All Bernd Up'],
               'path410': book.routes['Mini Hydro Tube'],
               'path5658': book.routes['Bitchin Corners'],
               'path5658-4': book.routes['Smol'],
           },
           layers=['Big', 'Base'],
           border='rect2027'),
SubAreaMap(name='Azain area map',
           parent=book.subareas['Azain'],
           outFileName='azain.png',
           fileName='Garden.svg',
           path_i='./maps/area/',
           path_o='./maps/area/',
           description='Azain area map',
           size='f',
           routes={
               'path738': book.routes['Gumby Crack'],
               'path736': book.routes['Gumby Slab'],
               'path734': book.routes['Gumby Arete'],
               'path732': book.routes['The Siren'],
               'path730': book.routes['Garden Variety'],
               'path728': book.routes['The Arboretum'],
               'path726': book.routes['Full Stroke'],
               'path724': book.routes['Philanthropy'],
               'path722': book.routes['Locksmith'],
               'path720': book.routes['Ground up Blowie'],
               'path718': book.routes['Night Crawler'],
               'path716': book.routes['The Good Slab'],
               'path714': book.routes['The Good'],
               'path712': book.routes['Another'],
               'path710': book.routes['Snakes and Martyrs'],
               'path708': book.routes['Next to the Good'],
               'path740': book.routes['Into the Light'],
               'path742': book.routes['Azain Crack'],
           },
           layers=['Azain', 'Base'],
           border='rect1376')
SubAreaMap(name='Big Fred area map',
           parent=book.subareas['Big Fred'],
           outFileName='Big Fred.png',
           fileName='Garden.svg',
           path_i='./maps/area/',
           path_o='./maps/area/',
           layers=['Big Fred', 'Base'],
           border='rect2908',
           description='Big Fred area map',
           routes={
               'path714-5': book.routes['Angry Grandma'],
               'path712-7': book.routes['Angry Mom'],
               'path712-6': book.routes['Easy Grandma'],
               'path710-5': book.routes['Big Fred'],
           })
SubAreaMap(name='Entrance area map',
           parent=book.subareas['entranceUpper'],
           outFileName='entranceUpper.png',
           fileName='upperGarden.svg',
           path_i='./maps/area/',
           path_o='./maps/area/',
           layers=['Entrance', 'Base'],
           border='rect27051',
           description='Entrance area map',
           routes={
               'path27105': book.routes['Pumpkin Spice'],
               'path27107': book.routes['Baseball'],
               'path27109': book.routes['Bunt'],
           })
SubAreaMap(name='Bread loaf/Scratch and Spliff area map',
           parent=book.subareas['The Bread Loaves/Scratch and Spliff'],
           outFileName='bread.png',
           fileName='upperGarden.svg',
           path_i='./maps/area/',
           path_o='./maps/area/',
           layers=['Bread', 'Base'],
           border='rect27128',
           size='f',
           description='Bread loaf/Scratch and Spliff area map',
           routes={
               'path27126': book.routes['Caliban\'s War'],
               'path27124': book.routes['Scratch'],
               'path27122': book.routes['Spliff'],
               'path27120': book.routes['Scratch and Spliff Traverse'],
               'path27118': book.routes['For What it\'s Worth'],
               'path27116': book.routes['Worf'],
               'path27114': book.routes['Bread Loaf Traverse'],
               'path27112': book.routes['Buddha\'s Belly'],
           })
SubAreaMap(name='Redneck Riviera area map',
           parent=book.subareas['Redneck Riviera'],
           fileName='redneck.svg',
           path_i='./maps/area/',
           path_o='./maps/area/',
           layers=['Redneck', 'Base'],
           border='rect3479',
           size='h',
           description='Redneck Riviera area map',
           routes={
               'path3423': book.routes['Pony Boy'],
               'path3421': book.routes['Monorail Project'],
               'path3419': book.routes['Ugly Face'],
               'path3417': book.routes['Binding of Isaac'],
               'path3415': book.routes['Moss Boss'],
               'path3413': book.routes['Chicken Tendies'],
               'path3411': book.routes['Teenage Libertarians'],
               'path3357': book.routes['Falcon\'s Reach'],
           })






if __name__ == '__main__':
    book.paths['LaTeXTemplates'] = '../LocalBoulders/templates/'
    book.paths['LaTeXOut'] = './sections/'
    book.paths['pdf'] = './'
    book.gen()
