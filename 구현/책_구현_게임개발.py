######## 삼성전자에서 자주나오는 문제 유형 ############
# 일반적으로 방향을 설정해 이동하는 문제 유형은 dx, dy를 따로 정해서 한다

# map에 int와 input().split()을 넣으면 split의 결과를 모두 int변환
n,m = map(int, input().split()) # n*m으로 이뤄진 직사각형 맵
# 방향값을 d로 지정
# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]

# 현재 캐릭터의 x,y좌표 방향을 입력받기
x , y, direction = map(int, input().split())
d[x][y] = 1 # 현배 좌표 방문처리

# 전체 맵 정보를 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 동서남북 방향 정리, 방향을 움직이기 위한 dx, dy
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전 turn_left함수 사용
# 이때 global키워드를 사용했는데, 이는 정수형변수인 
# direction 변수가 함수 바깥에서 선언된 전역변수
# 북(0) 동(1) 남(2) 서(3)
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
# 이동할 때는 x = nx, 이동 못하면 nx = x -+ dx[direction]
count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 이후 정면에 가보지 않은 탄이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue

    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time  += 1
    # 네 방향 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        
        # 뒤로 바다가 막혀있는 경우
        else:
            break
        turn_time = 0
# 정답출력
print(count)











