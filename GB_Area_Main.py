from dataStructure import Area, Subarea, Formation, Route, Variation
from GB_Book import book

Area(name='The Garden Main',
     parent=book,
     gps='44.44076010641458, -122.5752659013521',
     description='Located about 3.5 miles down Quartzville Road from Highway 20, park in the gravel pull out where the road bends '
                 'left just before you reach the boulders. The Garden Main bouldering area is true to its name. '
                 'A lush green space features moss covered boulders situated under a dense canopy.', )

Subarea(name='Entrance Area',
        parent=book.areas['The Garden Main'],
        description='A cluster of boulders situated in between the two main trails.'
        )
Subarea(name='Fight Club',
        parent=book.areas['The Garden Main'],
        description='Located in the southwest corner of the Garden main, the Fight Club zone is home to the '
                    'namesake V8 test piece as well as several other quality lines. Flat landings and easy access '
                    'make this a nice spot to spend some time')
Subarea(name='Undertow',
        parent=book.areas['The Garden Main'],
        description='Directly uphill from Fight Club are a few quality boulders separated by overgrown trails.')
Subarea(name='Meth Lab',
        parent=book.areas['The Garden Main'],
        description='Easily the most recognizable feature at the Garden, the Meth Lab boulder towers over all other stones in the '
                    'main area. Most climbs for this zone are located in a secluded natural amphitheater on the '
                    'uphill side of the boulder.')
Subarea(name='Big',
        parent=book.areas['The Garden Main'],
        description='In spite of this area\'s close proximity to both the main trail and the road the most of the climbs here are '
                    'very obscure. Several other lines around here have been documented over the years but they have yet '
                    'to be rediscovered.')
Subarea(name='Azain',
        parent=book.areas['The Garden Main'],
        description='Azain is a jumbled collection of rocks which forms the highest point of the Garden main.',
        )
Subarea(name='Child of God',
        parent=book.areas['The Garden Main'],
        description='The backside of the Azain formation is a nice area with a great variety of routes.',
        )
Subarea(name='François',
        parent=book.areas['The Garden Main'], )

Formation(name='Toilet Bowl',
          parent=book.subareas['Entrance Area'],
          description='If approaching via the main trail this is the first boulder you will encounter just off the road.')
Formation(name='Overhand',
          parent=book.subareas['Entrance Area'],
          description='a short prow in the rocky landscape between the two entrance trails.')
Formation(name='Boys In the Woods',
          parent=book.subareas['Entrance Area'],
          description='A low boulder with an identifiable scoop on the downhill side is located on the main trail '
                      'roughly 150\' uphill from the road.')
Formation(name='Tree Slab',
          parent=book.subareas['Entrance Area'],
          description='A narrow slab just uphill and to the right of the Boys in the Woods boulder.')
Formation(name='The Good Warm Up',
          parent=book.subareas['Entrance Area'],
          description='A tiny fin shaped boulder on the main trail.')
Formation(name='Tonsil',
          parent=book.subareas['Entrance Area'],
          description='A small hanging prow wedged under a larger hanging prow, which is itself wedged under the Meth Lab prow (a very big hanging prow).')
Formation(name='All Sorts of Ease',
          parent=book.subareas['Entrance Area'],
          description='A low angle slab under the Meth Lab prow.')
Formation(name='Three Star Ledge',
          parent=book.subareas['Entrance Area'],
          description='Angular boulder in the rocky landscape between the two entrance trails.')
Formation(name='Turtle Shell Boulder',
          parent=book.subareas['Entrance Area'],
          description='A short boulder with a low angle off-width crack. If approaching on the fight club trail this is '
                      'the first boulder that you will encounter')
Formation(name='The Office',
          parent=book.subareas['Fight Club'],
          description='A tall not quite vertical boulder is immediately on your right as you enter the Fight Club area.')
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
          description='The Trust boulder sits on an terrace behind Mini Me and to the Left of Tyler Durten.')
Formation(name='Mini Me',
          parent=book.subareas['Fight Club'],
          description='A short pointy boulder with a flat landing is nearly freestanding on the downhill side of the '
                      'Fight Club zone.', )
Formation(name='E\'s Dirty B',
          parent=book.subareas['Fight Club'],
          description='Following a faint trail west traveling past the trust boulder brings you to a Large boulder '
                      'which almost immediately gives way to low angle slab.')
Formation(name='Silly Steep',
          parent=book.subareas['Undertow'],
          description='Thin overhanging block left of the Undertow boulder.')
Formation(name='Undertow',
          parent=book.subareas['Undertow'],
          description='Relatively off the beaten path as far as classic garden boulders goes. Follow a faint trail '
                      'up hill past the trust boulder.')
Formation(name='Car Alarm',
          parent=book.subareas['Undertow'],
          description='This secluded block has a variety of worthwhile beginner climbs. Most of the rock is covered with holds so its also a good spot to play around and make up your own linkups.')
Formation(name='Chock Stone Highball',
          parent=book.subareas['Undertow'],
          description='')
Formation(name='Bubonic Plague',
          parent=book.subareas['Undertow'],
          description='A short boulder on the hillside in between Chock Stone Highball and the Meth Lab.')
Formation(name='Hanging Prow',
          parent=book.subareas['Undertow'],
          description='An eye catching hanging prow in between Chock Stone Highball and Nightcrawler.')
Formation(name='Meth Lab',
          parent=book.subareas['Meth Lab'], )
Formation(name='Swollen Member',
          parent=book.subareas['Meth Lab'],
          description='A small prow just out of the hill side above the Meth Lab boulder protrudes at a provocative angle.')
Formation(name='Meth Lab Highball',
          parent=book.subareas['Meth Lab'],
          description='Slabby boulder located to the left of Swollen Member. Not to be confused with the highballs on the actual Meth Lab boulder.')
Formation(name='Party Boulder',
          parent=book.subareas['Meth Lab'],
          description='This bulbous semi hanging boulder is directly uphill of Octernal.')
Formation(name='E\'s Boulder',
          parent=book.subareas['Meth Lab'],
          description='A large boulder directly to the right of Octernal holds a few notable routes.')
Formation(name='Little E Boulder',
          parent=book.subareas['Meth Lab'],
          description='A small boulder nestled in the alcove across from Enchilada')
Formation(name='The Bubbler',
          parent=book.subareas['Meth Lab'],
          description='A small unassuming block sits just downhill of E\'s boulder.')
Formation(name='Bitchin Corners',
          parent=book.subareas['Big'],
          description='A neat angular face sits on the downhill of an otherwise unremarkable boulder.')
Formation(name='Hueco Wabo',
          parent=book.subareas['Big'],
          description='An aesthetic boulder sits well off the beaten path.')
