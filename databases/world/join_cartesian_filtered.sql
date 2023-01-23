 	   select `country`.`Code` as 'country Primary Key',
 			  `city`.`ID` as 'city Primary Key',
              `city`.`CountryCode` as 'city Foreign Key'
         from `country`
straight_join `city`;


select `country`.`Code` as 'country Primary Key',
	   `city`.`ID` as 'city Primary Key',
	   `city`.`CountryCode` as 'city Foreign Key'
  from `country`
  join `city`
	on `country`.`Code` = `city`.`CountryCode`;
