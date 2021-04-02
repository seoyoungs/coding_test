# 좌표 이동할 때 쓰는 코드

# N입력받기
n = int(input())

# (x,y) 좌표이므로 (1,1)부터 시작

x, y = 1, 1
plans = input().split()

# 상하좌우 언급
dx = [0, 0, -1, 1] # x 이동 좌표
dy = [-1, 1, 0, 0] # y 이동 좌표
wh = ['L', 'R', 'U', 'D'] # 상하좌우

# 이동을 한개씩
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(wh)):
        if plan == wh[i]:
            nx = x + dx[1]
            ny = y + dy[1] # 이동 하나씩 하는 것 언급
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동수행
    x, y =nx, ny

print(x,y)





