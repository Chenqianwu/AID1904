-- 单行注释
/* 多行注释 */

-- 创建course表:id,cname,cduration
/*create table course(
    id int primary key auto_increment,
    cname varchar(30) not null,
    cduration int not null
);*/
-- 向course表中插入测试数据
/*insert into course(cname,cduration)
values
('Python基础',20),('Python高级',15),
('WEB基础',9),('Python Web',15),
('爬虫',10),('数据分析&人工智能',20);*/

-- 创建teacher表:id,name,age,gender,hobby,course_id
-- course_id是外键,引用自course表的主键id
/*create table teacher(
    id int primary key auto_increment,
    name varchar(30) not null,
    age int not null,
    gender varchar(2) not null,
    hobby varchar(50) not null,
    course_id int ,
    -- 外键约束
    constraint fk_course_teacher foreign key(course_id)
    references course(id)
);*/

-- 向teacher表中插入测试数据
/*insert into teacher
values
(null,'齐天大圣',28,'M','大保健',1),
(null,'吕泽Maria',30,'M','拍片',2),
(null,'赵萌萌',18,'F','看帅哥',3);*/

-- 创建major表 : id,m_name
/*create table major(
    id int primary key auto_increment,
    m_name varchar(30) not null
);*/

-- 向major表中插入数据
/*insert into major(m_name)
values('AID'),('UID'),('JSD'),('WEB');*/

-- 创建student表:id,name,age,gender,school,class_id,major_id
/*create table student(
    id int primary key auto_increment,
    name varchar(30) not null,
    age int not null,
    gender char(2) not null,
    school varchar(100) not null,
    class_id int not null,
    major_id int not null
)*/

-- 更新student表,增加外键关系在major_id上,引用自major表的主键id
/*alter table student
add constraint fk_major_student
foreign key(major_id)
references major(id);*/

-- 创建classinfo表:id,classname,status
/*create table classinfo(
    id int primary key auto_increment,
    classname varchar(20) not null,
    status tinyint
);*/

-- 修改student表结构,增加外键在class_id,引用自classinfo表的主键id
/*alter table student
add constraint fk_classinfo_student
foreign key(class_id)
references classinfo(id);*/

-- 创建score表:id,stu_id,course_id,score
/*create table score(
    id int primary key auto_increment,
    stu_id int not null,
    course_id int not null,
    score int not null,
    constraint fk_student_score foreign key(stu_id)
    references student(id),
    constraint fk_course_score foreign key(course_id)
    references course(id)
)*/

-- 向classinfo,student,score 表中插入测试数据
/*insert into classinfo values
(null,'1901',0),
(null,'1902',1),
(null,'1903',1),
(null,'1904',1),
(null,'1905',1);

insert into student(name,age,gender,school,class_id,major_id) values
('张三',30,'M','哈佛大学',2,1),
('李四',25,'M','剑桥大学',3,1),
('王二麻子',19,'F','五道口技术学院',2,1),
('王五',28,'M','麻省理工学院',2,1);*/

/*insert into score(stu_id,course_id,score) values
(1,1,98),(1,2,85),(1,3,96),
(2,1,69),(2,2,89),(2,4,65),
(3,2,76),(3,3,88),(3,4,75);*/

-- 删除score表中的fk_student_score外键
-- alter table score drop foreign key fk_student_score

-- 为score表中的stu_id增加外键,引用自student主键id,并设置级联操作
/*alter table score
add constraint fk_student_score
foreign key(stu_id)
references student(id)
on delete cascade
on update cascade*/

-- 使用内连接查询teacher和course表中的数据(姓名,年龄,课程名称,课时)
/*select t.name,t.age,c.cname,c.cduration
from teacher as t
inner join course as c
on t.course_id = c.id*/

-- 1.查询学员的姓名,年龄,所在班级名称,专业名称,并筛选出1902的学员
/*select s.name,s.age,c.classname,m.m_name
from student as s
inner join classinfo as c on s.class_id = c.id
inner join major as m on s.major_id = m.id
where c.classname='1902';*/

-- 2.查询学员的姓名,毕业院校,所在班级,考试科目,考试成绩
select s.name,s.school,c.classname,cou.cname,sc.score
from student as s
inner join classinfo as c on s.class_id = c.id
inner join score as sc on s.id = sc.stu_id
inner join course as cou on sc.course_id = cou.id;










