#!/usr/bin/env python3

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

# read the input file
with open(args.input_file, 'r') as input_file:
    input_data = input_file.read()
    # print(input_data)
    # input_lines = input_data.splitlines()
    page_number = 0
    for item in input_data:
        if input_data == page_delimiter:
            out_file = open(f'break_pg_{page_number}', 'w')
        elif input_data != page_delimiter:
            print(page_number)
            out_file.write(input_data)
        page_number += 1
        if page_number == 5:
            quit()
            
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