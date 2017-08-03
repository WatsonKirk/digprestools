import csv
from lxml import etree
from shutil import copyfile, move,copy
import os
from template import fill_template, dc_template
import datetime
import time
import hashlib

# read input
csv_file = 'transfer.csv'

def file_hash(filename):
	h = hashlib.sha1()
	with open(filename, 'rb', buffering=0) as f:
		for b in iter(lambda : f.read(128*1024), b''):
			h.update(b)
	return h.hexdigest()

with open(csv_file, 'rb') as csvfile:
	rows = csv.DictReader(csvfile)
	batch = ""
	#batch_dict = {}
	file_list = []
	first_row_dict = {}
	dt = datetime.datetime.now()
	now = time.mktime(dt.timetuple())
	for row in rows:
		if batch != row['batch']:
			# write the template???
			if batch != "":
				#template = fill_template(first_row_dict, file_list)
			
				file_list = []
				batch = row['batch']
				first_row_dict = row
			#batch_dict[batch] = {}
			#batch_dict[batch]['files'] = []
			#batch_dict[batch]['']
			
			# str(now) is included for debugging
			directory = str(now) +row['filename'].replace('.tif', '') 
			if not os.path.exists(directory):
				os.makedirs(directory + '/content/streams/')
			new_file = directory + '/content/ie.xml'
			dc_file = directory + '/dc.xml'
			dc_template_string = dc_template(row)
			with open(dc_file, 'w') as output_file:
				output_file.write(dc_template_string)

		input_file = '../tifs/' +row['filename']
		#sha = file_hash(input_file)
		#file_list.append([input_file, sha])

		template = fill_template(row)
		#move('../tifs/' +row['filename'], directory + '/content/streams')
		copy(input_file, directory + '/content/streams')
       	with open(new_file, 'w') as output_file:
          	output_file.write(template)
