/*
184.DepartmentHighestSalary
select data on orginal dataset

*/



SELECT d.name as Department, e.name as Employee, e.Salary
from Employee e, Department d
where e.DepartmentId = d.Id
and (e.DepartmentId, Salary) in (select DepartmentID, max(Salary)
from employee group by DepartmentId);
