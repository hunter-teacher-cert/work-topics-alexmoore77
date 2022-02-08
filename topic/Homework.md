Homework Assignment:

 Write a SQL join query that retrieves from the tables shared with you the records of all of the unexcused period attendance absences in the school for the week of  1-31-22 sorted by student name ascending.  You will use the resulting table of results, which you can call allCuts, in the async assignment.
 
>>Skills Learned:  SELECT, JOIN, ORDER BY, calculated fields, concatenation  

Hint #1:  Consider a cut to be any instance of a student scanning into the building and being marked absent in a class.

Hint #2:  You want to do an inner join on the absence table and the scan table, but you have no unique primary key and foreign key to join on.  Would it be possible to join on a calculated field of the student ID concatenated with the date?

Hint #3:  Before you can make the inner join work on the concatenated student ID and date, you need to update the date in one table or the other so that the formats match.  How can we modify the date programmatically within a query?
