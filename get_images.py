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
    pg_num = image.split('_')
    
    # don't include dot files
    if len(pg_num) > 2:
        pg_num = int(pg_num[2])

    # nested for loop's not great. Is there a better way to do this?
    for directory in directories:
        # ex 'Calochortus_venustus_pg_457'
        pg_num_dir = directory.split('_')
        pg_num_dir = int(pg_num_dir[-1])
        copy_dir = os.path.join(working_dir, directory)
        
        if (pg_num == pg_num_dir) and os.path.isdir(copy_dir) and os.path.isfile(image):
            new_image_name = os.path.join(copy_dir, image)
            copyfile(image, new_image_name)

