import csv
import re

csv_file_path = ('/Users/abc/Desktop/CF-BRSR-equities-25-Dec-2023.csv')

with open(csv_file_path, 'r') as file:
    csv_reader = csv.reader(file)
    #for pdf
    desired_column_pdf = 3
    column_values_pdf = []
    #for xbrl
    desired_column_xbrl = 4
    column_values_xbrl = []
    for row in csv_reader:
        if len(row) > desired_column_pdf:
            column_values_pdf.append(row[desired_column_pdf])
        if len(row) > desired_column_xbrl:
            column_values_xbrl.append(row[desired_column_xbrl])
        

column_values_pdf = list(filter(lambda x: x != 'https://nsearchives.nseindia.com/corporate/null', column_values_pdf))
file_name = []
for name_xbrl in column_values_xbrl:
    file_name.append(re.search(r'[^/]+$', name_xbrl).group())




