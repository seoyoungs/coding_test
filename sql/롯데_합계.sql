'''
ID별 합계

문제 설명
EMPLOYEES 테이블은 자동차 판매 회사에서 일하고 있는 직원의 정보가 담긴 테이블입니다. EMPLOYEES테이블 구조는 다음과 같으며, ID, NAME, SALARY, BRANCH_ID는 각각 직원의 아이디, 이름, 월급, 근무하는 대리점 아이디를 나타냅니다.

NAME	TYPE	NULLABLE
ID	INT	FALSE
NAME	VARCHAR(N)	FALSE
SALARY	NUMERIC(N,M)	FALSE
BRANCH_ID	INT	FALSE
문제
EMPLOYEES 테이블을 이용해 지점 별 총급여액이 얼마인지 조회하는 SQL문을 작성해주세요.
단, 결과는 지점의 ID순으로 정렬되어야 합니다.

예시
예를 들어 EMPLOYEES 테이블이 다음과 같다면

ID	NAME	SALARY	BRANCH_ID
4603	Alayna	180	15
4651	Juliet	300	17
864	Holly	330	16
2842	Kyra	280	16
15번 지점의 총급여액은 180 (Alayna)
16번 지점의 총급여액은 330 + 280 (Holly, Kyra)
17번 지점의 총급여액은 300 (Juliet)

이므로, SQL을 실행하면 다음과 같이 출력되어야 합니다.

BRANCH_ID	TOTAL
15	180
16	610
17	300

'''
-- 코드를 입력하세요
SELECT BRANCH_ID, sum(SALARY) as TORAL
FROM EMPLOYEES
GROUP BY BRANCH_ID
ORDER BY BRANCH_ID

