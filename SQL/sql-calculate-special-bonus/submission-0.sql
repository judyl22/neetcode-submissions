-- Write your query below
SELECT employee_id, salary AS bonus
FROM employees
WHERE MOD(employee_id, 2) = 1 AND name NOT LIKE 'M%'

UNION ALL

SELECT employee_id, 0 AS bonus
FROM employees
WHERE MOD(employee_id, 2) = 0 OR name LIKE 'M%'

ORDER BY employee_id