import sys
sys.path.insert(1, '../LocalBoulders')
from dataStructure import Area, Subarea, Formation, Route, Variation
from GB_Book import book


Area(name='Pink Tag Boulders',
     parent=book,
     gps='44.43998124232581, -122.57539325959186',
     incomplete=True,
     description='Just across the road from the main area lay a few boulders on the banks of the River. Beware the '
                 'water level can rise quickly blocking off access to some of the boulders in this area. Consult '
                 'the USGS flow charts for below green peter damn to know when the river will be low. See driving '
                 'directions for the Garden Main area.',)
Subarea(name='',
        item_id='Pink Tag',
        parent=book.areas['Pink Tag Boulders'],)
        
      
if __name__ == '__main__':
    sys.exit()        