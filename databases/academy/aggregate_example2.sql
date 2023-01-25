  select g.`name` as 'Group',
		 group_concat(
			concat_ws(' ', c.`name`, c.`surname`) separator ', '
		 ) as 'Curators'
    from `groups` as g
    join `groups_curators` as gc
      on g.`id` = gc.`group_id`
    join `curators` as c
      on c.`id` = gc.`curator_id`
group by `Group`
  having count(*) > 1
order by g.`year`