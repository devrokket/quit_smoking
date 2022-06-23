import calendar
import sys
import datetime
from datetime import datetime
import pandas as pd

def my_calendar():
    print(calendar.calendar(2022))
    print(calendar.weekday(2022,5, 30))
    print(calendar.monthrange(2022, 5))

def my_datetime():
    date = datetime.date(2022,5,30)
    print(date)
    print(date.month)
    print(date.year)
    print(date.weekday())
    print(date.today)


print("[Creative Design Term Project]")
print("당신이 담배에 쓴 돈을 기록합니다.")
now = datetime.now().date()
print("오늘 날짜:", now)

totalCost = 0
cigarCost = 4500
cigarCount = int(input("담배 몇 갑을 구매하셨나요?"))


totalCost = cigarCount * cigarCost
print("사용자님이 지금까지 담배에 지출한 금액은 %d원입니다.", totalCost)
