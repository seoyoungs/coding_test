# 성적 순으로 보고 이름 출력하기
# 오름차순으로 출력하기

# n입력 받기
n = int(input())

# n명의 학생 정보를 입력받아 리스트에 저장
array = []
for i in range(n):
    input_data = input().split()
    # 이름은 문자열 그대로, 점수는 정수형으로 변환해 저장
    array.append(input_data[0], int(input_data[1]))

# 키(key)를 이용해, 점수를 기준점으로 정렬
array = sorted(array, key= lambda student: student[1])
# 기준점 정렬을 lambda를 통해서 정렬, student[1] 밑끝에 숫자를 기준으로 정렬

# 정렬이 수행된 결과를 출력
for student in array:
    print(student[0], end = '') # student[0] 이름을 출력







