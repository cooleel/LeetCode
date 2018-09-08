/*
620NotBoringMovies
X city opened a new cinema, many people would like to go to this cinema.
The cinema also gives out a poster indicating the movies’ ratings and descriptions.
Please write a SQL query to output movies with an odd numbered ID and a description
that is not 'boring'. Order the result by rating.

pretty easy one

*/

select *
from cinema
where (id % 2) <> 0
and description <>'boring'
order by rating desc;
