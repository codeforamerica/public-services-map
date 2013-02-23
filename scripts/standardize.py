import csv
import json

# example usage: 
# from standardize import output_to_csv
# output_to_csv("/Users/richa/cfa/public-services-map/data/OaklandUnifiedSchools.csv","/Users/richa/cfa/public-services-map/data/output.csv", indices = [1, 3, 2], headers = ["type", "name", "address"])

def clean(string):
	return string.replace("'", '').replace('"', '').strip()


def convert_to_csv(file_out, json_file):
	outfile = csv.writer(open(file_out, "w"))
	# outfile.writerow(headers)
	json_raw = open(json_file).readlines()
	json_object = json.loads(json_raw[0])
	for record in json_object:
		strings = []
		fields = []
		for f in record:
			fields.append(f)
		for field in fields:
			strings.append(record[field])
		print strings
		outfile.writerow(strings)

def the_basics(data, indices = None, delimiter = ","):
	data.next()
	for row in data:
		try:
			basics = []
			row = row.split(delimiter)
			if indices:
				for index in indices:
					basics.append(clean(row[index]))
			else: # Get first column
				basics.append(clean(row[0]))
			yield basics
		except:
			pass

def output_to_csv(file_in, file_out, indices = None, headers = None):
	outfile = csv.writer(open(file_out, "w"))
	outfile.writerow(headers)
	for record in the_basics(open(file_in, "r"), indices):
		outfile.writerow(record)

