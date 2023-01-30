select *
  from `country`
 where `code` = '';

insert `country`
	(`code`, `name`)
values
	(default, default);
