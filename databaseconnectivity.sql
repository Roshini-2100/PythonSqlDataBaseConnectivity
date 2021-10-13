create database pysql_db;
use pysql_db;
create table users(
ID integer auto_increment primary key,
NAME varchar(50),
AGE integer,
CITY varchar(50)
);
insert into users(NAME,AGE,CITY) values('ROSHINI',19,'OOTY'),('INDHU',20,'COIMBATORE'),('JYOTHI',21,'KERALA');
select * from users;