'''
문제 설명
ANIMAL_OUTS 테이블은 동물 보호소에서 입양 보낸 동물의 정보를 담은 테이블입니다.
ANIMAL_OUTS 테이블 구조는 다음과 같으며, ANIMAL_ID, ANIMAL_TYPE,
DATETIME, NAME, SEX_UPON_OUTCOME는 각각 동물의 아이디, 생물 종, 
입양일, 이름, 성별 및 중성화 여부를 나타냅니다.

NAME	TYPE	NULLABLE
ANIMAL_ID	VARCHAR(N)	FALSE
ANIMAL_TYPE	VARCHAR(N)	FALSE
DATETIME	DATETIME	FALSE
NAME	VARCHAR(N)	TRUE
SEX_UPON_OUTCOME	VARCHAR(N)	FALSE
보호소에서는 몇 시에 입양이 가장 활발하게 일어나는지 알아보려 합니다. 
0시부터 23시까지, 각 시간대별로 입양이 몇 건이나 발생했는지 
조회하는 SQL문을 작성해주세요. 이때 결과는 시간대 순으로 정렬해야 합니다.

예시
SQL문을 실행하면 다음과 같이 나와야 합니다.

HOUR	COUNT
0	0
1	0
2	0
3	0
4	0
5	0
6	0
7	3
8	1
9	1
10	2
11	13
12	10
13	14
14	9
15	7
16	10
17	12
18	16
19	2
20	0
21	0
22	0
23	0
'''

-- 코드를 입력하세요
# 어떤 변수에 특정 값을 할당 set

SET @HOUR = -1;
SELECT (@HOUR := @HOUR + 1) HOUR, (SELECT COUNT(*) FROM ANIMAL_OUTS WHERE HOUR(DATETIME) = @HOUR ) COUNT 
FROM ANIMAL_OUTS 
WHERE @HOUR < 23
# HOUR를 1씩 증가시키며 그에 따른 시간대별 입양 건수를 서브쿼리를 이용
# SET을 이용할 때는 대입 연산자를 '='를 사용하고 그 외에는 :=를 사용해야 합니다.







