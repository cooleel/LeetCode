/*
196DeleteDuplicateEmails

use 'delete' not 'distinct order by'
*/
delete from
Person
where
Id not in
(select Id
from (
select min(Id) as Id
from Person
group by Email) p
);
