Q1='''select a.id,a.fname,a.lname,a.gender from actor as a inner join cast  as c on a.id = c.pid inner join movie as m on m.id = c.mid where m.name  LIKE 'Annie%';'''
Q2='''select m.id,m.name,m.rank,m.year from movie as m inner join moviedirector as md on md.mid = m.id inner join director as d on d.id = md.did where d.fname = 'Biff' and d.lname = 'Malibu'  and m.year in (1999, 1994, 2003) order by m.rank DESC ,m.year ASC;'''
Q3='''select year ,count(id) from movie group by year having (select avg(rank) from movie) < avg(rank) ;'''
Q4='''select id,name,year,rank from movie where year = 2001  and rank < (select avg(rank) from movie) order by rank DESC limit 10;'''
Q7='''select fname,count(id) as count from director  group by fname having count > 1;'''
Q6='''select DISTINCT a.id from actor as a inner join cast  as c on a.id = c.pid inner join movie as m on m.id = c.mid group by m.id,a.id having count(DISTINCT c.role) >1 order by a.id ASC limit 100;'''
Q8='''SELECT id,fname,lname FROM Director
        WHERE EXISTS(SELECT * FROM Cast INNER JOIN MovieDirector ON 
        `MovieDirector`.mid=`Cast`.mid WHERE `Director`.id=`MovieDirector`.did
        GROUP BY `MovieDirector`.did,`Cast`.mid HAVING COUNT(DISTINCT `Cast`.pid)>=100) AND 
        NOT EXISTS(SELECT * FROM Cast INNER JOIN MovieDirector ON
        `MovieDirector`.mid=`Cast`.mid WHERE `Director`.id=`MovieDirector`.did
        GROUP BY `MovieDirector`.did,`Cast`.mid HAVING COUNT(DISTINCT `Cast`.pid)<100);'''