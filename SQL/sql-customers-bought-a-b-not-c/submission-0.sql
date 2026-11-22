-- Write your query below
SELECT c.customer_id, c.customer_name
FROM customers AS c
JOIN orders AS o
    ON c.customer_id = o.customer_id
GROUP BY c.customer_id
HAVING COUNT(*) FILTER (WHERE o.product_name = 'A') > 0
    AND COUNT(*) FILTER (WHERE o.product_name = 'B') > 0
    AND COUNT(*) FILTER (WHERE o.product_name = 'C') = 0
ORDER BY customer_name;