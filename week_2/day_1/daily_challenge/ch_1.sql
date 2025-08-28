CREATE TABLE actors (
    actor_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name  VARCHAR(50) NOT NULL,
    birth_date DATE
);
SELECT COUNT(*) AS total_actors
FROM actors;

INSERT INTO actors (first_name, last_name, birth_date)
VALUES ('', '', NULL);