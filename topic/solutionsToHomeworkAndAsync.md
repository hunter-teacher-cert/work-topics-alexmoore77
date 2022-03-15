Solutions - Not to be shared with the class until after due date:
Homework:
SELECT p.First, p.Last, p.StudentID, p.Grade, ScanTime, Status, Date, CourseSection, Attendance, Teacher, Period
FROM scanTimes AS s
INNER JOIN periodAttendance AS p
ON s.StudentID=p.StudentID AND substr(ScanTime, 1,inStr(ScanTime, ' ')-1)=p.Date
WHERE Attendance='A'
ORDER BY p.Last, p.First  
---------------------------------------------------------------------------------  
Async Assignment 1:
SELECT Teacher, COUNT(*) AS Total
FROM
(
SELECT *
FROM scanTimes AS s
INNER JOIN periodAttendance AS p
ON s.StudentID=p.StudentID AND substr(ScanTime, 1,inStr(ScanTime, ' ')-1)=p.Date
WHERE Attendance='A'
) AS allCuts
GROUP BY Teacher
ORDER BY Total DESC  
---------------------------------------------------------------------------------  
Async Assignment 2:
SELECT b.First, b.Last, b.StudentID, Grade,ScanTime, Status, Date, CourseSection, Attendance, Teacher, Period, Parent1Phone, Parent2Phone, ParentEmail
FROM
(
SELECT *
FROM scanTimes AS s
INNER JOIN periodAttendance AS p
ON s.StudentID=p.StudentID AND substr(ScanTime, 1,inStr(ScanTime, ' ')-1)=p.Date
WHERE Attendance='A'
) AS allCuts
LEFT JOIN bio AS b
ON allCuts.StudentID=b.StudentID  
---------------------------------------------------------------------------------  
Async Assignment 3:
SELECT * FROM
(
SELECT courseSection, teacher, COUNT(*) AS totalCuts
FROM
(
SELECT *
FROM scanTimes AS s
INNER JOIN periodAttendance AS p
ON s.StudentID=p.StudentID AND substr(ScanTime, 1,inStr(ScanTime, ' ')-1)=p.Date
WHERE Attendance='A'
) AS allCuts
GROUP BY courseSection
HAVING substr(courseSection,1,1)='M'
) AS myTable2
WHERE teacher IN ('Siena, V', 'Jarding, T', 'Rael, S', 'Oto, T', 'Klar, S', 'Pylant, C')
ORDER BY totalCuts DESC  
---------------------------------------------------------------------------------  
Async Assignment 4:
SELECT First, Last, StudentID, MAX(Pd1) AS Pd1_, MAX(Pd2) AS Pd2_, MAX(Pd3) AS Pd3_, MAX(Pd4) AS Pd4_, MAX(Pd5) AS Pd5_, MAX(Pd6) AS Pd6_, MAX(Pd7) AS Pd7_, MAX(Pd8) AS Pd8_, MAX(Pd9) AS Pd9_,
MAX(Pd1)+MAX(Pd2)+MAX(Pd3)+MAX(Pd4)+MAX(Pd5)+MAX(Pd6)+MAX(Pd7)+MAX(Pd8)+MAX(Pd9) AS TotalCuts
FROM
(
SELECT First, Last, StudentID, Period, COUNT(*) AS Total,
IIF (Period=1, COUNT(*), 0) AS Pd1,
IIF (Period=2, COUNT(*), 0) AS Pd2,
IIF (Period=3, COUNT(*), 0) AS Pd3,
IIF (Period=4, COUNT(*), 0) AS Pd4,
IIF (Period=5, COUNT(*), 0) AS Pd5,
IIF (Period=6, COUNT(*), 0) AS Pd6,
IIF (Period=7, COUNT(*), 0) AS Pd7,
IIF (Period=8, COUNT(*), 0) AS Pd8,
IIF (Period=9, COUNT(*), 0) AS Pd9
FROM
(
SELECT *
FROM scanTimes AS s
INNER JOIN periodAttendance AS p
ON s.StudentID=p.StudentID AND substr(ScanTime, 1,inStr(ScanTime, ' ')-1)=p.Date
WHERE Attendance='A'
)
GROUP BY StudentID, Period
)
GROUP BY StudentID, First, Last
ORDER BY Last, First 