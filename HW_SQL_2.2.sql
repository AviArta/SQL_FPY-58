
create table if not exists departments (
	id SERIAL primary key,
	name_department VARCHAR (60) not null
);

create table if not exists employees (
	id SERIAL primary key,
	name VARCHAR (20) not null,
	id_department integer not null references departments(id),
	chief integer references employees(id)
);

 --create table if not exists chiefs (
 	--chief_id integer references employees(id),
 	--department_id integer references departments(id),
 	--constraint pk primary key (chief_id, department_id)
 --);