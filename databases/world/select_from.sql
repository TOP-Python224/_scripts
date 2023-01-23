select `Code`,
	   `Name`,
       round(`Population`/1000000, 3) as 'Populaion, mlns'
  from `country`
