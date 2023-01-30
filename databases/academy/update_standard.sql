update `students`
   set `name` = concat_ws(' ', `name`, `surname`),
       `surname` = 'SRN'
 where `id` between 2501 and 2601;
 
  update `students`
	 set `name` = concat_ws(' ', `name`, `surname`)
order by `id` desc
limit 3;
