
/*
Table: Candidate

+-----+---------+
| id  | Name    |
+-----+---------+
| 1   | A       |
| 2   | B       |
| 3   | C       |
| 4   | D       |
| 5   | E       |
+-----+---------+  
Table: Vote

+-----+--------------+
| id  | CandidateId  |
+-----+--------------+
| 1   |     2        |
| 2   |     4        |
| 3   |     3        |
| 4   |     2        |
| 5   |     5        |
+-----+--------------+
id is the auto-increment primary key,
CandidateId is the id appeared in Candidate table.
Write a sql to find the name of the winning candidate, the above example will return the winner B.

+------+
| Name |
+------+
| B    |
+------+
*/


# Write your MySQL query statement below

select b.Name  from 
Vote a
inner join Candidate b  
on a.candidateId=b.Id
group by candidateId 
order by count(*) desc
limit 1

with a as (
 select CandidateId, rank() over (order by count(*) desc) rk
 from vote
 group by CandidateId
)
select name from candidate, a
where id = a.CandidateId
and a.rk = 1;
