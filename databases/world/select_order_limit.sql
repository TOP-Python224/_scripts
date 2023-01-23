  select `Name`,
	     `SurfaceArea`,
         `GNP`
    from `country`
order by `SurfaceArea` desc
   limit 10
