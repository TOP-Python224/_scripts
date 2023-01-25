  select d.`building`,
		 sum(d.`financing`) as 'Building financing'		 
    from `departments` as d
group by d.`building`
  having `Building financing` > 12000000
order by d.`building`
