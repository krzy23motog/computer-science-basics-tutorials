# SQL


## What Is the Difference Between INNER JOIN, LEFT JOIN, RIGHT JOIN, and FULL JOIN

- __inner__ means that it returns only the rows from both tables that satisfy the joining condition; 
- __outer__ joins return all the rows in one table, plus matching rows in the other table(s). 
- The exception is __FULL JOIN__, which returns all rows from __both tables__.

- INNER JOIN: Returns only matching rows from both tables
- LEFT JOIN: Returns all rows from the left table + matches from the right
- FULL OUTER JOIN: Returns everything from both tables, matched where possible

Left join:
```
SELECT
  fp.id,
  first_name,
  last_name,
  national_team_id,
  country,
  games_played
FROM football_players fp
LEFT JOIN national_team nt
ON fp.national_team_id = nt.id
ORDER BY fp.id;
```

Example 2:
```
SELECT
    c.customer_id,
    c.name,
    o.order_id,
    o.order_date,
    p.payment_id,
    p.amount
FROM customers c
LEFT OUTER JOIN orders o
    ON c.customer_id = o.customer_id
LEFT OUTER JOIN payments p
    ON o.order_id = p.order_id;
```
- Returns all customers
- If a customer has no orders → order_* columns = NULL
- If an order has no payment → payment_* columns = NULL

### ON vs WHERE in LEFT JOIN

```
LEFT JOIN orders o
ON c.customer_id = o.customer_id AND o.status = 'completed'
```
- Filters during the join
- Keeps all customers
- Only joins completed orders

```
LEFT JOIN orders o
ON c.customer_id = o.customer_id
WHERE o.status = 'completed'
```
- Filters after the join
- Removes NULLs → behaves like INNER JOIN

### Row Explosion

If you run:
```
SELECT *
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN payments p ON o.order_id = p.order_id;
```

You created a multiplicative join (row explosion): customer × orders × payments

Fix (aggregate before join):
```
WITH payment_totals AS (
    SELECT order_id, SUM(amount) AS total_paid
    FROM payments
    GROUP BY order_id
)
SELECT *
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
LEFT JOIN payment_totals p ON o.order_id = p.order_id;
```

### Find customers who do NOT have any orders

```
SELECT c.*
FROM customers c
LEFT JOIN orders o
    ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL;
```

## What are What Window Functions?

https://medium.com/@manutej/mastering-sql-window-functions-guide-e6dc17eb1995

A window function performs a calculation across a set of table rows that are somehow related to the current row. 
This is comparable to the type of calculation that can be done with an aggregate function. 
But unlike regular aggregate functions, use of a window function does not cause rows to become grouped into a single output row — the rows retain their separate identities. 
Behind the scenes, the window function is able to access more than just the current row of the query result.

Window functions apply to aggregate and ranking functions over a particular window (set of rows). OVER clause is used with window functions to define that window. OVER clause does two things : 
- Partitions rows to form a set of rows. (PARTITION BY clause is used) 
- Orders rows within those partitions into a particular order. (ORDER BY clause is used) 

The most practical example of this is a running total:
```
SELECT duration_seconds, SUM(duration_seconds) OVER (ORDER BY start_time) AS running_total
  FROM tutorial.dc_bikeshare_q1_2012
```

You can see that the above query creates an aggregation (running_total) without using GROUP BY.

Adding OVER designates it as a window function. __You could read the above aggregation as "take the sum of duration_seconds over the entire result set, in order by start_time."__

If you'd like to narrow the window from the entire dataset to individual groups within the dataset, you can use PARTITION BY to do so:
```
SELECT start_terminal,
       duration_seconds,
       SUM(duration_seconds) OVER
         (PARTITION BY start_terminal ORDER BY start_time)
         AS running_total
  FROM tutorial.dc_bikeshare_q1_2012
 WHERE start_time < '2012-01-08'
```

### Example 1: Find average salary of employees for each department and order employees within a department by age. 
```
SELECT Name, Age, Department, Salary, AVG(Salary) OVER( PARTITION BY Department) AS Avg_Salary
FROM employee
```
Result:
| Name 	  | Age   |	Department 	  | Salary 	  | Avg_Salary
|---------|-------|---------------|-----------|-----------
| Ramesh 	| 20 	  | Finance 	    | 50,000 	  | 40,000
| Suresh 	| 22 	  | Finance 	    | 50,000 	  | 40,000
| Ram 	  | 28 	  | Finance 	    | 20,000 	  | 40,000
| Deep 	  | 25 	  | Sales 	      | 30,000 	  | 25,000
| Pradeep |	22 	  | Sales 	      | 20,000 	  | 25,000

### Example 2: Calculate the average session duration for each session type?

Instead of this:
```
SELECT session_type, avg(session_end - session_start) AS duration
FROM twitch_sessions
GROUP BY session_type

```

Do this:

```
SELECT *, avg(session_end -session_start) OVER () AS duration
FROM twitch_sessions
```

### Example 3: Find the current salary of each employee assuming that salaries increase each year.

Instead of this:
```
SELECT id, first_name, last_name, department_id, max(salary)
FROM ms_employee_salary
GROUP BY id, first_name, last_name, department_id
```

