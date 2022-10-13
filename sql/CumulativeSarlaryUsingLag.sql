# Write your MySQL query statement below
with cte1 as (
select * from Employee where (month, id) not in
    (select max(month) as m, id from Employee group by id)),
cte2 as (
select *, lag(salary, 1, 0) over(partition by id order by month) as prev_month_salary, lag(salary, 2, 0) over(partition by id order by month) as sec_prev_month_salary,
    lag(month, 1, 0) over(partition by id order by month) as prev_month, lag(month, 2, 0) over(partition by id order by month) as sec_prev_month
     from cte1
)

select id, month, case when month - prev_month = 1 and prev_month - sec_prev_month = 1 then Salary + prev_month_salary + sec_prev_month_salary
when month - prev_month = 1 then Salary + prev_month_salary else Salary end as Salary
from cte2
order by id, month desc
