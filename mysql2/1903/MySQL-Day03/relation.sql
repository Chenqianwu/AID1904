create table teacher(
id int primary key,
tname varchar(20),
level varchar(20)
)charset=utf8;
insert into teacher values(1,'����Ա���','ţX'),(2,'�����','˾��');

create table course(
id int primary key,
cname varchar(20),
score int
)charset=utf8;
insert into course values(1,'HTML',5),(2,'Spider',5),(3,'MySQL',5);