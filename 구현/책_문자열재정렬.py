data = input()
result = [] # 알파벳
value = 0 # 숫자

# 문자를 하나씩 확인해
for x in data:
    # 알파벳인 경우 결과 리스트에 삽입 # 알파벳 코드 isalpha
    if x.isalpha():
        result.append(x)
    # 숫자는 따로 더하기
    else:
        value += int(x)

# 알파벳을 오름차순으로 정렬
result.sort()

# 숫자 하나라도 존재하는 경우 뒤에 삽입
if value != 0:
    result.append(str(value))

# 최종 결과 출력(리스트를 문자열로 변환하여 출력)
print(''.join(result))

