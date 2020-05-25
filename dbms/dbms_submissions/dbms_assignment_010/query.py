Q1 = '''SELECT  P.PLAYER_ID, MC.TEAM_ID, P.JERSEY_NO, P.NAME,P.DATE_OF_BIRTH, P.AGE FROM MATCHCAPTAIN AS MC JOIN PLAYER AS P ON MC.CAPTAIN = P.PLAYER_ID left JOIN GOALDETAILS AS GD ON GD.PLAYER_ID = MC.CAPTAIN WHERE GOAL_ID IS NULL'''
Q2='''select team_id,count(match_no) from matchteamdetails group by team_id;'''
Q3='''select team_id ,count(goal_id)*1.0/(select count(player_id) from player group by team_id) as avg_goal_score from goaldetails  group by team_id;'''
Q4='''select captain,count(match_no) from matchcaptain inner join player on `matchcaptain`.team_id = `player`.team_id where `player`.player_id=`matchcaptain`.captain group by `matchcaptain`.captain;'''
Q5='''select count (DISTINCT captain) from  match as m inner join matchcaptain as mc on m.match_no = mc.match_no where mc.captain = m.player_of_match;'''
Q6='''select p.player_id from player as p where exists (select captain from matchcaptain where captain=p.player_id) and not exists (select player_of_match from match where p.player_id=player_of_match);'''
Q7='''select strftime ('%m',play_date)as a,count(match_no) from match group by a;'''
#Q8='''SELECT JERSEY_NO,COUNT(CAPTAIN) AS NO_CAPTAINS FROM MATCHCAPTAIN MC JOIN PLAYER P ON MC.CAPTAIN = P.PLAYER_ID GROUP BY JERSEY_NO ORDER BY NO_CAPTAINS DESC, JERSEY_NO DESC;'''
Q8='''select jersey_no,count(captain) as no_captains from matchcaptain as mc inner join player as p on mc.team_id =p.team_id where p.player_id = mc.captain group by jersey_no order by no_captains DESC,jersey_no DESC;'''  
Q9='''select p.player_id,AVG(audience) from player as p inner join matchteamdetails as mtd on p.team_id =mtd.team_id inner join match as m on m.match_no = mtd.match_no group by p.player_id order by AVG(audience) DESC,p.player_id DESC;'''
Q10='''select team_id ,avg(age) from player group by team_id;'''
Q11='''select avg(age) from matchcaptain inner join player on player.team_id=matchcaptain.team_id where captain = player.player_id;'''
Q12='''select strftime ('%m',date_of_birth)as month,count(player_id) as no_of_players from player group by month order by no_of_players DESC,month DESC;'''
Q13='''SELECT CAPTAIN ,COUNT(win_lose) NO_OF_WINS FROM MATCHTEAMDETAILS MTD JOIN MATCHCAPTAIN MC ON MTD.MATCH_NO = MC.MATCH_NO WHERE WIN_LOSE ="W" AND MTD.TEAM_ID = MC.TEAM_ID GROUP BY CAPTAIN ORDER BY  NO_OF_WINS DESC;'''

