# 1a. Collecting COVID-19 data from a Github repository and parsing the data elements into a csv file
import requests, csv
url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv'
res = requests.get(url)
content = res.content.decode('iso-8859-1')
f = open('covid_data.csv', "w", newline ='')
f.write("")
f.close()


f = open('covid_data.csv', "a", newline ='')
writer = csv.writer(f, delimiter = ',', lineterminator ='\n')
for row in csv.reader(content.splitlines()):
    writer.writerow(row)
f.close()

# Overviewing the colleced COVID-19 morbidity data file
n=0
with open('covid_data.csv', 'r') as f:
    reader = csv.reader(f)
    for line in reader:
        print(line)
        if n>5:
            break
        n+=1
# 1b. Collecting distance data from the webportal of National Bureau of Economic Research
# Overviewing the downloaded distance data
with open ('distance_data.csv', 'r') as f:
    i=0
    for line in f:
        print (line)
        if i>3:
            break
        i+=1

# 1c. Collecting NY state population data by web-scraping
# Fetching NY state population data by web scraping

import requests
url = 'https://www.newyork-demographics.com/counties_by_population'

r = requests.get(url)
text =r.text
county_names=[]
county_populations=[]
data = text.split("\n")
n=0
for line in data:
        if '-demographics">'in line: # This is an example of some 'detective' works needed to fetch required data
            county_names.append(line.split('">')[1].replace('</a>',''))
        elif ',' in line:
            if '      ' in line:
                county_populations.append(line.replace(' ', ''))# Removing all extra spaces

#print(td[2])
'''
for c in text:
    td = text.split("<td>")
    county = td[2]
    population = td[3]
    print(county[:-23].split(">")[1])
    print(population[7:22])
'''

#print(len(td))
#print(td[2:3])
#print(county[:-23].split(">")[1].)
#print(population[7:22])

# 1d. Creating a csv file containing population data
import csv
population_dict = {county_names[i]: county_populations[i] for i in range(len(county_names))}
header = ["county", "population"]

with open('population_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for k,v in population_dict.items():
        writer.writerow([k,v])
 # Checking the popilation CSV file
 import csv
n=0

with open ('population_data.csv', 'r') as f:
    reader = csv.reader(f)

    for row in reader:
        print(row)
        if n>5:
            break
# Making a dictionary with county names as keys and populations as values
population_dict = {county_names[i]: county_populations[i] for i in range(len(county_names))}

#2a. Filtering the morbidity data and creating a new file with the filtered data
# Filtering data and  making a new csv file with only New York county data from the imported csv
import csv

f2 = open('covid_data_filtered.csv', "w", newline ='')
f2.write("")
f2.close()


f2 = open('covid_data_filtered.csv', "a", newline ='')

writer = csv.writer(f2, delimiter = ',', lineterminator ='\n')

with open ('covid_data.csv', 'r') as f1:
    reader = csv.reader(f1)

    for row in reader:
        if 'date' in row:
            writer.writerow(row)
        elif (row[2]) == 'New York':
            #print(row)
            writer.writerow(row)

f2.close()


# checking the filtered data file
n=0
with open('covid_data_filtered.csv', 'r') as f:
    reader = csv.reader(f)
    for line in reader:
        print(line)
        if n>5:
            break
        n+=1

# 2b. Filtering the county distance data and creating a new file with the filtered data
# It was observed that the all fips codes of NY state counties started with '36'
import csv

f2 = open('distance_data_filtered.csv', "w")
f2.write("")
f2.close()


f2 = open('distance_data_filtered.csv', "a")

writer = csv.writer(f2, delimiter = ',', lineterminator ='\n')

with open ('distance_data.csv', 'r') as f1:
    reader = csv.reader(f1)

    for row in reader:
        if row[0][:2] =='36'and row[2][:2]=='36':
            writer.writerow(row)

f2.close()

# checking the filtered data file
with open ('distance_data_filtered.csv', 'r') as f:
    i=0
    for line in f:
        print (line)
        if i>3:
            break
        i+=1


# 2c. Checking the NY state county names 'collected' by the scraping
print(county_names)


# 1. Final checking of the content before sending to the database
import csv
n1=0
n2=0
n3=0

with open ('distance_data_filtered.csv', 'r') as f1:
    reader1 = csv.reader(f1)
    for row1 in reader1:
        print(row1)
        if n1>4:
            break
        n1+=1


with open ('covid_data_filtered.csv', 'r') as f2:
    reader2 = csv.reader(f2)
    for row2 in reader2:
        print(row2)
        if n2>4:
            break
        n2+=1

with open ('population_data.csv', 'r') as f3:
    reader3 = csv.reader(f3)
    for row3 in reader3:
        print(row3)
        if n3>4:
            break
        n3+=1
# 3b. Connecting clarkson database
import pymysql
conn = pymysql.connect(host='mysql.clarksonmsda.org', \
                       port=3306, \
                       user='******', \
                       passwd='********', \
                       db='maitryj_FinalProject_IA626', autocommit=True)
cur = conn.cursor(pymysql.cursors.DictCursor)

# Constructing SQL for creating 3 tables in database (one for each of the data files)

CREATE TABLE IF NOT EXISTS `nycovidcase` (
  `caseid` int(5) NOT NULL AUTO_INCREMENT,
  `date` date,
  `county` varchar(25),
  `state` varchar(25),
  `fips` varchar(10),
  `cases` int(5),
  `death` int(5),
   PRIMARY KEY (`caseid`)
)


CREATE TABLE IF NOT EXISTS `nypopulation` (
    `populationid` int(5) NOT NULL AUTO_INCREMENT,
    `county` varchar(25),
    `population` int(10),
    PRIMARY KEY (`populationid`)
)


)

