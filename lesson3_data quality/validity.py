"""
Your task is to check the "productionStartYear" of the DBPedia autos datafile for valid values.
The following things should be done:
- check if the field "productionStartYear" contains a year
- check if the year is in range 1886-2014
- convert the value of the field to be just a year (not full datetime)
- the rest of the fields and values should stay the same
- if the value of the field is a valid year in the range as described above,
  write that line to the output_good file
- if the value of the field is not a valid year as described above, 
  write that line to the output_bad file
- discard rows (neither write to good nor bad) if the URI is not from dbpedia.org
- you should use the provided way of reading and writing data (DictReader and DictWriter)
  They will take care of dealing with the header.

You can write helper functions for checking the data and writing the files, but we will call only the 
'process_file' with 3 arguments (inputfile, output_good, output_bad).
"""
import csv
import pprint
import re

INPUT_FILE = 'autos.csv'
OUTPUT_GOOD = 'autos-valid.csv'
OUTPUT_BAD = 'FIXME-autos.csv'

def process_file(input_file, output_good, output_bad):

    with open(input_file, "r") as f,open(output_good, "w") as g,open(output_bad, "w") as x:
        reader = csv.DictReader(f)
        header = reader.fieldnames
        
        goodwriter = csv.DictWriter(g, delimiter=",", fieldnames= header)
        goodwriter.writeheader()
       
        badwriter = csv.DictWriter(x, delimiter=",", fieldnames= header)
        badwriter.writeheader()
        
        for row in reader:
            tocheck=row['productionStartYear']
            URI=row['URI']
            if row['URI'].find('dbpedia.org')>-1:
                try:
                    row['productionStartYear'] = int(row['productionStartYear'][:4])
                    if row['productionStartYear'] in range(1886,2014):
                        goodwriter.writerow(row)
                    else:
                        badwriter.writerow(row)
                except ValueError: 
                    badwriter.writerow(row)

def test():

    process_file(INPUT_FILE, OUTPUT_GOOD, OUTPUT_BAD)


if __name__ == "__main__":
    test()