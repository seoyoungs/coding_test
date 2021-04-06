# ================== sorted 소스코드 ================================
# sorted는 리스트, 딕셔너리 자료형 등을 입력받아서 정렬된 결과를 출력한다
array = [7,5,9,0,3,1,6,2,4,8]

result = sorted(array)
print(result)

# ================== sort 소스코드 ==================================
array = [7,5,9,0,3,1,6,2,4,8]

array.sort()
print(array)

# ================== 정렬 라이브러리에서 key를 활용한 소스코드 =======
array = [('바나나', 2), ('사과', 5), ('당근', 3)]

def setting(data):
    result = sorted(array, key = setting)

print(result)

