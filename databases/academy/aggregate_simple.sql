select count(*) from `students`;

select avg(`rating`) from `students`;

select round(sum(`financing`) / 1000000, 2) as 'Total financing, mlns'
  from `faculties`;
