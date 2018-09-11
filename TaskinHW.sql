## Homework Assignment

--* 1a. Display the first and last names of all actors from the table `actor`. 

	SELECT first_name,
			last_name
	FROM actor;

--* 1b. Display the first and last name of each actor in a single column in upper case letters. Name the column `Actor Name`. 

    SELECT UPPER(CONCAT(first_name," ",last_name)) AS 'Actor_name'
    FROM actor;

--* 2a. You need to find the ID number, first name, and last name of an actor, of whom you know only the first name, "Joe." What is one query would you use to obtain this information?

    SELECT actor_id, first_name, last_name
    FROM actor
    WHERE first_name = 'Joe';
  	
--* 2b. Find all actors whose last name contain the letters `GEN`:

    SELECT  actor_id, 
            first_name, 
            last_name
    FROM    actor
    WHERE   last_name LIKE '%GEN%';
  	
--* 2c. Find all actors whose last names contain the letters `LI`. This time, order the rows by last name and first name, in that order:

    SELECT 	actor_id,
            first_name,
		    last_name
    FROM actor
    WHERE last_name LIKE '%LI%'
    ORDER BY last_name, first_name;

--* 2d. Using `IN`, display the `country_id` and `country` columns of the following countries: Afghanistan, Bangladesh, and China:

    SELECT country_id, country
    FROM country
    WHERE country IN ('Afghanistan', 'Bangladesh', 'China');

--* 3a. Add a `middle_name` column to the table `actor`. Position it between `first_name` and `last_name`. Hint: you will need to specify the data type.

    ALTER TABLE actor
    ADD COLUMN middle_name varchar(50) AFTER first_name;
  	
--* 3b. You realize that some of these actors have tremendously long last names. Change the data type of the `middle_name` column to `blobs`.

    ALTER TABLE actor
    MODIFY COLUMN middle_name blob;

--* 3c. Now delete the `middle_name` column.

    ALTER TABLE actor
    DROP COLUMN middle_name;

--* 4a. List the last names of actors, as well as how many actors have that last name.

    SELECT      last_name, 
                COUNT(last_name) AS 'Count_of_last_name'
    FROM        actor
    GROUP BY    last_name;
  	
--* 4b. List last names of actors and the number of actors who have that last name, but only for names that are shared by at least two actors

    SELECT      last_name, 
                COUNT(last_name) AS 'Count_of_last_name'
    FROM        actor
    GROUP BY    last_name
    HAVING COUNT(last_name) >1;
  	
--* 4c. Oh, no! The actor `HARPO WILLIAMS` was accidentally entered in the `actor` table as `GROUCHO WILLIAMS`, the name of Harpo's second cousin's husband's yoga teacher. Write a query to fix the record.

    UPDATE TABLE
    SET first_name = 'HARPO'
    WHERE first_name = 'GROUCHO'
    AND last_name = 'WILLIAMS';
  	
--* 4d. Perhaps we were too hasty in changing `GROUCHO` to `HARPO`. It turns out that `GROUCHO` was the correct name after all! In a single query, if the first name of the actor is currently `HARPO`, change it to `GROUCHO`. Otherwise, change the first name to `MUCHO GROUCHO`, as that is exactly what the actor will be with the grievous error. BE CAREFUL NOT TO CHANGE THE FIRST NAME OF EVERY ACTOR TO `MUCHO GROUCHO`, HOWEVER! (Hint: update the record using a unique identifier.)

    UPDATE  actor
    SET     first_name =
    CASE
        WHEN    first_name = 'HARPO'
        THEN 'GROUCHO'
        ELSE    'MUCHO GROUCHO'
    END
    WHERE actor_id = 172 ;

