# 퀵정렬은 기준을 설정한 다음 큰 수와 작은 수를 교환한 후 리스트를 반으로 
# 나누는 방식으로 동작한다
# 퀵정렬은 피벇이 사용된다
# 피벗: 큰 숫자와 작은 숫자를 교환할 때 교환하기 위한 기준

# 일반 퀵 정렬 코드
array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
    if start >= end: # 원소가 1개인 경우 종료
        return
    pivot = start # 피벗은 첫번째 원소
    left = start + 1
    right = end
    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right: # 엇갈렸다면 작은 데이터와 피벗을 ㄱ체
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰데이터를 교체
            array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽부분과 오른쪽 부분에서 각각 정렬수행
    quick_sort(array, start, right -1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)

#====================== 파이썬의 장점을 살린 퀵정렬 ==================
array = [5,6,9,0,3,1,6,2,4,8]

def q_sort(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <=1 :
        return array
    
    pivot = array[0] # 피벗은 첫번째 원소
    tail = array[1:] # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고 전체리스트를 반환함
    return q_sort(left_side) + [pivot] + q_sort(right_side)

print(q_sort(array))




