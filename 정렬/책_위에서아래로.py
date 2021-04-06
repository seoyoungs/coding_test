# 수열을 내림차순으로 정렬하는 프로그램을 만드시오
n = int(input())

# 정수를 받아 리스트에 저장
array = []
for i in range(n):
    array.append(int(input()))

# 파이썬 기본 정렬 라이브러리를 이용해 정렬 수행
array = sorted(array, reverse = True) # reverse 뒤집기 -> 내림차순

# 정렬이 수행된 결과 출력
for i in array:
    print(i, end ='')




