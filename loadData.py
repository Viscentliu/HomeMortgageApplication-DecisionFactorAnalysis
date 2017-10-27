import csv

RAW_DATA_PATH = 'data/ny_hmda_2015_raw.CSV'


def viewDataCSV(path):
	with open(path, 'rb') as csvfile:
		spamreader = csv.reader(csvfile)
		possible_action = dict()
		for row in spamreader:
			if row[1] not in possible_action:
				possible_action[row[1]] = 1
			else:
				possible_action[row[1]] += 1
		for item in possible_action:
			print item, possible_action[item]

viewDataCSV(RAW_DATA_PATH)