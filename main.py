import csv, sys, datetime
import pprint
from itertools import groupby
from shutil import copyfile, move
import os
from template import ie_template, dc_template

def main():
    input_csv, input_dir, output_dir = check_arguments()

    with open(input_csv, 'rb') as csvfile:
        rows = csv.DictReader(csvfile)

        batches = get_batches(rows)

        for i in batches:
            batch = batches[i]

            directory = output_dir + "/batch" + str(i)
            if not os.path.exists(directory):
                os.makedirs(directory + '/content/streams/')

            new_file = directory + '/content/ie.xml'
            ie_template_string = ie_template(batch)

            dc_file = directory + '/dc.xml'
            dc_template_string = dc_template(batch)

            with open(new_file, 'w') as output_file:
                output_file.write(ie_template_string)

            with open(dc_file, 'w') as output_file:
                output_file.write(dc_template_string)

            for row in batch:
                copyfile( input_dir + '/../files/' + row['filename'], directory + '/content/streams/' + row['filename'])


def check_arguments():
    # check for arguments
    if len(sys.argv) < 3:
        print("Please pass the input csv as the first argument and the output dir as the second argument")
        print("Example:\n\tpython main.py \"example/1/inputs/scripts/transfer.csv\" \"example/1/outputs\"")
        sys.exit(1)
    input_csv = sys.argv[1]
    if not os.path.exists(input_csv):
        print(input_csv + " does not exist")
        sys.exit(1)

    input_dir = os.path.dirname(os.path.realpath(input_csv))
    output_dir = sys.argv[2]
    output_dir = output_dir + "/" + datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    return input_csv, input_dir, output_dir


def get_batches(rows):
    batches = {}
    for k, g in groupby(rows, lambda x: x['batch']):
        batches[k] = []
        for i in g:
            batches[k].append(i)

    return batches

if __name__ == "__main__":
    main()
