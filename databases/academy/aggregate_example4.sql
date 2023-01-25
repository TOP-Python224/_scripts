  select f.`name` as 'Faculty',
		 count(s.`id`) as 'Total students'
    from `students` as s
    join `groups_students` as gs
      on s.`id` = gs.`student_id`
	join `groups` as g
      on g.`id` = gs.`group_id`
	join `departments` as d
      on d.`id` = g.`department_id`
	join `faculties` as f
      on f.`id` = d.`faculty_id`
group by `Faculty`
order by `Total students` desc