Formation(name='Baldo',
          parent=book.subareas['Big'], )
Formation(name='Crazy Cool',
          parent=book.subareas['Big'],
          description='A small boulder with an eye catching arête leans against the "Big" boulder\'s western face.')
Formation(name='Big',
          parent=book.subareas['Big'],
          description='The "Big" boulder is a large moss covered boulder on the eastern boundary of the Garden Main '
                      'area, in other guides this has also been called "roadside", and "North Block".')
Formation(name='Classique',
          parent=book.subareas['Big'], )
Formation(name='Small',
          parent=book.subareas['Big'], )
Formation(name='The Good',
          parent=book.subareas['Azain'],
          description='Continuing up the main trail from Boys in the Woods leads to a good boulder with two routes on '
                      'the downhill face.')
Formation(name='Next to the Good',
          parent=book.subareas['Azain'],
          description='A slender boulder hangs off the ground to the left of the Good.')
Formation(name='Nightcrawler',
          parent=book.subareas['Azain'],
          description='This iconic double arête boulder sits like a throne near the top of the Azain formation.')
Formation(name='Azain Spire',
          parent=book.subareas['Azain'],
          description='A thin triangular flake stands on end behind swollen member and in front of Azain.')
Formation(name='Light Cave',
          parent=book.subareas['Azain'],
          description='A cave directly behind Azain Spire is mostly full of bats and trash. Consider going somewhere else if the bats are active down here. Even if they aren\'t around maybe plan on taking a shower once your done.')
Formation(name='Azain',
          parent=book.subareas['Azain'],
          description='The huge walls of the Azain formation are located just off the main trail behind The Good.')
Formation(name='Locksmith',
          parent=book.subareas['Child of God'],
          description='A tall narrow boulder that leans up against the backside of Azain.')
Formation(name='Garden Roof',
          parent=book.subareas['Child of God'],
          description='Just past the locksmith is a wide short overhang which sits opposite a field of blackberries on '
                      'the main trail.')
Formation(name='Gumby Wall',
          parent=book.subareas['Child of God'],
          description='Continuing past the Garden Roof leads to the Gumby Wall. Look for the obvious overhanging prow of '
                      'the siren.')
Formation(name='Gumby Crack',
          parent=book.subareas['Child of God'],
          description='Immediately to the right of the Gumby Wall is another slab that\'s broken by a juggy horizontal crack.')
Formation(name='François',
          parent=book.subareas['François'],
          description='The main trail veers left into a narrow corridor in between this large boulder and Azain.')
Formation(name='Scary Grandma',
          parent=book.subareas['François'],
          description='A secluded boulder can be approached by staying right at the fork when the main trail turns left around François.')
Formation(name='Fern Sully',
          parent=book.subareas['François'],)
Route(name='Raphael Crack',
      parent=book.formations['Turtle Shell Boulder'],
      grade=0,
      rating=1,
      description='Climb the wide crack from a stand start.')
Route(name='Donatello',
      parent=book.formations['Turtle Shell Boulder'],
      grade=1,
      rating=1,
      description='start on a flat ledge where the rock angle changes. Slap a low angle arête until you can hike your '
                  'feet up. Only somewhat distinct from Leonardo.')
Route(name='Leonardo',
      parent=book.formations['Turtle Shell Boulder'],
      grade=3,
      rating=1,
      description='Lay down start with hands on a low broken flake. With difficulty pull off the ground and slap a slopey ledge traverse up and left until you can rock over onto the downhill face. Sort of like a worse version of boys in the woods.')
Route(name='Toilet Bowl',
      parent=book.formations['Toilet Bowl'],
      grade=1,
      rating=1,
      description='Stand start on a protruding block with left hand on an under cling and right hand on a knob. Pull a few moves to gain the lip of the boulder.')
Route(name='Toilet Bowl Traverse',
      parent=book.formations['Toilet Bowl'],
      grade=0,
      rating=2,
      description='Starting on a good rail at the lower left of the boulder. Traverse the lip topping out at the highest point or continue all the way until the boulder recedes into the hill.', )
Route(name='Boys in the Woods',
      parent=book.formations['Boys In the Woods'],
      grade=4,
      rating=2,
      description='Start on a low jug just before the scoop at the lowest part of the boulder. Climb up the left '
                  'arête of the scoop until you can flop in. Some may consider this an eliminate since, with '
                  'difficulty, you could also just mantle directly into the scoop.', )
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
Route(name='Spider Bumps',
      parent=book.formations['Boys In the Woods'],
      grade=4,
      rating=1,
      description='Start on a thin crimp rail over a dabby rock. Maneuver yourself to a good jug using almost non existent holds while trying not to dab.')
Route(name='Tree Slab',
      parent=book.formations['Tree Slab'],
      grade="1+",
      rating=2,
      description='Climb the center of the slab from a stand start.')
Route(name='The Good Warm Up',
      parent=book.formations['The Good Warm Up'],
      grade=0,
      rating=1,
      description='Whether or not this is a good warmup is debatable. Sit start with hands matched on a good rail. Climb the short face using both arêtes. Also known as Shark Fin.')
Route(name='Three Star Ledge',
      parent=book.formations['Three Star Ledge'],
      grade=2,
      rating=2,
      description='Stand start with hands matched on the ledge. Chuck out to the left arête and follow it to the apex of the boulder. The small boulders at the base are off.')
Route(name='Overhand',
      parent=book.formations['Overhand'],
      grade=8,
      rating=2,
      serious=1,
      FA='Matt Slayton',
      description='Climbs a short overhang starting at the bottom of the left arête. Try not to blow the last move. Also known as Evolve to Be More.')
Route(name='Goose Egg',
      parent=book.formations['Overhand'],
      grade=5,
      rating=1,
      FA='Isaac Tuomi',
      description='On the right side of the roof of the overhand boulder. Scrunchy start with left hand on the big ledge and right hand on an opposing corner.')
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
                  'vertical side pull sloper on the blunt right corner and left hand on a juggy under cling.  Shorter '
                  'climbers will have difficulty reaching the starting holds. After establishing the rock below is '
                  'off.')
Route(name='Gingiva',
      name_unconfirmed=True,
      parent=book.formations['Tonsil'],
      grade=2,
      rating=1,
      description='Climbs the boulder below Tonsil. Sit start with low holds on the right arête. Pull a few awkward '
                  'moves into a cramped top out.')
Route(name='Trust',
      parent=book.formations['Trust'],
      grade=2,
      rating=3,
      description='Sit start in compression on a hanging refrigerator block. Climb straight up through a sloping '
                  'ledge to the top. Look for the juggy crack ~1ft inset from the lip.')
