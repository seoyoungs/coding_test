# 상하좌우 문제와 비슷
## 상하좌우는 x,y형태로 쓰였으면 여기서는 step이 대신한다.
# 체스판은 8*8로 구성되있고
# 나이트는 2가지 경로로 움직일 수 있다
# 1. 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
# 2. 수직으로 두칸 이동한 뒤에 수평으로 한 칸 이동하기

# 현재나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1 # 아스키 코드 값으로 1~9까지 만듬
# int(ord(input_data[0])) → 는 a,b,c, 등등 열이 주어질때 
# 그열의 아스키코드값을 정수로 나타냄을 의미한다.
# int(ord(‘a’)) + 1 -> 현재 열의 위치에서 첫번째 값인 a번째를 빼고 
# +1 을해야 현재위치를 나타내는 열의값을 알수있다. (정수로표현함)

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1)]

# 8가지 방향에 대해 각 위치로 이동해 가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1
print(result)


