# 일단 h 먼저 정의
h = int(input())

# 전체 시, 분, 초의 경우의 수는 24*60*60
# 3중 반복문을 이용해 계산할 수 있다.

count = 0
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            # 만약 3이라는 숫자가 들어간다는 것 가정
            if '3' in str(i) + str(j) + str(k):
                count += 1


print(count)





