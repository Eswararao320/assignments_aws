{"filter":false,"title":"query.py","tooltip":"/dbms/dbms_submissions/dbms_assignment_010/query.py","undoManager":{"mark":6,"position":6,"stack":[[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":2}],[{"start":{"row":0,"column":0},"end":{"row":3,"column":24},"action":"insert","lines":["Q1 = '''SELECT  P.PLAYER_ID, MC.TEAM_ID, P.JERSEY_NO, P.NAME,P.DATE_OF_BIRTH, P.AGE ","FROM MATCHCAPTAIN AS MC JOIN PLAYER AS P ON MC.CAPTAIN = P.PLAYER_ID","left JOIN GOALDETAILS AS GD ON GD.PLAYER_ID = MC.CAPTAIN","WHERE GOAL_ID IS NULL'''"],"id":3}],[{"start":{"row":0,"column":84},"end":{"row":1,"column":0},"action":"remove","lines":["",""],"id":4}],[{"start":{"row":0,"column":152},"end":{"row":1,"column":0},"action":"remove","lines":["",""],"id":5}],[{"start":{"row":0,"column":152},"end":{"row":0,"column":153},"action":"insert","lines":[" "],"id":6}],[{"start":{"row":0,"column":209},"end":{"row":1,"column":0},"action":"remove","lines":["",""],"id":7}],[{"start":{"row":0,"column":209},"end":{"row":0,"column":210},"action":"insert","lines":[" "],"id":8}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":0,"column":210},"end":{"row":0,"column":210},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1589456214286,"hash":"aba127a4e2c210b1c4b9ecf3adfcb1d9db902e1f"}