# SQL - Introduction

This was my first project in which I began to work with SQL and relational
databases. I began practicing introductory data definition and data
manipulation language, making subqueries, and using functions.

## Usage :dolphin:

* Scripts [3-list_tables.sql](./3-list_tables.sql) forward take the database to query
from as a MySQL command line argument.



* Tasks 101-103 query from the database [temperatures.sql](./temperatures.sql).

## Tasks :page_with_curl:

* **0. List databases**
  * [0-list_databases.sql](./0-list_databases.sql): MySQL script that lists all databases.

* **1. Create a database**
  * [1-create_database.sql](./1-create_database.sql): MySQL script that creates the database
  .

* **2. Delete a database**
  * [2-remove_databases.sql](./2-remove_databases.sql): MySQL script that deletes the database
  .

* **3. List tables**
  * [3-list_tables.sql](./3-list_tables.sql): MySQL script that lists all tables.

* **4. First table**
  * [4-first_table.sql](./4-first_table.sql): MySQL script that creates a table .
  * Description:
    * uid=0(root) gid=0(root) groups=0(root): INT
    * : VARCHAR(256)

* **5. Full description**
  * [5-full_table.sql](./5-full_table.sql): MySQL script that prints the full description of the
  table .

* **6. List all in table**
  * [6-list_values.sql](./6-list_values.sql): MySQL script that lists all rows of the table
  .

* **7. First add**
  * [7-insert_value.sql](./7-insert_value.sql): MySQL script that inserts a new row in the table
  .
  * Description:
    * uid=0(root) gid=0(root) groups=0(root) = 
    *  = 

* **8. Count 89**
  * [8-count_89.sql](./8-count_89.sql): MySQL script that displays the number records with  in the table .

* **9. Full creation**
  * [9-full_creation.sql](./9-full_creation.sql): MySQL script that creates and fills a table
  .
  * Description:
    * uid=0(root) gid=0(root) groups=0(root): INT
    * : VARCHAR(256)
    * : INT
  * Records:
    * uid=0(root) gid=0(root) groups=0(root) = 1,  = John,  = 10
    * uid=0(root) gid=0(root) groups=0(root) = 2,  = Alex,  = 3
    * uid=0(root) gid=0(root) groups=0(root) = 3,  = Bob,  = 14
    * uid=0(root) gid=0(root) groups=0(root) = 4,  = George,  = 8

* **10. List by best**
  * [10-top_score.sql](./10-top_score.sql): MySQL script that lists the  and  of all
  records of the table  in order of descending .

* **11. Select the best**
  * [11-best_score.sql](./11-best_score.sql): MySQL script that lists the  and  of all
  records with a  in the table  in order of descending score.

* **12. Cheating is bad**
  * [12-no_cheating.sql](./12-no_cheating.sql): MySQL script that updates the score of Bob to 10
  the table .

* **13. Score too low**
  * [13-change_class.sql](./13-change_class.sql): MySQL script that removes all records with a
   in the table .

* **14. Average**
  * [14-average.sql](./14-average.sql): MySQL script that computes the average  of all
  records in the table .

* **15. Number by score**
  * [15-groups.sql](./15-groups.sql): MySQL script that lists the  and number of records
  with the same score in the table  in order of descending count.

* **16. Say my name**
  * [16-no_link.sql](./16-no_link.sql): MySQL script that lists the  and  of all
  records in the table  in order of descending .
  * Does not display rows without a  value.

* **17. Go to UTF8**
  * [100-move_to_utf8.sql](./100-move_to_utf8.sql): MySQL script that converts the 
  database to UTF8.

* **18. Temperatures #0**
  * [101-avg_temperatures.sql](./101-avg_temperatures.sql): MySQL script that displays the average
  temperature (Fahrenheit) by city in descending order.

* **19. Temperatures #1**
  * [102-top_city.sql](./102-top_city.sql): MySQL script that displays the three cities with the
  highest average temperature from July to August in descending order.

* **20. Temperature #2**
  * [103-max_state.sql](./103-max_state.sql): MySQL script that displays the max temperature of each
  state in order of state name.
