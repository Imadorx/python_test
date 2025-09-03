select * from language;
select * from film;

select f.title, f.description,l.name
from  film f
join language l on f.language_id=l.language_id; 


select f.title, f.description,l.name
from  film f
LEFT JOIN language l on f.language_id=l.language_id; 

CREATE TABLE new_film (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

INSERT INTO new_film (name) VALUES 
('Inception'),
('Titanic'),
('The Matrix'),
('Avatar');

CREATE TABLE customer_review (
    review_id SERIAL PRIMARY KEY,
    film_id INT REFERENCES new_film(id) ON DELETE CASCADE,
    language_id INT REFERENCES language(language_id),
    title VARCHAR(255) NOT NULL,
    score INT CHECK(score BETWEEN 1 AND 10),
    review_text TEXT,
    last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO customer_review (film_id, language_id, title, score, review_text)
VALUES 
(1, 1, 'Amazing movie!', 9, 'The concept is brilliant and well executed.'),
(2, 1, 'Classic masterpiece', 10, 'A timeless love story with epic visuals.');

select * from customer_review;