  select d.`name` as 'Department',
		 cast(avg(t.`salary`) as unsigned) as 'Average teachers\' salary'
    from `teachers` as t
    join `lectures` as l
      on t.`id` = l.`teacher_id`
	join `groups_lectures` as gl
      on l.`id` = gl.`lecture_id`
	join `groups` as g
      on g.`id` = gl.`group_id`
	join `departments` as d
      on d.`id` = g.`department_id`
group by `Department`
order by `Average teachers' salary`