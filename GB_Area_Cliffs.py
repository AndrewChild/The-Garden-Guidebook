import sys
sys.path.insert(1, '../LocalBoulders')
from dataStructure import Area, Subarea, Formation, Route, Variation
from GB_Book import book


Area(name='Garden Cliffs',
     parent=book,
     gps='44.43998124232581, -122.57539325959186',
     incomplete=True,
     description='PLACEHOLDER',)
Subarea(name='',
        item_id='Cliffs',
        parent=book.areas['Garden Cliffs'],)
        

if __name__ == '__main__':
    sys.exit()        