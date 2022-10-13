"""
Create cumulated salary
"""
select id, month, salary
from (
        select id, month, 
            sum(salary) over(partition by id order by month range between 2 PRECEDING and current row) salary,
            row_number() over(partition by id order by month desc) month_order
        from Employee 
    ) t
    where month_order > 1
