/*
610TireangleJudegment

x+y >z and abs(x-y)<z
*/

select x,y,z,
case when x+y >z and abs(x-y)<z then 'Yes'
else 'No' end as 'triangle'
from triangle;