--* 5a. You cannot locate the schema of the `address` table. Which query would you use to re-create it? 

  * Hint: [https://dev.mysql.com/doc/refman/5.7/en/show-create-table.html](https://dev.mysql.com/doc/refman/5.7/en/show-create-table.html)

  SHOW CREATE TABLE address;

--* 6a. Use `JOIN` to display the first and last names, as well as the address, of each staff member. Use the tables `staff` and `address`:

    SELECT      s.first_name, 
                s.last_name, 
                a.address
    FROM staff AS s
    LEFT JOIN address AS a
    ON s.address_id = a.address_id;

--* 6b. Use `JOIN` to display the total amount rung up by each staff member in August of 2005. Use tables `staff` and `payment`. 

  SELECT    s.first_name, 
            s.last_name, 
            SUM(p.amount)
  FROM      staff AS s
  INNER JOIN payment AS p
  ON        p.staff_id = s.staff_id
  WHERE MONTH(p.payment_date) = 08 AND YEAR(p.payment_date) = 2005
  GROUP BY  s.staff_id;

--* 6c. List each film and the number of actors who are listed for that film. Use tables `film_actor` and `film`. Use inner join.

    SELECT 	f.title,
            COUNT(fa.actor_id) AS '# of actors'
    FROM film AS f
    JOIN film_actor AS fa
    ON f.film_id = fa.film_id
    GROUP BY f.title
    ;
  	
--* 6d. How many copies of the film `Hunchback Impossible` exist in the inventory system?

    SELECT f.title, COUNT(inventory_id) AS 'Inventory stock'
    FROM film as f
    JOIN inventory as i
    ON  f.film_id = i.film_id
    WHERE f.title = 'Hunchback Impossible';

--* 6e. Using the tables `payment` and `customer` and the `JOIN` command, list the total paid by each customer. List the customers alphabetically by last name:

    SELECT c.last_name, c.first_name, SUM(p.amount) AS 'Total $ Received'
    FROM payment AS p
    JOIN customer AS c
    ON p.customer_id = c.customer_id
    GROUP BY c.customer_id
    ORDER BY c.last_name, c.first_name;



--* 7a. The music of Queen and Kris Kristofferson have seen an unlikely resurgence. As an unintended consequence, films starting with the letters `K` and `Q` have also soared in popularity. Use subqueries to display the titles of movies starting with the letters `K` and `Q` whose language is English. 

    SELECT f.title
    FROM film as f
    JOIN language as l
    ON f.language_id = l.language_id
    WHERE f.title LIKE 'K%' OR f.title LIKE 'Q%'
    AND f.language_id in
    (
        SELECT language_id
        FROM language
        WHERE name = 'English'
    )
    ;

--* 7b. Use subqueries to display all actors who appear in the film `Alone Trip`.

    SELECT a.first_name, a.last_name
    FROM actor as a
    JOIN film_actor as fa 
    ON a.actor_id = fa.actor_id
    WHERE film_id IN
    (
        SELECT film_id
        FROM film
        WHERE title = 'Alone Trip'
    )
    ;

   
--* 7c. You want to run an email marketing campaign in Canada, for which you will need the names and email addresses of all Canadian customers. Use joins to retrieve this information.

    SELECT first_name, last_name, email, country
    FROM customer AS cu
    JOIN address AS a
    ON cu.address_id = a.address_id
    JOIN city AS ci
    ON a.city_id = ci.city_id
    JOIN country AS co
    ON co.country_id = ci.country_id
    WHERE co.country = 'canada';

--* 7d. Sales have been lagging among young families, and you wish to target all family movies for a promotion. Identify all movies categorized as famiy films.

    SELECT title, c.name
    FROM film AS f
    JOIN film cateogry AS fc
    ON f.film_id = fc.film_id
    JOIN category as c
    ON c.category_id = fc.category_id
    WHERE name = 'family';

--* 7e. Display the most frequently rented movies in descending order.

    SELECT title, COUNT(title) AS 'Count_of_titles'
    FROM film AS f
    JOIN inventory AS i
    ON f.film_id = i.film_id
    JOIN rental AS r
    ON i.inventory_id = r.inventory_id
    GROUP by title
    ORDER BY rentals desc;
  	
--* 7f. Write a query to display how much business, in dollars, each store brought in.

    SELECT s.store_id, SUM(amount) AS 'Total_amount'
    FROM payment AS p
    JOIN rental AS r
    ON p.rental_id = r.rental_id
    JOIN inventory AS i
    ON i.inventory_id = r.inventory_id
    JOIN store AS s
    ON s.store_id = i.store_id
    GROUP BY s.store_id;	

--* 7g. Write a query to display for each store its store ID, city, and country.

    SELECT store_id, city, country
    FROM store AS s
    JOIN address AS a
    ON s.address_id = a.address_id
    JOIN city AS ci
    ON ci.city_id = a.city_id
    JOIN country co
    ON ci.country_id = co.country_id;	
  	
--* 7h. List the top five genres in gross revenue in descending order. (**Hint**: you may need to use the following tables: category, film_category, inventory, payment, and rental.)

    SELECT SUM(amount) AS 'Total_Sales', c.name AS 'Genre'
    FROM payment AS p
    JOIN rental AS r
    ON p.rental_id = r.rental_id
    JOIN inventory AS i
    ON r.inventory_id = i.inventory_id
    JOIN film_category AS fc
    ON i.film_id = fc.film_id
    JOIN category c
    ON fc.category_id = c.category_id
    GROUP BY c.name
    ORDER BY SUM(amount) DESC;
  	
--* 8a. In your new role as an executive, you would like to have an easy way of viewing the Top five genres by gross revenue. Use the solution from the problem above to create a view. If you haven't solved 7h, you can substitute another query to create a view.

    CREATE VIEW top_five_genres AS
    SELECT SUM(amount) AS 'Total_Sales', c.name AS 'Genre'
    FROM payment AS p
    JOIN rental AS r
    ON p.rental_id = r.rental_id
    JOIN inventory AS i
    ON r.inventory_id = i.inventory_id
    JOIN film_category AS fc
    ON i.film_id = fc.film_id
    JOIN category c
    ON fc.category_id = c.category_id
    GROUP BY c.name
    ORDER BY SUM(amount) DESC
    LIMIT 5;
  	
--* 8b. How would you display the view that you created in 8a?

  SELECT * 
  FROM top_five_genres;

--* 8c. You find that you no longer need the view `top_five_genres`. Write a query to delete it.

  DROP VIEW top_five_genres;
