# # Write your MySQL query statement below
# select customer_id from customer,product where 
# customer.product_key=product.product_key group by customer_id 
# having count(customer.product_key)=(select count(product_key) from product);

SELECT customer_id 
FROM Customer 
GROUP BY customer_id 
HAVING COUNT(DISTINCT product_key) = (SELECT COUNT(DISTINCT product_key) FROM Product);
