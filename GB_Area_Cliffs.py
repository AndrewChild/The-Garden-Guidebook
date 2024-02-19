from dataStructure import Area, Subarea, Formation, Route, Variation
from GB_Book import book

Area(name='Garden Cliffs',
     parent=book,
     gps='44.43998124232581, -122.57539325959186',
     description='Located about 3.7 miles down Quatzville Road from Highway 20, park in a small pull out on the river side of the road or park as for the Garden Main and walk a few hundred yards down the road. The approach trail is located directly across from the parking pull out and can be identified by a stone stairway climbing out of the roadside ditch. Follow the meandering trail a few hundered yards to the Garden Cliff.\n\nThe Garden Cliffs are the premier sport climbing destination of the Sweethome area. Although the extensive cliff face is visible from the road most of the routes at the cliffs were developed much later than the boulders.\n\nTake note that the top of the cliff is not easily accesible and none of the routes in this area can be top roped without leading. The majority of the routes in this area feature high first bolts which were placed with stick clipping in mind. Don\'t fret if you forgot your stick clip at home, a community stick lives at the cliffs and can ususally be found near the entrance to the Garden Cliff.', )
     
     
Subarea(name='The Garden Cliff',
        parent=book.areas['Garden Cliffs'],
        description='The largest of the area\'s cliffs is also conveniently the closest to the road. This cliff features varied climbing at grades rangeing from 5.9 to 5.13- in a variety of stlyes. Many sections of the wall are shaded by large maple trees, which provide some relief in the hotter months. See area description for appoach')
Subarea(name='Fairy Tale Wall',
        parent=book.areas['Garden Cliffs'],
        description='Following the main trail past the Garden Cliff brings you to a second, much smaller cliff.' )
Subarea(name='Cabbage Patch/ Thunderdome',
        description='Even futher down the main trail is a third cliff which hosts a good selection of more moderate climbs.',
        note = 'This area is incomplete. Look forward to more information in future revisions of this book or contribute your own knowledge on github.',
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
          parent=book.subareas['Cabbage Patch/ Thunderdome'],
          description='')
Formation(name='Johny Cash\'s Thunderdome',
          parent=book.subareas['Cabbage Patch/ Thunderdome'],
          description='')
          
          
Route(name='Bonsai',
      parent=book.formations['Garden Cliff Right Side'],
      grade='5.12a',
      grade_unconfirmed=True,
      description='20\', Sport, 2 bolts. Climb a techy dihedral just to the right of a low roof. This could almost be bouldered.',
      )
Route(name='Ladybug',
      parent=book.formations['Garden Cliff Right Side'],
      grade='5.10d',
      rating=1,
      description='25\', Sport, 5 bolts. This bewilderingly difficult climb follows the shallow dihedral just to the right of a tree.',
      )
Route(name='John Henry\'s Hammer',
      parent=book.formations['Garden Cliff Right Side'],
      grade='5.10c/d',
      rating=2,
      FA='Jayson Nissen',
      description='50\', Sport, 6 bolts. Start on a tombstone flake and follow a crack system right before meandering back right and finishing in a short dihedral. This route was originally climbed on gear.',
      )
Route(name='Yggdrasil',
      parent=book.formations['Garden Cliff Right Side'],
      grade='5.11a',
      rating=3,
      FA='Jayson Nissen',
      description='50\', Sport, 6 bolts. Start as for John Henry\'s Hammer, but stay left after the first bolt.',
      )
Route(name='Scorpion Revenge',
      parent=book.formations['Garden Cliff Right Side'],
      grade='5.11b',
      rating=2,
      FA='Micah Klesik',
      description='50\', Sport, 6 bolts. Starts with a few bouldery moves up a left facing ramp then continues through small crimps before some bigger moves on jugs. Many of the crimps on this route have broken and are much smaller than they used to be.',
      )
Route(name='Snug as a Snail',
      parent=book.formations['Garden Cliff Right Side'],
      grade='5.11c',
      rating=2,
      FA='Jayson Nissen',
      description='50\', Sport, 5 bolts. Climbs an obvious flared dihedral before gaining good holds higher up.',
      )