CREATE TABLE IF NOT EXISTS `nydistance` (
  `distanceid` int(5) NOT NULL AUTO_INCREMENT,
   `fips1` varchar(10),
  `distance` int(4),
  `fips2` varchar(10),
   PRIMARY KEY (`distanceid`)
)


# Creating Table nycovidcase

cur.execute('''

CREATE TABLE IF NOT EXISTS `nycovidcase` (
  `caseid` int(5) NOT NULL AUTO_INCREMENT,
  `date` date,

  `county` varchar(25),
  `state` varchar(25),
  `fips` varchar(10),
  `cases` int(5),
  `death` int(5),
   PRIMARY KEY (`caseid`)
);
''')
# Creating Table nydistance
cur.execute('''

CREATE TABLE IF NOT EXISTS `nydistance` (
  `distanceid` int(5) NOT NULL AUTO_INCREMENT,
   `fips1` varchar(10),
  `distance` float(4),
  `fips2` varchar(10),
   PRIMARY KEY (`distanceid`)
);
''')

# Creating Table nypopulation
cur.execute('''

CREATE TABLE IF NOT EXISTS `nypopulation` (
  `populationid` int(5) NOT NULL AUTO_INCREMENT,
   `county` varchar(25),
  `population` int(10),
   PRIMARY KEY (`populationid`)
);
''')

 # 4a. Checking covid_data_filtered.csv as a list of dictionary before inserting rows into database table
 with open('covid_data_filtered.csv') as f:
    data = [{k: str(v) for k, v in row.items()}
        for row in csv.DictReader(f, skipinitialspace=True)]
    print(data[0:3])

# 4b. Inserting rows into nycovidcase by utilizing 'block size' concept
import pymysql,csv,time,datetime
# Inserting rows (in blocks, for faster operations) from csv into database table

sql = '''
INSERT INTO `nycovidcase`
(
`date`, `county`,`state`,`fips`,
`cases`,`death`
)
 VALUES (%s,%s,%s,%s,%s,%s);
 '''

tokens =[]
n= 0
i=0
blocksizes = [4000]

for bs in blocksizes:
    start = time.time()


    for line in data:
        tokens.append((line["date"],
                  line["county"],
                  line["state"],
                  line["fips"],
                  line["cases"],
                  line["deaths"]))
        if i % bs == 0:
            n+=1
            bstart = time.time()
            cur.executemany(sql,tokens)
            conn.commit()
            tokens = []
        i+=1
    print ("block size: " + str(bs) + " - total time : " + str(time.time() - start))
    if len(tokens) > 0:
        cur.executemany(sql,tokens)
        conn.commit()

cur.close()
# 4c. preparing 'data' object(a list of dictionary) for inserting rows into the corresponding database table

with open('covid_data_filtered.csv') as f:
    data = [{k: str(v) for k, v in row.items()}
        for row in csv.DictReader(f, skipinitialspace=True)]
    #print(data[0], '\n')



# 4c. Checking distance_data_filtered.csv as a list of dictionary before inserting rows into database table
# Checking csv content as a list of dictionary before inserting them into database table
import csv
c=0
with open('distance_data_filtered.csv') as f:
    data = [{k: str(v) for k, v in row.items()}
        for row in csv.DictReader(f, skipinitialspace=True)]
    print(data[0:3])

# Inserting rows into nycdistance
conn = pymysql.connect(host='mysql.clarksonmsda.org', \
                       port=3306, \
                       user='******', \
                       passwd='********', \
                       db='maitryj_FinalProject_IA626', autocommit=True)
cur = conn.cursor(pymysql.cursors.DictCursor)

import pymysql,csv,time,datetime

#4c. preparing 'data' object(a list of dictionary) for inserting rows into the corresponding database table

c=0
with open('distance_data_filtered.csv') as f:
    data = [{k: str(v) for k, v in row.items()}
        for row in csv.DictReader(f, skipinitialspace=True)]
    # print(data[0], '\n')


# 4d. Inserting rows (in blocks, for faster operations) from csv into database table
sql = '''
INSERT INTO `nydistance`
(
`fips1`, `distance`,`fips2`
)
 VALUES (%s,%s,%s);
 '''

tokens =[]
n= 0
i=0
blocksizes = [400]

for bs in blocksizes:
    start = time.time()


    for line in data:
        tokens.append((line["fips1"],
                  line["distance"],
                  line["fips2"]))
        if i % bs == 0:
            n+=1
            bstart = time.time()
            cur.executemany(sql,tokens)
            conn.commit()
            tokens = []
        i+=1
    print ("block size: " + str(bs) + " - total time : " + str(time.time() - start))
    if len(tokens) > 0:
        cur.executemany(sql,tokens)
        conn.commit()

