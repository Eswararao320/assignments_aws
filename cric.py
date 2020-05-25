class match:
    def __init__(self,players_count,total_score,ball_count,overs):
        self.batsman_score=0
        self.total_score=0
        self.overs=0.0
        self.ball_count=0.1
        
    def bowling (self):
        self.batsman_score+=1
        self.ball_count+=0.1
        if self.ball_count<=0.6:
            self.ball_count=0.0
            self.overs=self.overs+1.0+self.ball_count
        else:
            self.overs=self.ball_count
        
    def over (self):
        self.overs+=self.ball_count
    