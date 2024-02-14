-- creates the database hbtm_Od_usa and table states in MySQL server

create database if not eixsts hbtn_0d_usa;
create table if not exists hbtn_0d_usa.states (id int not null primary key auto_increment, name varchar(256) not null);
