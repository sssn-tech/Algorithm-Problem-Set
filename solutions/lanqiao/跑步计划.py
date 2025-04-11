# 日期题, python逃课

from datetime import datetime
from datetime import timedelta

start = datetime(2023, 1, 1, 0, 0, 0)
end = datetime(2024, 1, 1, 0, 0, 0)
one_day = timedelta(days=1)

def run5(t: datetime) -> bool:
    if '1' in str(t.year) or '1' in str(t.month) or '1' in str(t.day) or t.weekday() == 0:
        return True
    return False

ans = 0
while start != end:
    # print(f'{start}', end='')
    if run5(start):
        ans += 5
        # print(f'{start}run 5')
    else:
        ans += 1
        # print('run 1')
    start += one_day

print(ans)