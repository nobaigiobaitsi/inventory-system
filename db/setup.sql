create database if not exists inventory_db;

use inventory_db;

create table if not exists products (
id int auto_increment primary key,
name varchar(100) not null unique,
category varchar(50),
quantity int not null default 0,
price decimal(10,2) not null,
added_on datetime default current_timestamp,
last_updated datetime default current_timestamp on update current_timestamp
);