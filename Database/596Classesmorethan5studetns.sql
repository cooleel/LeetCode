/*
596Classes more than 5 studetns

students can not be duplicated count
*/

select class
from courses
group by class
having count(distinct student) >=5;
