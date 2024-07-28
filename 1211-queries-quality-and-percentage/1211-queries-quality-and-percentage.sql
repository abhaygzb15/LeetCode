# Write your MySQL query statement below
select query_name,
round(sum(rating/position)/count(*),2) as "quality",
round(100* SUM(CASE WHEN rating < 3 THEN 1 ELSE 0 END) / COUNT(*), 2) AS "poor_query_percentage"
from queries 
where query_name is not null
group by query_name;