Do this:

```
SELECT DISTINCT id, first_name, last_name, department_id, max(salary) OVER(PARTITION BY id, first_name, last_name, department_id)
FROM ms_employee_salary
```

## CTE

https://www.geeksforgeeks.org/cte-in-sql/

The common table expression (CTE) is a temporary named result set that you can reference within a SELECT, INSERT, UPDATE, or DELETE statement.

CTEs act as virtual tables (with records and columns) that are created during query execution, used by the query, and deleted after the query executes

```
WITH my_cte AS (
  SELECT a,b,c
  FROM T1
)
SELECT a,c
FROM my_cte
WHERE ....
```

OR

```
WITH highest AS (
  SELECT
    branch,
    date,
    MAX(unit_price) AS highest_price
  FROM sales
  GROUP BY branch, date
)
SELECT
  sales.*,
  h.highest_price
FROM sales
JOIN highest h
  ON sales.branch = h.branch
    AND sales.date = h.date
```

A __recursive__ CTE is one that references itself within that CTE. The recursive CTE is useful when working with hierarchical data as the CTE continues to execute until the query returns the entire hierarchy.

```
WITH RECURSIVE  cte_name AS (
     CTE_query_definition  -- non recursive query term
UNION ALL
     CTE_query_definition  -- recursive query term
)
SELECT * FROM cte_name;
```

Count up until 3
```
WITH countUp AS ( 
    SELECT 1 as n
    UNION ALL
    SELECT n+1 FROM countUp WHERE n<3
)
SELECT * FROM countUp
```

Find ancestors:
```
with name_tree as (
   select id, parent_id, name
   from the_unknown_table
   where id = 1 -- this is the starting point you want in your recursion
   union all
   select c.id, c.parent_id, c.name
   from the_unknown_table c
     join name_tree p on p.parent_id = c.id  -- this is the recursion
) 
select *
from name_tree
where id <> 1; -- exclude the starting point from the overall result

```

## Tests

https://www.windowfunctions.com


## Interview Questions

### UPDATE from a SELECT statement

```
UPDATE Per
SET 
Per.PersonCityName=Addr.City, 
Per.PersonPostCode=Addr.PostCode
FROM Persons Per
INNER JOIN
AddressList Addr
ON Per.PersonId = Addr.PersonId
```

```
UPDATE Persons
SET  Persons.PersonCityName=(SELECT AddressList.PostCode
                            FROM AddressList
                            WHERE AddressList.PersonId = Persons.PersonId)
```

### Repeated Payments

Stripe asked this tricky SQL interview question, about identifying any payments made at the same merchant with the same credit card for the same amount within 10 minutes of each other and reporting the count of such repeated payments.

| transaction_id	  | merchant_id	| credit_card_id	  | amount	| transaction_timestamp
|-------------------|-------------|-------------------|---------|----------------
| 1	                | 101	        | 1	                | 100   	| 09/25/2022 12:00:00
| 2	                | 101	        | 1	                | 100	    | 09/25/2022 12:08:00

```
WITH payments AS (
  SELECT 
    merchant_id, 
    EXTRACT(EPOCH FROM transaction_timestamp - LAG(transaction_timestamp) OVER( PARTITION BY merchant_id, credit_card_id, amount ORDER BY transaction_timestamp)
    )/60 AS minute_difference 
  FROM transactions) 

SELECT COUNT(merchant_id) AS payment_count
FROM payments 
WHERE minute_difference <= 10;
```
- EXTRACT pulls a specific component from a date/time or interval. 
- EPOCH: Give me the total time in second

### How Do You Filter GROUP BY Groups

After the filtering criteria are specified in __HAVING__, the query will return all the data that satisfies the criteria.

```
SELECT
  department,
  AVG(salary) AS average_salary
FROM salaries
GROUP BY department
HAVING AVG(salary) < 5500;
```

### Find the Top n Rows in SQL Using a Window Function and a CTE

The task here is to return the top three highest paid employees in each department, together with their salary and department.

```
WITH ranking AS (
  SELECT
    first_name,
    last_name,
    salary,
    department,
    DENSE_RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS salary_rank
  FROM salary
)
 
SELECT *
FROM ranking
WHERE salary_rank <= 3
ORDER BY department, salary_rank;
```

- DENSE_RANK: assigns a rank based on salary within each department
- PARTITION BY department
  - Resets ranking for each department
  - Each department is ranked independently
- ORDER BY salary DESC: Highest salary gets rank = 1

### Compute the Difference Between Two Rows (Delta) Using Window Functions

You need to show the actual revenue, time period, and monthly difference (delta) between the actual and the previous month.

```
SELECT
  actual_revenue,
  actual_revenue - LAG(actual_revenue) OVER (ORDER BY period ASC) AS monthly_revenue_change,    
 period
FROM revenue
ORDER BY period;
```
- LAG() returns the previous row’s value based on the ordering.
- ORDER BY period ASC:  Defines the sequence of rows


## Tests

https://www.windowfunctions.com/questions/over/

## References

https://learnsql.com/blog/advanced-sql-interview-questions/?gad_source=1

https://datalemur.com/blog/advanced-sql-interview-questions

