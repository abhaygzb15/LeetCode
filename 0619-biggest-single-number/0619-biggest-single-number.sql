# Write your MySQL query statement below
SELECT COALESCE(MAX(num), NULL) AS num from
(
    select num from mynumbers group by num having count(*)=1)
as single;