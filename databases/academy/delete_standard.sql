-- safe mode on
delete from `students`
-- `id` является первичным ключом таблицы `students`
where `id` = 2608;


-- safe mode off
delete from `students`
-- `name` не является первичным ключом таблицы `students`
where `name` like '%SRN%';

delete from `students`
order by `id` desc
limit 5;
