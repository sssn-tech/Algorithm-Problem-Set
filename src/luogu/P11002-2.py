from datetime import datetime
from datetime import timedelta

ST = datetime(1970, 1, 1, 0, 0, 0)
def last_ring(date_str: str, time_str: str, x: int) -> str:
    ed = datetime.strptime(date_str+' '+time_str, '%Y-%m-%d %H:%M:%S')
    delta = ed - ST
    minute_tot = int(delta.total_seconds() // 60)
    minute_rev = minute_tot % x
    
    ans = ed - timedelta(minutes=minute_rev)

    return ans.replace(second=0).strftime('%Y-%m-%d %H:%M:%S')
T = int(input())
for _ in range(T):
    date, time, x = input().split()
    print(last_ring(date, time, int(x)))