Route(name='Mini Me',
      parent=book.formations['Mini Me'],
      grade=3,
      rating=1,
      description='start on blunt corner. Make tricky moves to a blocky jug to the lip and traverse left to an easy '
                  'top over a rocky landing.')
Route(name='Austin Powers',
      parent=book.formations['Mini Me'],
      grade=5,
      rating=2,
      description='Start straddling a blunt corner with your left hand on a lemon sized knob and right on a low side pull crimp, Crank to a jug and move right into top of Dr. Evil. Also known as Macro Me. Starting as for Mini Me is also a valid interpretation of this line.')
Route(name='Dr. Evil',
      parent=book.formations['Mini Me'],
      rating=2,
      grade=4,
      description='sit start in compression with left hand on a low sloper side pull and right hand on the arête. '
                  'Pull some tricky moves to gain better holds either rolling onto the right hand slab early or '
                  'staying on the arête the whole way. Starting "one move in" with your right hand on the good obvious side pull is an all together more enjoyable experience if a little easier.')
Route(name='Project Mayhem',
      parent=book.formations['Tyler Durten'],
      rating=1,
      grade="1+",
      description='Start on a heinous crimp rail and punch out left to much better holds.')
Route(name='Angel Face',
      parent=book.formations['Tyler Durten'],
      grade=6,
      grade_unconfirmed=True,
      description='Start as for Tyler Durten but climb more or less straight up using the sloping rib on the upper '
                  'right side of the boulder')
Route(name='Durten Layback',
      parent=book.formations['Tyler Durten'],
      grade=1,
      rating=1,
      description='Stand start and climb the right corner using the Fight Club boulder for feet. Is chimneying between the boulders off? Asking for a friend.')
Route(name='Dwight Schrute',
      parent=book.formations['The Office'],
      grade=1,
      serious=1,
      rating=2,
      description='Climb the slab over a narrow, but flat landing.')
Route(name='Jim Halpert',
      parent=book.formations['The Office'],
      rating=0,
      grade=1,
      serious=2,
      description='Starting on the right edge of the block climb climb the right corner over a rocky landing. Either '
                  'pull some harder moves to stay on the downhill face or round the corner to the right and pull '
                  'some easier moves over a worse landing. Grade and rating unconfirmed.',
      grade_unconfirmed=True)
Route(name='Michael Scott',
      parent=book.formations['The Office'],
      grade=3,
      serious=1,
      rating=2,
      description='Climb the center of the boulder using a cool sloper and some perchy feet.')
Route(name='Daryl Philbin',
      parent=book.formations['The Office'],
      rating=3,
      grade="1/2",
      serious=1,
      description='Starting at the Center of the block climb left on good holds to the arête. Climb up the arête '
                  'until you can reach good face holds up right and continue through a, thankfully, juggy top out. '
                  'Left and right alternative starts add a little variety but do not change the grade. Mind the rock at the base of the climb. This line was originally referred to as The Burning Bus in reference to an unfortunate hitch hiker that was encountered on the road in.')
Route(name='Routes on the Backside',
      item_id='Backside of Office',
      parent=book.formations['The Office'],
      grade='?',
      description='The faces on the backside of this boulder have been discovered and forgotten several times over the years. Reestablishing these lines is a project for the future.')
Route(name='Vince',
      parent=book.formations['Crash Test Dummies'],
      rating=2,
      grade=2,
      description='Squat start on good edges. Navigate a crescent shaped side pull rail to a delicate top out. Make '
                  'sure to clean the top out before attempting.')
Route(name='The Ear',
      parent=book.formations['Fight Club'],
      rating=3,
      grade="3",
      description='Start on the arête at the far right end of the boulder. Climb straight up through tricky holds '
                  'to a heady top out. Veering onto the face instead of using the good holds on the right arête '
                  'bumps the grade up to around V4.')
Route(name='Fight Club',
      parent=book.formations['Fight Club'],
      rating=3,
      grade=8,
      FA='Craig Malik',
      description='Area classic, this rig is a feather in any would be crushers cap. Start on the far right arête as for Ear. '
                  'Traverse across the angle change and top out above a bubbly crimp rail on the overhanging face.')
Route(name='Fight Club 2',
      parent=book.formations['Fight Club'],
      grade=10,
      rating=2,
      FA='Griffin Thoms',
      description='Sit start with hands matched low on the left arête of the overhanging boulder. Climb across the overhang topping as for Fight Club.')
Route(name='Brewmaster',
      parent=book.formations['Fight Club'],
      grade=5,
      rating=2,
      description='Not to be mistaken for Fight Club 2. Sit start in the same spot but climb up the arête. Starting a '
                  'move or two in brings the grade down a bit. This is also known as tool shed direct.')
Route(name='Green Hell',
      parent=book.formations['E\'s Dirty B'],
      rating=2,
      grade=2,
      description='Squat start on an angled rail at chest level to the left of the cave. The path of least resistance leads left but climbing straight up is also possible at a similar grade.', )
Route(name='E\'s Dirty B',
      parent=book.formations['E\'s Dirty B'],
      rating=2,
      grade=5,
      description='Start with hands matched on a lumpy flake in the back of a small cave. Using sloping edges out right and a '
                  'difficult under cling navigate out of the cave trending right at the lip to a jug. The final '
                  'slab quest is an enjoyable and easy top out. Also known as Trouble with Bubbles.', )
Route(name='Unknown',
      parent=book.formations['E\'s Dirty B'],
      grade='1/2',
      item_id='Unknown on E\'s Dirty B',
      rating=1,
      description='A hard squat start on a faint ripple leads to easier climbing. Starts just right of the cave.', )
Route(name='Silly Steep Mantle',
      parent=book.formations['Silly Steep'],
      grade=4,
      rating=2,
      description='Stand start with good compression holds in the roof. Make a hard pull to the juggy edge below the '
                  'lip and figure out how to get your body over the top. Starting from the juggy edge knocks the '
                  'grade down to V2/3. This route is also known as Flipside.')
Route(name='Spray Skirt',
      parent=book.formations['Undertow'],
      grade=8,
      rating=2,
      description='Sit start with left hand in a slopey dish and right hand on a low side pull. Pull some bizarre moves to gain the "boob holds" at the start of Undertow, continue up and left through a series of heinous crimps. Avoid standing on Silly Steep and Mantle.')
Route(name='Undertow',
      parent=book.formations['Undertow'],
      grade=3,
      rating=3,
      description='Start on two boob shaped slopers at head height. Climb straight up using face holds and the right '
                  'arête.')
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
      rating=2,
      serious=2,
      description='Stand start on the far right side of the boulder using a good left hand sidepull and a bad right hand sidepull, both at head height. Follow the path of least resistance using face holds and a right facing corner to a high top out over a blocky landing.')
