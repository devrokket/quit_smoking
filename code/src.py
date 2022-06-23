# [Creative Design]_Term-project
## 담뱃값 누적 계산기
import datetime # Please download module of 'datetime' 

totalCost = 0
cigarCost = 4500
totalCigar = 0

print("[Creative Design Term Project]", "당신이 담배에 쓴 돈을 기록합니다")

while True:
    dt_now = datetime.datetime.now()
    print("담배를 구입한 시각:",dt_now)

    
    cigarCount = int(input("오늘은 담배 몇 갑을 구매하셨나요?"))
    if cigarCount == 0:
        print("돛대가 아니군요!")
    else:
        totalCost = totalCost + cigarCount * cigarCost
        totalCigar = totalCigar + cigarCount

    print("사용자님이 지금까지 구입한 담배 갑 수는 %d갑 입니다."%totalCigar)
    print("사용자님이 지금까지 담배에 지출한 금액은 %d원입니다.\n"%totalCost)
    
    ending = str(input("프로그램을 종료하려면 '종료'를 입력하세요.\n"))
    
    if ending =='종료':
        break
    else:
        continue

if totalCost >= 1000000:
    print("지금까지 담배에 쓴 돈이 100만원을 넘겼습니다..!")
