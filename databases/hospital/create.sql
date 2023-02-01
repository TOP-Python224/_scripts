drop database if exists hospital;

create database hospital;
use hospital;

create table departments (
	`id` tinyint unsigned not null auto_increment primary key,
    `name` varchar(100) not null unique,
    constraint `CH_departments_name` check (`name` <> '')
);

create table wards (
	`id` smallint unsigned not null auto_increment primary key,
    `name` char(6) not null unique,
    constraint `CH_wards_name` check (`name` <> ''),
    `department_id` tinyint unsigned not null
);

create table doctors (
	`id` smallint unsigned not null auto_increment primary key,
    `name` varchar(30) not null,
    constraint `CH_doctors_name` check (`name` <> ''),
    `surname` varchar(30) not null,
    constraint `CH_doctors_surname` check (`surname` <> ''),
    `salary` decimal(8,2) not null,
    constraint `CH_doctors_salary` check (`salary` > 0),
    `premium` decimal(8,2) not null default 0,
    constraint `CH_doctors_premium` check (`premium` >= 0)
);

create table vacations (
	`id` mediumint not null auto_increment primary key,
	`doctor_id` smallint unsigned not null,
    `start_date` date not null,
    `end_date` date not null,
    constraint `CH_vacations_end_date` check (`end_date` > `start_date`)
);

create table specializations (
	`id` tinyint unsigned not null auto_increment primary key,
    `name` varchar(100) not null unique,
    constraint `CH_specializations_name` check (`name` <> '')
);

create table doctors_specializations (
	`doctor_id` smallint unsigned not null,
	`specialization_id` tinyint unsigned not null,
    constraint primary key (`doctor_id`, `specialization_id`)
);

create table sponsors (
	`id` smallint not null auto_increment primary key,
    `name` varchar(100) not null unique,
    constraint `CH_sponsors_name` check (`name` <> '')
);

create table donations (
	`id` smallint unsigned not null auto_increment primary key,
    `amount` decimal(11,2) not null,
    constraint `CH_donations_amount` check (`amount` > 0),
    `date` date not null default (curdate()),
    `sponsor_id` smallint not null,
    `department_id` tinyint unsigned not null
);


alter table wards
	add constraint `FK_wards_department_id` 
		foreign key (`department_id`)
		references departments (`id`);

alter table vacations
	add constraint `FK_vacations_doctor_id` 
		foreign key (`doctor_id`)
		references doctors (`id`);

alter table doctors_specializations
	add constraint `FK_doctors_specializations_doctor_id` 
		foreign key (`doctor_id`)
		references doctors (`id`),
	add constraint `FK_doctors_specializations_specialization_id` 
		foreign key (`specialization_id`)
		references specializations (`id`);

alter table donations
	add constraint `FK_donations_sponsor_id` 
		foreign key (`sponsor_id`)
		references sponsors (`id`),
	add constraint `FK_donations_department_id` 
		foreign key (`department_id`)
		references departments (`id`);

