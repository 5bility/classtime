drop database if exists classtime;

create database classtime;
use classtime;

create user 'classtimepm'@'%' identified by 'ct1234';
grant all privileges on classtime.* to 'classtimepm'@'%';

flush privileges;

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