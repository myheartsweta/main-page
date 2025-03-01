CREATE DATABASE sales_data;
USE sales_data;
SELECT * FROM retail_sales_dataset LIMIT 10;

##count total rows#
select count(*)from_sales_dataset limit 20;

##check for null values
select age, count(*)as null_count
from retail_sales_dataset
where age is null
group by age;

##total sales revenue
SELECT Product_Category, SUM(Quantity) AS Total_Sold
FROM retail_sales_dataset
GROUP BY Product_Category
ORDER BY Total_Sold DESC
LIMIT 5;

SELECT * FROM retail_sales_dataset LIMIT 10;

#count the number of rfecords
select count(*) from retail_sales_dataset;

#data filtering
select * from retail_sales_dataset where Quantity = 4;

#get transaction from a spesinfic date range
select * from retail_sales_dataset where Date between '2023-01-01' and '2023-10-01';

#aggregation grouping
#total revenue generated
select sum(Total_Amount) as total_revenue from retail_sales_dataset;

#revenue generated per product
select Product_Category, sum(Total_Amount) as revenue from retail_sales_dataset group by Product_Category;

#average sales gender wise
select Gender, avg(Total_Amount) as avg_amnt from retail_sales_dataset group by Gender;

#advance
##finding the top 5 heighest sellinag products
select Product_category, sum(Total_Amount) as total_sales from retail_sales_dataset
group by Product_Category
order by total_sales desc;

#data cleaning  and transformations
###identify duplicate records
select Product_category, date, count(*)
from retail_sales_dataset
group by Product_Category, date
having count(*)>1;

#replace null values in the total amount column
update retail_sales_dataset
set Quantity=0
where Quantity is null;






