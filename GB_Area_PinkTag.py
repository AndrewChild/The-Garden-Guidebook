import sys
sys.path.insert(1, '../LocalBoulders')
from dataStructure import Area, Subarea, Formation, Route, Variation
from GB_Book import book


Area(name='Pink Tag Boulders',
     parent=book,
     gps='44.43998124232581, -122.57539325959186',
     incomplete=True,
     description='Just across the road from the main area lay a few boulders on the banks of the River. Beware at very high cfs most of the area will be underwater. Since the River is dam controlled the water level can shift rapidy. Consult '
                 'the USGS flow charts for below green peter damn to know when the river will be low. See driving '
                 'directions for the Garden Main area.',)
Subarea(name='',
        item_id='Pink Tag',
        parent=book.areas['Pink Tag Boulders'],)
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
      grade_unconfirmed=True,)
Route(name='Jonah\'s Dab Rig',
      parent=book.formations['Jonah\'s Dab Rig'],
      grade=9,
      rating=2,)
Route(name='Frat House',
      parent=book.formations['Frat House'],
      grade=2,
      grade_unconfirmed=True,)
Route(name='Frat Mouse',
      parent=book.formations['Frat House'],
      grade=1,
      grade_unconfirmed=True,)
Route(name='Belushi',
      parent=book.formations['Frat House'],
      grade=5,
      grade_unconfirmed=True,)
Route(name='Lippity Split',
      parent=book.formations['Frat House'],
      grade=5,
      grade_unconfirmed=True,)
Route(name='Le Lemét',
      parent=book.formations['Frat House'],
      grade=9,
      FA='Jonah Kreitzberg',
      grade_unconfirmed=True,)
Route(name='Farley Prep',
      parent=book.formations['Frat House'],
      grade=9,
      FA='Cooper Doe and Jonah Kreitzberg',
      grade_unconfirmed=True,)
Variation(name='Workshop 68',
          parent=book.routes['Jonah\'s Dab Rig'],
          grade=11,
          FA='Jonah Kreitzberg',
          grade_unconfirmed=True,)
Variation(name='Knowledge is Good',
          parent=book.routes['Farley Prep'],
          grade=7,
          grade_unconfirmed=True,)
        
      
if __name__ == '__main__':
    sys.exit()        