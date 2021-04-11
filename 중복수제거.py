\
# 중복수 제거
def solution(arr):
    answer = []
    for i in arr:
        if i not in answer:
            answer.append(i)
    print('Hello Python')
    return answer

# 짝수단위 중복 수 제거
def solution(arr):
    answer = []
    answer.append(arr[0]) 
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]: # 앞뒤 두개씩 비교
            answer.append(arr[i]) # 같으면 한개만 출력
    print('Hello Python')
    return answer