Route(name='Car Alarm Traverse',
      parent=book.formations['Car Alarm'],
      grade=2,
      rating=2,
      description='Stand start with hands on an in cut rail at the far left end of the wall. Traverse right to pup truck staying below the lip the whole time. The reverse goes at the same grade.')
Route(name='White Rhino',
      name_unconfirmed=True,
      parent=book.formations['Car Alarm'],
      grade=1,
      rating=1,
      description='Stand start just left of 2 ton Chevy with left hand in a baseball size dish and right hand on the juggy part of a protruding rib. Climb up and left.')
Route(name='2 Ton Chevy',
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
      description='stand start with hands on an under cling at knee height. Using some tricky holds and a good left foot lunge out and left to a jug rail at the lip.')
Route(name='Panic Button',
      name_unconfirmed=True,
      parent=book.formations['Car Alarm'],
      grade=0,
      rating=1,
      description='Stand start just to the left of a rounded corner with feet on a blocky protrusion and not much for hands. Climb up and along the rounded corner.')
Route(name='Meth Lab Project',
      parent=book.formations['Meth Lab'],
      serious=3,
      description='The obvious prow on the front of the Meth Lab boulder has a bolted anchor at the top. Maybe '
                  'someone has top roped it, but who knows. It\'s likely that this has never been climbed by any other '
                  'means. The ethics of climbing this behemoth are contentious but the author of this book holds that it is fair game to '
                  'bolt it as a sport route. If you have the desire to install hardware consider '
                  'figuring the route out on TR first before placing new equipment.')
Route(name='Don\'t Blow the Jug',
      parent=book.formations['Meth Lab'],
      grade='2+',
      rating=2,
      serious=1,
      description='Start at the base of the wide crack. Climb inverted in the off-width until you can make use of a jug to '
                  'squeeze into the crack. Walk through the crack to the far side of the boulder.')
Route(name='Trust Issues',
      parent=book.formations['Meth Lab'],
      serious=2,
      grade='8',
      rating=3,
      FA='Dallas Mulkey',
      description='Sit start at the base of a diagonal crack. Proceed up and left over a subpar landing.')
Route(name='Leave it to Jesus',
      parent=book.formations['Meth Lab'],
      rating=3,
      grade=1,
      description='Also known as Showboat. Start with hands on sloping edges. Use one or two intermediate holds to reposition yourself and make a long pull to the lip. Short but brilliant.')
Route(name='Smackdown',
      parent=book.formations['Meth Lab'],
      rating=2,
      grade=7,
      description='Start standing with left hand either on a gaston or a big undercling gaston and right hand on a jug side pull. Crank some powerful moves on bad feet '
                  'and follow the line of crimps to a top out left.')
Route(name='Heisenburg',
      parent=book.formations['Meth Lab'],
      grade=7,
      grade_unconfirmed=True,
      FA='Matt Slayton',
      description='Start on a blocky jug at the base of a right facing rib. The difficulty of this route has been thought to be anywhere between V6 and V9 depending on beta.')
Route(name='Guillotine',
      name_unconfirmed=True,
      parent=book.formations['Meth Lab'],
      rating=2,
      grade=4,
      description='Start under clinging on the hanging \"Guillotine blade\" flake left of Octernal. Climb straight up.')
Route(name='Octernal',
      parent=book.formations['Meth Lab'],
      rating=3,
      grade=7,
      description='For many this is the local test piece. Start sitting '
                  'with left hand on a sloping triangular rib and right hand on a slopey crimp at the arête. Crank a few hard '
                  'moves to gain the lip then traverse left through a crimp rail to a pumpy top out. Originally known as \"Tom\'s bad trip\".')
Route(name='Two Blows One Stroke',
      parent=book.formations['Meth Lab'],
      grade=6,
      description='Sit start on two single pad edges just to the left of a right facing rib. Pop a left foot onto a '
                  'third  slightly wider edge and crank a few moves to gain a good edge roughly 7ft off the ground. '
                  'From here trend right into a flake.')
Route(name='West Arête',
      parent=book.formations['Meth Lab'],
      grade=0,
      rating=2,
      description='Start on an obvious chest high jug rail and climb the short arête. More fun that it looks.')
Route(name='Southern Discomfort',
      parent=book.formations['Meth Lab'],
      grade=10,
      serious=1,
      rating=2,
      description='With a right hand side pull crimp and left hand under cling, start on a bubbly lump over a rocky pit on the west face of the meth lab boulder. Crank a short travese left and on good in cuts before a poweful vertical finish. A substantial amount of padding is required to protect the pit under the beginning of this route.')
Route(name='Swollen Member',
      parent=book.formations['Swollen Member'],
      grade=3,
      rating=2,
      description='A classic hazing route. Start hugging the underside of the block with good hand holds '
                  'on each side of the stubby prow. Maneuver yourself into a less scandalous orientation using toe '
                  'hooks, heel hooks, and  all manner of dirty tricks.')
Route(name='Phallacy',
      parent=book.formations['Swollen Member'],
      grade='8/9',
      FA='Payton Hansen',
      description='Stand start with your right hand on an in cut sloper around the corner and left on a side pull cutout. Move up the steep face without dabbing. ')
Route(name='Meth Lab Highball',
      parent=book.formations['Meth Lab Highball'],
      rating=2,
      grade=1,
      serious=1,
      description='Stand start with left hand on a slopey ledge and right hand on a diagonal in cut seam. Pull yourself onto the ledge and climb a tenuous slab using a blunt corner for your right hand.')
Route(name='Meth Lab Highball Right',
      parent=book.formations['Meth Lab Highball'],
      rating=1,
      grade=1,
      description='Start as for Meth Lab Highball but pull yourself around the blunt corner into a mossy scoop. Continue right to an easy top out.')
Route(name='Turd Party UR Invited',
      parent=book.formations['Party Boulder'],
      rating=1,
      grade='7/8',
      FA=r'Justin Cheng/Evan Powers',
      description='Stand start with left hand on a sloper and right hand on a thin crimp at the back of a sloper.')
Route(name='Gargoyle',
      name_unconfirmed=True,
      parent=book.formations['E\'s Boulder'],
      rating=2,
      grade=3,
      description='Starts with a low right hand in cut and traverses left across the boulder before circling back '
                  'along the lip before topping out. Sit start on the ramp for style points.')
Route(name='Slam Dunk',
      parent=book.formations['E\'s Boulder'],
      grade=7,
      rating=2,
      description='Sit start with hands matching on a crimp rail on the lower right hand side of a small overhang. '
                  'Pull a few moves into the namesake slam dunk maneuver followed by an easy top out.')
