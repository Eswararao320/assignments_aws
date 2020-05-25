Q1='''SELECT fname,lname FROM (Actor INNER JOIN Cast on `Cast`.pid = `Actor`.id) INNER JOIN Movie on `Movie`.id = `Cast`.mid WHERE `Movie`.id = 12148;'''
Q2='''SELECT COUNT(`Movie`.id) FROM (Movie INNER JOIN Cast on `Movie`.id = `Cast`.mid )INNER JOIN Actor on `Cast`.pid = `Actor`.id WHERE `Actor`.fname LIKE 'Harrison (I)' and `Actor`.lname LIKE 'Ford';'''      
Q3='''SELECT DISTINCT(`Actor`.id) FROM (Actor INNER JOIN Cast on `Cast`.pid = `Actor`.id) INNER JOIN Movie on `Movie`.id = `Cast`.mid WHERE `Movie`.name LIKE 'Young Latin Girls%';'''
Q4='''SELECT COUNT(DISTINCT `Actor`.id)FROM (Actor INNER JOIN Cast on `Cast`.pid = `Actor`.id) INNER JOIN Movie on `Movie`.id = `Cast`.mid WHERE year BETWEEN 1990 and 2000;'''