Route(name='Scorpion Hitchhikers Toilet Bowl Odyssey',
      parent=book.formations['Garden Cliff Right Side'],
      grade='5.11b',
      rating=3,
      FA='Jayson Nissen',
      description='50\', Sport, 5 bolts. Starting just left of Snug pull a few jugy moves to gain a left leaning crescent and follow it to an exhillerating dynamic move after the third bolt. After a jug rest continue through another 15\' of pumpy climbing until you gain a no hands rest on a ledge at the top of the wall. Why the anchor is not accessible from this ledge is a mystery a bonus few techy moves leads to a tenuous stance at the anchor.',
      )
Route(name='Daring to Fly',
      parent=book.formations['Garden Cliff Right Side'],
      grade='5.11d',
      rating=3,
      FA='Micah Klesik',
      description='55\', Sport, 7 bolts. Start on the left side of a small cave and climb the aesthtic pillar.',
      )
Route(name='Community',
      parent=book.formations['Garden Cliff Right Side'],
      grade='5.9',
      rating=1,
      FA='Jayson Nissen',
      description='55\', Sport, 7 bolts. Starting in the same alcove as Daring to Fly climb the right facing ramp up and left to a ledgy top. This route has a reputation for being weird and techy not the easiest lead at the grade. There are also several cracks where you could practice gear placements on route.',
      )
Route(name='Blackberry Jam',
      parent=book.formations['Garden Cliff Right Side'],
      grade='5.10-',
      grade_unconfirmed=True,
      FA='Jayson Nissen',
      description='45\', Trad, gear to 3\". Climb a dirty right facing dihedral and link into a less pleasant fist crack up and right. Finishes at a bolted anchor.',
      )
Route(name='Anaphylactic Shock',
      parent=book.formations['Garden Cliff Right Side'],
      grade='5.12a',
      rating=1,
      description='40\', Mixed, 3 bolts and gear to 0.75\". Climb a left leaning crack to an easy mantle at the top of a small roof. Enjoy a no hands rest before a difficult boulder problem at the anchor.',
      )
Route(name='Fight Club (Round Two)',
      parent=book.formations['Garden Cliff Right Side'],
      grade='5.12b',
      rating=3,
      FA='Micah Klesik',
      description='50\', Sport, 7 bolts. Not to be confused with Fight Club (the boulder problem) or Fight Club 2 (the boulder problem), Fight Club Round Two is one of the primeir sport climbing test pieces at the cliffs. Starts on a right facing corner before traversing under the roof until you can grapple your way up to the techy headwall. The crux section of the route is equipped with perma draws, get on it!'
      )
Route(name='Cutting Crack',
      parent=book.formations['Garden Cliff Right Side'],
      grade='5.9',
      rating=1,
      FA='Micah Klesik',
      description='20\', Trad, gear to 2\". Follow a short hand crack until you can clip one of the perma draws for Fight Club. Lower here or continue up.'
      )
Route(name='Butterfly Effect',
      parent=book.formations['Garden Cliff Right Side'],
      grade='5.13a/b',
      FA='Evan Powers',
      description='40\', Sport, 6 bolts. Climbs more or less straight up through a low bolcky ledge followed by thin crimps and a bouldery roof pull. Reportedly climbs like low 5.12 endurance into V7/8 with no rest. The middle of the route is equiped with permas.'
      )
Route(name='Slithering Skink',
      parent=book.formations['Garden Cliff Right Side'],
      grade='5.10d',
      rating=3,
      FA='Jayson Nissen',
      description='40\', Sport, 6 bolts. Start as for butterfly effect but cut left at the blocky ledge and traverse into a big corner. Follow good holds up and overhang and into a techy sequence through a short dihedral.'
      )
Route(name='Stasis Chamber',
      parent=book.formations['Garden Cliff Right Side'],
      grade='5.12b',
      rating=2,
      FA='Andrew Child',
      description='40\', Sport, 6 bolts. Climb a steep prow to the left of the slithering skink corner. After gaining the big ledge rejoin with skink.'
      )
Route(name='Wildlings',
      parent=book.formations['Garden Cliff Right Side'],
      grade='5.11d',
      rating=2,
      FA='Kevin Paurelli',
      description='40\', Sport, 6 bolts. Traverse left under the Stasis chamber prow into a sustained dihedral.'
      )
