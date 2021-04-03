# a b; a와 b는 -100,000과 100,000 사이의 정수이다.
# 예제 입력 2 
# 4 5
# 예제 출력 2 
# 9

a, b = map(int, input().split())
print(a+b)

#  map에 int와 input().split()을 넣으면 split의 결과를 모두 int로 변환해줍니다
#  (실수로 변환할 때는 int 대신 float를 넣습니다.)
