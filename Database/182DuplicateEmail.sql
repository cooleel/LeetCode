/*
182DuplicateEmail

count >1

*/

select Email
from Person
group by Email
having count(*)>1;
