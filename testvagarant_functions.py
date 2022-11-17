class ipl:
    def __int__(self):
        self.ipl_dic={}
    def addpoints(self,team,points):
        if  team in self.ipl_dic.keys():
            lst=[points]
            self.ipl_dic={team:lst}
        else:
            self.ipl_dic[points].extend(points)
    def two_consecutive_losses(self):
        lst=[]
        for team,points in self.ipl_dic.items():
            if points[0]==0 and points[1]==0:
                lst.append(team)
        return lst

    def n_consecutive_losses(self,n):
        lst_win=[]
        lst_loss=[]
        for team,points in self.ipl_dic.items():
            for i in range(n):
                if points[i]==0:
                    pass
                
                else:
                    break
            else:
                lst_loss.append(team)
            for i in range(n):
                if points[i]==1:
                    pass
                
                else:
                    break
            else:
                lst_win.append(team)

    def average(self,team):
        d={}
        for team_name in team:
            sum1=0
            for teams,points in self.ipl_dic.items():
                if teams==team_name:
                    for i in points:
                        sum1+=i
                    d{teams}=sum1/len(points)






    


    


