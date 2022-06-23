# [Creative Design]_Term-project
## 담뱃값 누적 계산기
import time
import datetime

totalCost = 0
totalCigar = 0
cigarCost = 4500

print("[Creative Design Term Project]")
print("당신이 담배에 쓴 돈을 기록합니다.")

while True:
    cigarCount = int(input("오늘은 담배 몇 갑을 구매하셨나요?"))
    if cigarCount == 0:
        print("돛대가 아니었군요!")
    else:
        totalCost = totalCost + cigarCount * cigarCost
        totalCigar = totalCigar + cigarCount
        
    print("사용자님이 지금까지 구입한 담배 갑 수는 %d갑 입니다."%totalCigar)
    print("사용자님이 지금까지 담배에 지출한 금액은 %d원입니다.\n"%totalCost)
    
