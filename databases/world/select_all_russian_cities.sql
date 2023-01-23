select `Code`, `Name`
  from `country`
 where `Name` like 'russia%';

select `Name`
  from `city`
 where `CountryCode` = 'RUS';
