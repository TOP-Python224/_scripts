select `country`.`Name` as 'Country',
	   `city`.`Name` as 'Capital'
  from `country`
  join `city`
    on `country`.`Capital` = `city`.`ID`;
