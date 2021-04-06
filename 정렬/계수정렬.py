# 특정한 데이터에서만 사용이 가능하나 매우 빠른 정려 알고리즘이다
# 보통 성적 데이터 같은 곳에 많이 쓰인다

array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

# 모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1 # 각 데이터에 해당하는 인덱스의 값 증가

for i in range(len(count)): # 리스트에 기록된 정렬 정보 확인
    for j in range(count[i]):
        print(i, end='') # 띄워쓰기를 구분으로 횟수만큼 인덱스 출력






