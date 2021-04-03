'''
특정조건이란 현재 캐릭터의 점수를 N이라고 할 때 자릿수를 기준으로
점수 N을 반으로 나누어 왼쪽 부분의 각 자릿수의 합과 오른쪽 부분의
각 자릿수의 합과 오른쪽 부분의 각 자릿수의 합을 더한 값이 동일한 상황을
의미합니다. 예를 들어 현재 점수가 123,402라면 왼쪽 부분의 
각 자릿수의 합은 1+2+3 오른쪽 부분의 각 자릿수의 합은 4+0+2이므로 두 합이 
6으로 동일해 럭키 스트레이트를 사용할 수 있습니다

입력예시 123402 출력예시 LUCKY

'''
# 항상 짝수만 가능
# 양쪽의 숫자 합이 동일하면 LUCKY, 아니면 READY

n = int(input())
length = len(n)
summary = 0

# 왼쪽부분의 합 더하기
for i in range(length/2):
    summary += int(n[i])

# 오른쪽부분의 합 빼기
for i in range(length//2, length):
    summary -= int(n[i])

# 왼쪽과 오른쪽 부분 동일한지 검사
if summary ==0 :
    print('Lucky')
else :
    print('READY')



