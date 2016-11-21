
source2 = 'pisa2012.csv'
sourse3 = "MS12student_data.csv"

import csv

result_dict = dict()
result_list = list()

# Pupil performance in mathematics is coded by plausible values & can be found in columns: PV1MATH
data_filter = 'PV1MATH'

# Country name
data_country = 'NC'

with open(source2, 'rb') as csvfile1:
    source_reader = csv.DictReader(csvfile1, delimiter=',', quotechar='"')
   
   
    for row in source_reader:

    	# creating dictionery entry, where the key is a country, and the value is a list of counts for
    	# each level of scores, total number of students from the coutry, and the total of the averages.
        result_dict[row[data_country]] = result_dict.get(row[data_country], [0,0,0,0,0,0,0,0,0])
        result_dict[row[data_country]][8] += 1

        if float(row[data_filter]) > 669.3:
            result_dict[row[data_country]][6] += 1
            result_dict[row[data_country]][7] += float(row[data_filter])

        elif float(row[data_filter])> 607.0:
            result_dict[row[data_country]][5] += 1
            result_dict[row[data_country]][7] += float(row[data_filter])

        elif float(row[data_filter])> 544.7:
            result_dict[row[data_country]][4] += 1
            result_dict[row[data_country]][7] += float(row[data_filter])

        elif float(row[data_filter])> 482.4:
            result_dict[row[data_country]][3] += 1
            result_dict[row[data_country]][7] += float(row[data_filter])

        elif float(row[data_filter]) > 420.1:
            result_dict[row[data_country]][2] += 1
            result_dict[row[data_country]][7] += float(row[data_filter])

        elif float(row[data_filter]) > 357.8:
            result_dict[row[data_country]][1] += 1
            result_dict[row[data_country]][7] += float(row[data_filter])

        else:
            result_dict[row[data_country]][0] += 1 
            result_dict[row[data_country]][7] += float(row[data_filter])
   

with open(sourse3, 'wb') as csvfile3:
    fieldnames = ['Country', 'Below Level 1','Level 1','Level 2','Level 3','Level 4','Level 5','Level 6','Average Score']
    writer = csv.DictWriter(csvfile3, fieldnames = fieldnames, restval="")
    writer.writeheader()

    for key, value in  result_dict.items():
        
        average = value[7] / value[8]
        writer.writerow({'Country': key, 'Below Level 1':value[0],'Level 1':value[1],'Level 2':value[2],'Level 3':value[3],
            'Level 4':value[4],'Level 5':value[5],'Level 6':value[6], 'Average Score': average})


