'''
문제 설명
고고학자인 "튜브"는 고대 유적지에서 보물과 유적이 가득할 것으로 
추정되는 비밀의 문을 발견하였습니다. 
그런데 문을 열려고 살펴보니 특이한 형태의 자물쇠로 잠겨 있었고 
문 앞에는 특이한 형태의 열쇠와 함께 자물쇠를 푸는 방법에 대해 
다음과 같이 설명해 주는 종이가 발견되었습니다.

잠겨있는 자물쇠는 격자 한 칸의 크기가 1 x 1인 N x N 크기의 정사각 격자 형태이고 
특이한 모양의 열쇠는 M x M 크기인 정사각 격자 형태로 되어 있습니다.

자물쇠에는 홈이 파여 있고 열쇠 또한 홈과 돌기 부분이 있습니다. 
열쇠는 회전과 이동이 가능하며 열쇠의 돌기 부분을 
물쇠의 홈 부분에 딱 맞게 채우면 자물쇠가 열리게 되는 구조입니다. 
자물쇠 영역을 벗어난 부분에 있는 열쇠의 홈과 돌기는 자물쇠를 여는 데 
영향을 주지 않지만, 자물쇠 영역 내에서는 열쇠의 돌기 부분과 자물쇠의 
홈 부분이 정확히 일치해야 하며 열쇠의 돌기와 자물쇠의 돌기가 만나서는 안됩니다. 
또한 자물쇠의 모든 홈을 채워 비어있는 곳이 없어야 자물쇠를 열 수 있습니다.

열쇠를 나타내는 2차원 배열 key와 자물쇠를 나타내는 
2차원 배열 lock이 매개변수로 주어질 때, 열쇠로 자물쇠를 열수 있으면 true를, 
열 수 없으면 false를 return 하도록 solution 함수를 완성해주세요.

제한사항
key는 M x M(3 ≤ M ≤ 20, M은 자연수)크기 2차원 배열입니다.
lock은 N x N(3 ≤ N ≤ 20, N은 자연수)크기 2차원 배열입니다.
M은 항상 N 이하입니다.
key와 lock의 원소는 0 또는 1로 이루어져 있습니다.
0은 홈 부분, 1은 돌기 부분을 나타냅니다.

입출력 예
key	                                 lock	                               result
[[0, 0, 0], [1, 0, 0], [0, 1, 1]]	[[1, 1, 1], [1, 1, 0], [1, 0, 1]]   	true
'''
# 완전탐색
def rotate_90(a):
    n = len(a) # 행 길이 계산
    m = len(a[0]) # 열 길이 계산
    result = [[0] * n for _ in range(m)] # 결과 리스트
    for i  in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]
    return result

# 자물쇠의 중간 부분이 모두 1인지 확인
def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return True

def solution(key, lock):
    n = len(lock)  # 자물쇠 크기
    m = len(key)  # 열쇠 크기
    # 자물쇠의 크기를 기존의 3배로 변환
    new_lock = [[0]*(n*3) for _ in range(n*3)]
    # 새로운 자물쇠의 중앙 부분에 기존의 자물쇠 넣기
    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j] # 자물쇠를 3배행렬 가운데에 안착
    
    # 4가지 방향에 대해서 확인
    for rotation in range(4):
        key = rotate_90(key)  # 처음부터 돌리고 시작
        for x in range(n*2):
            for y in range(n*2):
                for i in range(m):
                    for j in range(m): # 열쇠의 활동 반경을 (2n+m)x(2n+m)으로 설정 -> 사실상 전범위
                        new_lock[x + i][y + j] += key[i][j] # 열쇠행렬+자물쇠행렬
                if check(new_lock) == True: # 열쇠+자물쇠로 3배 행렬의 가운데 NxN부분이 모두 1이면 True
                    return True
                # 자물쇠에 열쇠를 끼워넣기
                for i in range(m):  # 열쇠부분 제거하고 다시 끼우기 위한 for문 (시도 후 남아있으면 안되니까!)    
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j] # +되었던거 그냥 원상 복구 시켜줌
    return False # 모든 경우의 수를 다 해봐도 가운데 NxN부분이 모두 1이 아니면 False




