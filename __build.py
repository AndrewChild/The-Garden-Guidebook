import sys
import time
sys.path.insert(1, '../LocalBoulders')
from data.GB_Book import book
from data.GB_Area_Main import *
from data.GB_Area_PinkTag import *
from data.GB_Area_Cliffs import *
from data.GB_Area_Upper import *
from data.GB_Area_ClearCut import *
from data.GB_Area_Quartz import *
from data.GB_Area_Other import *
from images.GB_Images_high_priority import *
from images.GB_Images_Main import *
from images.GB_Images_PinkTag import *
from images.GB_Images_Cliffs import *
from images.GB_Images_Upper import *
from images.GB_Images_ClearCut import *
from images.GB_Images_Quartz import *
from images.GB_Images_Other import *
from images.GB_Images_low_priority import *
from images.GB_Inserts import *


if __name__ == '__main__':
    # Record the start time
    start_time = time.perf_counter()
    book.file_name = 'guideBook_print'
    book.format_options.append('blank_page_after_title')
    book.format_options.append('no_image_rotation')
    book.update()
    book.gen()
    book.format_options.remove('blank_page_after_title')
    book.format_options.remove('no_image_rotation')
    book.format_options.append('skip_action_photos')
    book.format_options.append('skip_text_inserts')
    book.file_name = 'guideBook'
    book.gen()

    with open('missing_info.txt', 'w') as f:
        f.write('----Formations with no gps----\n')
        for formation in book.formations.values():
            if not formation.gps and formation.name:
                f.write(formation.name+'\n')

        f.write('\n----climbs with no description----\n')
        for climb in book.climbs.values():
            if not climb.description or 'PLACEHOLDER' in climb.description:
                f.write(climb.name+'\n')

        f.write('\n----climbs with no rating----\n')
        for climb in book.climbs.values():
            if climb.rating == -1 and 'Project' not in climb.name:
                f.write(climb.name+'\n')

        f.write('\n----climbs with no topo----\n')
        for climb in book.climbs.values():
            if not climb.hasTopo:
                f.write(climb.name+'\n')

    elapsed_time = time.perf_counter() - start_time
    print(f"Elapsed time: {elapsed_time:.4f} seconds")