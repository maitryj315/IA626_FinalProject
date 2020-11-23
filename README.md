# IA626_FinalProject


                                          IA 626 Final Project
                       Title-Exploring correlation between COVID-19 morbidity rate in the counties of New York state
                        and distances of the counties from New York city.
                                        November 22, 2020
                                        Submitted by - Jeenat Maitry

![logo.jpg](attachment:logo.jpg)

## Part A: Data acquisition
Data sources
For this project, necessary data were collected from the following 3 sources:

1.Github repository (Daily Covid-19 morbidity)(https://github.com/nytimes/covid-19-data)<br>
2.National Bureau of Economic Research (County Distance Database)(https://www.nber.org/research/data/county-distance-database)
<br>3.New York Demographics (Population in different counties of New York state)(https://www.newyork-demographics.com/)
<br> The process flow for this project explains it in a small scale:

![ProcessFlow_V1.png](attachment:ProcessFlow_V1.png)

                            Figure: Process flow of the project explaining various steps
1a. COVID-19 data was acquired from the GitHub repository with get request to the website. Then parsing of the data elements  was done into a csv file called covid_data.csv. Then inspection of the data was done, following table has some data as an example:

| date | county | state |fips | cases | deaths |
| --- | --- | --- | --- | --- | --- |
| 2020-01-21 | Snohomish | Washington | 53061 | 1 | 0 |
| --- | --- | --- | --- | --- | --- |
| 2020-01-22 | Snohomish | Washington | 53061 | 1 | 0 |
| --- | --- | --- | --- | --- | --- |
| 2020-01-23 | Snohomish | Washington | 53061 | 1 | 0 |
| --- | --- | --- | --- | --- | --- |
| 2020-01-24 | Cook | Illinois |17031 | 1 | 0 |
| --- | --- | --- | --- | --- | --- |
| 2020-01-24 | Snohomish | Washington | 53061 | 1 | 0 |
| --- | --- | --- | --- | --- | --- |
| 2020-01-25 | Orange | California | 06059 | 1 | 0 |

                            Table: showing some of the extracted COVID-19 data

1b.Collecting distance data from the web portal of National Bureau of Economic Research<br> As we are dealing with the New York state county data only and the maximum distance was less than 400 miles from the epicenter of the COVID-19 disease, which is New York City. Here for the sake of the analysis only New York county that is Manhattan city was considered as the center. So, the file which contained counties within 500 miles distance was our target file.
The required CSV file (2010 census data) was directly downloaded from https://www.nber.org/research/data/county-distance-database by clicking on the link given in the web portal (Link url: https://data.nber.org/distance/2010/sf1/county/sf12010countydistancemiles.csv.zip )

zip file was downloaded thereby and when extracted, it revealed the following csv: sf12010countydistancemiles.csv

The extracted file was renamed as 'distance_data.csv' and it was moved to the directory that contains this notebook.
Overviewing the downloaded distance data with python, it was observed that distance among each of the counties of the USA are given here; hence the file is large. So, I decided to make a smaller file by filtering some data (to keep only New York state counties). Following table shows some data as an example.


|county1 |   county2| mi_to_county |
| --- | --- | --- |
| 01001 | 01021 | 22.4629943022086 |
| --- | --- | --- |
| 01001 | 01085 | 26.8446865669988 |
| --- | --- | --- |
| 01001 | 01051 | 29.5175849409829 |
| --- | --- | --- |
| 01001 | 01047 | 30.7763708418057 |

                                     Table: showing some of the extracted distance data
1c.Collecting NY state population data by web-scraping<br>
From the NY state demographic website NY state population data were fetched by web scraping.
```
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
```
1d. Creating a csv file containing population data<br>
New csv file called population_data.csv contained the population data of the New York state counties. Then the CSV file which contained the population data were inspected making a dictionary with county names as keys and populations as values and here  some of the data shown.

```
population_dict = {county_names[i]: county_populations[i] for i in range(len(county_names))}

```

| county | population |
| --- | --- |
| Kings | 2559903 |
| --- | --- |
| Queens | 2253858 |
| --- | --- |
| New York | 1628706 |
| --- | --- |
| Suffolk | 1476601 |
| --- | --- |
| Bronx | 1418207 |
| --- | --- |
| Nassau | 1356924 |


                                     Table: showing some of the extracted population data


2a. Filtering the morbidity data and creating a new file with the filtered data
The file contained all the county data of the United States. So, data was filtered and a new csv file called covid_data_filtered.csv was created which contained only New York state county data.
Here are some of the data.

| date | county | state |fips | cases | deaths |
| --- | --- | --- | --- | --- | --- |
| 2020-03-01 | New York | New York | 36061 | 1 | 0 |
| --- | --- | --- | --- | --- | --- |
| 2020-03-02 | New York | New York | 36061 | 1 | 0 |
| --- | --- | --- | --- | --- | --- |
| 2020-03-03 | New York | New York | 36061 | 2 | 0 |
| --- | --- | --- | --- | --- | --- |
| 2020-03-04 | New York | New York | 36061 | 2 | 0 |
| --- | --- | --- | --- | --- | --- |
| 2020-03-04 | Westchester | New York | 36119 | 9 | 0 |
| --- | --- | --- | --- | --- | --- |
| 2020-03-05| Nassau | New York | 36059 | 1 | 0 |

                                     Table: showing some of the extracted NY state county data

2b. Filtering the county distance data and creating a new file with the filtered data<br>
It was observed that the all fips code of NY state counties started with '36'which is the state code.
checking the filtered data file further subsection was done based on state code '36' and the file was named as distance_data_filtered.csv.


|county1 |   county2| mi_to_county |
| --- | --- | --- |
| 36001 | 36093 | 16.2301528273665 |
| --- | --- | --- |
| 36001 | 36039 | 22.6607026010004 |
| --- | --- | --- |
| 36001 | 36095 | 23.611569815475 |
| --- | --- | --- |
| 36001 | 36083 | 24.8616219873773 |
| --- | --- | --- |
| 36001 | 36021 | 29.4495615480702 |


                                     Table: showing some of the extracted NY state county distance data


2c. Checking the NY state county names 'collected' by the web scraping<br> New York State has 62 counties and by web scraping got the county names.

|county_name |   county_name |  county_name | county_name |
| --- | --- | --- | --- |
| Kings County | Queens County | New York County | Otsego County |
| --- | --- | --- | --- |
| Suffolk County | Bronx County| Nassau County | Columbia County |
| --- | --- | --- | --- |
| Westchester County | Erie County | Monroe County | Genesee County |
| --- | --- | --- | --- |
| Richmond County | Onondaga County | Orange County | Fulton County |
| --- | --- | --- | --- |
| Rockland County | Albany County | Dutchess County | Franklin County |
| --- | --- | --- | --- |
| Saratoga County | Oneida County | Niagara County | Montgomery County |
| --- | --- | --- | --- |
| Broome County | Ulster County | Rensselaer County | Tioga County |
| --- | --- | --- | --- |
| Schenectady County | Chautauqua County | Oswego County | Cortland County |
| --- | --- | --- | --- |
| Jefferson County | Ontario County | St. Lawrence County | Chenango County |
| --- | --- | --- | --- |
| Tompkins County | Putnam County | Steuben County | Greene County |
| --- | --- | --- | --- |
| Wayne County | Chemung County | Clinton County | Allegany County |
| --- | --- | --- | --- |
| Cayuga County | Cattaraugus County | Sullivan County | Madison County |
| --- | --- | --- | --- |
| Warren County |Livingston County | Herkimer County | Washington County |
| --- | --- | --- | --- |
| Delaware County | Orleans County | Wyoming County | Essex County |
| --- | --- | --- | --- |
| Seneca County | Schoharie County | Lewis County | Yates County |
| --- | --- | --- | --- |
| Schuyler County | Hamilton County | --- | --- |

                                     Table: showing NY state county names

![map%20of%20New%20York.png](attachment:map%20of%20New%20York.png)

                                     Figure: showing NY state counties in a map

 NY city comprises of Brooklyn (Kings County), Bronx (Bronx County), Manhattan (New York County), Queens (Queens County) and Staten Island (Richmond County). All of these 5 counties considered together as New York city. As the whole city was equally affected, we would not consider the counties of the city.

3.Transferring data to a relational database<br>
Joining and filtering data can be easily done by SQL queries if we have data in a relational database. So, we are now transferring the csv files as three tables in a MySQL database

The following csv files were transferred to a MySQL database (hosted by Clarkson MSDA)<br>

'distance_data_filtered.csv'<br>
'covid_data_filtered.csv'<br>
'population_data.csv'<br>

We'll name the database table respectively as following:<br>
nydistance<br>
nycovidcase<br>
nypopulation<br>

## Part B: Building the database

3a. Final checking of the content before sending to the database


|fips1 |   fips2| distance in mile |
| --- | --- | --- |
| 36001 | 36093| 16.23015283 |
| --- | --- | --- |
| 36001 | 36039 | 22.6607026 |
| --- | --- | --- |
| 36001 | 36095 | 23.6115698 |
| --- | --- | --- |
| 36001 | 36083 | 24.86162199 |
| --- | --- | --- |
| 36001 | 36021 | 29.44956155 |

                                 Table: Checking NY state distance data before inserting into database

| date | county | state |fips | cases | deaths |
| --- | --- | --- | --- | --- | --- |
| 2020-03-01 | New York | New York | 36061 | 1 | 0 |
| --- | --- | --- | --- | --- | --- |
| 2020-03-02 | New York | New York | 36061 | 1 | 0 |
| --- | --- | --- | --- | --- | --- |
| 2020-03-03 | New York | New York | 36061 | 2 | 0 |
| --- | --- | --- | --- | --- | --- |
| 2020-03-04 | New York | New York | 36061 | 2 | 0 |
| --- | --- | --- | --- | --- | --- |
| 2020-03-04 | Westchester | New York | 36119 | 9 | 0 |
| --- | --- | --- | --- | --- | --- |
| 2020-03-05| Nassau | New York | 36059 | 1 | 0 |

                                   Table: checking COVID-19 data before inserting into database


| county | population |
| --- | --- |
| Kings | 2559903 |
| --- | --- |
| Queens | 2253858 |
| --- | --- |
| New York | 1628706 |
| --- | --- |
| Suffolk | 1476601 |
| --- | --- |
| Bronx | 1418207 |
| --- | --- |
| Nassau | 1356924 |


                                    Table: checking NY state population data before inserting into database




3b.Following steps were followed to build the database
![Database_stages.png](attachment:Database_stages.png)


                                    Figure: Steps to follow in database

<br>i. Establishing Connection with Clarkson database
<br>ii. Creating tables in database
<br>iii. Inserting data in nycovidcase table
<br>iv. Inserting data in nydistance table
<br>v. Inserting data in nypopulation table

Constructing SQL for creating 3 tables in database (one for each of the data files)
```
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
```



![database.png](attachment:database.png)

                                    Figure: Database showing 3 tables



4a. Checking covid_data_filtered.csv as a list of dictionary before inserting rows into database table.

| key | value |
| --- | --- |
| date | 2020-03-01 |
| --- | --- |
| county | New York |
| --- | --- |
| state | New York |
| --- | --- |
| fips | 36061 |
| --- | --- |
| cases | 1 |
| --- | --- |
| deaths | 0 |

                                Table: checking COVID-19 data before inserting into database as key value pair


4b. Inserting rows into nycovidcase table by utilizing 'block size' concept
Although the csv files here are not too large, still using this concept of sending data in chunks for the sake of a'good practice' so that the codes remain scalable for large data sets.

block size: 4000 - total time : 1.1710128784179688

![database%20table.png](attachment:database%20table.png)

                                Figure: Some COVID-19 data in the database


4c. Checking distance_data_filtered.csv as a list of dictionary before inserting rows into database table


| key | value |
| --- | --- |
| fips1 | 36001 |
| --- | --- |
| distance | 16.23015283 |
| --- | --- |
| fips2 |36093 |

                    Table: checking distance data before inserting into database as key value pair


4d. Inserting rows into nycdistance table
block size: 400 - total time : 0.5940568447113037


4e. Checking population_data_filtered.csv as a list of dictionary before inserting rows into database table

| key | value |
| --- | --- |
| county | Kings |
| --- | --- |
| population| 2559903 |
| --- | --- |
| county |Queens |
| --- | --- |
| population| 2253858 |
| --- | --- |
| county | New York |
| --- | --- |
| population | 1628706 |

                            Table: checking population data before inserting into database as key value pair

4f. Inserting rows into nypopulation table

block size: 20 - total time : 0.16524147987365723
Combining Data using SQL

For answering the research question (Is there any relation between COVID-19 infection rate with different New York State counties and their distance from New York City?), We need to join the following three tables:

<br>nycovidcase
<br>nydistance
<br>nypopulation

We'll filter out the following information in a combined (joined) view table

From table 1 : the number of total case <br>From table 2 : the distance of each county from Manhattan, NYC <br>From table 3 : population of each county (to determine the Rate of infection among the population in each county)

<br>a.Connecting clarkson database
<br>b.Checking population data

Making a function for executing sql commands<br>Fetches(from a connected database) the result of the given sql command
        which should be written in between triple quotes.
       Establishing the database connection and cursor as 'cur' is a prerequisite
```
def execute_sql(sql):
    cur.execute(sql)
    result = cur.fetchall()
    return result
```
Checking function to fetch data from nydistance table
```
execute_sql('''SELECT * FROM nydistance LIMIT 5''')

```
executing sql command returns the following result.

| distanceid | 1 | fips1 | 36013 | distance | 359.0 | fips2 | 36103 |
| --- | --- | --- | --- | --- | --- |--- | --- |
| distanceid | 2 | fips1 | 36103 | distance | 359.0 | fips2 | 36103 |
| --- | --- | --- | --- | --- | --- |--- | --- |
| distanceid | 3 | fips1 | 36063 | distance | 359.0 | fips2 | 36103 |
| --- | --- | --- | --- | --- | --- |--- | --- |
| distanceid | 4 | fips1 | 36103 | distance | 357.0 | fips2 | 36063 |
| --- | --- | --- | --- | --- | --- |--- | --- |
| distanceid | 5 | fips1 | 36029 | distance | 357.0 | fips2 | 36063 |

                        Table: checking distance data using function definition named execute_sql

Checking population data
 ```
 execute_sql('''SELECT * FROM `nypopulation`limit 5''')

```


| populationid | 1 | county | Kings | population | 2559903 |
| --- | --- | --- | --- | --- | --- |
| populationid | 2 | county | Queens | population | 2253858 |
| --- | --- | --- | --- | --- | --- |
| populationid | 3 | county | New York | population | 1628706 |
| --- | --- | --- | --- | --- | --- |
| populationid | 4 | county | Suffolk | population | 1476601|
| --- | --- | --- | --- | --- | --- |
| populationid | 5 | county | Bronx | population | 1418207 |

                        Table: checking population data using function definition named execute_sql

# Part C: Answering the research question
We wanted to know whether there is any relation between the COVID infection rate among the population of the NY state counties and their distance from the New York City. We collected the required data, transferred them to a database, made a new table with the required fields and imported back the table as a CSV. Now we can do the 'analytic' operations to find out the answer.
Checking COVID case data
```
execute_sql('''SELECT * FROM `nycovidcase`limit 5''')
```
| caseid | 1 | date | datetime.date(2020, 3, 1) | county | New York | state | New York | fips | 36061 | cases| 1 | death | 0 |
| --- | --- | --- | --- | --- | --- |--- | --- | --- | --- | --- | --- |--- | --- |
| caseid | 2 | date | datetime.date(2020, 3, 2) | county | New York |state | New York | fips | 36061 | cases | 1 | death | 0 |
| --- | --- | --- | --- | --- | --- |--- | --- | --- | --- | --- | --- |--- | --- |
| caseid | 3 | date | datetime.date(2020, 3, 3) | county | New York | state | New York | fips | 36061 | cases | 2 | death | 0 |
| --- | --- | --- | --- | --- | --- |--- | --- | --- | --- | --- | --- |--- | --- |
| caseid | 4 | date | datetime.date(2020, 3, 4) | county | New York  |state | New York | fips | 36061 | cases | 2 | death | 0 |
| --- | --- | --- | --- | --- | --- |--- | --- | --- | --- | --- | --- |--- | --- |
| caseid | 5 | date | datetime.date(2020, 3, 4) | county | Westchester |state | New York | fips | 36119 | cases | 9 | death | 0 |

                        Table: checking COVID-19 data using function definition named execute_sql

5.Calculation of infection rate per NY state county in comparison to their distance

```
execute_sql('''SELECT c.county, d.distance as Distance_From_Manhattan, c.cases as Total_Case_On_Nov13_2020, p.population, c.cases/p.population*100 as Infection_Rate

FROM nycovidcase c, nydistance d, nypopulation p

WHERE d.fips1 = '36061'

AND d.fips2 = c.fips

AND p.county = c.county

AND c.date = '2020-11-13'`LIMIT 5''')

```


| County | Rockland | Case_Rate | 6.0060 | Distance_From_NYC | 26.0 |
| --- | --- | --- | --- | --- | --- |
| County | Westchester | Case_Rate | 4.5121 | Distance_From_NYC | 29.0 |
| --- | --- | --- | --- | --- | --- |
| County | Nassau | Case_Rate | 3.9259 |  Distance_From_NYC | 20.0 |
| --- | --- | --- | --- | --- | --- |
| County | Orange | Case_Rate | 3.8772 | Distance_From_NYC | 47.0 |
| --- | --- | --- | --- | --- | --- |
| County | Suffolk | Case_Rate | 3.5550 | Distance_From_NYC | 68.0 |

                            Table: Calculation of infection rate and distance using function definition named execute_sql

6.Creating a csv file with infection rate and distance

```
import csv
n=0
with open('rate_vs_distance.csv', 'r') as f:
    reader = csv.reader(f)

    for column in reader:
        print(column)
        if n>3:
            break
        n+=1
```

| county | infection_Rate | Distance_From_NYC |
| --- | --- | --- |
| Rockland | 6.0060 | 26 |
| --- | --- | --- |
| Westchester | 4.5121 | 29 |
| --- | --- | --- |
| Nassau | 3.9259 | 20 |
| --- | --- | --- |
| Orange | 3.8772 | 47 |


                            Table: checking imported csv file for infection rate and distance

7.Visualization

Exporting the content of the view table named rate_vs_distance.csv as a csv
The content of the view table will now be exported to "Infection_Rate_Vs_Distance_2020_11_13.csv" for further operations.
```
import csv
n=0
with open('Infection_Rate_Vs_Distance_2020_11_13.csv', 'r') as f:
    reader = csv.reader(f)

    for line in reader:
        print(line)
        if n>5:
            break
        n+=1
```

|county_name |   Distance_From_Manhattan |  Total_Case_On_Nov13_2020 | population |Infection_Rate |
| --- | --- | --- | --- |--- |
| Allegany | 233 | 589 | 46091 | 1.2779 |
| --- | --- | --- | --- |--- |
| Cattaraugus | 264 | 661 | 76117 | 0.8684 |
| --- | --- | --- | --- |--- |
| Cayuga | 204 | 609 | 76576 | 0.7953 |
| --- | --- | --- | --- |--- |
| Chautauqua | 300 | 1210 | 126903 | 0.9535 |
| --- | --- | --- | --- |--- |
| Chemung | 172 | 2280 | 83456 | 2.7320 |
| --- | --- | --- | --- |--- |
| Clinton | 275 | 356 | 80485 | 0.4423' |
| --- | --- | --- | --- |--- |

                            Table: Total COVID-19 case with infection rate and distance



Checking correlation by a scatterplot

```
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

```


![correlation.png](attachment:correlation.png)Text(0,0.5,'COVID Infection Percentage *10,000')

                                Figure: Scatter plot showing correlation of COVID-19 infection rate and distance from NYC

Just by observing the scatterplot, we can visually confirm that there is a negative correlation between the distance of a county from Manhattan and its COVID-19 infection rate. So, in the next section, we'd go for checking it's statistical significance.

Finding the Pearson's coefficient and testing its statistical significance at a 95% level confidence.
The python package 'scipi' is used to find the Pearson correlation coefficient
We can test the significance with different confidence level, here the test with 95% confidence.
```
test_level_percentage = 95

alpha = 1-test_level_percentage/100

from scipy.stats import pearsonr
stat, p = pearsonr(distance_from_Manhattan, infection_rate)
print('stat=%.3f, p=%.3f' % (stat, p))
if p > alpha:
    print('No significant dependency')
else:
    print('The correlation is statistically significant at a '+ str(test_level_percentage)+'% '+'confidence level')
```
The result shows stat=-0.490, p=0.000
The correlation is statistically significant at a 95% confidence level

![Scatterplot.png](attachment:Scatterplot.png)

                            Figure: Scatter plot showing COVID-19 infection rate and distance from Manhattan

Conclusion

The answer of the research question is 'Yes', meaning that there is a moderate statistically significant relation between the COVID-19 infection rate among the population in NY state counties and their distances from New York City (Manhattan) at a significance level of 95%.

The less the distance of a county from New York city, the more is the COVID infection rate among its population.



```python

```