Route(name='E\'s',
      parent=book.formations['E\'s Boulder'],
      grade=7,
      rating=2,
      description='Stand start with hands matched on a head high crimp rail. Pull a few thin moves to a '
                  'big ledge.')
Route(name='Enchilada',
      rating=2,
      parent=book.formations['E\'s Boulder'],
      grade='8/9',
      FA='Griffin Thoms',
      description='Low ball. Sit start with hands matched on a crimp at the lower right of a crescent shaped rail. '
                  'Thrutch your way through a few hard moves to a good jug followed by a \"still on\" top out.')
Route(name='Little Enchilada',
      rating=2,
      parent=book.formations['Little E Boulder'],
      grade=7,
      description='Sit start with left hand on a flat edge and right on a juggy undercling in a cavity at the base of the short vertical face. Some arête slapping and knee bar trickery may be required to gain the flat ledge at the top.')
Route(name='Chillum',
      parent=book.formations['The Bubbler'],
      grade=2,
      rating=1,
      description='Squat start on a a bubbly ledge, pull a few unassuming moves to gain the top. If only it was longer.')
Route(name='The Bubbler',
      parent=book.formations['The Bubbler'],
      grade=6,
      rating=2,
      description='This short boulder is surprisingly hard. Sit start with left hand near the base of big left facing side pull rail and right hand on a cool narrow pinch. This route was originally climbed without using the jug ledge out right, climbing in this style is a fun challenge.')
Route(name='Left Corner',
      parent=book.formations['Bitchin Corners'],
      description='Credible sources claim that the master gardeners of the early 2000\'s era did a line that links the sit start of Bitchin Corners into the upper left arête on the boulder. Looks heinous or morpho or both.'
      )
Route(name='Bitchin Corners',
      grade=2,
      rating=1,
      parent=book.formations['Bitchin Corners'],
      description='Stand start with left hand on a high diagonal crimp and right hand on an arête pinch.'
      )
Route(name='Bitchin Arête',
      grade=6,
      grade_unconfirmed=True,
      parent=book.formations['Bitchin Corners'],
      description='Sit start as for Bitchin Corners sit and climb the right side of the arête.'
      )
Route(name='Frontside Baldo',
      parent=book.formations['Baldo'],
      grade=2,
      rating=2,
      description='Sit start with left hand on a juggy side pull and right hand at the bottom of the diagonal crack. Climb the triangular face using the crack and holds on both arêtes.'
      )
Route(name='Hueco Wabo',
      grade=3,
      grade_unconfirmed=True,
      parent=book.formations['Hueco Wabo'],
      description='Stand start on good side pull under clings pull some rad moves to an insecure, scary top out. '
                  'It\'s possible to bail right at almost any point on this route, but that\'s no fun. A sit start '
                  'might also exist but looks un-fun. Grade unconfirmed.')
Route(name='Crazy Cool Arête',
      parent=book.formations['Crazy Cool'],
      grade=5,
      rating=1,
      description='Sit start straddling the arête with left hand on a shallow ripple and right hand on a single pad edge.')
Route(name='Cargo Net Project',
      grade='?',
      parent=book.formations['Big'],
      description='The big cave on the downhill side of the boulder is just begging to be climbed, unfortunately the landing is really bad.')
Route(name='Mini Hydrotube',
      grade=2,
      serious=2,
      rating=1,
      parent=book.formations['Big'],
      description='Climb the well featured face using holds on both sides of a blunt corner. The top of this is pure choss and more committing than it looks, maybe just do it on TR.')
Route(name='All Berned Down',
      grade=10,
      grade_unconfirmed=True,
      parent=book.formations['Big'],
      description='Starting in the vicinity of All Berned Up and climb straight up the steep face to gain friable holds on the blunt arête. This route and its twin, All Berned Up, have been the source of much confusion over the decades. Credible sources have verified that both routes have been climbed but they have not seen traffic in the recent past.')
Route(name='All Berned Up',
      grade=10,
      grade_unconfirmed=True,
      parent=book.formations['Big'],
      description='Follows a hanging knife flake. Apparently there were multiple holds along both sides of the flake, but '
                  'they all broke off. It\'s unclear if this line has been climbed in it\'s current state.')
Route(name='Slabarific',
      parent=book.formations['Big'],
      grade=1,
      rating=2,
      serious=2,
      description='Climb the left side of the big slab. Be careful most of the rock on this route is suspect. This could also be easily top roped from the bolted anchor at the top of the boulder.')
Route(name='Big Slab Right',
      parent=book.formations['Big'],
      grade=0,
      rating=2,
      serious=1,
      description='Climb the right side of the big slab.')
Route(name='Pockets',
      parent=book.formations['Big'],
      grade=4,
      rating=2,
      serious=1,
      description='Sit start on a good rail just below the angle change. A few hard moves bring you to a long and enjoyable slab.')
Route(name='Classique',
      parent=book.formations['Classique'],
      grade=2,
      rating=1,
      description='Sit start on a chunky ledge. Climb up and left using face holds and the arête. Climbing to the right side of the arête trivializes the route.')
Route(name='Smol',
      name_unconfirmed=True,
      parent=book.formations['Small'],
      grade=2,
      rating=1,
      description='Sit start with left hand on good side pull pod. Right hand on crimp just below the angle change. '
                  'Pull a few bear huggy moves to get on to. Better than it looks.')
Route(name='Tip Toe',
      name_unconfirmed=True,
      parent=book.formations['Small'],
      grade=4,
      rating=1,
      description='Sit start on the far right side of the boulder and traverse the lip topping on the left side. Alternatively you can just grovel straight up from the start at a lower grade.')
Route(name='The Good Slab',
      parent=book.formations['The Good'],
      grade=1,
      rating=2,
      description='Squat start on an in cut flake at knee height. Climb the slab around the corner from The Good.')
Route(name='The Good',
      parent=book.formations['The Good'],
      grade=3,
      rating=2,
      description='Start using any of the holds on the juggy flake on the right side of the boulder\'s downhill face. This route was originally named Psipsina, but was always refereed to as "That V3", then eventually "The Good V3".')
Route(name='Another',
      parent=book.formations['The Good'],
      grade=3,
      rating=1,
      serious=1,
      description='start with opposing side pulls on the center of the boulder\'s downhill face. Traverse to the left '
                  'arête and ascend using delicate feet and un-ideal hands. Mind the uneven landing. Aggressive cleaning has reviled that the dirty ledge to the left of the rock is in fact part of the rock so stepping of here is still on route, but it\'s cooler if you don\'t.')
