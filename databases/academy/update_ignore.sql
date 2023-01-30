update ignore `students`
   set `id` = `id` + 1
 where `id` between 2600 and 2610;
 
 update ignore `students`
   set `surname` = char(rand()*150, rand()*150, rand()*150 using utf8mb4)
 where `id` between 2501 and 2601;
