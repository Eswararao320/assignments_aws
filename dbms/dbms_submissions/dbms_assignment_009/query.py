Q1='''SELECT AVG(age) from Player;'''
Q2='''SELECT match_no,play_date FROM Match WHERE audience > 50000 ORDER BY match_no ASC;'''
Q3='''select team_id,count(win_lose) from matchteamdetails where win_lose = 'W' group by team_id order by count(win_lose) DESC;'''
Q4='''select match_no,play_date from match where stop1_sec > (select AVG(stop1_sec) from match) order by match_no DESC;'''
Q5='''SELECT `Match`.match_no,`Team`.name,`Player`.name FROM Team INNER JOIN MatchCaptain on `Team`.team_id = `MatchCaptain`.team_id INNER JOIN Player on `MatchCaptain`.captain = `Player`.player_id INNER JOIN Match on `Match`.match_no=`MatchCaptain`.match_no WHERE captain = player_id ORDER BY `Match`.match_no ASC,`Team`.name ASC ;'''                  
Q6='''SELECT `match`.match_no,`player`.name,`player`.jersey_no FROM match INNER JOIN player on `player`.player_id = `match`.player_of_match  ORDER BY `match`.match_no ASC;''' 
Q7='''SELECT `team`.name,avg(age) from team inner join player on `player`.team_id = `team`.team_id group  by `team`.team_id having avg(age)>26;'''
Q8='''select `player`.name,jersey_no,age,count(goal_id) from player inner join goaldetails on `goaldetails`.player_id = `player`.player_id where age <= 27 group by `player`.player_id having count(goal_id) >=1 order by count(goal_id) DESC,`player`.name ASC;'''
### ulter native model Q8='''select `player`.name,jersey_no,age,count(goal_score) from player inner join goaldetails on `goaldetails`.player_id = `player`.player_id inner join match on `match`.match_no = `goaldetails`.match_no where age <= 27 group by `player`.player_id having count(goal_score) >=1 order by count(goal_score) DESC,`player`.name ASC;'''
Q9='''select team_id,(count(goal_id)*100.0/(select count(goal_id) FROM goaldetails))as count FROM goaldetails GROUP BY team_id ;'''
Q10='''select AVG(c) from (select count(goal_id) as c from goaldetails group by team_id);'''
Q11='''select player_id,name,date_of_birth from player where not exists (select goaldetails .player_id from goaldetails where `goaldetails`.player_id = `player`.player_id);'''
Q12='''select `team`.name,`match`.match_no,`match`.audience,`match`.audience - (select avg(`match`.audience) from match inner join matchteamdetails on `match`.match_no=`matchteamdetails`.match_no  WHERE`team`.team_id=`matchteamdetails`.team_id) as a_a from team inner join matchteamdetails on `team`.team_id=`matchteamdetails`.team_id inner join match on `match`.match_no=`matchteamdetails`.match_no;'''