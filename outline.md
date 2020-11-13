## 1. Project Title:
Exploring correlation between COVID morbidity in the counties of New York state and distances of the counties  from New York city.

## 2.Objectives

### 2.1 General objective: 
Checking and visualizing correlations among specific features from two data sets after conducting  ETL process using python programming language

### 2.2 Specific objectives: 

(i) Fetching and parsing COVID morbidity data from a Github repository (https://github.com/nytimes/covid-19-data) and data on distances among counties of the New York state from NBER database (https://www.nber.org/research/data/county-distance-database)

(ii) Filtering and cleansing data according to the analytical requirements

(iii)  Checking correlation between COVID morbidity in counties  and the distance of the counties from New York City (the epi center of the outbreak in the state of New York)

(iv) Visualization of the findings

### 3. Methodology
County Distances are great-circle distances calculated using the Haversine formula based on internal points in the geographic area. Counties are from Census 2000 SF1 and Census 2010 SF1 files. The county codes are FIPS County codes. The first two digits of the FIPS county codes are FIPS State codes.
Then from both the file the counties of NY will be separated and both the file will be merged with the ZIP and analyzed to find out the minimum date, maximum date, max patient per county, min patient per county, total patient per county, total death per county, case rate, death rate, comparison of distance of each county and the number of case of patient of each county. Here New York County (Manhattan borough) will be considered as the standard point for distance as New York was the hub of the disease as the early days of the disease.
After analysis the result will be written as a markdown file and uploaded in my GitHub repository named IA626_FinalProject.



```python

```
