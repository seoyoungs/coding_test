'''
깊이 우선 탐색

문제
어떤 시골의 중학교에는 부근의 3개 초등학교를 졸업한 남녀 학생들이 입학한다.
1학년 1반을 맡게 된 김갑동 선생님은 자기 반에 배정된 학생들을 
대상으로 하여 짝을 정하려고 한다. 
1학년 1반에 배정 된 학생들은 남자와 여자가 각각 N 명씩이다. 
김갑동 선생님은 서로 모르는 학생끼리 짝이 되도록 하기 위해 
같은 초등학교 출신이 아닌 남학생과 여학생을 짝으로 정하기로 원칙을 세웠다. 
예를 들어, 다음 표와 같이 1학년 1반에 학생들이 왔다고 하자.

위의 경우에는 다음과 같이 짝을 하면 서로 다른 초등학교 출신의 
남녀 학생들로 짝을 정할 수 있다.

A초등 남학생 3명과 B초등 여학생 3명
A초등 남학생 1명과 C초등 여학생 1명
B초등 남학생 1명과 A초등 여학생 1명
C초등 남학생 1명과 A초등 여학생 1명

김갑동 선생님의 문제를 해결하는 프로그램을 작성하시오.

입력
첫 줄에는 남학생 (또는, 여학생) 수를 나타내는 
정수 N (3≤N≤100,000)이 주어진다. 
둘째 줄에는 A초등학교 출신의 남학생 수와 여학생 수가 주어진다. 
셋째 줄에는 B초등학교 출신의 남학생 수와 여학생 수가 주어진다. 
넷째 줄에는 C초등학교 출신의 남 학생 수와 여학생 수가 주어진다. 
모든 학생수는 0 이상이다.

출력
김갑동 선생님의 원칙대로 모든 학생들의 짝을 정할 수 있으면 
첫 줄에 1을 출력하고, 그렇지 않으면 0을 출력한다.

첫 줄에 1을 출력한 경우는, 
둘째 줄에 A초등 남학생과 B초등 여학생의 짝 수와 
A초등 남학생과 C초등 여학생의 짝 수를, 
셋째 줄에 B초등 남학생과 A초등 여학생의 
짝 수와 B초등 남학생과 C초등 여학생의 짝 수를, 
넷째 줄에 C초등 남학생과 A초등 여학생의 
짝 수와 C초등 남학생과 B초등 여학생의 짝 수를 출력한다. 
(총 6번 반복문)

숫자와 숫자 사이에는 빈칸을 하나 둔다.
짝 정하는 방법이 여럿인 경우에는 아무거나 한 방법을 출력한다.

예제 입력 1 
6
a: 4 d: 2
b: 1 e: 3
c: 1 f: 1
예제 출력 1 
1
3 1
1 0
1 0
'''

n = int(input())

school = []
result = True

# (남녀 나눈다 x,y)
for i in range(0,3):
    x, y = map(int, input().split())
    school.append(x)
    school.append(y)

# 총 6가지로 나눌수 있다
for i in range(0, school[0]+1):
    a = i
    d = school[0] - a # a남과 c여가 짝이되는수= a남-a남과 b여
    e = school[5] - d # b남과 c여가 짝 되는 수 = c여 - a남c여
    b = school[2] - e # b남과 a여가 짝 되는 수 = b남 - b남c여
    c = school[1] - b # c남과 a여가 짝 되는 수 = a여 - b남a여
    f = school[4] - c # c남과 b여가 짝 되는 수 = c남 - c남a여

    if a >= 0 and b >= 0 and c >= 0 and d >= 0 and e >= 0 and f >= 0:
        print(1)
        print(a,d)
        print(b,e)
        print(c,f)
        result = False
        break

if result:
    print(0)

    


