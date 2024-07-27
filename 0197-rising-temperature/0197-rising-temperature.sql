# Write your MySQL query statement below
SELECT current.id FROM Weather current
JOIN Weather previous
ON current.recordDate = DATE_SUB(previous.recordDate, INTERVAL -1 DAY)
WHERE current.temperature > previous.temperature;
