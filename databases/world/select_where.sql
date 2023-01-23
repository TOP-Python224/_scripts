  select `Name`,
         round(`Population`/1000000, 1) as 'Populaion, mlns'
    from `country`
   where `Population` > 10000000
order by `Populaion, mlns`
