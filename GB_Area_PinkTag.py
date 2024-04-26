from dataStructure import Area, Subarea, Formation, Route, Variation
from GB_Book import book

Area(name='Pink Tag Boulders',
     parent=book,
     gps='44.43998124232581, -122.57539325959186',
     description='Just across the road from the main area lay a few boulders on the banks of the River. Beware that at high flow rates most of the area will be underwater. Since the River is dam controlled the water level can shift rapidly. Consult '
                 'the USGS flow charts for below green peter damn to know when the river will be low.\n\nSee driving '
                 'directions for the Garden Main area.',)
Subarea(name='',
        item_id='Pink Tag',
        parent=book.areas['Pink Tag Boulders'],
        format_options=['suppress_page_break'])
Formation(name='Pissing Boulder',
          parent=book.subareas['Pink Tag'],
          description='This blunt overhanging corner is the first boulder that you walk by when entering Pink Tag.')
Formation(name='Jonah\'s Dab Rig',
          parent=book.subareas['Pink Tag'],
          description='')
Formation(name='Frat House',
          parent=book.subareas['Pink Tag'],
          description='')
Route(name='Territorial Pissings',
      parent=book.formations['Pissing Boulder'],
      grade=5,
      grade_unconfirmed=True,
      description='Stand start and climb prow. Horrible rock.',)
Route(name='Jonah\'s Dab Rig',
      parent=book.formations['Jonah\'s Dab Rig'],
      grade=9,
      rating=2,
      description='Start standing in compression with left hand on a good side pull and right hand on a blocky sloper, both near eye level. Crank a few powerful moves followed by several dabby moves climbing out of a small hole. Not dabbing is a significant contributor to the overall difficulty.')
Route(name='Frat House',
      parent=book.formations['Frat House'],
      grade=2,
      rating=1,
      serious=2,
      description='Sit start with a juggy left hand side pull and right hand meet hook on the corner of a low protrusion. Pull a few moves in compression before trending right to top over frat mouse. Climbing this with ample padding might re-contextualize the star rating and the seriousness.')
Route(name='Frat Mouse',
      parent=book.formations['Frat House'],
      grade=1,
      rating=0,
      serious=1,
      description='Start on a flexing crack in the broken rock. Climb straight up using opposing side pulls. The landing requires substantial padding to be made safe.')
Route(name='Belushi',
      parent=book.formations['Frat House'],
      grade='5/7',
      rating=2,
      serious=1,
      grade_unconfirmed=True,
      description='Start matched in a threaded jug. Use all manner of trickery to pull the short roof and mantle your way to victory. Be careful even though the meat of this boulder is shorter than your average 8th grader the landing is uneven and swinging off the lip can send you tumbling towards the river (ask me how I know).')
Route(name='Lippity Split',
      parent=book.formations['Frat House'],
      grade=5,
      grade_unconfirmed=True,
      description='Start on the big horn at the far left of the lip and traverse right topping out above Farley Prep.')
Route(name='Le Lemét',
      parent=book.formations['Frat House'],
      grade=9,
      FA='Jonah Kreitzberg',
      grade_unconfirmed=True,
      description='Sit start on jugs in the big pod climb up and right on thin edges.')
Route(name='Farley Prep',
      parent=book.formations['Frat House'],
      grade=9,
      FA='Jonah Kreitzberg',
      grade_unconfirmed=True,
      description='Sit start with left hand on a small under clinging side pull and right hand on a lump on the arête. The lip is right there, how hard could it be?')
Variation(name='Workshop 68',
          parent=book.routes['Jonah\'s Dab Rig'],
          grade=11,
          FA='Jonah Kreitzberg',
          rating=2,
          description='Sit start the dab rig. Begin in compression way under the roof with left hand on either in cut edge and right hand on some marginal nothing. Squeeze out the steep prow.')
Variation(name='Knowledge is Good',
          parent=book.routes['Belushi'],
          grade=7,
          grade_unconfirmed=True,
          description='Start as for Belushi and link into Lippity Split.')
        
      
if __name__ == '__main__':
    sys.exit()        