Route(name='Next to the Good',
      parent=book.formations['Next to the Good'],
      grade=3,
      rating=1,
      serious=1,
      description='Stand start with right hand on a crimp rail under the overhang and left on a high diagonal side pull. A few burly moves give way to a low angle slab. Bailing into the gully instead of climbing the upper slab doesn\'t change the grade, but it is cheating.'
      )
Route(name='From Minnesota with Love',
      parent=book.formations['Next to the Good'],
      grade=3,
      rating=1,
      serious=1,
      description='Stand start with hands on opposed side pulls using the cheater stone below as a foot. A few techy moves gains an airy top out.'
      )
Route(name='Snakes and Martyrs',
      parent=book.formations['Azain Spire'],
      grade=0,
      rating=3,
      description=' Stand start in a juggy seam. Could be scary if you are new to climbing outside.'
      )
Route(name='Ground up Blowie',
      parent=book.formations['Azain'],
      rating=2,
      grade=5,
      description='Start at the base of a diagonal finger crack. Follow the crack around a dabby tree and onto an easy '
                  'slab. This route was named as an homage to the first ascent when the top out was cleaned via '
                  'leaf blower from a stance mid route.')
Route(name='Piranesi',
      parent=book.formations['Azain'],
      grade='6/7',
      FA='Andrew Child',
      rating=2,
      serious=1,
      description='Start as for Ground up Blowie but exit the crack early and climb straight up the tall face. The risk factor of this climb can be mostly diminished with enough pads and good spotters.',
      )
Route(name='Into the Light',
      parent=book.formations['Light Cave'],
      grade=6,
      FA='Eric Brown',
      grade_unconfirmed=True, 
      description='Stand start with your right hand above head height on the juggy part of the arête and left hand a little lower on an under cling. Climb into the light.',
      )
Route(name='Garden Groove',
      parent=book.formations['Azain'],
      grade='5.10b',
      rating=2,
      description='40\', Mixed. 1 bolt. One of the better moderate rope climbs at the garden, this route would see tons more traffic if it were at the cliff. Climb the crack to a bolt protected crux bulge followed by easier climbing to a bolted anchor which may or may not be covered in moss. The crack protects well with a few nuts or cams to 0.75. The section above the crack is much more challenging than it appears from the ground. Take caution some of bolts on this route have a lot of rust.')
Route(name='Sometimes',
      parent=book.formations['Azain'],
      grade=3,
      rating=1,
      description='Starting on Garden Groove traverse right around the corner on reachy holds until you can scramble onto a big ledge over the main trail, drop off. Staying lower in the middle section adds difficulty.')
Route(name='Brontosaurus',
      parent=book.formations['Azain'],
      serious=3,
      FA='Matt Slayton',
      description='Climb the North East corner of the Azain wall to the top of the formation. Be aware that the rock quality at the top of the wall is incredibly poor.')
Route(name='Simpson\'s First',
      parent=book.formations['Azain'],
      grade=0,
      rating=1,
      description='Climb the dirty slab to the left of the locksmith. Fun if you like highballs.')
Route(name='Nightcrawler',
      parent=book.formations['Nightcrawler'],
      grade=10,
      rating=2,
      FA='Jonah Kreitzberg',
      description='Sit start at a juggy under cling on the right arête. Believe it or not this is a completely '
                  'different boulder than Hula.')
Route(name='Locksmith',
      parent=book.formations['Locksmith'],
      grade=4,
      rating=3,
      serious=2,
      description='Also known as Hula. Sit start with a juggy left hand side pull and right hand on an under cling edge. Pull a few '
                  'crimpy moves until you can reach a good hold on the arête. Rock over onto the slab and quest to '
                  'the top. Be sure to clean the upper section before attempting this rig.')
Route(name='Philanthropy',
      parent=book.formations['Locksmith'],
      grade=4,
      rating=1,
      serious=2,
      description='Stand start with wide hands, left on a crimp sloper and right on a crimp side pull. Pull a few '
                  'techy moves to gain good jugs and rock over onto the slab. follow the path of least resistance or '
                  'least moss to the top.')
Route(name='Oregon Arête',
      parent=book.formations['Garden Roof'],
      grade=4,
      rating=2,
      serious=1,
      description='Sit start with left hand on huge side pull and right hand on a shallow crimpy thing on the arête. Crank your way to a no fall zone slab quest top out. This would get tons of traffic if the landing were flat.'
      )
Route(name='Full Stroke',
      parent=book.formations['Garden Roof'],
      grade=2,
      rating=2,
      serious=1,
      description='Stand start on a jug flake. Trend left to a high top in a shallow chimney.'
      )
Route(name='Eurovision',
      parent=book.formations['Garden Roof'],
      grade=2,
      rating=2,
      description='Start as for full stroke and climb up and right along the edge of a flared seam to a big knob. Drop off. A straight up top out probably would go, at the cost of a lot of vegetation.'
      )
Route(name='Garden Project',
      parent=book.formations['Garden Roof'],
      description='Project. Sit start at the base of the low roof and climb into garden variety or Sebulba. Once '
                  'climbed this will be one of the hardest routes in Oregon.')
Route(name='Garden Variety',
      parent=book.formations['Garden Roof'],
      grade=4,
      rating=1,
      description='Use a pad stack to start on high side pulls climb straight up the shallow grove topping in the same place as The Arboretum. The difficulty of this route is probably dependent on how tall you are or how many pads you stack.')
Route(name='The Arboretum',
      parent=book.formations['Garden Roof'],
      grade=11,
      rating=3,
      description='Stand start with left hand on a big under cling and right in a small dish. Climb up and left.')
Route(name='The Other Berned',
      parent=book.formations['Garden Roof'],
      rating=0,
      grade=10,
      grade_unconfirmed=True,
      description='Sit start on small opposing crimps at the far right of the block, climb more or less straight up '
                  'on exfoliating rock. Due to the crumbly nature of the rock its hard to tell what, if anything, '
                  'this ever was. It\'s unclear if this has been climbed in its current state.')
Route(name='Somewhere In-Between',
      parent=book.formations['Gumby Wall'],
      grade=1,
      rating=2,
      description='Climb the narrow chimney. Fun if you\'re into that kind of thing.')
Route(name='The Siren',
      parent=book.formations['Gumby Wall'],
      grade=5,
      rating=3,
      description='Sit start at the base of the prow with one hand on an in cut ledge and the other on the slopey rib below. Climb the prow using a few different beta options. This route is also referred to as Witch Hunt.')
Route(name='Gumby Arête',
      parent=book.formations['Gumby Wall'],
      grade=2,
      rating=2,
      description='Stand start on under clings at the left side of the face. Challenge yourself by staying on the '
                  'arête the whole way up or bail onto the ledge out right and top as for Gumby Slab.', )
