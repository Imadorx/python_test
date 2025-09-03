CREATE TABLE CUSTOMER_2 (
c_id serial primary key ,
first_name varchar(40),
last_name varchar(50) NOT NULL
);

CREATE TABLE CUSTOMER_profile (
p_id serial PRIMARY KEY ,
isloggedIn boolean default FALSE ,
customer_id integer REFERENCES CUSTOMER_2 (c_id) ON DELETE CASCADE 
);

insert into customer_2 (first_name, last_name) values ('john' , 'doe')
insert into customer_2 (first_name, last_name) values ('jerome', 'lalu')
insert into customer_2 (first_name, last_name) values ('lea', 'rive')

insert into customer_profile (isloggedIn , customer_id ) values (true, (select c_id from customer_2 where first_name= 'jhon'));
insert into customer_profile (isloggedIn , customer_id ) values (false, (select c_id from customer_2 where first_name= 'jerome'));

select c.first_name , p.isloggedIn from customer_2 c
join customer_profile p
on c.c_id = p.customer_id 
where p.isloggedIn = true ; 

select c.first_name , p.isloggedIn from customer_2 c
left join customer_profile p
on c.c_id = p.customer_id 

SELECT COUNT(*) AS not_logged_in_customer_2
FROM customer_2 c
JOIN customer_profile p ON c.c_id = p.customer_id
WHERE p.isLoggedIn = FALSE;

--------------------- part 2 ------------------------

create table Book (
book_id serial PRIMARY KEY ,
title  varchar (40) NOT NULL,
author varchar(40) not null
);

insert into Book (title , author ) values ('Alice In Wonderland', 'Lewis Carroll');
insert into Book (title , author ) values ('Harry Potter',' J.K Rowling');

insert into Book (title , author ) values ('To kill a mockingbird ',' Harper Lee');

CREATE TABLE Student (
    student_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    age INT CHECK (age <= 15)
);

INSERT INTO Student (name, age) VALUES
('John', 12),
('Lera', 11),
('Patrick', 10),
('Bob', 14);

CREATE TABLE Library (
    book_fk_id INT REFERENCES Book(book_id) ON DELETE CASCADE ON UPDATE CASCADE,
    student_fk_id INT REFERENCES Student(student_id) ON DELETE CASCADE ON UPDATE CASCADE,
    borrowed_date DATE,
    PRIMARY KEY (book_fk_id, student_fk_id, borrowed_date)
);

INSERT INTO Library (book_fk_id, student_fk_id, borrowed_date)
VALUES (
    (SELECT book_id FROM Book WHERE title = 'Alice In Wonderland'),
    (SELECT student_id FROM Student WHERE name = 'John'),
    '2022-02-15'
);

INSERT INTO Library (book_fk_id, student_fk_id, borrowed_date)
VALUES (
    (SELECT book_id FROM Book WHERE title = 'To kill a mockingbird'),
    (SELECT student_id FROM Student WHERE name = 'Bob'),
    '2021-03-03'
);

INSERT INTO Library (book_fk_id, student_fk_id, borrowed_date)
VALUES (
    (SELECT book_id FROM Book WHERE title = 'Alice In Wonderland'),
    (SELECT student_id FROM Student WHERE name = 'Lera'),
    '2021-05-23'
);

INSERT INTO Library (book_fk_id, student_fk_id, borrowed_date)
VALUES (
    (SELECT book_id FROM Book WHERE title = 'Harry Potter'),
    (SELECT student_id FROM Student WHERE name = 'Bob'),
    '2021-08-12'
);

SELECT * FROM Library;

SELECT s.name, b.title, l.borrowed_date
FROM Library l
JOIN Student s ON l.student_fk_id = s.student_id
JOIN Book b ON l.book_fk_id = b.book_id;

select * from  Student

SELECT AVG(s.age) AS avg_age
FROM Library l
JOIN Student s ON l.student_fk_id = s.student_id
JOIN Book b ON l.book_fk_id = b.book_id
WHERE b.title = 'Alice In Wonderland';

DELETE FROM Student WHERE name = 'Bob';


