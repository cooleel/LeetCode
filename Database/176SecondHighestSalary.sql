/*
176. Second Highest Salary
without limit
*/


select max(Salary) as SecondHighestSalary
from Employee
where Salary not in
(select max(Salary)
from Employee);