Route(name='Gumby Slab',
      parent=book.formations['Gumby Wall'],
      grade=1,
      rating=3,
      description='Stand start in the center of the face. This can be scary if not used to climbing outdoors.', )
Route(name='Gumby Crack',
      parent=book.formations['Gumby Crack'],
      grade=0,
      rating=2,
      description='Climb the well featured wall to the right of Gumby slab from a stand start. Arguably harder than Gumby Slab.', )
Route(name='Chock Stone Highball',
      parent=book.formations['Chock Stone Highball'],
      grade=4,
      grade_unconfirmed=True, )
Route(name='Bubonic Plague',
      parent=book.formations['Bubonic Plague'],
      grade=2,
      rating=2,
      description='Stand start with a blocky hold near the top of a short overhang. Meander your way to the top.', )
Route(name='Headbanger\'s Ball',
      parent=book.formations['Hanging Prow'],
      item_id='Hanging Prow Project',
      FA='Evan Powers',
      grade=8,
      description='Start in compression and pull a few moves along the belly of the prow before working your way right to a sharp top out.', )
Route(name='Geodesic Wiener',
      parent=book.formations['François'],
      grade=3,
      rating=1,
      grade_unconfirmed=True,
      description='start at the bottom of an obvious seam. This has been climbed both as a drop off (ending at the top of the seam) and as a highball (continuing straight up).')
Route(name='Pseudorapidity',
      parent=book.formations['François'],
      grade=6,
      rating=3,
      serious=2,
      FA='Matt Slayton',
      description='Start as for Geodesic Wiener and trend right following a fun variety of holds to a high top out. This route was originally called "Stairway to Heaven"')
Route(name='Schrödinger Project',
      parent=book.formations['François'],
      grade='?',
      description='The sheer wall to the left of François bears a line of faint holds that have been so far unclimbed.')
Route(name='François',
      parent=book.formations['François'],
      grade=3,
      rating=2,
      serious=2,
      grade_unconfirmed=True,
      description='This highball has a storied legacy. It seems that at one point it was a well traveled classic but '
                  'it has since faded into mossy obscurity. Two (very controversial) bolts exist on the face so you '
                  'could climb it as a sport route but based on the amount of visible surface rust you are probably safer over pads.')
Route(name='Shake it Out',
      parent=book.formations['François'],
      item_id='Shake it Out Frank',
      grade=1,
      serious=2,
      rating=2,
      description='Not to be confused with the obscure highball of the same name on the undertow boulder, this obscure highball climbs more like a short J-Tree 5.7 than a boulder. You could protect the crack with nuts and a few cams.')
Route(name='Easy Grandma',
      name_unconfirmed=True,
      parent=book.formations['Scary Grandma'],
      grade=0,
      rating=1,
      description='Squat start on a juggy flake and climb using face holds the arête to a pyramid hold 12ft off the ground.')
Route(name='Angry Mom',
      parent=book.formations['Scary Grandma'],
      grade=2,
      rating=2,
      serious=1,
      description='Stand start over a ledge foot climb left around a flake then veer hard right towards the arête. '
                  'Exciting. Starting on sharp crimps to the right adds variety but doesn\'t feel like a distinct '
                  'route')
Route(name='Scary Grandma',
      parent=book.formations['Scary Grandma'],
      grade=6,
      rating=3,
      serious=2,
      FA='Eric Brown',
      description='An awkward start on a ramp leads to a series of perfect thin crimps followed by a committing crux at the top. Rehearsing the moves on top rope is recommended as falling at the crux would be a bad time.')
Route(name='Fern Sully',
      parent=book.formations['Fern Sully'],
      grade=7,
      rating=1,
      FA='Jonathan Breckheimer',
      description='Squat start with a low left hand under cling and right hand a small single pad crimp. Difficulty eases noticeably after the first move.')
Variation(name='Turtle Traverse',
          parent=book.routes['Leonardo'],
          grade='4',
          rating=2,
          description='Start as for Leonardo, but stay low and traverse left into Raphael Crack. Not quite as contrived as it looks.')
Variation(name='Pure Tonsil',
          parent=book.routes['Tonsil'],
          rating=2,
          grade=6,
          description='Climb tonsil starting in compression on head high slopers without using the boulder below it as a foot. Conditions and body type will play a large role in the experienced difficulty of this climb.')
Variation(name='Prowed',
          parent=book.routes['Tonsil'],
          serious=2,
          description='Climb tonsil but instead of doing the normal top out, continue climbing the steep prow above it. '
                      'Reportedly this was an old school classic.')
Variation(name='Tabor Tots',
          parent=book.routes['Boys in the Woods'],
          grade='?',
          description='Climb boys in the woods, but instead of topping traverse left along the lip of the boulder all the way to the apex on the back side. Also called "A Boy and His Wood". Unclear if this has actually been done before.')
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
                      'stay left on the arête. Authors note: other guides identify several other variations on '
                      'this route, this book intentionally omits other variations in preference of encouraging '
                      'climbers to find their own beta.')
Variation(name='Tyler Durten Dyno',
          parent=book.routes['Project Mayhem'],
          grade='?',
          description='It has been speculated that the dyno from the starting hold straight to the lip will go.')
Variation(name='Spray Against the Undertow',
          parent=book.routes['Undertow'],
          grade=6,
          rating=2,
          description='Sit start as for Spray Skirt, climb into Undertow. This route is also called Dark Crystal.')
Variation(name='Undertow Sit Start',
          parent=book.routes['Undertow'],
          grade=7,
          rating=3,
          description='Sit start left hand on a broken side pull and right '
                      'hand on a low under cling, climb into undertow. At one point this line was simply referred to as '
                      'Undertow, for this book modern naming standards have been conserved.')
Variation(name='Shake it Out',
          parent=book.routes['Simple Math'],
          grade=3,
          rating=1,
          description='Stand start as for Simple Math and climb straight up into riptide.')
Variation(name='EZe',
          parent=book.routes['Cuba Gooding'],
          grade=3,
          rating=1,
          description='Climb Cuba Gooding but use good holds to pull into the scoop and exit early.')
Variation(name='Leave it to Jesus Sit Start',
          parent=book.routes['Leave it to Jesus'],
          grade=7,
          grade_unconfirmed=True,
          description='Sit start on razor crimps to the lower left of the stand start. A key hold has broken on this, but it seems like the moves still go.')
Variation(name='Leave it to Jesus Left',
          parent=book.routes['Leave it to Jesus'],
          grade=10,
          grade_unconfirmed=True,
          description='Sit start as for Trust Issues and traverse right all the way into Leave it to Jesus.')
