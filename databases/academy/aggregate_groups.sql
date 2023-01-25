  select f.`name` as 'Faculty',
		 d.`name` as 'Department'
    from `faculties` as f
    join `departments` as d
      on f.`id` = d.`faculty_id`
order by f.`name`;

  select f.`name` as 'Faculty',
		 d.`name` as 'Department'
    from `faculties` as f
    join `departments` as d
      on f.`id` = d.`faculty_id`
group by `Faculty`
order by f.`name`;

  select f.`name` as 'Faculty',
		 group_concat(d.`name` separator ', ') as 'Departments'
    from `faculties` as f
    join `departments` as d
      on f.`id` = d.`faculty_id`
group by `Faculty`
order by f.`name`;
