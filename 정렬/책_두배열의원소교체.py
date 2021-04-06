# 두 개의 배열 AB를 가지고 있다 두 배열은 N개의 원소로 구성되어 있으며
# 배열 A, B를 서로 바꿔 최종적으로 합이 최대가 되게 하는 것

n, k = map(int, input().split()) # n,k 입력받기
a =list(map(int, input().split()))
b =list(map(int, input().split()))

a.sort() # 배열 A 오름차순으로 정렬
b.sort(reversed=True) # 배열 B 내림차순으로 정렬

# 첫 번째 인덱스부터 확인가능하며, 두 배열의 원소를 최대 k번 비교
for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else: # A의 원소가 B의 원소보다 크거나 반복문 탈출
        break

print(sum(a)) # 배열 A의 모든 원소의 합을 출력