cur.close()
# 4e. Checking distance_data_filtered.csv as a list of dictionary before inserting rows into database table
# Checking csv content as a list of dictionary before inserting them into database table
with open('population_data.csv') as f:
    data = [{k: str(v) for k, v in row.items()}
        for row in csv.DictReader(f, skipinitialspace=True)]
    print(data[0:3])

# 4f. Inserting rows into nypopulation
conn = pymysql.connect(host='mysql.clarksonmsda.org', \
                       port=3306, \
                       user='******', \
                       passwd='********', \
                       db='maitryj_FinalProject_IA626', autocommit=True)
cur = conn.cursor(pymysql.cursors.DictCursor)

import pymysql,csv,time,datetime

# preparing 'data' object(a list of dictionary) for inserting rows into the corresponding database table

c=0
with open('population_data.csv') as f:
    data = [{k: str(v) for k, v in row.items()}
        for row in csv.DictReader(f, skipinitialspace=True)]
    # print(data[0], '\n')


# Inserting rows (in blocks, for faster operations) from csv into database table

sql = '''
INSERT INTO `nypopulation`
(
 `county`,`population`
)
 VALUES (%s,%s)
 '''

tokens =[]
n= 0
i=0
blocksizes = [20]

for bs in blocksizes:
    start = time.time()


    for line in data:
        tokens.append((line["county"],
                  line["population"]))
        if i % bs == 0:
            n+=1
            bstart = time.time()
            cur.executemany(sql,tokens)
            conn.commit()
            tokens = []
        i+=1
    print ("block size: " + str(bs) + " - total time : " + str(time.time() - start))
    if len(tokens) > 0:
        cur.executemany(sql,tokens)
        conn.commit()

cur.close()
# Connecting clarkson database
import pymysql
conn = pymysql.connect(host='mysql.clarksonmsda.org', \
                       port=3306, \
                       user='******', \
                       passwd='********', \
                       db='maitryj_FinalProject_IA626', autocommit=True)
cur = conn.cursor(pymysql.cursors.DictCursor)

 # Making a function for executing sql commands
def execute_sql(sql):
    '''Fetches(from a database) the result of the given sql command.
       Establishing the database connection and ccursor as 'cur' is a prerequisite'''
    cur.execute(sql)
    result = cur.fetchall()
    return result

# Checking distance data with function definition
execute_sql('''SELECT * FROM nydistance LIMIT 5''')

#  Checking population data with function definition
execute_sql('''SELECT * FROM `nycovidcase`limit 5''')

# Calculating infection rate
sexecute_sql('''SELECT c.county, d.distance as Distance_From_Manhattan, c.cases as Total_Case_On_Nov13_2020, p.population, c.cases/p.population*100 as Infection_Rate

FROM nycovidcase c, nydistance d, nypopulation p

WHERE d.fips1 = '36061'

AND d.fips2 = c.fips

AND p.county = c.county

AND c.date = '2020-11-13'
LIMIT 5
''')

#Making a view table with the fields joined from 3 tables
execute_sql(''' CREATE VIEW Infection_Rate_Vs_Distance_2020_11_13 AS

SELECT c.county, d.distance as Distance_From_Manhattan, c.cases as Total_Case_On_Nov13_2020, p.population, c.cases/p.population*100 as Infection_Rate

FROM nycovidcase c, nydistance d, nypopulation p

WHERE d.fips1 = '36061'

AND d.fips2 = c.fips

AND p.county = c.county

AND c.date = '2020-11-13';

''')
#Overviewing the Infection_Rate_Vs_Distance_2020_11_13.csv imported from database
import csv
n=0
with open('Infection_Rate_Vs_Distance_2020_11_13.csv', 'r') as f:
    reader = csv.reader(f)

    for line in reader:
        print(line)
        if n>5:
            break
        n+=1
# Making the plot
import matplotlib.pyplot as plt
import csv
distance_from_Manhattan, infection_rate  = [], []
n=0
with open('Infection_Rate_Vs_Distance_2020_11_13.csv') as csv_file:
    reader = csv.reader(csv_file)

    for column in reader:
        if n>0:
            distance_from_Manhattan.append(float(column[1]))
            infection_rate.append(float(column[2]))
        n+=1
plt.scatter(distance_from_Manhattan, infection_rate)

plt.xlabel("Distance from Manhattan (Miles)")
plt.ylabel("COVID Infection Percentage *10,000")
# Finding the Pearson's coefficient and testing its statistical significance at a 95% level
test_level_percentage = 95

alpha = 1-test_level_percentage/100

from scipy.stats import pearsonr
stat, p = pearsonr(distance_from_Manhattan, infection_rate)
print('stat=%.3f, p=%.3f' % (stat, p))
if p > alpha:
    print('No significant dependancy')
else:
    print('The coorelation is statistically significant at a '+ str(test_level_percentage)+'% '+'confidence level')
