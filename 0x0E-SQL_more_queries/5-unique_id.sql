-- creates table unique id on MySQL server

create table if not exists unique_id (id int unique default 1, name varchar(256));
