import sys
sys.path.insert(1, '../LocalBoulders')
from dataStructure import *


book = Book(
    name='The Garden Boulders: Local Boulders Guidebook Builder Proof of Concept v0.6',
    author='Andrew Child',
)
bookPhotos = {
    'austinPowers': Photo(
        name='Austin Powers',
        fileName='AustinPowers.jpg',
        description='Carson cranking across the face on Austin Powers.'),
    'undertow': Photo(
        name='Undertow',
        fileName='Undertow.jpg',
        description='Rob on Undertow'),
    'fightClub': Photo(
        name='Fight Club',
        fileName='FightClub2.jpg',
        description='Michael near the top of Fight Club.'),
    'octurnal': Photo(
        name='Octurnal',
        fileName='Octurnal.jpg',
        description='Carson landing the big throw on Octurnal. Classic!'),
    'smackdown': Photo(
        name='Smackdown',
        fileName='Smackdown.jpg',
        description='Andrew posting up at the start of Smackdown'),
}
bookAreas = {
    'garden': Area(
        name='The Garden Main',
        parent=book,
        description='The Garden Main bouldering area is true to its name. A lush green space features moss covered '
                    'boulders situated under a dense canopy. The area is visible from the road, though weirdly '
                    'easy to miss at first pass, look for the boulders on the left (uphill) side about 3.5 miles '
                    'down queartzville road.',
    ),
    'upperGarden': Area(
        name='Upper Garden',
        parent=book,
        description='Just up the road from the main area lays a talus field. Lack of shade, blackberries, poison '
                    'oak, and a 3 minute approach all make this area less desireable and less traveled then the Main',
    ),
    'pinkTag': Area(
        name='Pink Tag Boulders',
        parent=book,
        description='Just across the road from the main area lay a few boulders on the banks of the River',
    ),
    'quartzville': Area(
        name='Quartzville Creek',
        parent=book,
        description='About an hour further down the road from the main area there are a few interesting boulders '
                    'in a creek. Generally lower temperatures, free camping, and pleasant swimming holes make this '
                    'a nice mid summer spot'
    ),
}
bookSubAreas = {
    'entranceMain': Subarea(
        name='Entrance Area',
        parent=bookAreas['garden'],
    ),
    'fightClub': Subarea(
        name='Fight Club',
        parent=bookAreas['garden'],
        description='Located in the southwest corner of the Garden main, The Fight Club zone is home to the '
                    'namesake V8 test piece as well as several other quality lines. Flat landings and easy access '
                    'make this a nice spot to spend some time',
        photos=[
        bookPhotos['fightClub'],
        ]
    ),
    'methLab': Subarea(
        name='Meth Lab',
        parent=bookAreas['garden'],
        description='Easily the most recognizable feature at the Garden, the Meth Lab boulder towers over all other stones in the '
                    'main area. Most climbs for this zone are located in a secluded natural amphitheater on the '
                    'uphill side of the boulder.',
        photos=[
        bookPhotos['octurnal'],
        ]
    ),
    'roadSide': Subarea(
        name='Roadside Area',
        parent=bookAreas['garden'],
    ),
    'azainFront': Subarea(
        name='Azain Frontside',
        parent=bookAreas['garden'],
    ),
    'azainBack': Subarea(
        name='Azain Backside',
        parent=bookAreas['garden'],
    ),
    'entranceUpper': Subarea(
        name='Entrance Area',
        parent=bookAreas['upperGarden'],
    ),
    'breadLoaves': Subarea(
        name='The Bread Loaves',
        parent=bookAreas['upperGarden'],
    ),
    'strangeLove': Subarea(
        name='Dr. Strangelove Area',
        parent=bookAreas['upperGarden'],
    ),
    'pinkTag': Subarea(
        name='',
        parent=bookAreas['pinkTag'],
    ),
    'redneckRiviera': Subarea(
        name='Redneck Riviera',
        parent=bookAreas['quartzville'],
    ),
    'minersCamp': Subarea(
        name='Old Miner\'s Camp',
        parent=bookAreas['quartzville'],
    ),
}
bookBoulders = {
    'turtleShell': Boulder(
        name='Turtle Shell Boulder',
        parent=bookSubAreas['entranceMain'],
        description='A short boulder with a low angle offwidth crack.'
    ),
    'toiletBowl': Boulder(
        name='Toilet Bowl',
        parent=bookSubAreas['entranceMain'],
        description='If approaching via the main trail this is the first boulder you will encounter just of the road.'
    ),
    'boysWoods': Boulder(
        name='Boys In the Woods',
        parent=bookSubAreas['entranceMain'],
        description='A low boulder with an identifiable scoop on the downhill side is located right on the main trail.'
    ),
    'treeSlab': Boulder(
        name='Tree Slab',
        parent=bookSubAreas['entranceMain'],
        description='A narrow slab just uphill and to the right of the Boys in the Woods boulder.'
    ),
    'office': Boulder(
        name='The Office',
        parent=bookSubAreas['fightClub'],
        description='A tall not quite vertical boulder is immediately on your right as you enter the Fight Club Area'
    ),
    'fightClub': Boulder(
        name='Fight Club',
        parent=bookSubAreas['fightClub'],
        description='The obvious overhanging boulder with an interesting bubbly texture.'
    ),
    'tylerDurten': Boulder(
        name='Tyler Durten',
        parent=bookSubAreas['fightClub'],
        description='Just to the left of the fight club boulder is a tall wall with few features other than a '
                    'distinctive crimp rail at eye level.'
    ),
    'miniMe': Boulder(
        name='Mini Me',
        parent=bookSubAreas['fightClub'],
        description='A short pointy boulder with a flat landing is nearly freestanding on the downhill side of the '
                    'Fight Club zone',
        photos=[
        bookPhotos['austinPowers']
            ],
    ),
    'trust': Boulder(
        name='Trust',
        parent=bookSubAreas['fightClub'],
        description='The Trust boulder sits on an elevated platform behind Mini Me and to the Left of Tyler Durten'
    ),
    'eDirty': Boulder(
        name='E\'s Dirty B',
        parent=bookSubAreas['fightClub'],
        description='Following a faint trail west traveling past the trust boulder brings you to a Large boulder '
                    'which almost immediately gives way to low angle slab.'
    ),
    'sillySteep': Boulder(
        name='Silly Steep',
        parent=bookSubAreas['fightClub'],
        description='Thin overhanging block left of the Undertow boulder.'
    ),
    'undertow': Boulder(
        name='Undertow',
        parent=bookSubAreas['fightClub'],
        description='Realatively off the beaten path as far as classic garden boulders goes. Follow a faint trail '
                    'upill past the trust boulder.',
        photos=[
        bookPhotos['undertow']
            ],
    ),
    'methLab': Boulder(
        name='Meth Lab',
        parent=bookSubAreas['methLab'],
        photos=[
            bookPhotos['smackdown'],
        ]
    ),
    'swollen': Boulder(
        name='Swollen Member',
        parent=bookSubAreas['methLab'],
        description='A small prow just out of the hill side above the Meth Lab boulder at a provocative angle.'
    ),
    'eBoulder': Boulder(
        name='E\'s Boulder',
        parent=bookSubAreas['methLab'],
        description='A large boulder directly to the right of Octurnal holds a few notable routes.'
    ),
    'bubbler': Boulder(
        name='The Bubbler',
        parent=bookSubAreas['methLab'],
        description='A small unassuming block sits just downhill of E\'s boulder.'
    ),
    'bitchin': Boulder(
        name='Bitchin Corners',
        parent=bookSubAreas['roadSide'],
        description=''
    ),
    'roadside': Boulder(
        name='Roadside',
        parent=bookSubAreas['roadSide'],
        description=''
    ),
    'theGood': Boulder(
        name='The Good',
        parent=bookSubAreas['azainFront'],
        description=''
    ),
    'nextGood': Boulder(
        name='Next to The Good',
        parent=bookSubAreas['azainFront'],
        description=''
    ),
    'azainFront': Boulder(
        name='Azain Front Side',
        parent=bookSubAreas['azainFront'],
        description=''
    ),
    'nightCrawler': Boulder(
        name='Night Crawler',
        parent=bookSubAreas['azainFront'],
        description=''
    ),
    'intro': Boulder(
        name='Intro Boulder',
        parent=bookSubAreas['entranceUpper'],
        description=''
    ),
    'lowerBread': Boulder(
        name='Lower Bread Loaf',
        parent=bookSubAreas['breadLoaves'],
        description=''
    ),
    'upperBread': Boulder(
        name='Upper Bread Loaf',
        parent=bookSubAreas['breadLoaves'],
        description=''
    ),
    'drStrange': Boulder(
        name='Dr. Strange Love',
        parent=bookSubAreas['strangeLove'],
        description=''
    ),
    'tecnu': Boulder(
        name='Tecnu Boulder',
        parent=bookSubAreas['pinkTag'],
        description=''
    ),
    'jonahDab': Boulder(
        name='Jonah\'s Dab Rig',
        parent=bookSubAreas['pinkTag'],
        description=''
    ),
    'farley': Boulder(
        name='Farley Prep',
        parent=bookSubAreas['pinkTag'],
        description=''
    ),
    'ponyBoy': Boulder(
        name='Pony Boy',
        parent=bookSubAreas['redneckRiviera'],
        description=''
    ),
    'monorail': Boulder(
        name='Monorail',
        parent=bookSubAreas['redneckRiviera'],
        description=''
    ),
    'yoMamma': Boulder(
        name='Yo Mamma Boulder',
        parent=bookSubAreas['redneckRiviera'],
        description=''
    ),
    'mossBoss': Boulder(
        name='Moss Boss',
        parent=bookSubAreas['redneckRiviera'],
        description=''
    ),
    'fourPointFive': Boulder(
        name='The 4.5',
        parent=bookSubAreas['redneckRiviera'],
        description=''
    ),
    'dabRig': Boulder(
        name='The Dab Rig',
        parent=bookSubAreas['minersCamp'],
        description=''
    ),
}
bookRoutes = {
    'raphael': Route(
        name='Raphael Crack',
        parent=bookBoulders['turtleShell'],
    ),
    'toilet': Route(
        name='Toilet Bowl',
        parent=bookBoulders['toiletBowl'],
    ),
    'bubbles': Route(
        name='Scrubbing Bubbles',
        parent=bookBoulders['toiletBowl'],
    ),
    'boysInTheWoods': Route(
        name='Boys in the Woods',
        parent=bookBoulders['boysWoods'],
        grade=4,
        rating=3,
        description='Start on a low jug just before the scoop at the lowest part of the boulder. Climb up the left '
                    'arete of the scoop until you can flop in. Some may consider this an eliminate since, with '
                    'difficulty, you could also just mantle directly into the scoop.',
    ),
    'cubaGooding': Route(
        name='Cuba Gooding',
        parent=bookBoulders['boysWoods'],
        description='Start as for Boys in the Woods but climb right along the lip of the scoop until you can reach the '
                    'holds at the top of Ice Cubes Shiny Jerry Curl'
    ),
    'shinyJerry': Route(
        name='Ice Cubes Shiny Jerry Curl',
        parent=bookBoulders['boysWoods'],
        description='Start on a low sloping edge and pull some sneaky moves to gain a knife edge crimp at eye level. '
                    'Continue straight up.'
    ),
    'treeSlab': Route(
        name='Tree Slab',
        parent=bookBoulders['treeSlab'],
        grade=1,
        rating=3,
        description='Climb the center of the slab.'
    ),
    'trust': Route(
        name='Trust',
        parent=bookBoulders['trust'],
        grade=2,
        rating=4,
        description='Sit start in compression on a hanging refrigerator block. Climb straight up through a slopeing '
                    'ledge to the top. Look for the juggy crack ~1ft inset from the lip.'
    ),
    'miniMe': Route(
        name='Mini Me',
        parent=bookBoulders['miniMe'],
        grade=3,
        rating=0,
        description='start on blunt corner. Make tricky moves to a blocky jug to the lip and traverse left to an easy '
                    'top over a rocky landing'
    ),
    'austinPowers': Route(
        name='Austin Powers',
        parent=bookBoulders['miniMe'],
        grade=5,
        rating=2,
        description='Start as for Mini Me but move right into top of Dr. Evil'
    ),
    'drEvil': Route(
        name='Dr. Evil',
        parent=bookBoulders['miniMe'],
        rating=2,
        grade=3,
        description='sit start on lowest holds of a compressiony arete with left foot over a small rock. '
                    'Pull some tricky moves to gain better holds either rolling onto the right hand slab early or '
                    'staying on the arete the whole way.'
    ),
    'tylerDurten': Route(
        name='Tyler Durten',
        parent=bookBoulders['tylerDurten'],
        rating=1,
        grade=3,
        description='Start on a henious crimp rail and punch out left to much better holds.'
    ),
    'daryl': Route(
        name='Daryl Philbin',
        parent=bookBoulders['office'],
        rating=4,
        grade=1,
        serious=1,
        description='Starting at the Center of the block climb left on good holds to the arete. Climb up the arete '
                    'until you can reach good face holds up right and continue through a, thankfully, juggy top out. '
                    'Mind the rock at the base of the climb. Left and right alternative starts add a little variety but do '
                    'not change the grade.'
    ),
    'ear': Route(
        name='The Ear',
        parent=bookBoulders['fightClub'],
        rating=4,
        grade=2,
        description='Start on the arete at the far right end of the boulder. Climb straight up through tricky holds '
                    'to a heady top out.'
    ),
    'fightClub': Route(
        name='Fight Club',
        parent=bookBoulders['fightClub'],
        rating=4,
        grade=8,
        description='Area classic, this rig is a feather in any would be crushers cap. Start on the far right arete as for Ear. '
                    'Traverse across the angle change and top out above a bubbly crimp rail on the overhanging face.'
    ),
    'fightClubLeft': Route(
        name='Fight Club Left',
        parent=bookBoulders['fightClub'],
        description='PLACEHOLDER'
    ),
    'eDirty': Route(
        name='E\'s Dirty B',
        parent=bookBoulders['eDirty'],
        rating=3,
        grade=5,
        description='Start on a lumpy flake in the back of a small cave. Using slopeing edges out right and a '
                    'difficult undercling navigate out of the cave trending right at the lip to a jug. The final '
                    'slab quest is an enjoyable and easy top out.',
    ),
    'sillySteep': Route(
        name='Silly Steep Mantle',
        parent=bookBoulders['sillySteep'],
        description='PLACEHOLDER'
    ),
    'undertow': Route(
        name='Undertow',
        parent=bookBoulders['undertow'],
        description='PLACEHOLDER'
    ),
    'tidepool': Route(
        name='Tide Pool',
        parent=bookBoulders['undertow'],
        description='PLACEHOLDER'
    ),
    'methLab': Route(
        name='Meth Lab Project',
        parent=bookBoulders['methLab'],
        serious=3,
        description='The obvious prow on the front of the Meth Lab boulder has top rope anchors but a route up it has '
                    'likely never been free\'ed even on TR. The ethics of climbing this behemoth are contentious but '
                    'in my opion it is fair game to bolt as a sport route. If you have the desire to do so consider '
                    'working it out on TR first before placing new equipment.'
    ),
    'dontBlow': Route(
        name='Don\'t Blow the Jug',
        parent=bookBoulders['methLab'],
        grade=2,
        description='Start at the base of the wide crack. Climb the offwidth until you can make use of a jug to '
                    'squeeze into the crack. Walk through the crack to the far side of the boulder.'
    ),
    'trustIssues': Route(
        name='Trust Issues',
        parent=bookBoulders['methLab'],
        serious=2,
        description='PLACEHOLDER'
    ),
    'leaveJesus': Route(
        name='Leave It to Jesus',
        parent=bookBoulders['methLab'],
        description='PLACEHOLDER'
    ),
    'smackdown': Route(
        name='Smackdown',
        parent=bookBoulders['methLab'],
        rating=4,
        grade=7,
        description='Start standing with left hand gaston and right hand jug sidepull. Crank some powerful moves on bad feet '
                    'and follow the line of crimps to a top out left'),
    'heisenburg': Route(
        name='Heisenburg',
        parent=bookBoulders['methLab'],
        description='PLACEHOLDER'
    ),
    'learys': Route(
        name='Learys Lunge',
        parent=bookBoulders['methLab'],
        description='PLACEHOLDER'
    ),
    'guillotine': Route(
        name='Guillotine',
        parent=bookBoulders['methLab'],
        rating=3,
        grade=4,
        description='Start underclinging on the hanging \"Guillotine blade\" flake left of Octurnal. Climb straight up.'
    ),
    'octurnal': Route(
        name='Octurnal',
        parent=bookBoulders['methLab'],
        rating=5,
        grade=7,
        description='For many this is THE local test piece in the area. Start sitting '
                    'with left hand on a sloping triangular rib and right hand on a slopey cripm at the arete. Crank a few hard '
                    'moves to gain the lip then traverse left through the lightning bolt hold to a pumpy top out. Originally known as \"Tom\'s phsychadelic trip\".'),
    'twoBlows': Route(
        name='Two Blows One Stroke',
        parent=bookBoulders['methLab'],
        description='PLACEHOLDER'
    ),
    'slamDunk': Route(
        name='Slam Dunk',
        parent=bookBoulders['eBoulder'],
        description='PLACEHOLDER'
    ),
    'e7': Route(
        name='E\'s V7',
        parent=bookBoulders['eBoulder'],
        description='PLACEHOLDER'
    ),
    'enchilada': Route(
        name='Enchilada',
        rating=3,
        parent=bookBoulders['eBoulder'],
        grade=9,
        description='Start matched on a good flat rail low to the ground with some awkward feet options. Cross into a '
                    'comfortable crimp and fire up left before coming back right to a flat jug. Pretty classic as far as low balls go!'),
}
bookVariations = {
    'mrBigglesworth': Variation(
        name='Mr. Bigglesworth',
        parent=bookRoutes['drEvil'],
        grade=1,
        rating=1,
        description='Start on good crimps right of the arete just before the angle change, continue straight up or '
                    'move left onto the arete. Authors note: other guides identify several other variations on '
                    'this route, I am of the opinion that further variations are overly restrictive'),
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
    'jesusSit': Variation(
        name='Leave it to Jesus Sit',
        parent=bookRoutes['leaveJesus'],
    ),
    'octurnalDirect': Variation(
        name='Direct Exit',
        parent=bookRoutes['octurnal'],
        grade=7,
        rating=5,
        description='Of all the Octurnal exits this one has the most interesting moves. Climb Octurnal to the ledge '
                    'then pull some tricky moves to round the right arete. Continue on through a heads up top out.'),
    'octurnalCenter': Variation(
        name='Center Exit',
        parent=bookRoutes['octurnal'],
        grade=7,
        rating=4,
        description='The easiest top option for this boulder involves pulling through a suprisingly good side pull '
                    'above the left end of the ledge. For years this variation livided in moss covered obscurity '
                    'climbing it will make you wonder why the awkward pumpfest traverse exit is the default line'),
    'harborFreight': Variation(
        name='Harbor Freight',
        parent=bookRoutes['smackdown'],
        grade=8,
        description='Sit down start at the lowest available holds and climb into Smackdown. This was literally '
                    'unearthed when a local climber yarded a large rock out from the landing of Smackdown using a '
                    'chain and come along. The device broke in the process inspiring the name of the route.'),
}
bookTopos = {
    'miniMe': Topo(
        name='miniMe',
        boulder=bookBoulders['miniMe'],
        fileName='miniMe2.svg',
        size='f',
        description='Routes on Mini Me, Trust, and Tyler Durten',
        routes={
            'path302': bookRoutes['miniMe'],
            'path355': bookRoutes['austinPowers'],
            'path406': bookRoutes['drEvil'],
            'path963': bookRoutes['trust'],
            'path965': bookRoutes['tylerDurten'],
            'path4734': bookVariations['durtenDyno'],
            'path1264': bookRoutes['miniMe'],
            'path291': bookRoutes['austinPowers'],
            'path2046': bookRoutes['drEvil'],
            'path2048': bookRoutes['trust'],
            'path2050': bookRoutes['tylerDurten'],
            'path291-0': bookVariations['durtenDyno'],
        }
    ),
}
bookSubAreaMaps = {
    'fightClub': SubAreaMap(
        name='Fight Club area map',
        subArea=bookSubAreas['fightClub'],
        fileName='fightClub.svg',
        description='Fight Club Area Map',
        routes={
            'path3073': bookRoutes['eDirty'],
            'path3073-9': bookRoutes['sillySteep'],
            'path3073-4': bookRoutes['undertow'],
            'path3073-94': bookRoutes['tidepool'],
            'path3073-1': bookRoutes['trust'],
            'path3073-0': bookRoutes['tylerDurten'],
            'path3073-6': bookRoutes['drEvil'],
            'path3073-998': bookRoutes['austinPowers'],
            'path3073-8': bookRoutes['fightClubLeft'],
            'path3073-988': bookRoutes['ear'],
            'path3073-3': bookRoutes['daryl'],
        }
    ),
    'undertow': SubAreaMap(
        name='Undertow area map',
        subArea=bookSubAreas['fightClub'],
        fileName='undertow.svg',
        description='Undertow area map',
        routes={
            'path3073': bookRoutes['eDirty'],
            'path3073-9': bookRoutes['sillySteep'],
            'path3073-4': bookRoutes['undertow'],
            'path3073-94': bookRoutes['tidepool'],
            'path3073-1': bookRoutes['trust'],
            'path3073-0': bookRoutes['tylerDurten'],
            'path3073-6': bookRoutes['drEvil'],
            'path3073-998': bookRoutes['austinPowers'],
            'path3073-8': bookRoutes['fightClubLeft'],
            'path3073-988': bookRoutes['ear'],
            'path3073-3': bookRoutes['daryl'],
        }
    )
}


if __name__ == '__main__':
    book.gen()