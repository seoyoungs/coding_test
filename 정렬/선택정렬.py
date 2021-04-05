# 매번 작은 것을 선택한다는 의미에서 선택행렬이라고 한다

# 선택 정렬 소스 코드
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인덱스
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] # 스와프

print(array)
# 스와프 : 특정한 리스트가 주어졌을 때 두 변수의 위치를 변경하는 작업을 의미한다
# 데이터가 큰것에는 안쓰고 작은것에 자주쓰인다
# 알고리듬 문제풀이로는 좀 느리다

