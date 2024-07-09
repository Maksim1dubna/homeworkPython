from datetime import datetime
class SuperDate:
    def __init__(self, datearg):
        self.datearg = datearg

    def get_season(self):
        m = self.datearg.month
        x = m % 12 // 3 + 1
        if x == 1:
            season = print("Winter")
        if x == 2:
            season = print("Spring")
        if x == 3:
            season = print("Summer")
        if x == 4:
            season = print("Autumn")
        return season
    def get_time_of_day(self):
        x = self.datearg.hour
        if x>=6 and x<=12:
            time = print("Morning")
        if x>=12 and x<=18:
            time = print("Day")
        if x>=18 and x<=0:
            time = print("Evening")
        if x>=0 and x<=6:
            time = print("Night")
        return time


x = SuperDate(datetime(2023,12,1, 6))
x.get_season()
x.get_time_of_day()
