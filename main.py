import csv
from lxml import etree
from shutil import copyfile, move
import os
from template import fill_template, dc_template

# read input
csv_file = 'transfer.csv'

with open(csv_file, 'rb') as csvfile:
    rows = csv.DictReader(csvfile)
    for row in rows:
        # first file
        directory = row['filename'].replace('.pdf', '') 
        
        if not os.path.exists(directory):
            os.makedirs(directory + '/content/streams/')

        shutil.move('../pdfs/' +directory + '.pdf', directory + '/content/streams')
        new_file = directory + '/content/ie.xml'
        template = fill_template(row)

        dc_file = directory + '/dc.xml'
        dc_template_string = dc_template(row)

        with open(new_file, 'w') as output_file:
            output_file.write(template)

        with open(dc_file, 'w') as output_file:
            output_file.write(dc_template_string)
