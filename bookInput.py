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
bookAreas = {
    'garden': Area(
        name='The Garden Main',
        parent=book,
        gps='44.44076010641458, -122.5752659013521',
        description='Located about 3.5 miles down quatzville road from highway 20, park in the Gravel pull out where the road bends '
                    'left just before you reach the boulders. The Garden Main bouldering area is true to its name. '
                    'A lush green space features moss covered '
                    'boulders situated under a dense canopy.',),
    'pinkTag': Area(
        name='Pink Tag Boulders',
        parent=book,
        gps='44.43998124232581, -122.57539325959186',
        description='Just across the road from the main area lay a few boulders on the banks of the River. See driving '
                    'directions for the Garden Main area.',),
    'upperGarden': Area(
        name='Armageddon',
        parent=book,
        gps='44.43959094940084, -122.58215256842753',
        description='Located about 3.2 miles down quatzville road from highway 20, park in the Gravel pull out where the road bends '
                    'about 0.1 miles before you reach a turnoff to a gravel road (which leads to the boulders). This '
                    'area is also known as the upper garden. The lack of shade, the blackberries, the poison '
                    'oak, and the 3 minute approach all make this area less desirable and less traveled then the Main',),
    'quartzville': Area(
        name='Quartzville Creek',
        parent=book,
        description='About an hour further down the road from the main area there are a few interesting boulders '
                    'in a creek. Generally lower temperatures, free camping, and pleasant swimming holes make this '
                    'a nice mid summer spot.'),
}
bookSubAreas = {
    'entranceMain': Subarea(
        name='Entrance Area',
        parent=bookAreas['garden'],
        description='A cluster of boulders situated inbetween the two main trails.'
    ),
    'fightClub': Subarea(
        name='Fight Club',
        parent=bookAreas['garden'],
        description='Located in the southwest corner of the Garden main, The Fight Club zone is home to the '
                    'namesake V8 test piece as well as several other quality lines. Flat landings and easy access '
                    'make this a nice spot to spend some time'),
    'undertow': Subarea(
        name='Undertow',
        parent=bookAreas['garden'],
        description='Directly uphill from Fightclub are a few quality boulders separated by overgrown trails.'),
    'methLab': Subarea(
        name='Meth Lab',
        parent=bookAreas['garden'],
        description='Easily the most recognizable feature at the Garden, the Meth Lab boulder towers over all other stones in the '
                    'main area. Most climbs for this zone are located in a secluded natural amphitheater on the '
                    'uphill side of the boulder.'),
    'big': Subarea(
        name='Big',
        parent=bookAreas['garden']),
    'azain': Subarea(
        name='Azain',
        parent=bookAreas['garden'],
        description='Azain is a jumbled collection of rocks which forms the highest point of the Garden main.',
        ),
    'bigFred': Subarea(
        name='Big Fred',
        parent=bookAreas['garden'],),
    'pinkTag': Subarea(
        name='',
        parent=bookAreas['pinkTag'],),
    'entranceUpper': Subarea(
        name='Entrance Area',
        parent=bookAreas['upperGarden'],),
    'breadLoaves': Subarea(
        name='The Bread Loaves',
        parent=bookAreas['upperGarden'],),
    'strangeLove': Subarea(
        name='Dr. Strangelove Area',
        parent=bookAreas['upperGarden'],),
    'redneckRiviera': Subarea(
        name='Redneck Riviera',
        parent=bookAreas['quartzville'],
        gps='44.570410945356336, -122.4060701729652',
        description='Redneck rivierra is located on Quartzville road apporximately 20.6 miles from highway 20 park in '
                    'the gravel pull out on the creek side of the road. This '
                    'is a nice spot with good swimming access and a few established routes on both sides of the river. '
                    'The locals like to use this spot to pan for gold. In my experience they are friendly and willing '
                    'to share the space.'),
    'minersCamp': Subarea(
        name='Old Miner\'s Camp',
        parent=bookAreas['quartzville'],
        gps='44.58651338802075, -122.35033857932665',
        description='Located on Quartzville approximately 24.8 miles from highway 20, the old miner\'s camp is a '
                    'popular group campsite there are a few good sized boulders in the river only one boulder has '
                    'established lines on it. Park either at the camp day use area or on the side of the road '
                    'immediately above the Dab Rig boulder.'),
}
bookBoulders = {
    'toiletBowl': Boulder(
        name='Toilet Bowl',
        parent=bookSubAreas['entranceMain'],
        description='If approaching via the main trail this is the first boulder you will encounter just of the road.'),
    'boysWoods': Boulder(
        name='Boys In the Woods',
        parent=bookSubAreas['entranceMain'],
        description='A low boulder with an identifiable scoop on the downhill side is located on the main trail '
                    'roughly 150ft uphill from the road.'),
    'goodWarm': Boulder(
        name='The Good Warmup',
        parent=bookSubAreas['entranceMain'],
        description='A tiny finshaped boulder on the main trail.'),
    'treeSlab': Boulder(
        name='Tree Slab',
        parent=bookSubAreas['entranceMain'],
        description='A narrow slab just uphill and to the right of the Boys in the Woods boulder.'),
    'tonsil': Boulder(
        name='Tonsil',
        parent=bookSubAreas['entranceMain'],
        description='A small hanging prow wedged under a larger hanging prow, which is itself wedged under the Meth Lab prow (a very big hanging prow).'),
    'allSorts': Boulder(
        name='All Sorts of Ease',
        parent=bookSubAreas['entranceMain'],
        description='A low angle slab under the Meth Lab prow'),
    'threeStar': Boulder(
        name='Three Star Ledge',
        parent=bookSubAreas['entranceMain'],
        description='Angular boulder in the rocky landscape between the two entrance trails.'),
    'overhand': Boulder(
        name='Overhand',
        parent=bookSubAreas['entranceMain'],
        description='a short prow in the rocky landscape between the two entrance trails.'),
    'turtleShell': Boulder(
        name='Turtle Shell Boulder',
        parent=bookSubAreas['entranceMain'],
        description='A short boulder with a low angle offwidth crack. If approaching on the fight club trail this is '
                    'the first boulder that you will encounter'),
    'office': Boulder(
        name='The Office',
        parent=bookSubAreas['fightClub'],
        description='A tall not quite vertical boulder is immediately on your right as you enter the Fight Club Area'),
    'crashTest': Boulder(
        name='Crash Test Dummies',
        parent=bookSubAreas['fightClub'],
        description='A small boulder in between The Office and Fight Club.'),
    'fightClub': Boulder(
        name='Fight Club',
        parent=bookSubAreas['fightClub'],
        description='The obvious overhanging boulder with an interesting bubbly texture.'),
    'tylerDurten': Boulder(
        name='Tyler Durten',
        parent=bookSubAreas['fightClub'],
        description='Just to the left of the fight club boulder is a tall wall with few features other than a '
                    'distinctive crimp rail at eye level.'),
    'trust': Boulder(
        name='Trust',
        parent=bookSubAreas['fightClub'],
        description='The Trust boulder sits on an terrace behind Mini Me and to the Left of Tyler Durten'),
    'miniMe': Boulder(
        name='Mini Me',
        parent=bookSubAreas['fightClub'],
        description='A short pointy boulder with a flat landing is nearly freestanding on the downhill side of the '
                    'Fight Club zone',),
    'eDirty': Boulder(
        name='E\'s Dirty B',
        parent=bookSubAreas['fightClub'],
        description='Following a faint trail west traveling past the trust boulder brings you to a Large boulder '
                    'which almost immediately gives way to low angle slab.'),
    'sillySteep': Boulder(
        name='Silly Steep',
        parent=bookSubAreas['undertow'],
        description='Thin overhanging block left of the Undertow boulder.'),
    'undertow': Boulder(
        name='Undertow',
        parent=bookSubAreas['undertow'],
        description='Realatively off the beaten path as far as classic garden boulders goes. Follow a faint trail '
                    'upill past the trust boulder.'),
    'carAlarm': Boulder(
        name='Car Alarm',
        parent=bookSubAreas['undertow'],
        description='This secluded block has a variety of worthwhile beginner climbs. Most of the rock is covered with holds so its also a good spot to play around and make up your own linkups.'),
    'chockStone': Boulder(
        name='Chockstone Highball',
        parent=bookSubAreas['undertow'],
        description=''),
    'methLab': Boulder(
        name='Meth Lab',
        parent=bookSubAreas['methLab'],
        description='Routes listed in counter clockwise order beginning under the large prow of the downhill face.'),
    'swollen': Boulder(
        name='Swollen Member',
        parent=bookSubAreas['methLab'],
        description='A small prow just out of the hill side above the Meth Lab boulder protrudes at a provocative angle.'),
    'innerSanctum': Boulder(
        name='Inner Sanctum',
        parent=bookSubAreas['methLab'],
        description='Slabby boulder to the left of Swollen Member.'),
    'eBoulder': Boulder(
        name='E\'s Boulder',
        parent=bookSubAreas['methLab'],
        description='A large boulder directly to the right of Octurnal holds a few notable routes.'),
    'bubbler': Boulder(
        name='The Bubbler',
        parent=bookSubAreas['methLab'],
        description='A small unassuming block sits just downhill of E\'s boulder.'),
    'bitchin': Boulder(
        name='Bitchin Corners',
        parent=bookSubAreas['big'],
        description='A neet angular face sits on the downhill of an otherwise unremarkable boulder.'),
    'big': Boulder(
        name='Big',
        parent=bookSubAreas['big'],
        description='The "Big" boulder is a large moss covered boulder on the eastern boundary of the Garden Main '
                    'area, in other guides this has also been called "roadside", and "North Block"'),
    'hueco': Boulder(
        name='Hueco Wabo',
        parent=bookSubAreas['big'],
        description='An aesthetic boulder sits well off the beaten path'),
    'baldo': Boulder(
        name='Baldo',
        parent=bookSubAreas['big'],),
    'theGood': Boulder(
        name='The Good',
        parent=bookSubAreas['azain'],
        description='Continuing up the main trail from Boys in the Woods leads to a good boulder with two routes on '
                    'the downhill face.'),
    'nextGood': Boulder(
        name='Next to The Good',
        parent=bookSubAreas['azain'],
        description='A slender boulder hangs off the ground to the left of the Good.'),
    'nightCrawler': Boulder(
        name='Night Crawler',
        parent=bookSubAreas['azain'],
        description='This iconic double arete boulder hangs like a throne near the top of the Azain formation.'),
    'azainSpire': Boulder(
        name='Azain Spire',
        parent=bookSubAreas['azain'],
        description='A thin triangular flake stands on end behind swollen member and in front of Azain'),
    'azainFront': Boulder(
        name='Azain Front Side',
        parent=bookSubAreas['azain'],
        description='The tall walls of the Azain front side are located just off the main trail behind The Good.'),
    'azainBack': Boulder(
        name='Azain Back Side',
        parent=bookSubAreas['azain'],
        description='Continuing up the main trail will bring you between the Azain and Big Fred boulders to the Azain backside.'),
    'bigFred': Boulder(
        name='Big Fred',
        parent=bookSubAreas['bigFred'],
        description=''),
    'angryGrandma': Boulder(
        name='Angry Grandma',
        parent=bookSubAreas['bigFred'],
        description=''),
    'intro': Boulder(
        name='Intro Boulder',
        parent=bookSubAreas['entranceUpper'],
        description=''),
    'lowerBread': Boulder(
        name='Lower Bread Loaf',
        parent=bookSubAreas['breadLoaves'],
        description=''),
    'upperBread': Boulder(
        name='Upper Bread Loaf',
        parent=bookSubAreas['breadLoaves'],
        description=''),
    'drStrange': Boulder(
        name='Dr. Strange Love',
        parent=bookSubAreas['strangeLove'],
        description=''),
    'tecnu': Boulder(
        name='Tecnu Boulder',
        parent=bookSubAreas['pinkTag'],
        description=''),
    'jonahDab': Boulder(
        name='Jonah\'s Dab Rig',
        parent=bookSubAreas['pinkTag'],
        description=''),
    'farley': Boulder(
        name='Farley Prep',
        parent=bookSubAreas['pinkTag'],
        description=''),
    'ponyBoy': Boulder(
        name='Pony Boy',
        parent=bookSubAreas['redneckRiviera'],
        description=''),
    'monorail': Boulder(
        name='Monorail',
        parent=bookSubAreas['redneckRiviera'],
        description=''),
    'yoMamma': Boulder(
        name='Yo Mamma Boulder',
        parent=bookSubAreas['redneckRiviera'],
        description=''),
    'mossBoss': Boulder(
        name='Moss Boss',
        parent=bookSubAreas['redneckRiviera'],
        description=''),
    'fourPointFive': Boulder(
        name='The 4.5',
        parent=bookSubAreas['redneckRiviera'],
        description=''),
    'dabRig': Boulder(
        name='The Dab Rig',
        parent=bookSubAreas['minersCamp'],
        description=''),
}
bookRoutes = {
    'raphael': Route(
        name='Raphael Crack',
        parent=bookBoulders['turtleShell'],
        grade=0,
        rating=1,
        description='Climb the wide crack from a stand start.'
        ),
    'leonardo': Route(
        name='Leonardo',
        parent=bookBoulders['turtleShell'],
        grade=3,
        rating=1,
        description='Lay down start with hands lon a low broken flake. With difficulty pull off the ground and slap a slopey ledge traverse up and left until you can rock over onto the downhill face. Sort of like a worse version of boys in the woods.'
        ),
    'donatello': Route(
        name='Donatello',
        parent=bookBoulders['turtleShell'],
        grade=1,
        rating=1,
        description='start on a flat ledge where the rock angle changes. Slap a low angle arete until you can hike your feet up. Only somewhat distinct from Leonardo.'
        ),
    'toilet': Route(
        name='Toilet Bowl',
        parent=bookBoulders['toiletBowl'],
        grade=1,
        rating=1,
        description='Stand start on a protruding block with left hand on an undercling and right hand on a knob. Pull a few moves to gain the lip of the boulder.'), 
    'toiletTraverse': Route(
        name='Toilet Bowl Traverse',
        parent=bookBoulders['toiletBowl'],
        grade=0,
        rating=2,
        description='Starting on a good rail at the lower left of the boulder. Travers the lip topping out at the highest point or continue all the way until the boulder recedes into the hill'
        ),
    'boysInTheWoods': Route(
        name='Boys in the Woods',
        parent=bookBoulders['boysWoods'],
        grade=4,
        rating=2,
        description='Start on a low jug just before the scoop at the lowest part of the boulder. Climb up the left '
                    'arete of the scoop until you can flop in. Some may consider this an eliminate since, with '
                    'difficulty, you could also just mantle directly into the scoop.',),
    'cubaGooding': Route(
        name='Cuba Gooding',
        parent=bookBoulders['boysWoods'],
        grade=5, #unconfirmed
        description='Start as for Boys in the Woods but climb right along the lip of the scoop until you can reach the '
                    'holds at the top of Ice Cubes Shiny Jerry Curl'),
    'shinyJerry': Route(
        name='Ice Cubes Shiny Jerry Curl',
        parent=bookBoulders['boysWoods'],
        grade=6, #unconfirmed
        description='Start on a low sloping edge and pull some sneaky moves to gain a knife edge crimp at eye level. '
                    'Continue straight up.'),
    'treeSlab': Route(
        name='Tree Slab',
        parent=bookBoulders['treeSlab'],
        grade=1,
        rating=2,
        description='Climb the center of the slab from a stand start.'),
    'goodWarm': Route(
        name='The Good Warm Up',
        parent=bookBoulders['goodWarm'],
        grade=0), # unconfirmed
    'threeStar': Route(
        name='Three Star Ledge',
        parent=bookBoulders['threeStar'],
        grade=2,
        rating=2,
        description='Stand start with hands matched on the ledge. Chuck out to the left arete and follow it to the apex of the boulder. The small boulders at the base are off.'),
    'overhand': Route(
        name='Overhand',
        parent=bookBoulders['overhand'],
        grade=7,),  # unconfirmed
    'allSorts': Route(
        name='All Sorts of Ease',
        parent=bookBoulders['allSorts'],
        grade='B',
        rating=2,
        description='Climb the left side of the face on good holds. Fun.'),      
    'shadowGiants': Route(
        name='In the Shadow of Giants',
        parent=bookBoulders['allSorts'],
        grade=2,
        rating=1,
        description='Stand start with wide hands. Left hand on thin pinch at head height and right hang on a slightly higher small lumpy edge with a thumb catch. Pull a few delicate moves to gain the lip. A sit start looks doable, but unpleasant.'),  
    'tonsil': Route(
        name='Tonsil',
        parent=bookBoulders['tonsil'],
        grade=4,
        rating=2,
        description='Step off the boulder below to gain high starting holds. Begin in compression with right hand on a vertical side pull sloper on the blunt right corner and left hand on a juggy undercling.  Shorter climbers will have difficulty reaching the starting holds. After establishing the rock below is off.'),   
    'leftTonsil': Route(
        name='Unknown Left of Tonsil',
        parent=bookBoulders['tonsil'],
        grade=2,
        rating=0,
        description='Climbs the boulder below Tonsil. Sit start with low holds on the right arete. Pull a few awkward moves into a cramped top out.'),     
    'trust': Route(
        name='Trust',
        parent=bookBoulders['trust'],
        grade=2,
        rating=3,
        description='Sit start in compression on a hanging refrigerator block. Climb straight up through a slopeing '
                    'ledge to the top. Look for the juggy crack ~1ft inset from the lip.'),
    'miniMe': Route(
        name='Mini Me',
        parent=bookBoulders['miniMe'],
        grade=3,
        rating=0,
        description='start on blunt corner. Make tricky moves to a blocky jug to the lip and traverse left to an easy '
                    'top over a rocky landing'),
    'austinPowers': Route(
        name='Austin Powers',
        parent=bookBoulders['miniMe'],
        grade=5,
        rating=2,
        description='Start as for Mini Me but move right into top of Dr. Evil'),
    'drEvil': Route(
        name='Dr. Evil',
        parent=bookBoulders['miniMe'],
        rating=2,
        grade=4,
        description='sit start in compression with left hand on a low sloper sidepull and right hand on the arete. '
                    'Pull some tricky moves to gain better holds either rolling onto the right hand slab early or '
                    'staying on the arete the whole way.'),
    'tylerDurten': Route(
        name='Tyler Durten',
        parent=bookBoulders['tylerDurten'],
        rating=1,
        grade=3,
        description='Start on a henious crimp rail and punch out left to much better holds.'),
    'jim': Route(
        name='Jim Halpert',
        parent=bookBoulders['office'],
        rating=0,
        grade=1,
        serious=2,
        description='Starting on the right edge of the block climb climb the right corner over a rocky landing. Either '
                    'pull some harder moves to stay on the downhill face or round the corner to the right and pull '
                    'some easier moves over a worse landing. Grade and rating unconfirmed.'),
    'daryl': Route(
        name='Daryl Philbin',
        parent=bookBoulders['office'],
        rating=3,
        grade=1,
        serious=1,
        description='Starting at the Center of the block climb left on good holds to the arete. Climb up the arete '
                    'until you can reach good face holds up right and continue through a, thankfully, juggy top out. '
                    'Mind the rock at the base of the climb. Left and right alternative starts add a little variety but do '
                    'not change the grade.'),
    'vince': Route(
        name='Vince',
        parent=bookBoulders['crashTest'],
        rating=2,
        grade=2,
        description='Squat start on good edges. Navigate a crescent shaped sidpull rail to a delicate top out. Make '
                    'sure to clean the top out before attempting.'),
    'ear': Route(
        name='The Ear',
        parent=bookBoulders['fightClub'],
        rating=3,
        grade=2,
        description='Start on the arete at the far right end of the boulder. Climb straight up through tricky holds '
                    'to a heady top out.'),
    'fightClub': Route(
        name='Fight Club',
        parent=bookBoulders['fightClub'],
        rating=3,
        grade=8,
        description='Area classic, this rig is a feather in any would be crushers cap. Start on the far right arete as for Ear. '
                    'Traverse across the angle change and top out above a bubbly crimp rail on the overhanging face.'),
    'fightClubLeft': Route(
        name='Fight Club Left',
        parent=bookBoulders['fightClub'],
        description='PLACEHOLDER'),
    'brewmaster': Route(
        name='Brewmaster',
        parent=bookBoulders['fightClub'],
        description='PLACEHOLDER'),
    'eDirty': Route(
        name='E\'s Dirty B',
        parent=bookBoulders['eDirty'],
        rating=2,
        grade=5,
        description='Start with hands matched on a lumpy flake in the back of a small cave. Using slopeing edges out right and a '
                    'difficult undercling navigate out of the cave trending right at the lip to a jug. The final '
                    'slab quest is an enjoyable and easy top out.',),
    'sillySteep': Route(
        name='Silly Steep Mantle',
        parent=bookBoulders['sillySteep'],
        grade=4,
        rating=2,
        description='Stand start with good compression holds in the roof. Make a hard pull to the juggy edge below the '
                    'lip and figure out how to get your body over the top. Starting from the juggy edge knocks the '
                    'grade down to V2/3.'),
    'undertow': Route(
        name='Undertow',
        parent=bookBoulders['undertow'],
        grade=3,
        rating=3,
        description='Start on two boob shaped slopers at head height. Climb straight up using face holds and the right '
                    'arete.'),
    'riptide': Route(
        name='Riptide',
        parent=bookBoulders['undertow'],
        grade=3,
        rating=2,
        description='Start as for undertow but trend right around the corner to a juggy hueco top out.'),
    'tidepool': Route(
        name='Tidepool',
        parent=bookBoulders['undertow'],),
    'carAlarmTraverse': Route(
        name='Car Alarm Traverse',
        parent=bookBoulders['carAlarm'],
        grade=2,
        rating=2,
        description='Stand start with hands on an incut rail at the far left end of the wall. Traverse right to pup truck staying below the lip the whole time. The reverse goes at the same grade.'),
    'whiteRhino': Route(
        name='White Rhino',
        parent=bookBoulders['carAlarm'],
        grade=1,
        rating=1,
        description='Stand start just left of 2 ton Chevy with left hand in a baseball size dish and right hand on the juggy part of a protruding rib. Climb up and left.'),
    'twoTon': Route(
        name='2 Ton Chevey',
        parent=bookBoulders['carAlarm'],
        grade=1,
        rating=2,
        description='Squat start on a diagonal left hand edge and a shallow 3 finger pocket on your lower right. Climb up two flat ledges to the top.'),
    'pupTruck': Route(
        name='Pup Truck',
        parent=bookBoulders['carAlarm'],
        grade=0,
        rating=2,
        description='squat start on a blunt corner with right hand on a diagonal crimp and left hand in a shallow pocket.'),
    'compRoute': Route(
        name='Comp Route',
        parent=bookBoulders['carAlarm'],
        grade=0,
        rating=1,
        description='stand start with hands on an undercling at knee height. Using some tricky holds and a good left foot lunge out and left to a jug rail at the lip.'),
    'panicButton': Route(
        name='Panic Button',
        parent=bookBoulders['carAlarm'],
        grade=0,
        rating=1,
        description='Stand start just to the left of a rounded corner with feet on a blocky protrusion and not much for hands. Climb up and along the rounded corner.'),
    'methLab': Route(
        name='Meth Lab Project',
        parent=bookBoulders['methLab'],
        serious=3,
        description='The obvious prow on the front of the Meth Lab boulder has a bolted top rope anchor but a route up it has '
                    'likely never been free\'ed by any means. The ethics of climbing this behemoth are contentious but '
                    'in my opion it is fair game to bolt as a sport route. If you have the desire to do so consider '
                    'working it out on TR first before placing new equipment.'),
    'dontBlow': Route(
        name='Don\'t Blow the Jug',
        parent=bookBoulders['methLab'],
        grade='2+',
        rating=2,
        serious=1,
        description='Start at the base of the wide crack. Climb inverted in the offwidth until you can make use of a jug to '
                    'squeeze into the crack. Walk through the crack to the far side of the boulder.'),
    'trustIssues': Route(
        name='Trust Issues',
        parent=bookBoulders['methLab'],
        serious=2,
        grade='8+', #unconfirmed
        description='PLACEHOLDER'),
    'leaveJesus': Route(
        name='Leave It to Jesus',
        parent=bookBoulders['methLab'],
        rating=3,
        grade=2,
        description='Also known as Showboat. Start with hands on sloping edges. Use one or two intermediate holds to reposition yourself and make a long pull to the lip. Short but brilliant.'),
    'smackdown': Route(
        name='Smackdown',
        parent=bookBoulders['methLab'],
        rating=2,
        grade=7,
        description='Start standing with left hand gaston and right hand jug sidepull. Crank some powerful moves on bad feet '
                    'and follow the line of crimps to a top out left'),
    'heisenburg': Route(
        name='Heisenburg',
        parent=bookBoulders['methLab'],
        grade=9, #unconfirmed
        description='PLACEHOLDER'),
    'learys': Route(
        name='Learys Lunge',
        parent=bookBoulders['methLab'],
        grade=9, 
        rating=3,
        description='Start as for Heiserburg and dyno up and right to juggy holds at the lip.'),
    'guillotine': Route(
        name='Guillotine',
        parent=bookBoulders['methLab'],
        rating=2,
        grade=4,
        description='Start underclinging on the hanging \"Guillotine blade\" flake left of Octurnal. Climb straight up.'),
    'octurnal': Route(
        name='Octurnal',
        parent=bookBoulders['methLab'],
        rating=3,
        grade=7,
        description='For many this is THE local test piece. Start sitting '
                    'with left hand on a sloping triangular rib and right hand on a slopey cripm at the arete. Crank a few hard '
                    'moves to gain the lip then traverse left through the lightning bolt hold to a pumpy top out. Originally known as \"Tom\'s phsychadelic trip\".'),
    'twoBlows': Route(
        name='Two Blows One Stroke',
        parent=bookBoulders['methLab'],
        grade=6, #unconfirmed
        description='PLACEHOLDER'),
    'swollen': Route(
        name='Swollen Member',
        parent=bookBoulders['swollen'],
        grade=3,
        rating=2,
        description='A classic hazing route. Start hugging the underside of the block underside with good hand holds '
                    'on each side of the stubby prow. Manuver youself into a less scandelous orientation using toe '
                    'hooks, heel hooks and  all manner of dirty tricks.'),
    'innerSanctum': Route(
        name='Inner Sanctum',
        parent=bookBoulders['innerSanctum'],
        rating=2,
        grade=1,
        serious=1,
        description='Stand start with left hand on a slopey ledge and right hand on a diagonal incut seam. Pull yourself onto the ledge and climb a tenuous slab using a blunt corner for your right hand.'),
    'outerSanctum': Route(
        name='Outer Sanctum',
        parent=bookBoulders['innerSanctum'],
        rating=1,
        grade=1,
        description='Start as for Inner Sanctum but pull yourself around the blunt corner into a mossy scoop. Continue right to an easy top out.'),
    'slamDunk': Route(
        name='Slam Dunk',
        parent=bookBoulders['eBoulder'],
        grade=7, #unconfirmed
        description='PLACEHOLDER'),
    'e7': Route(
        name='E\'s',
        parent=bookBoulders['eBoulder'],
        grade=7, #unconfirmed
        description='PLACEHOLDER'),
    'enchilada': Route(
        name='Enchilada',
        rating=2,
        parent=bookBoulders['eBoulder'],
        grade=9,
        description='Start matched on a good flat rail low to the ground with some awkward feet options. Cross into a '
                    'comfortable crimp and fire up left before coming back right to a flat jug. Pretty classic as far as low balls go!'),
    'bitchin': Route(
        name='Bitchin Corners',
        grade=2, #unconfirmed
        parent=bookBoulders['bitchin'],),
    'baldo': Route(
        name='Frontside Baldo',
        parent=bookBoulders['baldo'],
        grade=2,
        rating=2,
        description='Sit start with left hand on a juggy side pull and right hand at the bottom of the diagonal crack. Climb the triangular face using the crack and holds on both aretes.'
        ),
    'hueco': Route(
        name='Hueco Wabo',
        grade=3, #unconfirmed
        parent=bookBoulders['hueco'],
        description='Stand start on good side pull underclings pull some rad moves to an insecure, scary top out. It\'s possible to bail right at almost any point on this route, but that\'s no fun. A sit start might also exist but looks unfun. Grade unconfirmed.'),
    'bernd': Route(
        name='All Bernd Up',
        grade=10, #unconfirmed
        parent=bookBoulders['big'],),
    'theGoodSlab': Route(
        name='The Good Slab',
        parent=bookBoulders['theGood'],
        grade=1,
        rating=2,
        description='Squat start on an incut flake at knee height. Climb the slab around the corner from The Good.'),
    'theGood': Route(
        name='The Good',
        parent=bookBoulders['theGood'],
        grade=3,
        rating=2,
        description='Start matched on a juggy flake on the right side of the boulder\'s downhill face.'),
    'another': Route(
        name='Another',
        parent=bookBoulders['theGood'],
        grade=3,
        rating=1,
        serious=1,
        description='start with opposing sidepulls on the center of the boulder\'s downhill face. Traverse to the left '
                    'arete and ascend using delecate feet and unideal hands. Mind the uneven landing. Aggresive cleaning has reveiled that the dirty ledge to the left of the rock is infact part of the rock so stepping of here is still on route I guess, but its cooler if you don\'t.'),
    'nextGood': Route(
        name='Next To the Good',
        parent=bookBoulders['nextGood'],
        grade=3,
        rating=1,
        serious=1,
        description='Stand start with right hand on a crimp rail under the overhang and left on a high diagonal side pull. A few burly moves give way to a low angle slab. Bailing into the gully instead of climbing the upper slab doesn\'t change the grade, but it is cheating.'
        ),
    'snakesMartyrs': Route(
        name='Snakes and Martyrs',
        parent=bookBoulders['azainSpire'],
        grade=0,
        rating=3,
        description=' Stand start in a juggy seam. Could be scary if you are uncomfortable climbing outside.'
    ),
    'blowie': Route(
        name='Ground Up Blowie',
        parent=bookBoulders['azainFront'],
        rating=2,
        grade=5,
        description='Start at the base of a diagonal finger crack. Follow the crack around a dabby tree and onto an easy '
                    'slab. This route was named as an omage to the first ascent when the top out was cleaned via '
                    'leafblower from a stance mid route.'),
    'intoTheLight': Route(
        name='Into the Light',
        parent=bookBoulders['azainFront'],
        grade=6, ), #unconfirmed
    'azainCrack': Route(
        name='Azain Crack',
        parent=bookBoulders['azainFront'],),
    'nightCrawler': Route(
        name='Night Crawler',
        parent=bookBoulders['nightCrawler'],
        grade=10,),
    'locksmith': Route(
        name='Locksmith',
        parent=bookBoulders['azainBack'],
        grade=4,
        rating=3,
        serious=2,
        description='Also known as Hula. Sit start with a juggy left hand sidebpull and right hand on an undercling edge. Pull a few '
                    'crimpy moves until you can reach a good hold on the arete. Rock over onto the slab and quest to '
                    'the top. Be sure to clean the upper section before attempting this rig.'),
    'philanthropy': Route(
        name='Philanthropy',
        parent=bookBoulders['azainBack'],
        grade=4,
        rating=1,
        serious=2,
        description='Stand start with wide hands, left on a crimp sloper and right on a crimp sidepull. Pull a few '
                    'techy moves to gain good jugs and rock over onto the slab. follow the path of least resistance or '
                    'least moss to the top.'),
    'fullStroke': Route(
        name='Full Stroke',
        parent=bookBoulders['azainBack'],
        grade=2,
        rating=2,
        serious=1,
        description='Stand start on a jug flake. Trend left to a high top in a shallow chimney.'
    ),
    'gardenProj': Route(
        name='Garden Project',
        parent=bookBoulders['azainBack'],
        description='Project. Sit start at the base of the low roof and climb into garden variety or Full Stroke. Once '
                    'climbed this will be one of the hardes routes in Oregon.'),
    'gardenVariety': Route(
        name='Garden Variety',
        parent=bookBoulders['azainBack'],
        grade=7, ), #unconfirmed
    'arboretum': Route(
        name='The Arboretum',
        parent=bookBoulders['azainBack'],
        grade=11,),
    'otherBernd': Route(
        name='The Other Bernd',
        parent=bookBoulders['azainBack'],
        grade=10, ), #unconfirmed
    'siren': Route(
        name='The Siren',
        parent=bookBoulders['azainBack'],
        grade=5,
        rating=3,
        description='Sit start at the base of the prow with one hand on an incut ledge and the other on the slopey rib below. Climb the prow using a few different beta options. This route is also refered to as "Witch Hunt".'),
    'gumbyArete': Route(
        name='Gumby Arete',
        parent=bookBoulders['azainBack'],
        grade=2,
        rating=2,
        description='Stand start on underclings at the left side of the face. Challenge yourself by staying on the '
                    'Arete the whole way up or bail onto the ledge out right and top as for Gumby Slab.',),
    'gumbySlab': Route(
        name='Gumby Slab',
        parent=bookBoulders['azainBack'],
        grade=1,
        rating=3,
        description='Stand start in the center of the face. This can be scary if not used to climbing outdoors.',),
    'gumbyCrack': Route(
        name='Gumby Crack',
        parent=bookBoulders['azainBack'],
        grade=0,
        rating=2,
        description='Climb the well featured wall to the right of Gumby slab from a stand start.',),
    'chockStone': Route(
        name='Chockstone Highball',
        parent=bookBoulders['chockStone'],
        grade=4, ), #unconfirmed
    'bigFred': Route(
        name='Big Fred',
        parent=bookBoulders['bigFred'],),
    'angryMom': Route(
        name='Angry Mom',
        parent=bookBoulders['angryGrandma'],
        grade=2, ), #unconfirmed
    'angryGrandma': Route(
        name='Angry Grandma',
        parent=bookBoulders['angryGrandma'],),
    'territorial': Route(
        name='Territorial Pissings',
        parent=bookBoulders['tecnu'],
        grade=5, ), #unconfirmed   
    'jonah': Route(
        name='Jonah\'s Dab Rig',
        parent=bookBoulders['jonahDab'],
        grade=9, ), #unconfirmed
    'workshop': Route(
        name='Workshop 68',
        parent=bookBoulders['jonahDab'],
        grade=11, ), #unconfirmed
    'socialismo': Route(
        name='Socialismo',
        parent=bookBoulders['jonahDab'],
        grade=10, ), #unconfirmed
    'knowledge': Route(
        name='Knowledge is Good',
        parent=bookBoulders['farley'],
        grade=7, ), #unconfirmed
    'leLemet': Route(
        name='Le Lemet',
        parent=bookBoulders['farley'],
        grade=9, ), #unconfirmed
    'fraley': Route(
        name='Farely Prep',
        parent=bookBoulders['farley'],
        grade=9, ), #unconfirmed     
    'ponyBoy': Route(
        name='Pony Boy',
        parent=bookBoulders['ponyBoy'],
        grade=2, 
        rating=0,), 
    'monorail': Route(
        name='Monorail Project',
        parent=bookBoulders['monorail'],
        description='Project. Start on the far right and traverse left along the lip.'), 
    'uglyFace': Route(
        name='Ugly Face',
        parent=bookBoulders['yoMamma'],
        grade=0, 
        serious=1,
        rating=1,), 
    'binding': Route(
        name='Binding of Isaac',
        parent=bookBoulders['yoMamma'],
        grade=2, 
        serious=1,
        rating=2,), 
    'mossBoss': Route(
        name='Moss Boss',
        parent=bookBoulders['mossBoss'],
        grade=3, 
        rating=1,), 
    'tendies': Route(
        name='Chicken Tendies',
        parent=bookBoulders['fourPointFive'],
        grade=1, 
        rating=1,), 
    'teenageLibertarians': Route(
        name='Teenage Libertarians',
        parent=bookBoulders['fourPointFive'],
        grade=4, 
        rating=3,), 
    'falcon': Route(
        name='Falcon\'s Reach',
        parent=bookBoulders['fourPointFive'],
        grade=3, 
        rating=1,), 
    'almonds': Route(
        name='Unsalted Almonds',
        parent=bookBoulders['dabRig'],
        grade=7,),  #Unconfirmed
    'dankCommander': Route(
        name='Dank Commander',
        parent=bookBoulders['dabRig'],
        grade=4, ), #Unconfirmed
}
bookVariations = {
    'threeStar': Variation(
        name='Three Star Ledge Variation',
        parent=bookRoutes['threeStar'],
        grade=2,
        rating=2,
        description='Squat start with feet on the small boulder below 3 star (it\'s on this time!) and hands on opposing underclings.'
        ),
    'panicButton': Variation(
        name='Panic Button Variation',
        parent=bookRoutes['panicButton'],
        grade=2,
        rating=2,
        description='Sit start and pull into the start of Panic Button instead of topping right head left over the techy slab.'
        ),
    'mrBigglesworth': Variation(
        name='Mr. Bigglesworth',
        parent=bookRoutes['drEvil'],
        grade=1,
        rating=2,
        description='Start on your choice of waist high holds, climb straight up the right face or '
                    'stay left on the arete. Authors note: other guides identify several other variations on '
                    'this route, this book intentionally omits other variations in preference of encouraging '
                    'climbers to find their own beta.'),
    'durtenDyno': Variation(
        name='Tyler Durten Dyno',
        parent=bookRoutes['tylerDurten'],
        grade='?',
        description='It has been speculated that the dyno from the starting hold straight to the lip will go.'),
    'ironCross': Variation(
        name='Iron Cross',
        parent=bookRoutes['trust'],
        grade=2,
        rating=1,
        description='Avoid the committing moves at the lip by traversing left early.'),
    'undertowSit': Variation(
        name='Spray Against the Undertow',
        parent=bookRoutes['undertow'],
        grade=6, #unconfirmed
        description='Sit start with left hand in a slopey dish and right hand on a low sidepull. Pull some bizzare '
                    'moves to join into Undertow.'),
    'undertowSitRight': Variation(
        name='Undertow Sit Start',
        parent=bookRoutes['undertow'],
        grade=7,
        rating=3,
        description='Sit start in the scoop ~4ft right of Undertow sit with left hand on a borken sidepull and right '
                    'hand on a low undercling, climb into undertow. At one point this line was simply refered to as '
                    'Undertow, for this book modern naming standards have been conserved.'),
    'jesusSit': Variation(
        name='Leave it to Jesus Sit Start',
        parent=bookRoutes['leaveJesus'],
        grade=8, ), #unconfirmed
    'octurnalDirect': Variation(
        name='Octurnal Direct Exit',
        parent=bookRoutes['octurnal'],
        grade=7,
        rating=3,
        description='Of all the Octurnal exits this one has the most interesting moves. Climb Octurnal to the ledge '
                    'then pull some tricky moves to round the right arete. Continue on through a heads up top out.'),
    'octurnalCenter': Variation(
        name='Octurnal Center Exit',
        parent=bookRoutes['octurnal'],
        grade='6/7',
        rating=2,
        description='The easiest top option for this boulder involves pulling through a suprisingly good side pull '
                    'above the left end of the ledge. For years this variation livided in moss covered obscurity. '
                    'Climbing it will make you wonder why the awkward pumpfest traverse exit is the default line'),
    'harborFreight': Variation(
        name='Harbor Freight',
        parent=bookRoutes['smackdown'],
        grade=8,
        rating=3,
        description='Sit down start with hands matched on a blocky undercling, climb into Smackdown. This variation was literally '
                    'unearthed when a local climber yarded a large rock out from the landing of Smackdown using a '
                    'chain and come along. The device broke in the process inspiring the name of the route.'),
    'innerSanctumSit': Variation(
        name='Inner Sanctum Sit Start',
        parent=bookRoutes['innerSanctum'],
        grade=3,
        rating=1,
        description='Sit start with left hand on a diagonal undercling rail and right hand on a low diagonal side pull edge. Doesn\'t add much to the stand start.'
    ),
    'intoTheLight': Variation(
        name='Into the Light Assis',
        parent=bookRoutes['intoTheLight'],
        grade=9,),
    'bitchinSit': Variation(
        name='Bitchin Corners Sit',
        parent=bookRoutes['bitchin'],
        grade=6,),
    'brainHaemorrhage': Variation(
        name='Brain Haemorrhage',
        parent=bookRoutes['locksmith'],
        grade=7, #unconfirmed
        description='Start as for locksmith and traverse right into philanthropy'),
    'sirenStand': Variation(
        name='The Siren Stand Start',
        parent=bookRoutes['siren'],
        grade=3,
        rating=2,
        description='Start with your left hand on the left arete and right hand on a good sidepull just above the sit '
                    'start holds.',),
    'bagTricks': Variation(
        name='Bag of Tricks',
        parent=bookRoutes['gumbySlab'],
        grade=3,
        rating=1,
        description='Start as for Siren and traverse right topping on either Gumby Arete or Gumby Slab.'),
}
bookPhotos = {
    # 'austinPowers': Photo(
    #     name='Austin Powers',
    #     fileName='AustinPowers.jpg',
    #     parent=bookBoulders['miniMe'],
    #     route=bookRoutes['austinPowers'],
    #     credit='Andrew Child',
    #     description='Carson cranking across the face on Austin Powers.'),
    'riptide': Photo(
        name='Riptide',
        fileName='Riptide.jpg',
        parent=bookBoulders['undertow'],
        route=bookRoutes['riptide'],
        credit='Andrew Child',
        description='Rob on Riptide'),
    'fightClub': Photo(
        name='Fight Club',
        fileName='FightClub2.jpg',
        parent=bookBoulders['fightClub'],
        route=bookRoutes['fightClub'],
        credit='Andrew Child',
        description='Michael near the top of Fight Club.'),
    'octurnal': Photo(
        name='Octurnal',
        fileName='Octurnal.jpg',
        parent=bookBoulders['methLab'],
        route=bookRoutes['octurnal'],
        credit='Andrew Child',
        description='Carson landing the big throw on Octurnal. Classic!'),
    # 'smackdown': Photo(
        # name='Smackdown',
        # fileName='Smackdown.jpg',
        # parent=bookBoulders['methLab'],
        # route=bookRoutes['smackdown'],
        # credit='Carson Dension',
        # description='Andrew posting up at the start of Smackdown'),
    'blowie': Photo(
        name='Ground up Blowie',
        fileName='blowie.jpg',
        parent=bookBoulders['azainFront'],
        route=bookRoutes['blowie'],
        credit='Michael Gardener Brown',
        description='Andrew strugling to finde a finger lock on Ground up Blowie'),
}
bookTopos = {
#    'miniMe': Topo(
#        name='miniMe',
#        parent=bookBoulders['miniMe'],
#        fileName='miniMe2.svg',
#        size='f',
#        description='Routes on Mini Me, Trust, and Tyler Durten',
#        routes={
#            'path302': bookRoutes['miniMe'],
#            'path355': bookRoutes['austinPowers'],
#            'path406': bookRoutes['drEvil'],
#            'path963': bookRoutes['trust'],
#            'path965': bookRoutes['tylerDurten'],
#            'path4734': bookVariations['durtenDyno'],
#            'path1264': bookRoutes['miniMe'],
#            'path291': bookRoutes['austinPowers'],
#            'path2046': bookRoutes['drEvil'],
#            'path2048': bookRoutes['trust'],
#            'path2050': bookRoutes['tylerDurten'],
#            'path291-0': bookVariations['durtenDyno'],
#        }),
    'bitchin': Topo(
        name='Bitchin Corners',
        parent=bookBoulders['bitchin'],
        fileName='bitchin.svg',
        size='h',
        description='Bitchin Corners',
        routes={
            'path1002': bookRoutes['bitchin'],
            'path1029': bookRoutes['bitchin'],
            'path1014': bookVariations['bitchinSit'],
            'path1031': bookVariations['bitchinSit'],
        }),
    'baldo': Topo(
        name='Baldo',
        parent=bookBoulders['baldo'],
        fileName='baldo.svg',
        size='h',
        description='Baldo',
        routes={
            'path862': bookRoutes['baldo'],
            'path864': bookRoutes['baldo'],
        }),
    'overhand': Topo(
        name='Overhand',
        parent=bookBoulders['overhand'],
        fileName='overhand.svg',
        size='h',
        description='Overhand',
        routes={
            'path293': bookRoutes['overhand'],
            'path443': bookRoutes['overhand'],
        }),
    'hueco': Topo(
        name='Hueco Wabo',
        parent=bookBoulders['hueco'],
        fileName='hueco.svg',
        size='h',
        description='Hueco Wabo',
        routes={
            'path1918': bookRoutes['hueco'],
            'path1920': bookRoutes['hueco'],
        }),
    'azainSpire': Topo(
        name='Azain Spire',
        parent=bookBoulders['azainSpire'],
        fileName='azainSpire.svg',
        size='h',
        description='Azain Spire',
        routes={
            'path724': bookRoutes['snakesMartyrs'],
            'path726': bookRoutes['snakesMartyrs'],
        }),
    'threeStar': Topo(
        name='Three Star Ledge',
        parent=bookBoulders['threeStar'],
        fileName='3star.svg',
        size='h',
        description='Three Star Ledge',
        routes={
            'path300': bookRoutes['threeStar'],
            'path583': bookRoutes['threeStar'],
            'path514': bookVariations['threeStar'],
            'path529': bookVariations['threeStar'],
            'path585': bookVariations['threeStar'],
        }),
    'theGood': Topo(
        name='The Good',
        parent=bookBoulders['theGood'],
        fileName='good.svg',
        size='f',
        description='The Good',
        routes={
            'path1453': bookRoutes['theGood'],
            'path1459': bookRoutes['theGood'],
            'path1451': bookRoutes['another'],
            'path1457': bookRoutes['another'],
            'path1445': bookRoutes['nextGood'],
            'path1447': bookRoutes['nextGood'],
            'path1449': bookRoutes['nextGood'],
            'path1455': bookRoutes['theGoodSlab'],
            'path1461': bookRoutes['theGoodSlab'],
        }),
    'fightClub': Topo(
        name='Fight Club Right Side',
        parent=bookBoulders['fightClub'],
        fileName='fightClub.svg',
        size='h',
        description='Fight Club Right Side',
        routes={
            'path1143': bookRoutes['fightClub'],
            'path1153': bookRoutes['fightClub'],
            'path1145': bookRoutes['ear'],
            'path1151': bookRoutes['ear'],
            'path1147': bookRoutes['vince'],
            'path1149': bookRoutes['vince'],
        }),
    'fightClub2': Topo(
        name='Fight Club Left Side',
        parent=bookBoulders['fightClub'],
        fileName='fightClub2.svg',
        size='h',
        description='Fight Club Left Side',
        routes={
            'path1299': bookRoutes['fightClub'],
            'path1301': bookRoutes['fightClub'],
            'path1297': bookRoutes['fightClubLeft'],
            'path1303': bookRoutes['fightClubLeft'],
            'path1293': bookRoutes['brewmaster'],
            'path1305': bookRoutes['brewmaster'],
        }),
    'eDirty': Topo(
        name='E\'s Dirty B',
        parent=bookBoulders['eDirty'],
        fileName='eDirty.svg',
        size='h',
        description='E\'s Dirty B',
        routes={
            'path1003': bookRoutes['eDirty'],
            'path1005': bookRoutes['eDirty'],
        }),
    'carAlarm': Topo(
        name='Car Alarm Downhill Side',
        parent=bookBoulders['carAlarm'],
        fileName='carAlarm.svg',
        size='f',
        description='Car Alarm Downhill Side',
        routes={
            'path674': bookRoutes['carAlarmTraverse'],
            'path676': bookRoutes['carAlarmTraverse'],
            'path670': bookRoutes['whiteRhino'],
            'path678': bookRoutes['whiteRhino'],
            'path668': bookRoutes['twoTon'],
            'path680': bookRoutes['twoTon'],
            'path666': bookRoutes['pupTruck'],
            'path682': bookRoutes['pupTruck'],
        }),
    'carAlarm2': Topo(
        name='Car Alarm Uphill Side',
        parent=bookBoulders['carAlarm'],
        fileName='carAlarm2.svg',
        size='h',
        description='Car Alarm Uphill Side',
        routes={
            'path824': bookRoutes['compRoute'],
            'path863': bookRoutes['compRoute'],
            'path851': bookRoutes['panicButton'],
            'path861': bookRoutes['panicButton'],
            'path857': bookVariations['panicButton'],
            'path859': bookVariations['panicButton'],
        }),
    'boysInTheWoods': Topo(
        name='Boys in the Woods',
        parent=bookBoulders['boysWoods'],
        fileName='BITW.svg',
        size='f',
        description='Boys in the Woods and Tree Slab',
        routes={
            'path300': bookRoutes['boysInTheWoods'],
            'path458': bookRoutes['boysInTheWoods'],
            'path1485': bookRoutes['cubaGooding'],
            'path460': bookRoutes['cubaGooding'],
            'path400': bookRoutes['shinyJerry'],
            'path462': bookRoutes['shinyJerry'],
            'path404': bookRoutes['treeSlab'],
            'path464': bookRoutes['treeSlab'],
        }),
    'enchilada': Topo(
        name='enchilada',
        parent=bookBoulders['eBoulder'],
        fileName='enchilada.svg',
        size='h',
        description='Enchilada',
        routes={
            'path848': bookRoutes['enchilada'],
            'path902': bookRoutes['enchilada'],
        }),
    'nightCrawler': Topo(
        name='nightCrawler',
        parent=bookBoulders['nightCrawler'],
        fileName='nightcrawler.svg',
        size='h',
        description='Night Crawler',
        routes={
            'path1342': bookRoutes['nightCrawler'],
            'path1396': bookRoutes['nightCrawler'],
        }),
    'methLab': Topo(
        name='Jesus',
        parent=bookBoulders['methLab'],
        fileName='jesus.svg',
        size='f',
        description='Methlab East Face',
        routes={
            'path1908': bookRoutes['dontBlow'],
            'path1910': bookRoutes['dontBlow'],
            'path1906': bookRoutes['trustIssues'],
            'path1912': bookRoutes['trustIssues'],
            'path1902': bookRoutes['leaveJesus'],
            'path1916': bookRoutes['leaveJesus'],
            'path1904': bookVariations['jesusSit'],
            'path1914': bookVariations['jesusSit'],
        }),
    'smackdown': Topo(
        name='smackdown',
        parent=bookBoulders['methLab'],
        fileName='smackdown.svg',
        size='h',
        description='Meth Lab backside',
        routes={
            'path5330': bookRoutes['smackdown'],
            'path5340': bookRoutes['heisenburg'],
            'path5332': bookVariations['harborFreight'],
            'path5334': bookRoutes['smackdown'],
            'path5334-8': bookRoutes['heisenburg'],
            'path5336': bookVariations['harborFreight'],
        }),
    'octurnal': Topo(
        name='octurnal',
        parent=bookBoulders['methLab'],
        fileName='octurnal.svg',
        size='f',
        description='Meth Lab backside',
        routes={
            'path952': bookRoutes['learys'],
            'path1586': bookRoutes['octurnal'],
            'path2313': bookVariations['octurnalCenter'],
            'path2362': bookVariations['octurnalDirect'],
            'path2305': bookRoutes['guillotine'],
            'path1163': bookRoutes['learys'],
            'path2364': bookRoutes['octurnal'],
            'path2372': bookRoutes['octurnal'],
            'path2368': bookVariations['octurnalCenter'],
            'path2366': bookVariations['octurnalDirect'],
            'path2370': bookRoutes['guillotine'],
        }),
    'octurnal2': Topo(
        name='octurnal2',
        parent=bookBoulders['methLab'],
        fileName='octurnal2.svg',
        size='h',
        description='Meth Lab across from E\'s',
        routes={
            'path3604': bookRoutes['twoBlows'],
            'path3553': bookVariations['octurnalDirect'],
            'path3608': bookRoutes['twoBlows'],
            'path3606': bookVariations['octurnalDirect'],
        }),        
    'locksmith': Topo(
        name='Locksmith',
        parent=bookBoulders['azainBack'],
        fileName='locksmith.svg',
        size='h',
        description='The Locksmith',
        routes={
            'path1894': bookRoutes['locksmith'],
            'path1898': bookRoutes['locksmith'],
            'path1896': bookVariations['brainHaemorrhage'],
            'path1900': bookVariations['brainHaemorrhage'],
        }),
    'arboretum': Topo(
        name='arboretum',
        parent=bookBoulders['azainBack'],
        fileName='arboretum.svg',
        size='f',
        description='Routes on the Azain Backside',
        routes={
            'path501': bookRoutes['gardenVariety'],
            'path505': bookRoutes['gardenProj'],
            'path293': bookRoutes['arboretum'],
            'path349': bookRoutes['otherBernd'],
            'path512': bookRoutes['gardenVariety'],
            'path510': bookRoutes['gardenProj'],
            'path508': bookRoutes['arboretum'],
            'path508-1': bookRoutes['otherBernd'],
        }),
    'siren': Topo(
        name='siren',
        parent=bookBoulders['azainBack'],
        fileName='siren.svg',
        size='h',
        description='The Siren',
        routes={
            'path5162': bookVariations['sirenStand'],
            'path4111': bookRoutes['siren'],
            'path4117': bookRoutes['gumbyArete'],
            'path4212': bookRoutes['otherBernd'],
            'path4115': bookVariations['bagTricks'],
            'path4175': bookRoutes['siren'],
            'path4175-8': bookRoutes['gumbyArete'],
            'path4175-8-6': bookRoutes['otherBernd'],
            'path4175-2': bookVariations['bagTricks'],
            'path4175-8-6-6': bookVariations['sirenStand'],
        }),
    'gumby': Topo(
        name='Gumby',
        parent=bookBoulders['azainBack'],
        fileName='gumby.svg',
        size='h',
        description='Gumby Slab',
        routes={
            'path1571': bookVariations['bagTricks'],
            'path1573': bookVariations['bagTricks'],
            'path1678': bookVariations['bagTricks'],
            'path1569': bookRoutes['gumbyArete'],
            'path1676': bookRoutes['gumbyArete'],
            'path1563': bookRoutes['gumbySlab'],
            'path1674': bookRoutes['gumbySlab'],
        }),
#    'methLab2': Topo(
#        name='Meth Lab',
#        parent=bookBoulders['methLab'],
#        fileName='Methlab.svg',
#        size='h',
#        description='Meth Lab uphill face',
#        routes={
#            'path1856': bookRoutes['smackdown'],
#            'path1874': bookRoutes['smackdown'],
#            'path1876': bookVariations['harborFreight'],
#            'path1858': bookRoutes['heisenburg'],
#            'path1878': bookRoutes['heisenburg'],
#            'path1860': bookRoutes['learys'],
#            'path1880': bookRoutes['learys'],
#            'path1866': bookRoutes['guillotine'],
#            'path1884': bookRoutes['guillotine'],
#            'path1864': bookRoutes['octurnal'],
#            'path1886': bookRoutes['octurnal'],
#            'path1868': bookVariations['octurnalCenter'],
#            'path1888': bookVariations['octurnalCenter'],
#            'path1862': bookVariations['octurnalDirect'],
#            'path1890': bookVariations['octurnalDirect'],
#            'path1872': bookRoutes['e7'],
#            'path1892': bookRoutes['e7'],
#        }),
    'miniMe3': Topo(
        name='Mini Me 3',
        parent=bookBoulders['miniMe'],
        fileName='miniMe3.svg',
        size='h',
        description='Mini Me',
        routes={
            'path1844': bookRoutes['drEvil'],
            'path1842': bookRoutes['drEvil'],
            'path1850': bookRoutes['drEvil'],
            'path1846': bookRoutes['austinPowers'],
            'path1852': bookRoutes['austinPowers'],
            'path1848': bookRoutes['miniMe'],
            'path1854': bookRoutes['miniMe'],
        }),
    'office': Topo(
        name='Office',
        parent=bookBoulders['office'],
        fileName='office.svg',
        size='h',
        description='The Office',
        routes={
            'path1834': bookRoutes['daryl'],
            'path1838': bookRoutes['daryl'],
            'path1836': bookRoutes['jim'],
            'path1840': bookRoutes['jim'],
        }),
#    'swollen': Topo(
#        name='swollen',
#        parent=bookBoulders['swollen'],
#        fileName='swollen.svg',
#        size='h',
#        description='Swollen Member',
#        routes={
#            'path5504': bookRoutes['swollen'],
#            'path5506': bookRoutes['swollen'],
#            'path5508': bookRoutes['swollen'],
#        }),
    'swollen2': Topo(
        name='swollen',
        parent=bookBoulders['swollen'],
        fileName='swollen2.svg',
        size='h',
        description='Swollen Member and Inner Sanctum',
        routes={
            'path1813': bookRoutes['innerSanctum'],
            'path2042': bookRoutes['innerSanctum'],
            'path1830': bookVariations['innerSanctumSit'],
            'path2040': bookVariations['innerSanctumSit'],
            'path1832': bookRoutes['outerSanctum'],
            'path2044': bookRoutes['outerSanctum'],
            'path1760': bookRoutes['swollen'],
            'path1811': bookRoutes['swollen'],
            'path2046': bookRoutes['swollen'],
        }),
    'toilet': Topo(
        name='Toilet Bowl',
        parent=bookBoulders['toiletBowl'],
        fileName='toiletBowl.svg',
        size='h',
        description='Toilet Bowl',
        routes={
            'path1752': bookRoutes['toilet'],
            'path1756': bookRoutes['toilet'],
            'path1754': bookRoutes['toiletTraverse'],
            'path1758': bookRoutes['toiletTraverse'],
        }),
    'tonsil': Topo(
        name='Tonsil',
        parent=bookBoulders['tonsil'],
        fileName='tonsil.svg',
        size='h',
        description='Tonsil',
        routes={
            'path1680': bookRoutes['allSorts'],
            'path1690': bookRoutes['allSorts'],
            'path1682': bookRoutes['shadowGiants'],
            'path1692': bookRoutes['shadowGiants'],
            'path1684': bookRoutes['leftTonsil'],
            'path1694': bookRoutes['leftTonsil'],
            'path1686': bookRoutes['tonsil'],
            'path1688': bookRoutes['tonsil'],
            'path1696': bookRoutes['tonsil'],
        }),
    'trust': Topo(
        name='Turtle',
        parent=bookBoulders['tylerDurten'],
        fileName='trust.svg',
        size='h',
        description='Trust and Tyler Durten',
        routes={
            'path678': bookRoutes['trust'],
            'path830': bookRoutes['trust'],
            'path776': bookVariations['ironCross'],
            'path832': bookVariations['ironCross'],
            'path834': bookRoutes['tylerDurten'],
            'path836': bookRoutes['tylerDurten'],
            'path838': bookVariations['durtenDyno'],
            'path840': bookVariations['durtenDyno'],
        }),
    'turtle': Topo(
        name='Turtle',
        parent=bookBoulders['turtleShell'],
        fileName='turtle.svg',
        size='h',
        description='Turtle Shell',
        routes={
            'path855': bookRoutes['raphael'],
            'path861': bookRoutes['raphael'],
            'path857': bookRoutes['leonardo'],
            'path863': bookRoutes['leonardo'],
            'path859': bookRoutes['donatello'],
            'path919': bookRoutes['donatello'],
        }),
    'undertow': Topo(
        name='Undertow',
        parent=bookBoulders['undertow'],
        fileName='undertow.svg',
        size='h',
        description='Undertow downhill face',
        routes={
            'path1097': bookRoutes['undertow'],
            'path1111': bookRoutes['undertow'],
            'path1099': bookVariations['undertowSit'],
            'path1105': bookVariations['undertowSit'],
            'path1101': bookVariations['undertowSitRight'],
            'path1107': bookVariations['undertowSitRight'],
            'path1103': bookRoutes['riptide'],
            'path1109': bookRoutes['riptide'],
        }),
    'undertow2': Topo(
        name='Undertow2',
        parent=bookBoulders['undertow'],
        fileName='undertow2.svg',
        size='h',
        description='Undertow East face',
        routes={
            'path932': bookRoutes['sillySteep'],
            'path942': bookRoutes['sillySteep'],
            'path938': bookRoutes['undertow'],
            'path946': bookRoutes['undertow'],
            'path934': bookVariations['undertowSit'],
            'path944': bookVariations['undertowSit'],
            'path936': bookVariations['undertowSitRight'],
            'path950': bookVariations['undertowSitRight'],
            'path1134': bookRoutes['riptide'],
            'path948': bookRoutes['riptide'],
            'path940': bookRoutes['tidepool'],
            'path952': bookRoutes['tidepool'],
        }),
}
bookAreaMaps = {
    'main': AreaMap(
        name='The Garden Main Area Overview',
        parent=bookAreas['garden'],
        fileName='Garden.png',
        size='f',
        description='The Garden Main Area Overview',
    )
}
bookSubAreaMaps = {
    'entranceMain': SubAreaMap(
        name='Entrance Area map',
        parent=bookSubAreas['entranceMain'],
        fileName='entranceMain.svg',
        description='Entrance Area map',
        routes={
        'path1767': bookRoutes['toiletTraverse'],
        'path1769': bookRoutes['toilet'],
        'path1771': bookRoutes['donatello'],
        'path1773': bookRoutes['leonardo'],
        'path1775': bookRoutes['raphael'],
        'path1777': bookRoutes['overhand'],
        'path1779': bookRoutes['threeStar'],
        'path1781': bookRoutes['allSorts'],
        'path1783': bookRoutes['shadowGiants'],
        'path1785': bookRoutes['tonsil'],
        'path1787': bookRoutes['boysInTheWoods'],
        'path1789': bookRoutes['shinyJerry'],
        'path1791': bookRoutes['treeSlab'],
        }),
    'fightClub': SubAreaMap(
        name='Fight Club Area map',
        parent=bookSubAreas['fightClub'],
        fileName='fightClub.svg',
        description='Fight Club Area map',
        routes={
        'path4077': bookRoutes['eDirty'],
        'path1519': bookRoutes['jim'],
        'path1517': bookRoutes['daryl'],
        'path1515': bookRoutes['vince'],
        'path1513': bookRoutes['ear'],
        'path1511': bookRoutes['fightClubLeft'],
        'path1509': bookRoutes['tylerDurten'],
        'path1507': bookRoutes['trust'],
        'path1505': bookRoutes['austinPowers'],
        'path1503': bookRoutes['drEvil'],
        }),
#    'fightClub': SubAreaMap(
#        name='Fight Club Area map',
#        parent=bookSubAreas['fightClub'],
#        fileName='fightClub.svg',
#        description='Fight Club Area Map',
#        routes={
#            'path3073': bookRoutes['eDirty'],
#            'path3073-9': bookRoutes['sillySteep'],
#            'path3073-4': bookRoutes['undertow'],
#            'path3073-94': bookRoutes['tidepool'],
#            'path3073-1': bookRoutes['trust'],
#            'path3073-0': bookRoutes['tylerDurten'],
#            'path3073-6': bookRoutes['drEvil'],
#            'path3073-998': bookRoutes['austinPowers'],
#            'path3073-8': bookRoutes['fightClubLeft'],
#            'path3073-988': bookRoutes['ear'],
#            'path3073-3': bookRoutes['daryl'],
#        }),
#    'undertow': SubAreaMap(
#        name='Undertow area map',
#        parent=bookSubAreas['undertow'],
#        fileName='undertow.svg',
#        description='Undertow area map',
#        routes={
#            'path3073': bookRoutes['eDirty'],
#            'path3073-9': bookRoutes['sillySteep'],
#            'path3073-4': bookRoutes['undertow'],
#            'path3073-94': bookRoutes['tidepool'],
#            'path3073-1': bookRoutes['trust'],
#            'path3073-0': bookRoutes['tylerDurten'],
#            'path3073-6': bookRoutes['drEvil'],
#            'path3073-998': bookRoutes['austinPowers'],
#            'path3073-8': bookRoutes['fightClubLeft'],
#            'path3073-988': bookRoutes['ear'],
#            'path3073-3': bookRoutes['daryl'],
#        }
#    )
}


if __name__ == '__main__':
    book.paths['LaTeXTemplates'] = '../LocalBoulders/templates/'
    book.paths['LaTeXOut'] = './sections/'
    book.paths['pdf'] = './'
    book.gen()
