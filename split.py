#!/usr/bin/env python3

'''
Iterate through text file that was translated from PDF.

python3 split.py -i new_test.txt --output-dir test_texts/
'''

import os
import argparse

# global settings
start_delimiter = '©'
end_delimiter = '©'
page_delimiter = ''

# parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input-file", required=True, help="input filename")
parser.add_argument("-o", "--output-dir", required=True, help="output directory")

args = parser.parse_args()

# if the given output directory does not exist, make it
if not os.path.isdir(args.output_dir):
    os.mkdir(args.output_dir)
current_directory = os.getcwd()
working_dir = os.path.join(current_directory, args.output_dir)

# read the input file
with open(args.input_file, 'r') as input_file:
    input_data = input_file.read()

    # split pages by special character
    single_page = input_data.split(page_delimiter)

    page_number = 0
    for item in single_page:
        
        # base directory where every species is stored
        os.chdir(working_dir)

        single_page_list = item.splitlines(0)
        
        # ignore empty pages
        if len(single_page_list) > 0:
            # remove leading and trailing whitespace
            new = [ i.strip() for i in single_page_list ]

            # remove empty spaces
            new = list(filter(None, new))

            # remove first item in list if it's obviously not a plant name
            def remove_non_species(text_lst):
                if len(text_lst[0]) >= 100 or text_lst[0][0:5] in ['Photo', 'Main ', 'Flowe', ',    ', 
                                                                   'Right', 'Seed ', 'Weber', 'Wild ',
                                                                   'Leave', 'Leaf_', '(cid:']:
                    text_lst = text_lst[1:]
                    text_lst = remove_non_species(text_lst)
                    return text_lst
                else:
                    return text_lst

            new = remove_non_species(new)

            # some plant names contain brackets. remove them for easier directory access
            # replace spaces with underscores for file and directory snake case
            plant_name = ''
            for char in new[0]:
                if char != '[' and char != ']': 
                    if char == ' ':
                        char = '_'
                    plant_name = plant_name + char

            # change to directory
            species_dir = plant_name + f"_pg_{page_number}" 
            os.mkdir(species_dir)
            os.chdir(species_dir)

            # save file with species name. first item in page list
            species_file = f'{plant_name}_pg_{page_number}.txt'
            out_file = open(species_file, 'w')
            out_file.write(str(new))
            out_file.close()
            page_number += 1

            
# # iterate through the input data by line
# input_lines = input_data.splitlines()
# while input_lines:
#     # discard lines until the next start delimiter
#     while input_lines and not input_lines[0].startswith(start_delimiter):
#         input_lines.pop(0)

#     # corner case: no delimiter found and no more lines left
#     if not input_lines:
#         break
#     print(input_lines)
#     # extract the output filename from the start delimiter
#     output_filename = input_lines.pop(0).replace(start_delimiter, "").strip()
#     output_path = os.path.join(args.output_dir, output_filename)