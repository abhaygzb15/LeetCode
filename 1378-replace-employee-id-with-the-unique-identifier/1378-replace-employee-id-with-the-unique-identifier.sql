# Write your MySQL query statement below
select unique_id,name from employees left outer join employeeUNI on employees.id=employeeuni.id;