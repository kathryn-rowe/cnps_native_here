#!/usr/bin/env python3

'''
Iterate through directory of native plant images that were extracted from a PDF.

python3 get_images.py --output-dir plant_species_text_img/ -i images/
'''

import os
import argparse
from shutil import copyfile

# parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("-o", "--output-dir", required=True, help="output directory")
parser.add_argument("-i", "--image-dir", required=True, help="image directory")

args = parser.parse_args()

parent_directory = os.getcwd()

working_dir = os.path.join(parent_directory, args.output_dir)
os.chdir(working_dir)
directories = os.listdir(working_dir)


image_dir = os.path.join(parent_directory, args.image_dir)
os.chdir(image_dir)
images = os.listdir(image_dir)

# parsing through the images leads to better results
# since multiple images can belong to the same directory
for image in images:
    # ex 'NativePlants2020_Page_204_Image_0002.jpg'
    # ['NativePlants2020', 'Page', '204', 'Image', '0002.jpg']
    pg_num = image.split('_')
    try:
        picture_number, file_type = pg_num[-1].split('.')
    except:
        pass
    
    # don't include dot files
    if len(pg_num) > 2:
        pg_num = int(pg_num[2])

    # nested for loop's not great. Is there a better way to do this?
    for directory in directories:
        # ex 'Calochortus_venustus_pg_457'
        directory_name_split = directory.split('-')
        # ['Corylus', 'cornuta', 'subsp', 'californica', 'pg', '83']

        # page numbers don't match exactly
        pg_num_of_directory = int(directory_name_split[-1]) + 2
        copy_dir = os.path.join(working_dir, directory)
        
        if (pg_num == pg_num_of_directory) and os.path.isdir(copy_dir) and os.path.isfile(image):
            # Heterotheca-sessiliflora-subsp-echioides-2.jpg
            new_image_name = ('-').join(directory_name_split[0:-2]) + "-" + picture_number[-1] + "." + file_type
            # print(new_image_name)
            new_image_name_path = os.path.join(copy_dir, new_image_name)
            copyfile(image, new_image_name_path)

