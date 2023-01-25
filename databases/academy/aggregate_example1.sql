  select d.`name` as 'Department',
		 count(*) as 'Number of groups'
    from `departments` as d
    join `groups` as g
      on d.`id` = g.`department_id`
group by `Department`
order by `Number of groups` desc