Route(name='Rain Shadow',
      parent=book.formations['Garden Cliff Right Side'],
      grade='5.11a/b',
      rating=1,
      FA='Jayson Nissen',
      description='30\', Sport, 3 bolts. Pull a few juggy moves through broken rock down low and negotiate a techy dihedral to clip the chains.'
      )
Route(name='Lenticular Cloud Project',
      parent=book.formations['Garden Cliff Right Side'],
      grade='5.?',
      description='Open Project. 40\', Sport, 8 bolts. Start on Rain shadow but traverse left after the second bolt and follow a weakness out the big roof, long slings are required on several bolts to prevent rope drag. A blank section immediately after the roof has foiled all ascent attempts so far. This project has been opend by it\'s developer with the caveat that he requests the FA to name the route \"Lenticular Cloud\".'
      )
Route(name='Vine Project',
      parent=book.formations['Garden Cliff Right Side'],
      grade='5.?',
      description='60\', Sport, 9 bolts. Open Project. Starts on the far end of the rain shadow ledge. This route was bolted and climbed as a dry tooling route, maybe it goes on fingers as well?'
      )
Route(name='Heirloom',
      parent=book.formations['Garden Cliff Middle'],
      grade='5.13c',
      rating=2,
      FA='Evan Powers',
      description='70\', Sport, ? bolts. Climbs an aesthic black arête.'
      )
Route(name='Chimeras',
      parent=book.formations['Garden Cliff Middle'],
      grade='5.13a',
      FA='JD Merritt',
      description='70\', Sport, 9 bolts. CLimb through the middle of a big scoop with a bouldery exit. Ignore the first bolt to prevent rope drag.'
      )
Route(name='Castle Black',
      parent=book.formations['Garden Cliff Middle'],
      grade='5.11a',
      rating=1,
      FA='Kevin Paurelli',
      description='50\', Sport, ? bolts. Originally this was a somewhat bold trad climb, it has since been bolted. Climb the lower cliff band to a right facing corner with a big ledge half way up. This route is baisically a waterfall in the winter and typically doesn\'t dry out until mid summer.'
      )
Route(name='Littlest Birds',
      parent=book.formations['Garden Cliff Middle'],
      grade='5.11b',
      rating=2,
      FA='Jayson Nissen',
      description='70\', Sport, 9 bolts. Start on Castle Black and cut right after the midway ledge. A techy sequence leads to sustained clibing up a well featured pillar.'
      )
Route(name='Seraphim Nachash',
      parent=book.formations['Garden Cliff Middle'],
      grade='5.11b/c',
      rating=3,
      FA='Jayson Nissen',
      description='70\', Sport, 10 bolts. Easy moves lead to a no hands rest on a ledge at the top of the lower cliffband. From here pull a crux seqence climbing into a corner followed by a long section of power endurance on good holds.'
      )
Route(name='My Empire of Dirt',
      parent=book.formations['Garden Cliff Middle'],
      grade='5.12b',
      rating=3,
      FA='Jayson Nissen',
      description='70\', Sport, 11 bolts. Climb Seraphim Nachash through its crux then cut left through a physical section of sidepulls and underclings. Continue up a sustained overhaing wall with big pulls between generally decent holds. This is a real power endurance testpiece.'
      )
Route(name='Honeycomb Project',
      parent=book.formations['Garden Cliff Left Side'],
      grade='5.?',
      description='50\', Sport, 9 bolts. Open Project. Start on a narrow ledge to the right of the top of the stairs. The section down low has so far never been climbed.'
      )
Route(name='Criss Cross Applesauce',
      parent=book.formations['Garden Cliff Left Side'],
      grade='5.11c',
      rating=2,
      FA='Kerstin Cullen',
      description='45\', Sport, 8 bolts. Start at the top of the stairs. After clipping the third bolt follow a jug rail up and right to hard to decipher crux at the end of a pumpy sequence. Climbing eases substantially after the crux.'
      )
Route(name='Vandals in the Graveyard',
      parent=book.formations['Garden Cliff Left Side'],
      grade='5.12a',
      rating=1,
      FA='Chris Nord',
      description='45\', Sport, 5 bolts. Start on Criss Cross Applesauce but continue straight up after the 3rd bolt. After a short bouldery sequence gain a left facing ramp and follow easy terrain back to the chains of Criss Cross Apple Sauce.',
      )
