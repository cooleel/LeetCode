/*
619BiggestSingleNumber
Table number contains many numbers in column num including duplicated ones.
Can you write a SQL query to find the biggest number, which only appears once.
+---+
|num|
+---+
| 8 |
| 8 |
| 3 |
| 3 |
| 1 |
| 4 |
| 5 |
| 6 |
*/

select if(count(*)=1,num,null) as num
from number
group by num
order by count(*),num desc limit 1;
