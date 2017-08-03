import csv, sys, datetime
from shutil import copyfile, move
import os
from template import fill_template, dc_template

#check for arguments
if len(sys.argv) < 3:
    print("Please pass the input csv as the first argument and the output dir as the second argument")
    print("Example:\n\tpython main.py \"example/1/inputs/xml/transfer.csv\" \"example/1/outputs\"")
    sys.exit(1)

input_csv  = sys.argv[1]
input_dir  = os.path.dirname(input_csv)
output_dir = sys.argv[2]
output_dir = output_dir + "/" + datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

with open(input_csv, 'rb') as csvfile:
    rows = csv.DictReader(csvfile)
    for row in rows:
        # first file
        directory = output_dir
        
        if not os.path.exists(directory):
            os.makedirs(directory + '/content/streams/')

        copyfile( input_dir + '/../tifs/' + row['filename'], directory + '/content/streams/' + row['filename'])
        new_file = directory + '/content/ie.xml'
        ie_template_string = fill_template(row)

        dc_file = directory + '/dc.xml'
        dc_template_string = dc_template(row)

        with open(new_file, 'w') as output_file:
            output_file.write(ie_template_string)

        with open(dc_file, 'w') as output_file:
            output_file.write(dc_template_string)
