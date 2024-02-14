-- creates database and user 

create database if not exists hbtm_0d_2;
create user if not exists 'user_0d_2'@'localost' identified by 'user_0d_2_pwd';
grant select on 'hbtm_0d_2'.* to 'user_0d_2'@'localhost';
flush privileges;
