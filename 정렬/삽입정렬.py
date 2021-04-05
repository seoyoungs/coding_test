# 데이터가 거의 정렬이 되었을때 쓰이는게 좋음
# 삽입정렬은 두 번째 데이터 부터 시작

array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1, len(array)): # 인덳스 0(맨앞)은 고정 1부터 시작
    for j in range(i, 0, -1): # 인덱스 i부터 1까지 감소하여 반복하는 문법
        if array[j] < array[j-1]: # 한 칸씩 왼쪽으로 이동하는 코드 -1
            array[j], array[j-1] = array[j-1], array[j] # 스와프
        else: # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
          break
print(array)

