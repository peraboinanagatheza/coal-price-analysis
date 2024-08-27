create database project;
use project;
create table merged_data(Date_Date date  ,Coal_RB_4800_FOB_London_Close_USD varchar(100),
Coal_RB_5500_FOB_London_Close_USD varchar(100),Coal_RB_5700_FOB_London_Close_USD varchar(100),
Coal_RB_6000_FOB_CurrentWeek_Avg_USD varchAr(100),Coal_India_5500_CFR_London_Close_USD varchar(100));
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/merged_data.csv'
INTO TABLE merged_data
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n' 
IGNORE 1 ROWS;
describe merged_data;
select * from merged_data; 
drop table merged_data;
ALTER TABLE merged_data MODIFY COLUMN Date_Date DATE;

# First Moment Business Decision / Measures of Central Tendency

SELECT AVG(Coal_RB_4800_FOB_London_Close_USD) FROM merged_data;
select avg(Coal_RB_5500_FOB_London_Close_USD) from merged_data;
select avg(Coal_RB_5700_FOB_London_Close_USD) from merged_data;
select avg (Coal_RB_6000_FOB_CurrentWeek_Avg_USD) from merged_data;
select avg(Coal_India_5500_CFR_London_Close_USD) from merged_data;

# Second Moment Business Decision / Measures of Dispersion
# Standard Deviation
SELECT STDDEV(Coal_RB_4800_FOB_London_Close_USD) AS Coal_RB_4800_FOB_London_Close_USD_stddev FROM merged_data;
select stddev(Coal_RB_5500_FOB_London_Close_USD) as Coal_RB_5500_FOB_London_Close_USD_stddev from merged_data;
select stddev(Coal_RB_5700_FOB_London_Close_USD) as Coal_RB_5700_FOB_London_Close_USD_stddev from merged_data;
select stddev(Coal_RB_6000_FOB_CurrentWeek_Avg_USD) as Coal_RB_6000_FOB_CurrentWeek_Avg_USD_stddev from merged_data;
select stddev(Coal_India_5500_CFR_London_Close_USD) as Coal_India_5500_CFR_London_Close_USD_stddev from merged_data;

# Range:
SELECT MAX(Coal_RB_4800_FOB_London_Close_USD) - MIN(Coal_RB_4800_FOB_London_Close_USD) AS Coal_RB_4800_FOB_London_Close_USD_range 
FROM merged_data;
select max(Coal_RB_5500_FOB_London_Close_USD) - min(Coal_RB_5500_FOB_London_Close_USD) as Coal_RB_5500_FOB_London_Close_USD_range
from merged_data;
select max(Coal_RB_5700_FOB_London_Close_USD) - min(Coal_RB_5700_FOB_London_Close_USD) as Coal_RB_5700_FOB_London_Close_USD_range 
from merged_data;
select max(Coal_RB_6000_FOB_CurrentWeek_Avg_USD) - min(Coal_RB_6000_FOB_CurrentWeek_Avg_USD) as Coal_RB_6000_FOB_CurrentWeek_Avg_USD_range
from merged_data;
select max(Coal_India_5500_CFR_London_Close_USD) - min(Coal_India_5500_CFR_London_Close_USD) as Coal_India_5500_CFR_London_Close_USD_range
from merged_data;

# Variance
SELECT VARIANCE(Coal_RB_4800_FOB_London_Close_USD) AS variance_Coal_RB_4800_FOB_London_Close_USD FROM merged_data;
select variance(Coal_RB_5500_FOB_London_Close_USD) as Coal_RB_5500_FOB_London_Close_USD_variance from merged_data;
select variance(Coal_RB_5700_FOB_London_Close_USD) as Coal_RB_5700_FOB_London_Close_USD_variance from merged_data;
select variance(Coal_RB_6000_FOB_CurrentWeek_Avg_USD) as Coal_RB_6000_FOB_CurrentWeek_Avg_USD from merged_data;
select variance(Coal_India_5500_CFR_London_Close_USD) as Coal_India_5500_CFR_London_Close_USD from merged_data;

# Third Moment Business Decision / Skewness

SELECT(SUM(POWER(Coal_RB_4800_FOB_London_Close_USD- (SELECT AVG(Coal_RB_4800_FOB_London_Close_USD) FROM merged_data), 3)) /
(COUNT(*) * POWER((SELECT STDDEV(Coal_RB_4800_FOB_London_Close_USD) FROM merged_data), 3))) AS skewness FROM merged_data;
select (sum(power(Coal_RB_5500_FOB_London_Close_USD- (select avg(Coal_RB_5500_FOB_London_Close_USD) from merged_data),3)) /
(count(*) * power((select stddev(Coal_RB_5500_FOB_London_Close_USD)from merged_data), 3))) as skewness from merged_data;
select (sum(power(Coal_RB_5700_FOB_London_Close_USD- (select avg(Coal_RB_5700_FOB_London_Close_USD) from merged_data),3)) /
(count(*) * power((select stddev(Coal_RB_5700_FOB_London_Close_USD)from merged_data), 3))) as skewness from merged_data;
select (sum(power(Coal_RB_6000_FOB_CurrentWeek_Avg_USD- (select avg(Coal_RB_6000_FOB_CurrentWeek_Avg_USD) from merged_data),3)) /
(count(*) * power((select stddev(Coal_RB_6000_FOB_CurrentWeek_Avg_USD)from merged_data), 3))) as skewness from merged_data;
select(sum(power(Coal_India_5500_CFR_London_Close_USD- (select avg(Coal_India_5500_CFR_London_Close_USD) from merged_data),3))/
(count(*) * power((select stddev(Coal_India_5500_CFR_London_Close_USD) from merged_data),3))) as skewness from merged_data;

# Fourth Moment Business Decision / Kurtosis

SELECT((SUM(POWER(Coal_RB_4800_FOB_London_Close_USD- (SELECT AVG(Coal_RB_4800_FOB_London_Close_USD) FROM MERGED_DATA), 4)) /
(COUNT(*) * POWER((SELECT STDDEV(Coal_RB_4800_FOB_London_Close_USD) FROM MERGED_DATA), 4))) - 3) AS kurtosis FROM MERGED_DATA;
select((sum(power(Coal_RB_5500_FOB_London_Close_USD- (select avg(Coal_RB_5500_FOB_London_Close_USD) from merged_data), 4)) /
(count(*)* power((select stddev(Coal_RB_5500_FOB_London_Close_USD) from merged_data),4))) - 3) as kurtosis from merged_data;
select((sum(power(Coal_RB_5700_FOB_London_Close_USD- (select avg(Coal_RB_5700_FOB_London_Close_USD) from merged_data),4)) /
(count(*) * power((select stddev(Coal_RB_5700_FOB_London_Close_USD) from merged_data),4))) - 3) as kurtosis from merged_data;
select((sum(power(Coal_RB_6000_FOB_CurrentWeek_Avg_USD - (select avg(Coal_RB_6000_FOB_CurrentWeek_Avg_USD) from merged_data),4)) /
(count(*) * power((select stddev(Coal_RB_6000_FOB_CurrentWeek_Avg_USD) from merged_data),4))) - 3) as kurtosis from merged_data;
select((sum(power(Coal_India_5500_CFR_London_Close_USD- (select avg(Coal_India_5500_CFR_London_Close_USD) from merged_data),4)) / 
(count(*) *power((select stddev(Coal_India_5500_CFR_London_Close_USD)from merged_data),4))) - 3) as kurtosis from merged_data;






