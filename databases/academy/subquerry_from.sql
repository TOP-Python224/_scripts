  select subq.`y` as 'Year',
		 round(avg(subq.`lc`)) as 'Lectures, avg'
	from ( select g.`year` as 'y',
				  count(l.`id`) as 'lc'
			 from `groups` as g
			 join `groups_lectures` as gl
			   on g.`id` = gl.`group_id`
			 join `lectures` as l
			   on l.`id` = gl.`lecture_id`
		 group by g.`name` ) as subq
group by subq.`y`
order by subq.`y`
