-- Write your query below
SELECT first_name, last_name, city, state
FROM person AS p
LEFT JOIN address AS a
ON p.person_id = a.person_id