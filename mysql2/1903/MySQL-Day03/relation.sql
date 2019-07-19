create table teacher(
id int primary key,
tname varchar(20),
level varchar(20)
)charset=utf8;
insert into teacher values(1,'³ÌÐòÔ±½ã½ã','Å£X'),(2,'³¬¸ç¸ç','Ë¾»ú');

create table course(
id int primary key,
cname varchar(20),
score int
)charset=utf8;
insert into course values(1,'HTML',5),(2,'Spider',5),(3,'MySQL',5);