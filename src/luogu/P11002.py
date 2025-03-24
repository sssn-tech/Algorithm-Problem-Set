from datetime import *
# 直接算出两个时间点中间有多少分钟

def isRun(year: int) -> bool:
    # 闰年: 能被4整除, 不能被100整除的是闰年, 此外, 被400整除的是闰年
    if year % 400 == 0:
        return True
    if year % 4 == 0 and year % 100 != 0:
        return True
    return False

def previous_ring(date: str, time: str, x: int) -> str:
    year_st, month_st, day_st = 1970, 1, 1
    hour_st, minute_st, _second_st = 0, 0, 0 # 秒数用不上
    year_ed, month_ed, day_ed = map(int, date.split('-'))
    hour_ed, minute_ed, _secon_ed = map(int, time.split(':'))

    minute_tot = 0
    for year in range(year_st, year_ed):
        if isRun(year):
            minute_tot += 60 * 24 * 366
        else:
            minute_tot += 60 * 24 * 365

    for month in range(month_st, month_ed):
        if isRun(year_ed) and month == 2:
            minute_tot += 60 * 24 * 29
        elif month == 2:
            minute_tot += 60 * 24 * 28
        elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            minute_tot += 60 * 24 * 31
        else:
            minute_tot += 60 * 24 * 30
    
    for day in range(day_st, day_ed):
        minute_tot += 60 * 24
    for hour in range(hour_st, hour_ed):
        minute_tot += 60
    minute_tot += minute_ed - minute_st # minute_st是0
    # 因为second_st是0, 所以无论如何也凑不齐整数分钟了, 忽略second_ed

    minute_rev = minute_tot % x # 需要把时钟往前拨minute_rev分钟
    # 因为数据保证了x <= 1000, 所以可以手动拨
    
    class Calender:
        def __init__(self, yr: int, mo: int, dy: int, hr: int, mn: int):
            self.year = yr
            self.month = mo
            self.day = dy
            self.hour = hr
            self.minute = mn
        
        def rev_1min(self) -> None:
            self.minute -= 1
            if self.minute < 0:
                self.minute = 59
                self.hour -= 1
                if self.hour < 0:
                    self.hour = 23
                    self.day -= 1
                    if self.day < 1:
                        self.month -= 1
                        if self.month < 1:
                            self.month = 12
                            self.year -= 1
                        if isRun(self.year) and self.month == 2:
                            self.day = 29
                        elif self.month == 2:
                            self.day = 28
                        elif self.month in [1, 3, 5, 7, 8, 10, 12]:
                            self.day = 31
                        else:
                            self.day = 30

        def show(self) -> str:
            return f'{self.year:04d}-{self.month:02d}-{self.day:02d} {self.hour:02d}:{self.minute:02d}:00'
        
    cal = Calender(year_ed, month_ed, day_ed, hour_ed, minute_ed)
    for i in range(minute_rev):
        cal.rev_1min()
    return cal.show()

T = int(input())
for i in range(T):
    date, time, x = input().split()
    x = int(x)
    print(previous_ring(date, time, x))