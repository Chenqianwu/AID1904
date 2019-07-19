select country,count(id) as cnt 
from sanguo
where gender='M'
group by country
order by cnt desc
limit 2