Route(name='Ovulation Send-sation',
      parent=book.formations['Garden Cliff Left Side'],
      grade='5.12a',
      rating=2,
      FA='Kerstin Cullen',
      description='45\', Sport, 6 bolts. Technical climbing leads small holds and pockets off of a low ledge. Joins Fertile crescent after the 4th bolt before a tricky roof pull to gain the anchor.',
      )
Route(name='Fertile Crescent',
      parent=book.formations['Garden Cliff Left Side'],
      grade='5.12a',
      rating=3,
      FA='Jayson Nissen',
      description='45\', Sport, 6 bolts. Climb the large left facing crescent feature until you join with Ovulation after the fourth bolt.',
      )
Route(name='My Secret Garden',
      parent=book.formations['Garden Cliff Left Side'],
      grade='5.11a',
      rating=3,
      FA='Jayson Nissen',
      description='45\', Sport, 6 bolts. Start on a big sloping rail and pull a few moves to reach good edges and manuver your way under a hanging block. Crank some big moves to get up and around the block onto easier terrain.',
      )
Route(name='Nest',
      parent=book.formations['Garden Cliff Left Side'],
      grade='5.10c',
      rating=2,
      FA=r'Kerstin Cullen/Jayson Nissen',
      description='45\', Sport, 6 bolts. Start in a little corner just left of My Secret Garden, Climb more or less straight up. Technical.',
      )
Route(name='A Garden Called Peace',
      parent=book.formations['Garden Cliff Left Side'],
      grade='5.10a',
      rating=3,
      FA=r'Kerstin Cullen/Jayson Nissen',
      description='45\', Sport, 6 bolts. Layback up a huge flake then find a good rest before pulling the crux at a little roof bulge. Take caution multiple people have sprained their ankle falling after the 3rd bolt, a hard catch from an attentive belayer will keep you from hitting the ledge below.',
      )
Route(name='Hive',
      parent=book.formations['Garden Cliff Left Side'],
      grade='5.10c',
      rating=1,
      FA='Jayson Nissen',
      description='50\', Sport, 9 bolts. Hard moves down low are followed by a good rest and a meandering path which climbs both sides of a leaning tower.',
      )
Route(name='Baba Yaga',
      parent=book.formations['Fairy Tale Wall'],
      grade='5.9',
      rating=1,
      FA='Kerstin Cullen',
      description='20\', Sport, 4 bolts. Climbing eases up after a few hard moves down low.',
      )
Route(name='Death of Koschei the Deathless',
      parent=book.formations['Fairy Tale Wall'],
      grade='5.11a',
      rating=1,
      FA='Jayson Nissen',
      description='20\', Sport, 4 bolts. Easy climbing surrounds a one move crux deadpoint.',
      )
Route(name='Feather of the Finest Falcon',
      parent=book.formations['Fairy Tale Wall'],
      grade='5.8',
      rating=1,
      FA='Jayson Nissen',
      description='25\', Sport, 4 bolts. A series of blocky ledges leads to a short but sweet wall.',
      )
Route(name='Fee-Fi-Fo-Fum',
      parent=book.formations['Fairy Tale Wall'],
      grade='5.10c',
      rating=2,
      FA='Jayson Nissen',
      description='25\', Sport, 5 bolts. Follow a technical slab to a cruxy pull on a bulgy protrusion.',
      )
Route(name='Don\'t Forget the Nooch',
      parent=book.formations['Cabbage Patch'],
      grade='5.4',
      FA='Jayson Nissen',
      grade_unconfirmed=True,
      )
Route(name='Tabouli',
      parent=book.formations['Cabbage Patch'],
      grade='5.7',
      FA='Jayson Nissen',
      grade_unconfirmed=True,
      )
Route(name='Babaganoush',
      parent=book.formations['Cabbage Patch'],
      grade='5.10b',
      FA='Mike Gunnels',
      grade_unconfirmed=True,
      )
Route(name='Kim Chi Corner',
      parent=book.formations['Cabbage Patch'],
      grade='5.11a',
      FA='Jayson Nissen',
      grade_unconfirmed=True,
      )