Variation(name='Learys Lunge',
          parent=book.routes['Heisenburg'],
          grade=9,
          rating=3,
          description='Start as for Heisenburg and dyno up and right to juggy holds at the lip.')
Variation(name='Octernal Direct Exit',
          parent=book.routes['Octernal'],
          grade=7,
          rating=3,
          description='Of all the Octernal exits this one has the most interesting moves. Climb Octernal to the ledge '
                      'then pull some tricky moves to round the right arête. Continue on through a heads up top out.')
Variation(name='Octernal Center Exit',
          parent=book.routes['Octernal'],
          grade='6/7',
          rating=2,
          description='The easiest top option for this boulder involves pulling through a surprisingly good side pull '
                      'above the left end of the ledge. For years this variation lived in moss covered obscurity. '
                      'Climbing it will make you wonder why the awkward pump fest traverse exit is the default line')
Variation(name='Sweet Home Traverse',
          parent=book.routes['Octernal'],
          grade='3/4',
          rating=2,
          description='Climb Octernal from the ledge. Starting one move lower (on the under cling) adds a grade.')
Variation(name='Harbor Freight',
          parent=book.routes['Smackdown'],
          grade=8,
          rating=3,
          FA='Craig Malik',
          description='Sit down start with hands matched on a blocky under cling, climb into Smackdown. This variation was literally '
                      'unearthed when a local climber yarded a large rock out from the landing of Smackdown using a '
                      'chain and come along. The device broke in the process inspiring the name of the route.')
Variation(name='Home Depot',
          parent=book.routes['Smackdown'],
          item_id='Harbor Freight Right Exit',
          grade=8,
          description='Climb Harbor Freight but head right at the top through a slot crimp to finish near the top out for Octernal. Optionally, continue traversing by down climbing the Sweet Home Traverse and finish as for Octernal Direct.')
Variation(name='Enchilada Left Project',
          parent=book.routes['Enchilada'],
          grade='?',
          description='A left exit seems like it might go.')
Variation(name='Enchilada Low Start Project',
          parent=book.routes['Enchilada'],
          grade='?',
          description='Start a few moves to the lower right on a dabby edge.')
Variation(name='E\'s Sit Start Project',
          name_unconfirmed=True,
          parent=book.routes['E\'s'],
          grade='?',
          description='It seems like a low start could go.')
Variation(name='Meth Lab Highball Sit Start',
          name_unconfirmed=True,
          parent=book.routes['Meth Lab Highball'],
          grade=3,
          rating=1,
          description='Sit start with left hand on a diagonal under cling rail and right hand on a low diagonal side pull edge. Doesn\'t add much to the stand start.')
Variation(name='Southern Discomfort Direct',
          parent=book.routes['Southern Discomfort'],
          grade=7,
          rating=2,
          serious=1,
          FA=r'Evan Powers/Michael Gardner-Brown',
          description='Start on a juggy under cling climb into the vertical upper half of Southern Discomfort.' )
Variation(name='Into the Light Assis',
          parent=book.routes['Into the Light'],
          grade=9,
          grade_unconfirmed=True,
          description='Sit start at the base of the arête and link into the stand.'
          )
Variation(name='Gargoyle Direct',
          name_unconfirmed=True,
          parent=book.routes['Gargoyle'],
          rating=2,
          grade=5,
          description='Starts as for Gargoyle but climbs straight up. Harder than it looks')
Variation(name='Layup',
          parent=book.routes['Slam Dunk'],
          grade=4,
          rating=2,
          description='Start as for Slam Dunk but stay low and use good holds out left to avoid the crux.')
Variation(name='Baller',
          parent=book.routes['Slam Dunk'],
          grade=7,
          rating=2,
          description='Start as for Slam Dunk but climb to the right using a far single pad side pull to crank a similar slam dunk maneuver but with opposite hands. This route blurs the line between an eliminate and a variation.')
Variation(name='Chillum Sit',
          parent=book.routes['Chillum'],
          grade=7,
          description='Start as for The Bubbler and climb into Chillum.')
Variation(name='Geodong',
          parent=book.routes['Geodesic Wiener'],
          grade=6,
          rating=2,
          serious=2,
          description='Continue Geodesic Wiener to the top by trending slightly left into a crack system at the top of the boulder.')
Variation(name='Bitchin Corners Sit',
          parent=book.routes['Bitchin Corners'],
          rating=2,
          grade=6,
          description='Sit start with hands matched on a sharp corner at the bottom of the right arête.')
Variation(name='Lower Back Pain Project',
          parent=book.routes['From Minnesota with Love'],
          grade='?',
          description='Climb the route without using the cheater stone.')
Variation(name='Garden Groove Extension',
          parent=book.routes['Garden Groove'],
          grade='5.10b',
          rating=2,
          description='50\', Mixed. 2 bolts. Continue past the first bolted anchor to another bolted anchor at the top of the boulder. Optional walk off.',)
Variation(name='Azain Crack',
          parent=book.routes['Garden Groove'],
          grade=1,
          rating=2,
          description='Climb to the top of the crack then drop off or down climb.',)
Variation(name='Brain Hemorrhage',
          parent=book.routes['Locksmith'],
          grade=7,
          rating=2,
          description='Start as for locksmith and traverse right into philanthropy.',
          grade_unconfirmed=True, )
Variation(name='Dream Weaver',
          parent=book.routes['Full Stroke'],
          grade=2,
          rating=1,
          serious=2,
          description='Start on full stroke, but instead of topping in the shallow grove traverse around the corner and finish on Oregon Arête.',)
Variation(name='Sebulba',
          parent=book.routes['Eurovision'],
          grade=3,
          rating=2,
          serious=1,
          description='climb Eurovision and continue right past the knob on jugs topping out above garden variety. The top is no gimme.'
          )
Variation(name='Arboretum Sit Start',
          parent=book.routes['The Arboretum'],
          grade='?',
          description='Sit Start somewhere in the vicinity of the Other Bearned, somehow link into Arboretum. Legend has it that this was climbed by a Eugene local in the early 2000s at V13. No one knows the name of said mystery crusher.', )
Variation(name='The Siren Stand Start',
          parent=book.routes['The Siren'],
          grade=3,
          rating=2,
          description='Start with your left hand on the left arête and right hand on a good side pull just above the sit '
                      'start holds.', )
Variation(name='Bag of Tricks',
          parent=book.routes['Gumby Slab'],
          grade=3,
          rating=1,
          description='Start as for Siren and traverse right topping on either Gumby Arête or Gumby Slab.')

if __name__ == '__main__':
    sys.exit()
