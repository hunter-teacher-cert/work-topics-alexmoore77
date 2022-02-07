Async Assignment:    

Create and post in the Slack at least one query from the challenge list below.  

SQL Challenge 1)  Intermediate - Write a query using the allCuts table to retrieve the list of all teachers whose classes are cut most often.

>>Skills Learned:  SELECT, GROUP BY, ORDER BY, aggregate functions, nested tables, calculated fields

Hint #1:  You will be using a nested query.  The query retrieves the allCuts table, which will be on the inside and surrounded by parentheses, and you will be selecting from this table.

Hint #2:  When you group by a field, every field in your returned table must be either that field or the result of an aggregate function.  For example, if you grouped by teacher, you could use the line SELECT teacher, COUNT(*) AS total FROM…

Hint #3:  Recall that GROUP BY must appear below the query that retrieves that allCuts table.

OR

SQL Challenge 2)  Easy - Use the allCuts table and the biographical table to retrieve a list of student cuts with outreach information sorted by guidance counselor.

>>Skills Learned:  SELECT, LEFT JOIN, nested tables, ORDER BY

Hint #1:  This is going to be a LEFT JOIN of the allCuts table and the biographical table because you want to include all students regardless of whether contact information is available for them in the biographical table.

Hint #2:  This LEFT JOIN is much easier than the allCuts INNER JOIN because the primary key and foreign key already exist as unique identifiers in the two tables.

Hint #3:  If you are retrieving a field that is named in both tables, you will need to indicate which version you are taking using syntax like this:  a.ID

OR

SQL Challenge 3)  Difficult - Write a query using the allCuts table to retrieve the list of sections of math that are cut most often.

>>Skills Learned:  SELECT, GROUP BY, HAVING, nested tables, logical operators, ORDER BY, IN()

Hint #1:  This will include GROUP BY, but you want to find a way to use only math classes.  Note that keyword HAVING is used with GROUP BY instead of WHERE.  

Hint #2:  You can use logical operators AND, OR, and NOT to be sure you are only including math class cuts.  Another way of doing this is to utilize the SQL IN() function.  

Hint #3:  You can sort descending to ensure that the math classes with the most cuts stand out.

OR

SQL Challenge 4)  Quite Difficult - Write a query using the allCuts table to retrieve a table listing every student with at least one cut and the number of times that student has cut class for each period of the day, the total number of cuts, and outreach information sorted by guidance counselor. 

>>Skills Learned:  SELECT, GROUP BY, HAVING, nested tables, IF(), ISNULL(), aggregate functions, self joins, calculated fields, aliasing

Hint #1:  You do not need to check for at least one cut because your allCuts table already provides this.  Instead, consider starting by using GROUP BY and HAVING with the aggregate function COUNT(*) to retrieve a table with a list of students who have cut first period and the number of times they have cut it.  Recall that you can GROUP BY multiple fields using the syntax GROUP BY field1, field2  On what fields will you group your data?

Hint #2:  Now you have cuts for first period, and you can run multiple queries to get cuts for second period, third period, etc.  The next step is to join these tables together using a self join.  You may want to alias your tables to make them easy to access.  On what field will you perform the self joins?

 Hint #3:  Now that you have all of this information, you need to display it and ensure that null values display 0 cuts for that period.  If you have aliased your grouped tables in a logical way, you can add fields such as the following:  pd1Table.cuts AS pd1, pd2Table.cuts AS pd2 …. pd1Table.cuts+pd2Table.cuts+pd3Table.cuts … AS Total
 
OR

SQL Challenge 5)  Coder’s Choice - Create any query that would retrieve data you believe a school administration may find to be useful in advancing student learning.


