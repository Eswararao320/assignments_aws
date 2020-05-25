Q1='''SELECT * from Movie ORDER BY rank DESC LIMIT 10;'''
Q2='''SELECT * from Movie ORDER BY rank DESC LIMIT 10,10;'''
Q3='''SELECT name from Movie WHERE year > 2004'''
Q4='''SELECT name from Movie WHERE rank < 1.1'''
Q5='''SELECT * FROM Movie WHERE year IN (2004,2005,2006);'''
Q6='''SELECT name,year FROM Movie WHERE name Like 'Harry%';'''
Q7='''SELECT * FROM Actor WHERE fname = 'Christin' and lname != 'Watson';'''
Q8='''SELECT * FROM Actor WHERE fname = 'Woody' and lname = 'Watson';'''
Q9='''SELECT name FROM Movie WHERE year IN (1990) and rank = 5;'''
Q10='''SELECT * FROM Actor WHERE fname = 'Christin' and lname = 'Watson';'''
Q11='''SELECT name FROM Movie WHERE year BETWEEN 2003 AND 2005;'''
Q12='''SELECT DISTINCT  year FROM Movie ORDER BY year ASC;'''
Q13='''SELECT * FROM Actor WHERE (fname = 'Christin' or lname = 'Watson') and (gender = 'M') LIMIT 10;'''
