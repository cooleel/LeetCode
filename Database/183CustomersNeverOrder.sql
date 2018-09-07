/*
183.Customers Who Never Order

easy
one trick: quote 'Customers'
*/

select c.Name as 'Customers'
from Customers c
where c.Id not in
(select CustomerId
from orders);
