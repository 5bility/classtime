drop database if exists classtime;

create database classtime;
use classtime;

create table user(
	id varchar(20) not null primary key,
    pw varchar(20) not null,
    name varchar(20) not null,
    nickname varchar(20) not null,
    depart varchar(20) not null,
    year int not null,
    sex varchar(3) not null
);

create table professor(
	id int not null primary key auto_increment,
    name varchar(20) not null,
    depart varchar(20) not null
);

create table lecture(
	id int not null primary key auto_increment,
    name varchar(30) not null,
    classroom varchar(20) not null,
    classtime varchar(50) not null,
    student_count int not null,
    professor_id int not null,
    foreign key (professor_id) references professor(id)
);

create table evaluation(
	id int not null primary key auto_increment,
    comment text not null,
    stars int not null,
    user_id varchar(20) not null,
    lecture_id int not null,
    foreign key (user_id) references user(id),
    foreign key (lecture_id) references lecture(id)
);

create table grade(
	id int not null primary key auto_increment,
    grade varchar(5) not null,
    year int not null,
    semester int not null,
    user_id varchar(20) not null,
    lecture_id int not null,
	foreign key (user_id) references user(id),
    foreign key (lecture_id) references lecture(id)
);

create table post(
	id int not null primary key auto_increment,
    title varchar(100) not null,
    content text not null,
    posttime datetime not null,
    recommends int not null,
    replys int not null,
    user_id varchar(20) not null,
    foreign key (user_id) references user(id)
);

create table recommend(
	id int not null primary key auto_increment,
    user_id varchar(20) not null,
    post_id int not null,
    foreign key (user_id) references user(id),
    foreign key (post_id) references post(id)
);

create table reply(
	id int not null primary key auto_increment,
    replytime datetime not null,
    comment text not null,
    is_added int not null,
    added_id int not null,
    user_id varchar(20) not null,
    post_id int not null,
    foreign key (user_id) references user(id),
    foreign key (post_id) references post(id)
);

insert into professor(name, depart) values('이재학', '컴퓨터공학부');
insert into professor(name, depart) values('전광일', '컴퓨터공학부');
insert into professor(name, depart) values('허훈식', '컴퓨터공학부');
insert into professor(name, depart) values('공기석', '컴퓨터공학부');
insert into professor(name, depart) values('김영곤', '컴퓨터공학부');
insert into professor(name, depart) values('박정민', '컴퓨터공학부');
insert into professor(name, depart) values('신성욱', '컴퓨터공학부');
insert into professor(name, depart) values('정성택', '컴퓨터공학부');
insert into professor(name, depart) values('최종필', '컴퓨터공학부');
insert into professor(name, depart) values('방영철', '컴퓨터공학부');
insert into professor(name, depart) values('서대영', '컴퓨터공학부');
insert into professor(name, depart) values('최진구', '컴퓨터공학부');
insert into professor(name, depart) values('정의훈', '컴퓨터공학부');
insert into professor(name, depart) values('배유석', '컴퓨터공학부');
insert into professor(name, depart) values('이보경', '컴퓨터공학부');
insert into professor(name, depart) values('한경숙', '컴퓨터공학부');

insert into lecture(name, classroom, classtime, student_count, professor_id) values('컴퓨터응용설계', 'E516', '목9-12', 50, 0);
insert into lecture(name, classroom, classtime, student_count, professor_id) values('유닉스시스템프로그래밍', 'E423', '화6-8목6-8', 40, 1);
insert into lecture(name, classroom, classtime, student_count, professor_id) values('웹서비스프로그래밍', 'E523', '화1-2목1-2', 40, 2);
insert into lecture(name, classroom, classtime, student_count, professor_id) values('프로그래밍', 'E423', '월2-3수6', 50, 5);
insert into lecture(name, classroom, classtime, student_count, professor_id) values('선형대수학', 'E516', '목9-12', 50, 13);