Route(name='Where Do You Go When the Sun Goes Down',
      parent=book.formations['Johny Cash\'s Thunderdome'],
      grade='5.11a',
      FA='Jayson Nissen',
      grade_unconfirmed=True,
      description='45\', Sport, 8 bolts. Follow a shallow right facing corner to a ledge, then trend left and up over a large detatched flake.'
      )
Route(name='I Dropped a Man in Reno',
      parent=book.formations['Johny Cash\'s Thunderdome'],
      grade='5.7',
      FA='Jayson Nissen',
      grade_unconfirmed=True,
      description='45\', Sport, 11 bolts. Start on the right side of a large flake. Traverse right along a shallow ledge (crossing over Where Do You Go When the Sun Goes Down) to a grove and follow it to the top.'
      )
Route(name='I Fell for You Like a Child',
      parent=book.formations['Johny Cash\'s Thunderdome'],
      grade='5.8',
      rating=2,
      FA='Jayson Nissen',
      description='35\', Sport, 6 bolts. Start on the right side of a large flake. From a stance at the top of the flake trend slightly right, off of the flake before continuing up through small pods.'
      )
Route(name='I Will Let You Down',
      parent=book.formations['Johny Cash\'s Thunderdome'],
      grade='5.6',
      rating=2,
      FA='Jayson Nissen',
      description='35\', Sport, 6 bolts. Climb the center of the large flake then continue up the right face of a low angle corner.',
      )
Route(name='A Million Dollars of Good',
      parent=book.formations['Johny Cash\'s Thunderdome'],
      grade='5.8',
      rating=2,
      FA='Jayson Nissen',
      description='35\', Sport, 7/6 bolts. Climb the left corner of the large flake before pulling onto a technical slab. Alternatively you can start as for I Will Let You Down and clip a connnector bolt as you walk across the top of the flake skipping the first two bolts. This route would get full stars if the rock quality were better.'
      )
Route(name='Stop Once to Wipe the Sweat Away',
      parent=book.formations['Johny Cash\'s Thunderdome'],
      grade='5.10a',
      rating=1,
      FA='Jayson Nissen',
      description='30\', Sport, 5 bolts. Start to the left of the large flake. A short sequence of difficult vertical climbing guards an enjoyable slab. This route is currently severly overgrown.'
      )
      
      
Variation(name='John to Snug Linkup',
          parent=book.routes['John Henry\'s Hammer'],
          grade='5.10c/d',
          rating=2,
          FA='Jayson Nissen',
          description='50\', Sport, 5 bolts. Start on John Henry\'s Hammer and trend diagonal left throught the broken section of rock linking into Snug as a Snail. Links the easiest sections of every route to the top of the wall.'
          )
Variation(name='Lazarus',
          parent=book.routes['Stasis Chamber'],
          grade='5.12c',
          rating=2,
          FA='Andrew Child',
          description='40\', Sport, 6 bolts. Climb Stasis to the ledge then instead of rolling onto the ledge traverse left around the corner and link into the finish of Wildlings.'
          )
Variation(name='Heirloom Left Project',
          parent=book.routes['Heirloom'],
          grade='5.?',
          description='The original line of the Heirloom project stays left when the Heirloom boltline veers right at the top.'
          )
Variation(name='Ovulation Send-sation Extension',
          parent=book.routes['Ovulation Send-sation'],
          grade='5.12a',
          grade_unconfirmed=True,
          description='A two bolt extension takes this climb or its neighbor from a ledge to the top of the cliff. Probably doesn\'t change the grade.'
          )
Variation(name='Honeycomb Traverse',
          parent=book.routes['Honeycomb Project'],
          grade='5.12a',
          rating=2,
          FA='Jayson Nissen',
          description='50\', Sport, 9 bolts. Start on Criss Cross Apple Sauce and traverse into Honeycomb after the third bolt. Avoids the blank section down low.'
          )
Variation(name='A Victem of the Times',
          parent=book.routes['Where Do You Go When the Sun Goes Down'],
          grade='5.10c',
          FA='Jayson Nissen',
      grade_unconfirmed=True,
          description='45\', Sport, 8 bolts. Start on Where Do You Go When the Sun Goes Down and link into the top of I dropped a Man in Reno.'
          )


if __name__ == '__main__':
    sys.exit()
