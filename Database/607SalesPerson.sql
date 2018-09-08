/*
607SalesPerson

Description

Given three tables: salesperson, company, orders.
Output all the names in the table salesperson, who didn’t have sales to company 'RED'.

*/

select name from salesperson
where sales_id not in
(select distinct sales_id from orders
where com_id = (select com_id from company where name = 'RED'));
