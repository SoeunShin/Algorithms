# Programmers 151138. 자동차 대여 기록에서 장기/단기 대여 구분하기

/*
CAR_RENTAL_COMPANY_RENTAL_HISTORY 테이블에서 대여 시작일이 2022년 9월에 속하는 대여 기록에 대해서 대여 기간이 30일 이상이면 '장기 대여' 
그렇지 않으면 '단기 대여' 로 표시하는 컬럼(컬럼명: RENT_TYPE)을 추가하여 대여기록을 출력하는 SQL문을 작성해주세요. 결과는 대여 기록 ID를 기준으로 내림차순 정렬해주세요.
*/

SELECT 
    HISTORY_ID, CAR_ID, 
    DATE_FORMAT(START_DATE, '%Y-%m-%d') AS START_DATE,
    DATE_FORMAT(END_DATE, '%Y-%m-%d') AS START_DATE,
    CASE
    WHEN DATEDIFF(END_DATE, START_DATE)+1 >= 30 THEN '장기 대여'
    ELSE '단기 대여' END AS RENT_TYPE
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE START_DATE LIKE '2022-09%'
ORDER BY HISTORY_ID DESC

# DATEDIFF(날짜1, 날짜2);
# 두 날짜 간의 차이를 가져오는 함수
# 날짜1 - 날짜2
# 예제: SELECT TIMESTAMPDIFF(QUARTER, '2017-03-01', '2018-03-28');
# 결과: 392
# 예제: SELECT DATEDIFF('2018-03-28 23:59:59', '2017-03-01 00:00:00');
# 결과: 392
