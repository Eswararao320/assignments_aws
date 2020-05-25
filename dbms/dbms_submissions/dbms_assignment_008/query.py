Q1 ='''SELECT d.id,d.fname FROM Director as d where not exists 
(select md.did FROM MovieDirector md INNER JOIN Movie m on md.mid=m.id 
where d.id=md.did and m.year < 2000) and exists(select md.did FROM 
MovieDirector md INNER JOIN movie m on md.mid=m.id where d.id=md.did and 
m.year > 2000) ORDER BY d.id  ASC;'''

Q2 = '''SELECT di.fname,(select m.name from moviedirector md inner join 
movie m on m.id=mid inner join director d on did=d.id where d.id=di.id 
order by rank desc limit 1) as name from director di limit 100;'''

Q3='''select * from actor as A where not exists (select m.id from movie 
as m inner join cast as c on m.id=c.mid where A.id=c.pid and m.year 
between 1990 and 2000) order by A.id DESC limit 100 ;'''


