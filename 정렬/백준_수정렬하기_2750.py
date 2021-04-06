'''
https://solved.ac/problems/tags
문제
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다. 
둘째 줄부터 N개의 줄에는 숫자가 주어진다. 
이 수는 절댓값이 1,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

출력
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

예제 입력 1 
5
5
2
3
4
1
예제 출력 1 
1
2
3
4
5
'''

# 중복되는 숫자 출력 안한다
n = int(input()) # 첫째 줄에서 이후 주어질 수의 개수를 입력 받는다.
num_list = [] # num_list를 통해 숫자들의 리스트를 만든다.

for i in range(n): # x만큼 반복하여 num_list에 항목들을 추가한다.
    num_list.append(int(input()))

num_list = sorted(num_list) # num_list를 sorted로 정렬한다.

for i in range(len(num_list)): # 숫자 중복되지 않게 출력
    print(num_list[i])


