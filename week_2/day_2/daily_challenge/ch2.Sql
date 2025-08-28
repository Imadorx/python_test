    SELECT COUNT(*) 
    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NULL )
-- ======Résultat : 0========

SELECT COUNT(*) 
FROM FirstTab 
WHERE id NOT IN (SELECT id FROM SecondTab WHERE id = 5);
-- ======Résultat : 2========

SELECT COUNT(*) 
FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab )
-- ======Résultat : 0========

SELECT COUNT(*) 
FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL )
-- ======Résultat : 2========